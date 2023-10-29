from PySide2.QtWidgets import *
from PySide2.QtGui import *
import sys
from CxulyDauTu import *

class NhapKDWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setup()
        self.show()

    def setup(self):
        self.setWindowTitle("Đầu tư kinh doanh")
        self.setGeometry(400, 400, 500, 200)
        self.setMinimumSize(500, 250)
        self.setIcon()
        vbox=QVBoxLayout()

        self.gridLayout1()

        vbox.addWidget(self.groupbox1)

        self.setLayout(vbox)

    def setIcon(self):
        appIcon=QIcon('business.png')
        self.setWindowIcon(appIcon)

    def gridLayout1(self):
        self.groupbox1 = QGroupBox("Nhập thông tin kinh doanh:")
        self.groupbox1.setFont(QFont("Times", 12))

        gridLayout=QGridLayout()

        lblDthu=QLabel("Doanh thu")
        self.nhapDthu=QLineEdit()
        self.nhapDthu.setPlaceholderText("Nhập doanh thu")
        gridLayout.addWidget(lblDthu,0,0)
        gridLayout.addWidget(self.nhapDthu,0,1)

        lblCphi = QLabel("Chi phí")
        self.nhapCphi = QLineEdit()
        self.nhapCphi.setPlaceholderText("Nhập chi phí")
        gridLayout.addWidget(lblCphi, 1, 0)
        gridLayout.addWidget(self.nhapCphi, 1, 1)

        lblThue = QLabel("Thuế")
        self.nhapThue = QLineEdit()
        self.nhapThue.setPlaceholderText("Nhập thuế")
        gridLayout.addWidget(lblThue, 2, 0)
        gridLayout.addWidget(self.nhapThue, 2, 1)

        self.btnkq=QPushButton("Kết quả")
        self.btnkq.clicked.connect(self.kqAction)
        gridLayout.addWidget(self.btnkq,3,1)

        self.groupbox1.setLayout(gridLayout)

    def kqAction(self):
        s1=self.nhapDthu.text()
        s2=self.nhapCphi.text()
        s3=self.nhapThue.text()
        xuly=xulyKD(s1,s2,s3)
        QMessageBox.about(self.btnkq, "Kết quả kinh doanh", xuly.xuatdautuKD())

if __name__ == '__main__':
    myapp=QApplication(sys.argv)

    window=NhapKDWindow()

    myapp.exec_()
    sys.exit()