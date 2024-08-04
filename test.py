import cv2
import numpy as np
import mediapipe as mp

LOW_COLOR1 = np.array([90, 64, 0])
HIGH_COLOR1 = np.array([240, 255, 255])
return_to_top = False

# Initialize camera capture object outside the loop
cap = cv2.VideoCapture(0)  # Select camera with index 0

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

while True:
    if return_to_top:
        now_img = cv2.imread("/home/mitsuki/catkin_ws/src/ros_try_final/photo/now_img.jpg") # Read the saved image
        cvt_yuv = cv2.cvtColor(now_img, cv2.COLOR_BGR2YUV) # RGB => YUV(YCbCr)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)) # clahe object creation
        cvt_yuv[:,:,0] = clahe.apply(cvt_yuv[:,:,0]) # Apply histogram equalization to luminance
        img = cv2.cvtColor(cvt_yuv, cv2.COLOR_YUV2BGR)
        LOW_COLOR1 = np.array([90, 64, 0])
        HIGH_COLOR1 = np.array([240, 255, 255])
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # BGR to HSV conversion
        bin_img1 = cv2.inRange(hsv, LOW_COLOR1, HIGH_COLOR1) # Create a mask
        mask = bin_img1
        movie_img = cv2.bitwise_and(img, img, mask= mask) # Extract specific color from original image
        cv2.imwrite("/home/mitsuki/catkin_ws/src/ros_try_final/photo/movie_img.jpg", movie_img) # Save the image

    success, image = cap.read()
    if not success or image is None:
        print("Failed to read frame from camera.")
        break

    # debug
    image_height = image.shape[0]
    # debug

    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)
    mp.solutions.drawing_utils.draw_landmarks(
            image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    cv2.imshow('MediaPipe Pose', image)

    if results.pose_landmarks is not None:
        # Process pose landmarks
        print('SUCCESS LANDMARKS')
        right_shoulder_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y
        left_shoulder_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y
        right_hip_landmark = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP]
        left_hip_landmark = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]

        if (right_hip_landmark is not None and left_hip_landmark is not None and
                right_hip_landmark.visibility > 0.5 and left_hip_landmark.visibility > 0.5) or \
           ((right_shoulder_y is not None and right_hip_landmark is not None) or \
           (left_shoulder_y is not None and left_hip_landmark is not None)):
            # Both hip landmarks are visible or at least one shoulder and hip landmark are visible
            right_hip_y = right_hip_landmark.y
            left_hip_y = left_hip_landmark.y

            # Define mask and save the image when conditions are met
            image_width, image_height = image.shape[1], image.shape[0]
            right_hip_x = int(right_hip_landmark.x * image_width)
            right_hip_y = int(right_hip_landmark.y * image_height)
            left_hip_x = int(left_hip_landmark.x * image_width)
            left_hip_y = int(left_hip_landmark.y * image_height)

            if (0 <= right_hip_x < image_width and 0 <= right_hip_y < image_height and
                    0 <= left_hip_x < image_width and 0 <= left_hip_y < image_height):
                # Save the image depicting the landmark
                cv2.imwrite("/home/mitsuki/catkin_ws/src/ros_try_final/photo/now_img.jpg", image)
                print("Image saved.")
                return_to_top = True  # Set return_to_top to True to process the saved image
        else:
            print('Not enough landmarks')

    else:
        print('NO POINT')

    k = cv2.waitKey(1)
    if k == 27:
        break

# Release capture object and close windows
cap.release()
cv2.destroyAllWindows()






