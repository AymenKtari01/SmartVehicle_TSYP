# SmartVehicle_TSYP

## Table of Contents

- [Introduction](#introduction)
- [Project Description](#project-description)
- [Technologies Used](#technologies-used)
- [Demo](#demo)
- [Security](#security)
- [Demo](#demo)

## Introduction

Step into the future of road safety with our innovative project aimed at creating a safer driving experience for all. Our endeavor revolves around two key components, meticulously designed to enhance Advanced Driver Assistance Systems (ADAS) and elevate the overall safety quotient of vehicles.



## Project Description

### Advanced Driver Assistance Systems (ADAS):
#### Driver Monitoring System (DMS):

The first part of our project features a robust Driver Monitoring System utilizing two computer vision models. The primary model keenly observes the driver's face, detecting signs of drowsiness, distraction, or inattentiveness by monitoring eye and mouth movements. This cutting-edge technology ensures that drivers stay alert and focused during their journeys.
Upper Body Activity Recognition:

Complementing the DMS, the second computer vision model concentrates on the upper body, detecting activities such as mobile phone usage, drinking, or engaging in distracting behaviors. Upon identifying potential risks, the system activates a sonorous alarm or delivers a voice message, prompting the driver to regain focus and avoid hazardous actions.
Intelligent Front Lights Upgrade:
Adaptive LED Lighting System:

As a transformative addition, the project introduces an upgraded front lighting system. By incorporating additional LEDs, precisely four on each side, the illumination becomes adaptive and responsive to the surrounding environment.
Radar-Assisted Light Adjustment:

A sophisticated radar system works in tandem with the LED lights. It assesses the presence of other vehicles in the vicinity, dynamically adjusting the intensity of the front lights. This intelligent adaptation ensures that the lights reduce their glare when another vehicle approaches, preventing discomfort or distraction for oncoming drivers during nighttime travel.

## Technologies Used

- **Ai model**:

   AI-driven prediction of driver behavior and drowsiness using advanced model.
- **Ai computer vision**:

   Real-time AI computer vision with Raspberry Pi camera for object detection.


## Demo
1. To run the backend of our application, follow these steps:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   pip install -r requirements.txt
   cd backend

   uvicorn main:app --reload
   ```
2. For the frontend, kidnly follow these steps:
      ```bash
   cd tsyp
   npm i
   npm run dev 
   ```
Provide instructions on how to set up the project locally. Include details about installing dependencies and running the application.

3. Setting up MongoDB

You have two options for setting up MongoDB for our application:

#### Option 1: Local MongoDB Installation

1. **Install MongoDB:**
   - Download and install MongoDB from [MongoDB Download Center](https://www.mongodb.com/try/download/community).
   - Follow the installation instructions for your operating system.

2. **Create Database and Collections:**
   - Open a terminal or command prompt.
   - Run MongoDB by executing the `mongod` command.
   - In a separate terminal, connect to the MongoDB server using the `mongo` command.
   - Create the "HealthData" database and the required collections:
     ```bash
     use HealthData
     db.createCollection("Users")
     db.createCollection("Doctors")
     ```

### Option 2: Using Docker

1. **Install Docker:**
   - Download and install Docker from [Docker Desktop](https://www.docker.com/products/docker-desktop).

2. **Run Docker Compose:**
   - Navigate to the root directory of the project.
   - Run the following command to start MongoDB using Docker Compose:
     ```bash
     docker-compose up
     ```
   - This command will pull the MongoDB image and start a container with the necessary configurations.

### Security 

To ensure the security of our application and protect sensitive data, we employ robust encryption measures before transmitting any information. The majority of our communications are conducted using the secure shell (SSH) protocol, adding an extra layer of protection against unauthorized access. Additionally, for local development purposes, we utilize mkcert to implement Transport Layer Security (TLS) on localhost. 


### Demo 

[Click here to watch the video](https://drive.google.com/drive/folders/1xW1XTwPF-ujhIRcMsu30sQzZztjd_cZP?usp=sharing)
