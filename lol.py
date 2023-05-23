import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt
from PyQt5.QtGui import QPixmap



class Card(QDialog):
    def __init__(self):
        super(Card, self).__init__()
        loadUi("card.ui", self)
        self.uploadIMGbutton.clicked.connect(self.uploadimagefunction)


    def uploadimagefunction(self):
        # Open a file dialog and get the path to the selected image file
        filepath, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")

        # Get the size of the label
        label_width = self.IMGbox.width()
        label_height = self.IMGbox.height()

        # Create a QPixmap object from the image file and scale it to fit inside the label
        pixmap = QPixmap(filepath).scaled(label_width, label_height, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Set the pixmap to the label
        self.IMGbox.setPixmap(pixmap)

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
trello = Card()
widget.addWidget(trello)
widget.resize(trello.size())
widget.show()
app.exec_()