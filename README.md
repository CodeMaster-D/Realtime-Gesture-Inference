# Hand Interaction & Face Validation System with MediaPipe

This project is a real-time computer vision application developed with Python, using the OpenCV and MediaPipe libraries. This application allows users to interact with objects on the screen using hand gestures after their face has been detected and validated in the correct position.

The system works in two main steps:
1.  **Face Validation:** The user must position their face within an oval displayed in the center of the screen.
2.  **Hand Interaction:** Once the face is validated, the user can use their index finger to touch colored boxes, which will trigger the playing of a sound file (musical note).

## Features

-   **Real-time Face Validation:** Uses MediaPipe Face Mesh to detect the face and ensure the user is in the specified position.
-   **Hand & Landmark Detection:** Tracks hand movements and 21 landmarks on each hand with MediaPipe Hands.
-   **Box-Based Interaction:** 5 interactive boxes with different colors and positions that can be triggered with the index finger.
-   **Sound Playback:** Plays different MP3 files (Do, Re, Mi, Fa, Sol) when the corresponding box is touched.
-   **Visual Feedback:** Provides real-time visual feedback, such as changes in the oval's color, a finger position marker, and highlighting of the selected box.
-   **Sound Spam Prevention:** Smart logic to ensure each sound is only played once when the finger enters the box area, preventing repeated playback.

## Prerequisites

Before you begin, ensure you have the following installed:

-   Python 3.7 or higher
-   Pip (Python package manager)
-   A functioning Web Camera

## Project Setup

Follow the steps below to set up and run this project on your computer.

### Step 1: Clone the Repository

First, clone this repository to your local machine using Git:

```bash
git clone https://github.com/username/your-repo-name.git
cd your-repo-name
```

*(Replace `username/your-repo-name` with your repository's URL)*

### Step 2: Create a Virtual Environment (Highly Recommended)

Using a virtual environment will isolate your project's dependencies from your global system.

**For Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**For macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

After activating the virtual environment, install all the required libraries with the following command:

```bash
pip install opencv-python mediapipe numpy playsound==1.2.2
```
> **Note:** Version `playsound==1.2.2` is often more stable and compatible. If you encounter issues, you can try other versions or an alternative library like `pygame.mixer`.

### Step 4: Prepare Sound Files

This code requires 5 sound files in `.mp3` format. Create a folder (or place them in the main project directory) and ensure you have files with the **exact** names as below:

-   `do.mp3`
-   `re.mp3`
-   `mi.mp3`
-   `fa.mp3`
-   `sol.mp3`

Make sure these files are in the **same directory as your Python file**, or you can modify the `AUDIO_FILENAMES` variable in the code to adjust their path.

## How to Use

Once all setup is complete, you can run the application:

1.  **Run the Script:** Open a terminal/command prompt in the project directory, then run the command:
    ```bash
    python main.py
    ```
    *(Replace `main.py` with your Python file name if it's different)*

2.  **Position Your Face:** Point your face at the camera. Position your face exactly in the center of the oval that appears on the screen. The oval will turn green and display "Face is correctly positioned, OK!" if the position is correct.

3.  **Interact with Your Hand:** After your face is validated, raise one of your hands in front of the camera. Point your index finger at one of the 5 colored boxes.

4.  **Listen to the Sound:** When your finger enters the box area, the application will play the musical note corresponding to that box and display the box's name on the screen.

5.  **Exit:** Press the `q` key on your keyboard to close the application.

## Project Structure

```
.
├── main.py                 # Main application script
├── do.mp3                  # Sound file for the Red box (Do)
├── re.mp3                  # Sound file for the Green box (Re)
├── mi.mp3                  # Sound file for the Blue box (Mi)
├── fa.mp3                  # Sound file for the Yellow box (Fa)
├── sol.mp3                 # Sound file for the Purple box (Sol)
└── README.md               # This documentation file
```

## Contributing

Contributions are highly appreciated! If you have ideas for new features, find bugs, or want to improve the code, please feel free to open an issue or submit a pull request.

1.  Fork this project
2.  Create a feature branch (`git checkout -b feature/NewFeature`)
3.  Commit your changes (`git commit -m 'Add a new feature'`)
4.  Push to the branch (`git push origin feature/NewFeature`)
5.  Open a Pull Request

## License

This project is licensed under the **Apache License 2.0**—see the **[LICENSE](LICENSE)** file for the full terms and the **[NOTICE](NOTICE)** file for copyright and attribution details.
