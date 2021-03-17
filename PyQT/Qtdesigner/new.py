import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap

class New(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnOpenFile.clicked.connect(self.open_file)
        self.btnResize.clicked.connect(self.my_resize)
        self.btnSave.clicked.connect(self.save)

    def open_file(self):
        image, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Open File',
            r'C:\Gabryel\Screenshots',
            #options=QFileDialog.DontUseNativeDialog            
        )

        self.inputOpenFile.setText(image)
        self.original_img = QPixmap(image)
        self.labelImg.setPixmap(self.original_img)
        self.inputWidth.setText(str(self.original_img.width()))
        self.inputHeight.setText(str(self.original_img.height()))

    def my_resize(self):
        width = int(self.inputWidth.text())
        self.newImage = self.original_img.scaledToWidth(width)
        self.labelImg.setPixmap(self.newImage)
        self.inputWidth.setText(str(self.newImage.width()))
        self.inputHeight.setText(str(self.newImage.height()))
    
    def save(self):
        image, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Save File',
            r'C:\Gabryel\Screenshots'        
        )
        self.newImage.save(image, 'PNG')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    new = New()
    new.show()
    qt.exec_()
