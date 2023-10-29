from CbieudoBar import *

class CnhapChiTieu(QWidget):
    def __init__(self):
        super().__init__()

        self.setup()
        self.show()

    def setup(self):
        self.setWindowTitle("Cảnh báo chi tiêu")
        self.setGeometry(300, 200, 500, 650)

        vbox = QVBoxLayout()

        label = QLabel('NHẬP CHI TIÊU')
        label.setFont(QFont("#9Slide03 HelvetIns", 20))
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.gridLayout1()
        self.gridLayout2()
        self.gridLayout3()
        self.gridLayout4()
        self.gridLayout5()
        self.gridLayout6()
        self.ButtonKetQua()

        vbox.addWidget(label)
        vbox.addWidget(self.groupbox1)
        vbox.addWidget(self.groupbox2)
        vbox.addWidget(self.groupbox3)
        vbox.addWidget(self.groupbox4)
        vbox.addWidget(self.groupbox5)
        vbox.addWidget(self.groupbox6)
        vbox.addWidget(self.groupbox7)

        self.setLayout(vbox)

    def gridLayout1(self):
        self.groupbox1 = QGroupBox()

        grid=QGridLayout()

        self.label = QLabel("Thiết yếu")
        self.label.setFont(QFont('#9Slide03 Cabin Bold', 13))
        icon1 = QIcon('thietyeu.png')
        label1 = QLabel(self)
        label1.setMaximumWidth(60)
        pixmap1 = icon1.pixmap(40, 40)
        label1.setPixmap(pixmap1)

        self.nhapThietyeu = QLineEdit()
        self.nhapThietyeu.setMaximumSize(250,30)
        self.nhapThietyeu.setFont(QFont("Arial",10))
        self.nhapThietyeu.setAlignment(Qt.AlignHCenter)
        self.nhapThietyeu.setPlaceholderText("Nhập tổng chi tiêu thiết yếu")
        file = XulyFile
        ptu = file.docfile(self, 'DS_chi_tieu.txt')
        self.nhapThietyeu.setText(ptu[0])

        grid.addWidget(label1,0,0)
        grid.addWidget(self.label,0,1)
        grid.addWidget(self.nhapThietyeu,0,3)

        self.groupbox1.setLayout(grid)
    def gridLayout2(self):
        self.groupbox2 = QGroupBox()

        grid=QGridLayout()

        self.label = QLabel("Giáo dục")
        self.label.setFont(QFont('#9Slide03 Cabin Bold', 13))
        icon1 = QIcon('education.png')
        label1 = QLabel(self)
        label1.setMaximumWidth(60)
        pixmap1 = icon1.pixmap(40, 40)
        label1.setPixmap(pixmap1)

        self.nhapGiaoduc = QLineEdit()
        self.nhapGiaoduc.setMaximumSize(250,30)
        self.nhapGiaoduc.setFont(QFont("Arial",10))
        self.nhapGiaoduc.setAlignment(Qt.AlignHCenter)
        self.nhapGiaoduc.setPlaceholderText("Nhập tổng chi tiêu giáo dục")
        file = XulyFile
        ptu = file.docfile(self, 'DS_chi_tieu.txt')
        self.nhapGiaoduc.setText(ptu[1])

        grid.addWidget(label1,0,0)
        grid.addWidget(self.label,0,1)
        grid.addWidget(self.nhapGiaoduc,0,3)

        self.groupbox2.setLayout(grid)
    def gridLayout3(self):
        self.groupbox3 = QGroupBox()

        grid=QGridLayout()

        self.label = QLabel("Tiết kiệm")
        self.label.setFont(QFont('#9Slide03 Cabin Bold', 13))
        icon1 = QIcon('save.png')
        label1 = QLabel(self)
        label1.setMaximumWidth(60)
        pixmap1 = icon1.pixmap(40, 40)
        label1.setPixmap(pixmap1)

        self.nhapTietkiem = QLineEdit()
        self.nhapTietkiem.setMaximumSize(250,30)
        self.nhapTietkiem.setFont(QFont("Arial",10))
        self.nhapTietkiem.setAlignment(Qt.AlignHCenter)
        self.nhapTietkiem.setPlaceholderText("Nhập tổng chi tiêu tiết kiệm")
        file = XulyFile
        ptu = file.docfile(self, 'DS_chi_tieu.txt')
        self.nhapTietkiem.setText(ptu[2])

        grid.addWidget(label1,0,0)
        grid.addWidget(self.label,0,1)
        grid.addWidget(self.nhapTietkiem,0,3)

        self.groupbox3.setLayout(grid)
    def gridLayout4(self):
        self.groupbox4 = QGroupBox()

        grid=QGridLayout()

        self.label = QLabel("Hưởng thụ")
        self.label.setFont(QFont('#9Slide03 Cabin Bold', 13))
        icon1 = QIcon('enjoy.png')
        label1 = QLabel(self)
        label1.setMaximumWidth(60)
        pixmap1 = icon1.pixmap(40, 40)
        label1.setPixmap(pixmap1)

        self.nhapHuongthu = QLineEdit()
        self.nhapHuongthu.setMaximumSize(250,30)
        self.nhapHuongthu.setFont(QFont("Arial",10))
        self.nhapHuongthu.setAlignment(Qt.AlignHCenter)
        self.nhapHuongthu.setPlaceholderText("Nhập tổng chi tiêu hưởng thụ")
        file = XulyFile
        ptu = file.docfile(self, 'DS_chi_tieu.txt')
        self.nhapHuongthu.setText(ptu[3])

        grid.addWidget(label1,0,0)
        grid.addWidget(self.label,0,1)
        grid.addWidget(self.nhapHuongthu,0,3)

        self.groupbox4.setLayout(grid)
    def gridLayout5(self):
        self.groupbox5 = QGroupBox()

        grid=QGridLayout()

        self.label = QLabel("Đầu tư")
        self.label.setFont(QFont('#9Slide03 Cabin Bold', 13))
        icon1 = QIcon('investment.png')
        label1 = QLabel(self)
        label1.setMaximumWidth(60)
        pixmap1 = icon1.pixmap(40, 40)
        label1.setPixmap(pixmap1)

        self.nhapDautu = QLineEdit()
        self.nhapDautu.setMaximumSize(250,30)
        self.nhapDautu.setFont(QFont("Arial",10))
        self.nhapDautu.setAlignment(Qt.AlignHCenter)
        self.nhapDautu.setPlaceholderText("Nhập tổng chi tiêu đầu tư")
        file = XulyFile
        ptu = file.docfile(self, 'DS_chi_tieu.txt')
        self.nhapDautu.setText(ptu[4])

        grid.addWidget(label1,0,0)
        grid.addWidget(self.label,0,1)
        grid.addWidget(self.nhapDautu,0,3)

        self.groupbox5.setLayout(grid)
    def gridLayout6(self):
        self.groupbox6 = QGroupBox()

        grid=QGridLayout()

        self.label = QLabel("Thiện tâm")
        self.label.setFont(QFont('#9Slide03 Cabin Bold', 13))
        icon1 = QIcon('care.png')
        label1 = QLabel(self)
        label1.setMaximumWidth(60)
        pixmap1 = icon1.pixmap(40, 40)
        label1.setPixmap(pixmap1)

        self.nhapThientam = QLineEdit()
        self.nhapThientam.setMaximumSize(250,30)
        self.nhapThientam.setFont(QFont("Arial",10))
        self.nhapThientam.setAlignment(Qt.AlignHCenter)
        self.nhapThientam.setPlaceholderText("Nhập tổng chi tiêu thiện tâm")
        file = XulyFile
        ptu = file.docfile(self, 'DS_chi_tieu.txt')
        self.nhapThientam.setText(ptu[5])

        grid.addWidget(label1,0,0)
        grid.addWidget(self.label,0,1)
        grid.addWidget(self.nhapThientam,0,3)

        self.groupbox6.setLayout(grid)

    def ButtonKetQua(self):
        self.groupbox7 = QGroupBox()
        grid=QGridLayout()

        self.btnKQ=QPushButton('XEM KẾT QUẢ')
        self.btnKQ.setMaximumSize(200,50)
        self.btnKQ.setFont(QFont('#9Slide03 Cabin Bold',12))
        self.btnKQ.clicked.connect(self.ketquaAction)

        grid.addWidget(self.btnKQ)
        self.groupbox7.setLayout(grid)
    def ketquaAction(self):
        a1=eval(self.nhapThietyeu.text())
        a2=eval(self.nhapGiaoduc.text())
        a3=eval(self.nhapTietkiem.text())
        a4=eval(self.nhapHuongthu.text())
        a5=eval(self.nhapDautu.text())
        a6=eval(self.nhapThientam.text())
        arr = [a1, a2, a3, a4, a5, a6]

        file = XulyFile()
        file.xoads('DS_chi_tieu.txt', '')
        for i in range(len(arr)):
            file.luufile('DS_chi_tieu.txt', str(arr[i]))
        self.goi = CbieudoBar()


if __name__ == '__main__':
    myapp=QApplication(sys.argv)

    window=CnhapChiTieu()

    myapp.exec_()
    sys.exit()