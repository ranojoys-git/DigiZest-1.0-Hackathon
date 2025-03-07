# Smart Home Automation - Face Recognition Module

This repository consists of a part of the project that we worked on during the **Digizest Hackathon 1.0**. We built a **Smart Home Automation System** that detects the presence of a known person in the house and automatically turns on the appliances according to the saved preferences of the person. It also turns off the appliances when no one is at home. This code is a small but crucial part of the system, responsible for **real-time face recognition** to identify individuals.

---

## **Overview**

The code in this repository uses **OpenCV** and **DeepFace** to perform real-time face detection and recognition. It captures video from a webcam, detects faces, and compares them with pre-loaded reference images to identify specific individuals. Based on the recognition results, the system can trigger specific actions (e.g., turning on lights, adjusting thermostat settings, etc.) as part of the larger home automation system.

---

## **How It Works**

1. The system captures video from a webcam.
2. Compares the detected faces with reference images using DeepFace.
3. Displays the recognition results on the screen (e.g., "RMATCH!", "PMATCH!", "NO PERSON!", "INTRUDER!").
4. Based on the recognition results, the larger home automation system can trigger specific actions.

---
