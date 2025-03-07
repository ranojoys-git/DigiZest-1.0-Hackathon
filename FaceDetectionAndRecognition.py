import threading
import cv2
from deepface import DeepFace

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Use the default camera (usually index 0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0

rano_match = False
pri_match = False
face_match = False
no_person = False  # Added a flag for no person detection

reference_img1 = cv2.imread("Ranojoy Pic.jpg")
reference_img2 = cv2.imread("Priyanshi Pic.jpg")

def check_face(frame):
    global rano_match, pri_match, face_match, no_person
    try:
        rano_match = False
        pri_match = False
        no_person = False  # Reset all flags

        if (DeepFace.verify(frame, reference_img1.copy()))['verified']:
            rano_match = True

        elif (DeepFace.verify(frame, reference_img2.copy()))['verified']:
            pri_match = True

        else:
            no_person = True  # Set the flag to indicate no person detected
    except ValueError:
        no_person = True  # Set the flag to indicate no person detected

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale (face detection works better in grayscale)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except Exception as e:
                print(f"Error in threading: {e}")
                pass
        counter += 1

        if rano_match:
            cv2.putText(frame, "RMATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        elif pri_match:
            cv2.putText(frame, "PMATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        elif no_person:
            cv2.putText(frame, "NO PERSON!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
        else:
            cv2.putText(frame, "INTRUDER!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
            '''
            # Convert the text to speech
            tts = gTTS(text="Intruder", lang="en")
            tts.save('intruder.mp3')
            # Play the audio
            play_audio('intruder.mp3')

            # play_audio(audio_file)
            '''

    cv2.imshow("Face Recognition with frame", frame)

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
