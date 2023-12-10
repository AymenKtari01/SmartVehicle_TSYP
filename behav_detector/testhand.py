import cv2
import mediapipe as mp
import numpy as np
from mediapipe.framework.formats import landmark_pb2
from keras.models import model_from_json

def mediapipeDetectHands(image, hands_module, emotion_model, min_detection_confidence=0.5, display=True):
    image_height, image_width, _ = image.shape
    output_image = image.copy()

    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = hands_module.process(img_rgb)

    detected_hands = []

    # Set the scaling factor for augmentation
    scaling_factor = 1.5

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            landmarks = []
            for landmark in hand_landmarks.landmark:
                x = int(landmark.x * image_width)
                y = int(landmark.y * image_height)
                landmarks.append((x, y))

            # Get the bounding box of the hand
            bbox = cv2.boundingRect(np.array(landmarks))

            x1, y1, w, h = bbox
            x2 = x1 + w
            y2 = y1 + h

            # Calculate the center of the bounding box
            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)

            # Calculate the new dimensions of the bounding box
            new_w = int(w * scaling_factor)
            new_h = int(h * scaling_factor)

            # Calculate the new coordinates of the bounding box to keep it centered
            x1 = max(0, center_x - new_w // 2)
            y1 = max(0, center_y - new_h // 2)
            x2 = min(image_width, center_x + new_w // 2)
            y2 = min(image_height, center_y + new_h // 2)

            # Draw the augmented rectangle around the hand
            cv2.rectangle(output_image, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=image_width // 200)

            # Extract the hand region
            detected_hand = image[y1:y2, x1:x2]

            # Perform emotion detection on the hand region
            if not detected_hand.size == 0:
                roi_gray_frame = cv2.cvtColor(detected_hand, cv2.COLOR_BGR2GRAY)
                cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)
                hand_prediction = emotion_model.predict(cropped_img)
                maxindex = int(np.argmax(hand_prediction))

                # Display emotion label on the output image
                cv2.putText(output_image, dict[maxindex], (x1 + 5, y1 - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

            detected_hands.append(landmarks)

            # Draw the hand landmarks on the output image
            mp.solutions.drawing_utils.draw_landmarks(
                output_image, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.get_default_hand_landmarks_style()
            )

    if display:
        cv2.imshow("Output", output_image)
    else:
        return output_image, detected_hands

# Set up Mediapipe Hands module
mp_hands = mp.solutions.hands
hands_module = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# Load the emotion detection model
json_file = open('hand_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
emotion_model = model_from_json(loaded_model_json)
emotion_model.load_weights("hand_model.h5")
print("Loaded emotion model from disk")

# Dictionary for mapping emotion labels to text
dict = {0: "Drinking", 1: "safe", 2: "Talking phone left", 3: "talking phone right", 4: "texting left", 5: "texting right"}

# Start the webcam feed
cap = cv2.VideoCapture(0)  # Open the default camera (usually built-in webcam)
mp_drawing_styles = mp.solutions.drawing_styles
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (1280, 720))

    # Call the hand detection function on each frame
    mediapipeDetectHands(frame, hands_module, emotion_model)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
