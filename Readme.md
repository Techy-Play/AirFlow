AIR-FLOW: GESTURE-CONTROLLED SCREEN SCROLLING
=============================================

Control your computer's scrolling using hand gestures through your webcam! ✌️

FEATURES
--------
- Real-time hand gesture recognition
- Vertical scrolling with two-finger gesture
- Visual feedback of hand landmarks
- Adjustable sensitivity settings
- Cross-platform compatibility (Windows/MacOS/Linux)

REQUIREMENTS
------------
- Python 3.7 or higher
- Webcam
- Essential Libraries:
  * mediapipe
  * opencv-python
  * pyautogui

INSTALLATION
------------
1. Clone the repository:
   git clone https://github.com/YOUR_USERNAME/Air-Flow.git
   cd Air-Flow

2. Install dependencies:
   pip install -r requirements.txt

   (If requirements.txt doesn't work, install manually:)
   pip install mediapipe opencv-python pyautogui

3. Verify installation:
   python --version

USAGE
-----
1. Run the program:
   python air_flow.py

2. Gesture Controls:
   - Show TWO FINGERS (index and middle) to activate
   - Move fingers DOWN to scroll DOWN
   - Move fingers UP to scroll UP
   - Press 'q' to quit program

3. Tips:
   * Ensure good lighting conditions
   * Keep hand visible in camera frame
   * Start with slow movements
   * Adjust sensitivity in code if needed

TROUBLESHOOTING
---------------
- Webcam not detected? Try:
  * Check camera permissions
  * Disconnect/reconnect webcam
  * Try camera index 1 in code (change cv2.VideoCapture(0) to 1)

- Library errors? Try:
  * Update pip: python -m pip install --upgrade pip
  * Reinstall requirements

CONTRIBUTING
------------
Contributions are welcome! 
1. Fork the project
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

LICENSE
-------
Distributed under the MIT License. See LICENSE for details.

ACKNOWLEDGMENTS
---------------
- MediaPipe for hand tracking models
- OpenCV for computer vision framework
- PyAutoGUI for screen control

CONTACT
-------
Your Name - lokeshpaneru20508@gmail.com
Project Link: https://github.com/Techy-Play/AirFlow