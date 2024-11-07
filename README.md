# NDI Overlay

NDI Overlay is a Python application that uses PyQt5 to create a transparent window displaying NDI (Network Device Interface) video streams. It leverages the NDI SDK to find and receive video sources over the network. I personally use this project for displaying truly transparent overlays over my screen.

## Features

- Displays transparent NDI video streams in a frameless, always-on-top window.
- Automatically finds available NDI sources on the network.
- Allows selection of NDI sources to display.

## Requirements

- Python 3.x
- PyQt5
- imutils
- numpy

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SiroxCW/NDI-Overlay.git
   cd NDI-Overlay
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application using the provided batch or VBScript file:

**Make sure to change the x, y, width, and height values in the `main.py` file to match your screen resolution.**

- On Windows, you can use `run.bat`:

  ```cmd
  run.bat
  ```

- Alternatively, use the VBScript `run.vbs` to hide the terminal:

  ```cmd
  cscript run.vbs
  ```

## Project Structure

- `main.py`: The main application file that sets up the PyQt5 window and handles NDI video display.
- `receiver.py`: Contains the logic for receiving NDI video frames.
- `finder.py`: Handles finding available NDI sources on the network.
- `lib.py`: Provides the CFFI interface to the program.
- `run.bat` and `run.vbs`: Scripts to run the application.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- [PyQt5](https://riverbankcomputing.com/software/pyqt/intro) for the GUI framework.
- [imutils](https://github.com/jrosebr1/imutils) for image processing utilities.
- [numpy](https://numpy.org/) for numerical operations.
