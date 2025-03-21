import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QTextEdit, QFileDialog

class YouTubeDownloader(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("YouTube Downloader")
        self.setGeometry(200, 200, 500, 400)
        
        layout = QVBoxLayout()
        
        self.url_label = QLabel("YouTube URL:")
        self.url_input = QLineEdit()
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)
        
        self.format_label = QLabel("Select Format:")
        self.format_dropdown = QComboBox()
        self.format_dropdown.addItems(["Best Video+Audio", "Audio Only (MP3)", "Video Only (MP4)"])
        layout.addWidget(self.format_label)
        layout.addWidget(self.format_dropdown)
        
        self.download_btn = QPushButton("Download")
        layout.addWidget(self.download_btn)
        
        self.status_text = QTextEdit()
        self.status_text.setReadOnly(True)
        layout.addWidget(self.status_text)
        
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    downloader = YouTubeDownloader()
    downloader.show()
    sys.exit(app.exec_())
