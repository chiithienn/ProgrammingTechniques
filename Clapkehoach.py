from CxemDS_kehoach import *

class Clapkehoach(QWidget):
    def __init__(self):
        super().__init__()

        self.setup_UI()
        self.show()

    def setup_UI(self):
        self.setWindowTitle("Lập kế hoạch chi tiêu")
        self.setGeometry(1000, 200, 700, 500)
        self.setMaximumSize(700,550)
        self.setMinimumSize(700,550)
        self.setWindowIcon(QIcon('plan.png'))

        self.gridLayout1()
        self.gridLayout2()
        self.gridLayout3()
        vbox=QVBoxLayout()

        #Tiêu đề 1
        tieude1=QLabel("CÁC MỤC QUẢN LÝ CHI TIÊU")
        tieude1.setFont(QFont("#9Slide03 HelvetIns",20))
        tieude1.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)

        self.space=QLabel()
        self.setMaximumHeight(20)
        self.space.setAlignment(Qt.AlignTop|Qt.AlignLeft)
        space2=QLabel()

        # Tiêu đề 2
        tieude2 = QLabel("CÁC MỤC CHI TIÊU")
        tieude2.setFont(QFont("#9Slide03 HelvetIns", 20))
        tieude2.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)

        # Sắp xếp
        vbox.addWidget(tieude1)
        vbox.addWidget(self.groupbox1)
        vbox.addWidget(self.space)
        vbox.addWidget(tieude2)
        vbox.addWidget(self.groupbox2)
        vbox.addWidget(space2)
        vbox.addWidget(self.groupbox3)

        self.setLayout(vbox)

    def gridLayout1(self):
        self.groupbox1 = QGroupBox("Chọn mục:")
        self.groupbox1.setFont(QFont("Times", 12))

        gridLayout = QGridLayout()

        #ComboBox 1
        self.cbb1=QComboBox()
        self.cbb1.setFont(QFont('Times',12))
        self.cbb1.setMinimumHeight(50)
        self.cbb1.addItems(['Thiết yếu','Giáo dục','Tiết kiệm','Hưởng thụ','Thiện tâm','Thu nhập','Vay nợ'])

        #Button Chọn
        btnChon=QPushButton("Chọn")
        btnChon.setFont(QFont('Times',12))
        btnChon.setMinimumHeight(50)
        btnChon.clicked.connect(self.chonAction)

        gridLayout.addWidget(self.cbb1,0,0)
        gridLayout.addWidget(btnChon,0,1)

        self.groupbox1.setLayout(gridLayout)
    def gridLayout2(self):
        self.groupbox2 = QGroupBox("Chọn mục:")
        self.groupbox2.setFont(QFont("Times", 12))

        gridLayout=QGridLayout()

        #ComboBox 2
        self.cbb2=QComboBox()
        self.cbb2.setFont(QFont('Times',12))
        self.cbb2.setMinimumHeight(50)

        #Button Thêm & Xóa
        btnThem=QPushButton("Thêm")
        btnThem.setFont(QFont('Times',12))
        btnThem.setMinimumHeight(50)
        btnThem.clicked.connect(self.themAction)
        btnXoa=QPushButton("Xóa")
        btnXoa.setFont(QFont('Times', 12))
        btnXoa.setMinimumHeight(50)
        btnXoa.clicked.connect(self.xoaAction)

        #Nhập
        self.nhapThemmuc=QLineEdit()
        self.nhapThemmuc.setFont(QFont('Times',12))
        self.nhapThemmuc.setMinimumHeight(50)
        self.nhapThemmuc.setAlignment(Qt.AlignVCenter|Qt.AlignLeft)
        self.nhapThemmuc.setPlaceholderText("Nhập mục cần thêm")

        gridLayout.addWidget(self.cbb2, 0, 0)
        gridLayout.addWidget(btnThem, 1, 1)
        gridLayout.addWidget(btnXoa, 0, 1)
        gridLayout.addWidget(self.nhapThemmuc,1,0)

        self.groupbox2.setLayout(gridLayout)

    def gridLayout3(self):
        self.groupbox3 = QGroupBox()
        hbox=QHBoxLayout()

        self.xemDS = QPushButton("Cập nhật danh sách")
        self.setFont(QFont('Times', 12))
        self.xemDS.setMinimumHeight(50)
        self.xemDS.setMaximumWidth(500)
        self.xemDS.clicked.connect(self.updateDSAction)

        hbox.addWidget(self.xemDS)

        self.groupbox3.setLayout(hbox)

    def chonAction(self):
        a1=self.cbb1.currentText()
        file = XulyFile()
        if a1 == 'Thiết yếu':
            ds = file.docfile('dsThietYeu.txt')
            self.path='dsThietYeu.txt'
            self.space.setText('Bạn đã chọn mục THIẾT YẾU')
        if a1 == 'Giáo dục':
            ds = file.docfile('dsGiaoDuc.txt')
            self.path='dsGiaoDuc.txt'
            self.space.setText('Bạn đã chọn mục GIÁO DỤC')
        if a1 == 'Tiết kiệm':
            ds = file.docfile('dsTietKiem.txt')
            self.path='dsTietKiem.txt'
            self.space.setText('Bạn đã chọn mục TIẾT KIỆM')
        if a1 == 'Thu nhập':
            ds = file.docfile('dsThuNhap.txt')
            self.path='dsThuNhap.txt'
            self.space.setText('Bạn đã chọn mục THU NHẬP')
        if a1 == 'Hưởng thụ':
            ds = file.docfile('dsHuongThu.txt')
            self.path='dsHuongThu.txt'
            self.space.setText('Bạn đã chọn mục HƯỞNG THỤ')
        if a1 == 'Thiện tâm':
            ds = file.docfile('dsThienTam.txt')
            self.path='dsThienTam.txt'
            self.space.setText('Bạn đã chọn mục THIỆN TÂM')
        if a1 == 'Vay nợ':
            ds = file.docfile('dsVayNo.txt')
            self.path='dsVayNo.txt'
            self.space.setText('Bạn đã chọn mục VAY NỢ')
        self.cbb2.clear()
        self.cbb2.addItems(ds)
        return self.path #Dùng cho hàm thêm, xóa
    def themAction(self):
        thongbao=QMessageBox.question(self,'Xác nhận','Bạn có muốn thêm mục mới?',QMessageBox.Yes|QMessageBox.No)
        if thongbao==QMessageBox.Yes:
            #Lưu lại giá  trị mới nhập trong textbox
            path = self.chonAction()
            s = [self.nhapThemmuc.text()]
            file = XulyFile()
            file.luufile(path, s)
            #Cập nhật lại danh sách
            ds = file.docfile(path)
            self.cbb2.clear()
            self.cbb2.addItems(ds)
            thongbao2=QMessageBox.information(self,'Thông báo','Bạn đã thêm mục thành công',QMessageBox.Ok)
        self.nhapThemmuc.setText('')

    def xoaAction(self):
        hoi=QMessageBox.question(self,'Xác nhận','Bạn có muốn xóa mục đã chọn',QMessageBox.Yes|QMessageBox.No)
        if hoi==QMessageBox.Yes:
            xoa=self.cbb2.currentText()
            path=self.chonAction()
            file=XulyFile()
            ds1=file.docfile(path)
            ds1.remove(xoa)
            file.xoads(path, ds1)
            ds2 = file.docfile(path)
            self.cbb2.clear()
            self.cbb2.addItems(ds2)
            thongbao=QMessageBox.information(self,'Thông báo','Bạn đã xóa mục thành công',QMessageBox.Ok)
    def updateDSAction(self):
        self.goi=CxemDS()

if __name__ == '__main__':
    myapp=QApplication(sys.argv)

    window=Clapkehoach()

    myapp.exec_()