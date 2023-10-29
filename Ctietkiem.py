from PySide2.QtWidgets import *
from PySide2.QtGui import *
import sys
from CxulyTietKiem import *

class TKWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setIcon()
        self.setup_UI()

        self.show()

    def setup_UI(self):
        self.setWindowTitle("Quản lý chi tiêu tiết kiệm")
        self.setGeometry(900, 400, 500, 200)
        self.setMinimumSize(500, 500)

        self.gridLayout1()
        self.gridLayout2()
        self.gridLayout3()
        vbox=QVBoxLayout()

        self.lblspace1=QLabel("")
        self.lblspace2 = QLabel("")
        self.lblspace3=QLabel("")

        tieude = QLabel("QUẢN LÝ TIẾT KIỆM")
        tieude.setFont(QFont("#9Slide03 HelvetIns", 18))
        tieude.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        vbox.addWidget(tieude)

        vbox.addWidget(self.groupbox1)#
        vbox.addWidget(self.lblspace1)
        vbox.addWidget(self.groupbox2)#
        vbox.addWidget(self.lblspace2)
        vbox.addWidget(self.groupbox3)#

        self.btnDongY=QPushButton("Đồng ý")
        self.btnDongY.setFont(QFont("Times",12))
        self.btnDongY.setMinimumHeight(30)
        self.btnDongY.clicked.connect(self.aboutBox)
        vbox.addWidget(self.btnDongY)
        vbox.addWidget(self.lblspace3)

        self.setLayout(vbox)

    def setIcon(self):
        appIcon=QIcon('money.png')
        self.setWindowIcon(appIcon)
    def gridLayout1(self):
        self.groupbox1 = QGroupBox("Chọn mục tiết kiệm:")
        self.groupbox1.setFont(QFont("Times", 12))

        gridLayout=QGridLayout()

        self.cbb1 = QComboBox()
        self.cbb1.addItems(
            ["Tích lũy/Tiết kiệm định kỳ", "Gửi tiết kiệm ngân hàng (Cố định)", "Gửi tiết kiệm ngân hàng (Định kỳ)"])
        btnChon = QPushButton("Chọn")
        btnChon.clicked.connect(self.chonMuc)
        gridLayout.addWidget(self.cbb1,0,0)
        gridLayout.addWidget(btnChon,0,1)

        self.groupbox1.setLayout(gridLayout)
    def gridLayout2(self):
        self.groupbox2 = QGroupBox("Tiết kiệm theo:")
        self.groupbox2.setFont(QFont("Times", 12))

        gridLayout=QGridLayout()

        self.cbbTime=QComboBox()
        #self.cbbTime.addItems(["Ngày","Tháng","Năm"])
        btnChonTime=QPushButton("Chọn")
        btnChonTime.clicked.connect(self.chonTime)
        gridLayout.addWidget(self.cbbTime,0,0)
        gridLayout.addWidget(btnChonTime,0,1)

        self.groupbox2.setLayout(gridLayout)
    def gridLayout3(self):
        self.groupbox3 = QGroupBox("Nhập:")
        self.groupbox3.setFont(QFont("Times", 12))

        gridLayout=QGridLayout()

        lbl1=QLabel("Số tiền")
        lbl2=QLabel("Thời gian")
        lbl3=QLabel("Lãi suất")
        gridLayout.addWidget(lbl1,0,0)
        gridLayout.addWidget(lbl2,1,0)
        gridLayout.addWidget(lbl3,2,0)

        self.nhapMoney=QLineEdit()
        self.nhapMoney.setPlaceholderText("Nhập số tiền")
        gridLayout.addWidget(self.nhapMoney,0,1)

        self.nhapTime=QLineEdit()
        self.nhapTime.setPlaceholderText("Nhập thời gian")
        gridLayout.addWidget(self.nhapTime,1,1)

        self.nhapLS=QLineEdit()
        self.nhapLS.setPlaceholderText("Nhập lãi suất")
        gridLayout.addWidget(self.nhapLS,2,1)

        self.groupbox3.setLayout(gridLayout)

    def chonMuc(self):
        a1=self.cbb1.currentText()
        if a1=="Tích lũy/Tiết kiệm định kỳ":
            self.lblspace1.setText("Đã chọn mục: Tích lũy/Tiết kiệm định kỳ")
            number=1
            self.nhapLS.setMaxLength(0)
            self.nhapLS.setPlaceholderText("Không thể nhập")
            self.cbbTime.clear()
            self.cbbTime.addItems(["Ngày", "Tháng", "Năm"])
        if a1=="Gửi tiết kiệm ngân hàng (Cố định)":
            self.lblspace1.setText("Gửi tiết kiệm ngân hàng (Cố định)")
            number=2
            self.nhapLS.setMaxLength(50)
            self.nhapLS.setPlaceholderText("Mời nhập lãi suất")
            self.cbbTime.clear()
            self.cbbTime.addItems(["Tháng", "Năm"])
        if a1=="Gửi tiết kiệm ngân hàng (Định kỳ)":
            self.lblspace1.setText("Gửi tiết kiệm ngân hàng (Định kỳ)")
            number=3
            self.nhapLS.setMaxLength(50)
            self.nhapLS.setPlaceholderText("Mời nhập lãi suất")
            self.cbbTime.clear()
            self.cbbTime.addItems(["Tháng", "Năm"])
        print("Đã click chọn mục 1")
        return number
    def chonTime(self):
        a2=self.cbbTime.currentText()
        if a2=="Ngày":
            self.lblspace2.setText("Đã chọn mục: Ngày")
            num=1
        if a2=="Tháng":
            self.lblspace2.setText("Đã chọn mục: Tháng")
            num=2
        if a2=="Năm":
            self.lblspace2.setText("Đã chọn mục: Năm")
            num=3
        return num

    def aboutBox(self):
        number = self.chonMuc()
        num = self.chonTime()
        if number == 1:
            self.s1 = self.nhapMoney.text()
            self.s2 = self.nhapTime.text()
            xuly = CtienTK(0, eval(self.s1), eval(self.s2), num)
            QMessageBox.about(self.btnDongY, "Thông tin", xuly.xuatTK())
        if number == 2:
            self.s1 = self.nhapMoney.text()
            self.s2 = self.nhapTime.text()
            self.s3 = self.nhapLS.text()
            xuly = CguiNH(0, eval(self.s1), eval(self.s2), self.s3,num)
            QMessageBox.about(self.btnDongY, "Thông tin", xuly.xuatTKNH())
        if number == 3:
            self.s1 = self.nhapMoney.text()
            self.s2 = self.nhapTime.text()
            self.s3 = self.nhapLS.text()
            xuly = CguiNH(0, eval(self.s1), eval(self.s2), self.s3,num)
            QMessageBox.about(self.btnDongY, "Thông tin", xuly.xuatTKDK())

if __name__ == '__main__':
    myapp=QApplication(sys.argv)

    window=TKWindow()

    myapp.exec_()
    sys.exit()