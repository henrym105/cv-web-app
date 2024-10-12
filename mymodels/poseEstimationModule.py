import cv2
import mediapipe as mp
import time
import os

class poseDetector:
    def __init__(self, mode = False, upBody = False, smooth = True, detectionConf = 0.5, trackingConf = 0.5 ) -> None:
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionConf = detectionConf
        self.trackingConf = trackingConf

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth, 
                                     min_detection_confidence=self.detectionConf, 
                                     min_tracking_confidence=self.trackingConf)


    def findPose(self, img, draw = True):
        """Find the pose and draw lines/dots on the image (set draw = False to disable)"""

        # send image to nn, receive list of coordinates for all 33 body landmarks (nose, hands, feet, etc.)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        
        # if any body parts are foung in the image, draw them 
        if draw and self.results.pose_landmarks:
            # Calculate the radius of the dots as 1/20th of the image width
            dot_radius = int(img.shape[1] / 100)
            line_thickness = int(dot_radius / 10)
            # Draw landmarks with the calculated dot size
            self.mpDraw.draw_landmarks(
                img, 
                self.results.pose_landmarks, 
                self.mpPose.POSE_CONNECTIONS,
                landmark_drawing_spec=self.mpDraw.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=dot_radius),
                connection_drawing_spec=self.mpDraw.DrawingSpec(color=(0, 0, 255), thickness=line_thickness)
            )

        return img


    def findFeet(self, img, draw=True):
        """
        :draw:
            - True = draws points on image_array
            - False = does not alter image, returns feet coordinates -> list([id, x, y], [id, x, y], ...)
        """

        feetList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                # get dimensions of the img frame
                h, w, c, = img.shape
                # print(id, lm)

                if id in [27, 28, 29, 30, 31, 32]:
                    # convert landmark coordinates from percentage of width and height to pixel coordinates
                    cx, cy = int(lm.x*w), int(lm.y*h)

                    # store coordinates in return list
                    feetList.append([id, cx, cy])

                    # draw cirle, if applicable
                    if draw:
                        cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
        if draw:
            return img
        else:
            return feetList
