import cv2
import mediapipe as mp
import pygame
import math

# ----------------- Alarm -----------------
pygame.mixer.init()
pygame.mixer.music.load("alarm.wav")

# ----------------- Functions -----------------

def distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def eye_aspect_ratio(landmarks, eye_points):
    p1 = landmarks[eye_points[0]]
    p2 = landmarks[eye_points[1]]
    p3 = landmarks[eye_points[2]]
    p4 = landmarks[eye_points[3]]
    p5 = landmarks[eye_points[4]]
    p6 = landmarks[eye_points[5]]

    vertical1 = distance(p2, p6)
    vertical2 = distance(p3, p5)
    horizontal = distance(p1, p4)

    return (vertical1 + vertical2) / (2 * horizontal)


LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

EAR_THRESHOLD = 0.23
CLOSED_FRAMES = 20

counter = 0
alarm_on = False

# ----------------- MediaPipe -----------------

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:

        for face_landmarks in results.multi_face_landmarks:

            landmarks = face_landmarks.landmark

            leftEAR = eye_aspect_ratio(landmarks, LEFT_EYE)
            rightEAR = eye_aspect_ratio(landmarks, RIGHT_EYE)

            ear = (leftEAR + rightEAR) / 2

            cv2.putText(frame,
                        f"EAR: {ear:.2f}",
                        (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        2)

            h, w, _ = frame.shape

            for lm in landmarks:
                x = int(lm.x * w)
                y = int(lm.y * h)

                cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

            # ---------------- Drowsiness ----------------

            if ear < EAR_THRESHOLD:

                counter += 1

                if counter >= CLOSED_FRAMES:

                    cv2.putText(
                        frame,
                        "DROWSINESS DETECTED!",
                        (40, 80),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 0, 255),
                        3
                    )

                    if not alarm_on:
                        pygame.mixer.music.play(-1)
                        alarm_on = True

            else:

                counter = 0

                if alarm_on:
                    pygame.mixer.music.stop()
                    alarm_on = False

    cv2.imshow("Driver Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

pygame.mixer.music.stop()

cap.release()
cv2.destroyAllWindows()