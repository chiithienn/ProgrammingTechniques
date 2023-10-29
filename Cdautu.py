from PySide2.QtWidgets import *
from PySide2.QtGui import *
import sys
from CxulyTietKiem import *
from CnhapKD import *
from CnhapCK import *

class DTWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setup()
        self.show()

    def setup(self):
        self.setWindowTitle("Quản lý chi tiêu đầu tư")
        self.setGeometry(400, 400, 600, 300)
        self.setMaximumSize(600, 300)

        self.gridLayout1()
        vbox=QVBoxLayout()
        vbox.addWidget(self.groupbox1)

        self.setLayout(vbox)

    def gridLayout1(self):
        self.groupbox1 = QGroupBox()
        self.groupbox1.setFont(QFont("Times", 13))

        vbox=QVBoxLayout()
        hbox=QHBoxLayout()

        tieude = QLabel("QUẢN LÝ ĐẦU TƯ")
        tieude.setFont(QFont("#9Slide03 HelvetIns", 23))
        tieude.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.cbb1=QComboBox()
        self.cbb1.setMinimumHeight(60)
        self.cbb1.setFont(QFont('Times',16))
        self.cbb1.addItems(['Kinh doanh','Chứng khoán'])


        btnChon=QPushButton("Chọn")
        btnChon.setFont(QFont('Times',16))
        btnChon.setMinimumHeight(60)
        btnChon.clicked.connect(self.chonAction)

        vbox.addWidget(tieude)
        hbox.addWidget(self.cbb1)
        hbox.addWidget(btnChon)
        vbox.addLayout(hbox)

        self.groupbox1.setLayout(vbox)
    def chonAction(self):
        s=self.cbb1.currentText()
        if s=="Kinh doanh":
            self.goi=NhapKDWindow()
        if s=="Chứng khoán":
            self.goi=NhapCKWindow()

if __name__ == '__main__':
    myapp=QApplication(sys.argv)

    window=DTWindow()

    myapp.exec_()
    sys.exit()