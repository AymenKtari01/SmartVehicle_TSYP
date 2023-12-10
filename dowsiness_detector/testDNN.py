
import cv2
import numpy as np
from keras.models import model_from_json

def cvDnnDetectFaces(image, opencv_dnn_model, emotion_model, min_confidence=0.5, display=True):
    image_height, image_width, _ = image.shape
    output_image = image.copy()

    preprocessed_image = cv2.dnn.blobFromImage(image, scalefactor=1.0, size=(300, 300),
                                               mean=(104.0, 117.0, 123.0), swapRB=False, crop=False)

    opencv_dnn_model.setInput(preprocessed_image)
    results = opencv_dnn_model.forward()

    detected_faces = []

    for face in results[0][0]:
        face_confidence = face[2]

        if face_confidence > min_confidence:
            bbox = face[3:]

            x1 = int(bbox[0] * image_width)
            y1 = int(bbox[1] * image_height)
            x2 = int(bbox[2] * image_width)
            y2 = int(bbox[3] * image_height)

            # Ensure that the face region is within the image boundaries
            if 0 <= x1 < x2 <= image_width and 0 <= y1 < y2 <= image_height:
                # Extract the face from the original image
                detected_face = image[y1:y2, x1:x2]

                # Check if the face region is non-empty before further processing
                if not detected_face.size == 0:
                    # Convert the face to grayscale
                    roi_gray_frame = cv2.cvtColor(detected_face, cv2.COLOR_BGR2GRAY)

                    # Resize the grayscale face image
                    cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)

                    # Predict the emotion
                    emotion_prediction = emotion_model.predict(cropped_img)
                    maxindex = int(np.argmax(emotion_prediction))

                    # Store the information about the detected face
                    detected_faces.append((x1, y1, x2, y2, vehicule_dict[maxindex]))

                    # Draw the rectangle on the output image
                    cv2.rectangle(output_image, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=image_width // 200)

                    # Display the emotion label on top of the rectangle
                    cv2.putText(output_image, vehicule_dict[maxindex], (x1 + 5, y1 - 20),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    if display:
        cv2.imshow("Output", output_image)
    else:
        return output_image, detected_faces

# Rest of your code remains unchanged

# Load the pre-trained model
prototxt_path = "deploy.prototxt"
caffemodel_path = "res10_300x300_ssd_iter_140000_fp16.caffemodel"
net = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)

# Load the emotion detection model
json_file = open('facefin1_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
emotion_model = model_from_json(loaded_model_json)
emotion_model.load_weights("facefin1_model.h5")
print("Loaded emotion model from disk")


# Dictionary for mapping emotion labels to text
vehicule_dict = {0: "active", 1: "reaching_behind",2:"sleep", 3: "talking",4:"yawn"}

# Start the webcam feed
cap = cv2.VideoCapture(0)  # Open the default camera (usually built-in webcam)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (1280, 720))

    # Call the face detection function on each frame
    cvDnnDetectFaces(frame, net, emotion_model)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
