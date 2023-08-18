# Mathpix Alternative for generate math equation in latex form with [Pix2Text](https://github.com/breezedeus/Pix2Text) and GUI using PyQt5

Convert images to text using Pix2Text OCR and PyQt5 GUI with screen snap feature (Now tested in Linux).X11 display manager supported.

## Introduction

This project aims to provide a user-friendly GUI for Optical Character Recognition (OCR) using the Pix2Text package. The GUI is built using PyQt5 and includes a screen capture feature to extract text from images.Thanks to
[Breezedeus](https://github.com/breezedeus).

## Features

[GUI Image](./images/image1.png)

-   Pix2Text OCR integration
-   PyQt5 GUI with intuitive interface
-   Screen capture capability
-   Linux compatibility
-   maim package integration (GNU compatibility)
-   Copy button the output as a text
-   Latex Generate compatibility.
    [Latex generate](./images/image4.png)

## Installation

1. REQUIREMENTS:

    1. Python 3.11
    2. Install the required dependencies:

    ```bash
        pip install pix2text PyQt5
    ```

    3. Maim Installation-(differ on linux package manager) for apt-get:

    ```bash
        sudo apt install maim
    ```

2. Clone the repository:

```bash
git clone https://github.com/
```

3. Installation of Requirements.txt:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the GUI application:

    ```bash
        python linux-main.py
    ```

2. Use the "Capture and Generate" button to take a screenshot of the desired area.

    [Generated text](./images/image2.png)

3. Click the "Copy Output" button for copying the output text/math-latex.

    [Copied Notification](./images/image3.png)

## License

This repository is licensed under the MIT License. See the `LICENSE` file for more information.

## Contribution

This repository is only run in the linux distribution.You can contribute to this repository by following [CONTRIBUTING.md](CONTRIBUTING.md).
