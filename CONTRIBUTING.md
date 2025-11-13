# Contributing to Hand Interaction & Face Validation System with MediaPipe

Thank you for your interest in contributing to the "Hand Interaction & Face Validation System with MediaPipe"! We welcome all forms of contribution, including but not limited to bug reports, feature requests, documentation improvements, and code enhancements.

## Code of Conduct

This project adheres to a Code of Conduct to ensure a welcoming and inclusive environment for all contributors. Please read [the full text](./CODE_OF_CONDUCT.md) to understand the actions that are and are not tolerated.

## Our Development Process

We use GitHub as our primary platform for tracking issues, discussing feature requests, and receiving pull requests. Our development process is centered around open collaboration to maintain the quality and functionality of this computer vision application.

## Pull Requests (PRs)

We enthusiastically welcome pull requests. To contribute to this project, please follow the steps below to ensure a smooth and efficient review process.

### 1. Fork the Repository and Create a Branch

-   Fork this repository to your GitHub account.
-   Create a new branch from the `main` branch for your specific contribution. Use a descriptive name for your branch, for example: `feature/add-pinch-gesture` or `fix/improve-face-detection-accuracy`.

### 2. Make Your Changes

-   The core logic of this project resides in `main.py`. Most of your changes will likely be in this file.
-   **Code Style:** Please adhere to [PEP 8](https://www.python.org/dev/peps/pep-0008/), the official Python style guide, to maintain code readability and consistency.
-   **Configuration:** Consider if your change can be made configurable (e.g., box colors, positions, sound file paths) instead of being hardcoded. Moving such values to a separate configuration file would be a valuable enhancement.
-   **Comments:** If you are adding complex logic, please add comments to explain your approach and make the code easier to understand for others.

### 3. Test Your Changes Thoroughly

Before submitting a pull request, it is crucial to test your changes.

-   **Run the Application:** Execute the script to ensure it runs without errors.
    ```bash
    python main.py
    ```
-   **Functionality Testing:** Test the specific feature you have modified.
    -   If you changed the face validation, test it with your face at various angles, distances, and lighting conditions.
    -   If you added a new gesture, ensure it is recognized reliably and doesn't conflict with existing gestures.
    -   If you modified the interaction boxes, verify that the sound feedback and visual highlights work correctly.
-   **Edge Case Testing:** Think about edge cases. What happens if the camera is not found? What if no hands or faces are detected for an extended period?

### 4. Commit, Push, and Open a Pull Request

-   **Commit:** Commit your changes with a clear and descriptive commit message. For example: "feat: Add pinch gesture support for playing a random sound".
-   **Push:** Push the committed changes to your forked repository's branch.
-   **Pull Request:** Open a pull request against the `main` branch of this repository. In your PR description, please provide:
    -   A clear summary of the changes you made.
    -   The reason for the change (e.g., what problem it solves or what new feature it adds).
    -   Any special instructions for testing your changes.

We will review your pull request as soon as possible and provide feedback. Thank you for helping to improve this project!

## Reporting Issues

We use GitHub Issues to track bugs and feature requests. When filing a new issue, please provide as much detail as possible to help us understand and address the problem.

-   **For Bug Reports:**
    -   **Title:** A concise and descriptive title (e.g., "Application crashes when hand moves out of frame quickly").
    -   **Description:** A detailed explanation of the problem.
    -   **Steps to Reproduce:** A step-by-step guide to reproduce the issue.
    -   **Environment:** Your operating system (e.g., Windows 11, macOS Sonoma, Ubuntu 22.04), Python version, and camera type (built-in, external USB).
    -   **Error Log:** If the application crashes, please include the full error traceback.

-   **For Feature Requests:**
    -   **Title:** A clear title for the feature (e.g., "Add support for custom sound packs").
    -   **Description:** A detailed description of the desired feature and why you think it would be a valuable addition.

## Issue Management Labels

We use the following labels to manage issues:

-   `good first issue`: Recommended for newcomers looking for a way to start contributing.
-   `help wanted`: We welcome contributions on these issues, but they may require significant work or investigation.
-   `bug`: Reports of unintended behavior or application crashes.
-   `enhancement`: Requests for new features or improvements to existing ones.
-   `documentation`: Issues related to improving the project's documentation (README, code comments, etc.).
-   `question`: General questions about the project.

## Areas of Contribution

If you're looking for ideas on how to contribute, here are some areas where we would particularly appreciate help:

1.  **New Gestures and Interactions:** Implement support for additional hand gestures (e.g., pinch, open palm, peace sign) to trigger different actions.
2.  **UI/UX Improvements:** Enhance the visual feedback. This could include smoother animations, more polished graphics, or a settings menu.
3.  **Performance Optimization:** The application runs in a real-time loop. Contributions that optimize frame processing, reduce CPU usage, or improve the overall performance would be highly valuable.
4.  **Configuration System:** Refactor the code to use a configuration file (e.g., `config.json` or `.env`) for settings like box positions, colors, sound file paths, and detection thresholds. This makes the application much more flexible.
5.  **Sound Management:** Improve the audio playback system, perhaps by allowing users to load custom sound files or by using a more robust audio library than `playsound`.
6.  **Code Modularity:** While the project is currently a single script, refactoring it into more modular components (e.g., separate classes for face detection, hand tracking, and UI rendering) could improve maintainability.

## License

By contributing to this project, you agree that your contributions will be licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for the full terms.
