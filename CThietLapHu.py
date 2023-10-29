from CbieudoPIE import *
from XulyFile import *

class CThietLapHu(QWidget):
    def __init__(self):
        super().__init__()

        self.setup()
        self.show()

    def setup(self):
        self.setWindowTitle("Thiết lập các hũ")
        self.setGeometry(300, 200, 450, 600)
        self.setMinimumSize(450,600)
        self.setMaximumSize(450,600)

        self.spin_box1()
        self.spin_box2()
        self.spin_box3()
        self.spin_box4()
        self.spin_box5()
        self.spin_box6()
        self.ButtonLuu()

        vbox=QVBoxLayout()

        vbox.addWidget(self.groupbox1)
        vbox.addWidget(self.groupbox2)
        vbox.addWidget(self.groupbox3)
        vbox.addWidget(self.groupbox4)
        vbox.addWidget(self.groupbox5)
        vbox.addWidget(self.groupbox6)
        vbox.addWidget(self.groupbox7)

        self.setLayout(vbox)

    #--------------------------------------------------------------
    def spin_box1(self):
        self.groupbox1 = QGroupBox('Đơn vị: vnđ')
        self.groupbox1.setFont(QFont("Times", 10))
        self.groupbox1.setAlignment(Qt.AlignRight)

        gridLayout = QGridLayout()

        self.label = QLabel("Thiết yếu")
        self.label.setFont(QFont('#9Slide03 Cabin Bold',13))
        icon1 = QIcon('thietyeu.png')
        label1 = QLabel(self)
        label1.setMaximumWidth(60)
        pixmap1 = icon1.pixmap(40, 40)
        label1.setPixmap(pixmap1)

        self.text1 = QLineEdit()
        self.text1.setFont(QFont("Arial",10))
        self.text1.setMaximumWidth(200)
        self.text1.setAlignment(Qt.AlignHCenter)
        file=XulyFile
        ptu=file.docfile(self,'Gia_tri_cac_hu.txt')
        self.text1.setText(ptu[0])

        gridLayout.addWidget(label1,0,0)
        gridLayout.addWidget(self.label, 0, 1)
        gridLayout.addWidget(self.text1,0,2)

        self.groupbox1.setLayout(gridLayout)
    def spin_box2(self):
        self.groupbox2 = QGroupBox()

        gridLayout = QGridLayout()

        self.label = QLabel("Giáo dục")
        self.label.setFont(QFont('#9Slide03 Cabin Bold', 13))
        icon1 = QIcon('education.png')
        label1 = QLabel(self)
        label1.setMaximumWidth(60)
        pixmap1 = icon1.pixmap(40, 40)
        label1.setPixmap(pixmap1)

        self.text2 = QLineEdit()
        # self.spinbox.setMaximum(100)
        self.text2.setFont(QFont("Arial", 10))
        self.text2.setMaximumWidth(200)
        self.text2.setAlignment(Qt.AlignHCenter)
        file = XulyFile
        ptu = file.docfile(self, 'Gia_tri_cac_hu.txt')
        self.text2.setText(ptu[1])

        gridLayout.addWidget(label1, 0, 0)
        gridLayout.addWidget(self.label,0,1)
        gridLayout.addWidget(self.text2,0,2)

        self.groupbox2.setLayout(gridLayout)
    def spin_box3(self):
        self.groupbox3 = QGroupBox()

        gridLayout = QGridLayout()

        self.label = QLabel("Tiết kiệm")
        self.label.setFont(QFont('#9Slide03 Cabin Bold', 13))
        icon1 = QIcon('save.png')
        label1 = QLabel(self)
        label1.setMaximumWidth(60)
        pixmap1 = icon1.pixmap(40, 40)
        label1.setPixmap(pixmap1)

        self.text3 = QLineEdit()
        # self.spinbox.setMaximum(100)
        self.text3.setFont(QFont("Arial", 10))
        self.text3.setMaximumWidth(200)
        self.text3.setAlignment(Qt.AlignHCenter)
        file = XulyFile
        ptu = file.docfile(self, 'Gia_tri_cac_hu.txt')
        self.text3.setText(ptu[2])

        gridLayout.addWidget(label1,0,0)
        gridLayout.addWidget(self.label,0,1)
        gridLayout.addWidget(self.text3,0,2)

        self.groupbox3.setLayout(gridLayout)
    def spin_box4(self):
        self.groupbox4 = QGroupBox()

        gridLayout = QGridLayout()

        self.label = QLabel("Hưởng thụ")
        self.label.setFont(QFont('#9Slide03 Cabin Bold', 13))
        icon1 = QIcon('enjoy.png')
        label1 = QLabel(self)
        label1.setMaximumWidth(60)
        pixmap1 = icon1.pixmap(40, 40)
        label1.setPixmap(pixmap1)

        self.text4 = QLineEdit()
        # self.spinbox.setMaximum(100)
        self.text4.setFont(QFont("Arial", 10))
        self.text4.setMaximumWidth(200)
        self.text4.setAlignment(Qt.AlignHCenter)
        file = XulyFile
        ptu = file.docfile(self, 'Gia_tri_cac_hu.txt')
        self.text4.setText(ptu[3])

        gridLayout.addWidget(label1,0,0)
        gridLayout.addWidget(self.label,0,1)
        gridLayout.addWidget(self.text4,0,2)

        self.groupbox4.setLayout(gridLayout)
    def spin_box5(self):
        self.groupbox5 = QGroupBox()

        gridLayout = QGridLayout()

        self.label = QLabel("Đầu tư")
        self.label.setFont(QFont('#9Slide03 Cabin Bold', 13))
        icon1 = QIcon('investment.png')
        label1 = QLabel(self)
        label1.setMaximumWidth(60)
        pixmap1 = icon1.pixmap(40, 40)
        label1.setPixmap(pixmap1)

        self.text5 = QLineEdit()
        self.text5.setFont(QFont("Arial", 10))
        self.text5.setMaximumWidth(200)
        self.text5.setAlignment(Qt.AlignHCenter)
        file = XulyFile
        ptu = file.docfile(self, 'Gia_tri_cac_hu.txt')
        self.text5.setText(ptu[4])

        gridLayout.addWidget(label1,0,0)
        gridLayout.addWidget(self.label,0,1)
        gridLayout.addWidget(self.text5,0,2)

        self.groupbox5.setLayout(gridLayout)
    def spin_box6(self):
        self.groupbox6 = QGroupBox()

        gridLayout = QGridLayout()

        self.label = QLabel("Thiện tâm")
        self.label.setFont(QFont('#9Slide03 Cabin Bold', 13))
        icon1 = QIcon('care.png')
        label1 = QLabel(self)
        label1.setMaximumWidth(60)
        pixmap1 = icon1.pixmap(40, 40)
        label1.setPixmap(pixmap1)

        self.text6 = QLineEdit()
        # self.spinbox.setMaximum(100)
        self.text6.setFont(QFont("Arial", 10))
        self.text6.setMaximumWidth(200)
        self.text6.setAlignment(Qt.AlignHCenter)
        file = XulyFile
        ptu = file.docfile(self, 'Gia_tri_cac_hu.txt')
        self.text6.setText(ptu[5])

        gridLayout.addWidget(label1,0,0)
        gridLayout.addWidget(self.label,0,1)
        gridLayout.addWidget(self.text6,0,2)

        self.groupbox6.setLayout(gridLayout)
    def ButtonLuu(self):
        self.groupbox7 = QGroupBox()
        grid=QGridLayout()

        self.btnLuu=QPushButton('Lưu')
        self.btnLuu.setMinimumSize(20,50)
        self.btnLuu.setFont(QFont('9Slide03 Cabin Bold',15))
        self.btnLuu.clicked.connect(self.luuAction)

        grid.addWidget(self.btnLuu)
        self.groupbox7.setLayout(grid)

    def spin_value(self):
        self.label.setText("Current Value Is : " + str(self.spinbox.value()))
    def luuAction(self):
        a1 = eval(self.text1.text())
        a2 = eval(self.text2.text())
        a3 = eval(self.text3.text())
        a4 = eval(self.text4.text())
        a5 = eval(self.text5.text())
        a6 = eval(self.text6.text())
        arr=[a1,a2,a3,a4,a5,a6]

        if (a1 + a2 + a3 + a4 + a5 + a6) == 0:
            QMessageBox.warning(self, "Thông báo",
                                "Lỗi! Không được để trống toàn bộ.", QMessageBox.Ok)
            #myapp.quit()
        else:
            file = XulyFile()
            file.xoads('Gia_tri_cac_hu.txt', '')
            for i in range(len(arr)):
                file.luufile('Gia_tri_cac_hu.txt', str(arr[i]))
            self.goi = giaodienPCCT(a1, a2, a3, a4, a5, a6)

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    window = CThietLapHu()
    myapp.exec_()
    sys.exit()