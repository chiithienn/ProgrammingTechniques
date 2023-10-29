from PySide2.QtWidgets import *
from PySide2.QtGui import *
import sys
from Ctietkiem import *
from Cdautu import *

class CgiaodienTKDT(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setup()
        self.show()

    def setup(self):
        self.setWindowTitle("Quản lý chi tiêu tiết kiệm và đầu tư")
        self.setGeometry(1300, 200, 600, 300)
        self.setMinimumSize(600, 300)

        self.gridLayout1()

        vbox=QVBoxLayout()
        vbox.addWidget(self.groupbox)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

    def gridLayout1(self):
        self.groupbox=QGroupBox()

        vbox=QVBoxLayout()
        hbox=QHBoxLayout()

        tieude = QLabel("QUẢN LÝ TIẾT KIỆM VÀ ĐẦU TƯ")
        tieude.setFont(QFont("#9Slide03 HelvetIns", 23))
        tieude.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # Button Tiết Kiệm
        btnTK = QPushButton("Tiết kiệm")
        btnTK.setFont(QFont("Arial", 13))
        btnTK.setMinimumHeight(60)
        btnTK.clicked.connect(self.chonTietKiem)
        # Button Đầu Tư
        btnDT = QPushButton("Đầu tư")
        btnDT.setFont(QFont("Arial", 13))
        btnDT.setMinimumHeight(60)
        btnDT.clicked.connect(self.chonDauTu)

        vbox.addWidget(tieude)
        hbox.addWidget(btnTK)
        hbox.addWidget(btnDT)
        vbox.addLayout(hbox)

        self.groupbox.setLayout(vbox)

    def chonTietKiem(self):
        self.goi=TKWindow()
    def chonDauTu(self):
        self.goi=DTWindow()

if __name__ == '__main__':
    myapp=QApplication(sys.argv)

    window=CgiaodienTKDT()

    myapp.exec_()