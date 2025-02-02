import cv2
import face_recognition
import numpy as np
from datetime import datetime

# List of known face encodings and their corresponding names
known_face_encodings = []
known_face_names = []

# Load sample images and learn face encodings
# Add your own images and names
image_path_name_pairs = [
    ("person.jpg", "Person")
]

for image_path, name in image_path_name_pairs:
    image = face_recognition.load_image_file(image_path)
    encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(encoding)
    known_face_names.append(name)

# Initialize attendance tracking
attendance_log = []

# Start webcam
video_capture = cv2.VideoCapture(0)

print("Starting Facial Recognition Attendance System. Press 'q' to quit.")

while True:
    # Capture a single frame from the video
    ret, frame = video_capture.read()

    # Resize frame for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Find all face locations and encodings in the frame
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        # Compare face with known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # Find the best match index
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        # Log attendance if a known face is recognized
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if name != "Unknown" and (name, current_time) not in attendance_log:
            attendance_log.append((name, current_time))
            print(f"Attendance logged: {name} at {current_time}")

        # Display bounding box and name
        top, right, bottom, left = [v * 4 for v in face_location]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

    # Display the resulting frame
    cv2.imshow('Facial Recognition Attendance System', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
video_capture.release()
cv2.destroyAllWindows()

# Save attendance log
with open("attendance_log.txt", "w") as file:
    for entry in attendance_log:
        file.write(f"{entry[0]} - {entry[1]}\n")

print("Attendance system exited. Log saved to attendance_log.txt.")
