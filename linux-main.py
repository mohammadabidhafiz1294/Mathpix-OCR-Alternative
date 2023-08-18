import sys
import subprocess
from pix2text import Pix2Text
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtCore import Qt
from io import BytesIO

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Capture to text/latex with pix2text')

        layout = QVBoxLayout()

        self.label = QLabel('Welcome, Capture to latex/screenshot !', self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        
        self.button = QPushButton('Capture and Generate', self)
        self.button.clicked.connect(self.capture_and_resize)
        layout.addWidget(self.button)

        self.copy_button = QPushButton('Copy Output', self)
        self.copy_button.clicked.connect(self.copy_output)
        layout.addWidget(self.copy_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def capture_and_resize(self):
        # Use the 'maim' command to capture a specific area screenshot
        maim_process = subprocess.Popen(['maim', '-s'], stdout=subprocess.PIPE)
        screenshot_data, _ = maim_process.communicate()

        # Initialize the pix2text library
        p2t = Pix2Text()

        # Convert the image data to text using pix2text
        text_equation = p2t(BytesIO(screenshot_data))

        # Extract relevant values from dictionaries and convert to a string representation
        text_equation_str = '\n\n'.join(item['text'] for item in text_equation)

        # Set the text of the QTextEdit widget
        self.label.setText(text_equation_str)

        #print(text_equation)

        # Display the converted text in the QLabel
        self.label.setText(text_equation_str)

        # Set the text copied self
        self.copied_text = text_equation_str

    def copy_output(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.copied_text)

        # Display a notification that the text has been copied
        QMessageBox.information(self, 'Text Copied!', 'The output text has been copied to the clipboard.')
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
