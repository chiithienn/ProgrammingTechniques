from PySide2.QtWidgets import *
from PySide2.QtGui import *
import sys
from CxulyDauTu import *

class NhapCKWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setup()
        self.show()

    def setup(self):
        self.setWindowTitle("  Đầu tư chứng khoán")
        self.setGeometry(400, 400, 500, 200)
        self.setMinimumSize(500, 300)
        self.setIcon()

        vbox=QVBoxLayout()

        self.gridLayout1()

        vbox.addWidget(self.groupbox1)

        self.setLayout(vbox)

    def setIcon(self):
        appIcon=QIcon('stock.png')
        self.setWindowIcon(appIcon)

    def gridLayout1(self):
        self.groupbox1 = QGroupBox("Nhập thông tin chứng khoán:")
        self.groupbox1.setFont(QFont("Times", 12))

        gridLayout=QGridLayout()

        lblGB=QLabel("Giá bán")
        self.nhapGB=QLineEdit()
        self.nhapGB.setPlaceholderText("Nhập giá bán")
        gridLayout.addWidget(lblGB,0,0)
        gridLayout.addWidget(self.nhapGB,0,1)

        lblGM = QLabel("Giá mua")
        self.nhapGM = QLineEdit()
        self.nhapGM.setPlaceholderText("Nhập giá mua")
        gridLayout.addWidget(lblGM, 1, 0)
        gridLayout.addWidget(self.nhapGM, 1, 1)

        lblSL = QLabel("Số lượng")
        self.nhapSL = QLineEdit()
        self.nhapSL.setPlaceholderText("Nhập số lượng")
        gridLayout.addWidget(lblSL, 2, 0)
        gridLayout.addWidget(self.nhapSL, 2, 1)

        lblThue = QLabel("Thuế")
        self.nhapThue = QLineEdit()
        self.nhapThue.setPlaceholderText("Nhập thuế")
        gridLayout.addWidget(lblThue, 3, 0)
        gridLayout.addWidget(self.nhapThue, 3, 1)

        lblCphi = QLabel("Phí giao dịch")
        self.nhapCphi = QLineEdit()
        self.nhapCphi.setPlaceholderText("Nhập phí giao dịch")
        gridLayout.addWidget(lblCphi, 4, 0)
        gridLayout.addWidget(self.nhapCphi, 4, 1)

        self.btnkq=QPushButton("Kết quả")
        self.btnkq.clicked.connect(self.kqAction)
        gridLayout.addWidget(self.btnkq,5,1)

        self.groupbox1.setLayout(gridLayout)

    def kqAction(self):
        s1=self.nhapGB.text()
        s2=self.nhapGM.text()
        s3=self.nhapSL.text()
        s4=self.nhapThue.text()
        s5=self.nhapCphi.text()
        xuly=xulyCK(s1,s2,s3,s4,s5)
        QMessageBox.about(self.btnkq, "Kết quả đầu tư chứng khoán", xuly.xuatdautuCK())

if __name__ == '__main__':
    myapp=QApplication(sys.argv)

    window=NhapCKWindow()

    myapp.exec_()
    sys.exit()