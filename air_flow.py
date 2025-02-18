# This is the First release of My Project!
# Import required libraries
import cv2  # For camera operations
import mediapipe as mp  # For hand tracking
import pyautogui  # For screen scrolling

class AirFlowGestureController:
    """
    A class to control screen scrolling using hand gestures via webcam.
    
    Attributes:
        hands: MediaPipe hands model
        drawing_utils: MediaPipe drawing utilities
        screen_height: Screen height for movement calculation
        prev_y: Previous y-coordinate of fingers for direction detection
    """
    
    def __init__(self):
        """Initialize mediapipe models and screen parameters"""
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.mp_drawing = mp.solutions.drawing_utils
        self.screen_height = pyautogui.size().height
        self.prev_y = 0
        self.scroll_threshold = 30  # Pixels to move before scrolling
        self.cooldown = 0  # Scroll cooldown counter

    def detect_fingers(self, hand_landmarks):
        """
        Detect which fingers are raised (open).
        Returns list of raised finger indices (0=thumb, 4=index finger)
        """
        raised_fingers = []
        finger_tips = [self.mp_hands.HandLandmark.INDEX_FINGER_TIP,
                      self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
        
        for tip in finger_tips:
            if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
                raised_fingers.append(tip)
        return raised_fingers

    def process_gesture(self, frame):
        """
        Process webcam frame to detect gestures and control scrolling
        """
        # Flip frame for mirror view and convert color space
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process frame with MediaPipe hands
        results = self.hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Detect raised fingers
                raised_fingers = self.detect_fingers(hand_landmarks)
                
                # Check if two fingers are up (index and middle)
                if len(raised_fingers) == 2:
                    # Get current finger position (average of two fingers)
                    current_y = (hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y + 
                                hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y) / 2
                    
                    # Convert normalized coordinates to pixel values
                    current_y_px = current_y * self.screen_height
                    
                    # Calculate movement difference
                    delta_y = current_y_px - self.prev_y
                    
                    # Check cooldown and movement threshold
                    if self.cooldown <= 0 and abs(delta_y) > self.scroll_threshold:
                        if delta_y > 0:
                            pyautogui.scroll(-40)  # Scroll down
                        else:
                            pyautogui.scroll(40)   # Scroll up
                        
                        # Reset cooldown and previous position
                        self.cooldown = 5
                        self.prev_y = current_y_px
                    
                    # Draw hand landmarks
                    self.mp_drawing.draw_landmarks(
                        frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
        
        # Reduce cooldown each frame
        if self.cooldown > 0:
            self.cooldown -= 1

        return frame

def main():
    """Main function to run the Air-Flow program"""
    controller = AirFlowGestureController()
    cap = cv2.VideoCapture(0)  # Access webcam

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            continue

        # Process frame for gesture detection
        processed_frame = controller.process_gesture(frame)

        # Display output
        cv2.imshow('Air-Flow Gesture Control', processed_frame)

        # Exit on 'q' press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()