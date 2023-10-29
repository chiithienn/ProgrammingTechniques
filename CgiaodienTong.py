from CnhapChiTieu import *
from CThietLapHu import *
from Clapkehoach import *
from CgiaodienTKDT import *


class CgiaodienTong(QWidget):
    def __init__(self):
        super().__init__()

        self.setup()
        self.show()

    def setup(self):
        self.setWindowTitle("Giao diện chính")
        self.setGeometry(820, 200, 700, 450)

        self.gridLayout()

        vbox=QVBoxLayout()

        vbox.addWidget(self.groupbox1)

        self.setLayout(vbox)

    def gridLayout(self):
        self.groupbox1=QGroupBox()
        self.groupbox1.setStyleSheet('border :1px solid black')

        vbox=QVBoxLayout()
        hbox1=QHBoxLayout()
        hbox2 = QHBoxLayout()
        #Tiêu đề
        self.lblTieude=QLabel('QUẢN LÝ CHI TIÊU')
        self.lblTieude.setFont(QFont("#9Slide03 HelvetIns", 30))
        self.lblTieude.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        #Tạo nút
        self.btnLapKH=QPushButton('   Lập kế hoạch')
        self.btnTKDT=QPushButton('   Tiết kiệm - Đầu tư')
        self.btnThietlaphu=QPushButton('   Thiết lập ngân sách')
        self.btnMucdoChitieu=QPushButton('   Mức độ chi tiêu')
        #Thêm icon cho nút
        self.btnLapKH.setIcon(QIcon('plan.png'))
        self.btnTKDT.setIcon(QIcon('save.png'))
        self.btnThietlaphu.setIcon(QIcon('budget.png'))
        self.btnMucdoChitieu.setIcon(QIcon('chi tiêu.png'))
        #Font chữ
        self.btnLapKH.setFont(QFont('Calibri',15))
        self.btnTKDT.setFont(QFont('Calibri',15))
        self.btnThietlaphu.setFont(QFont('Calibri',15))
        self.btnMucdoChitieu.setFont(QFont('Calibri',15))
        #Kích cỡ
        self.btnLapKH.setMinimumHeight(50)
        self.btnTKDT.setMinimumHeight(50)
        self.btnThietlaphu.setMinimumHeight(50)
        self.btnMucdoChitieu.setMinimumHeight(50)
        #Sự kiện clicked của button
        self.btnLapKH.clicked.connect(self.lapkehoach_ACT)
        self.btnTKDT.clicked.connect(self.tietkiem_dautu_ACT)
        self.btnThietlaphu.clicked.connect(self.thietlapngansach_ACT)
        self.btnMucdoChitieu.clicked.connect(self.mucdochitieu_ACT)
        #Sắp xếp
        vbox.addWidget(self.lblTieude)
        hbox1.addWidget(self.btnLapKH)
        hbox1.addWidget(self.btnTKDT)
        hbox2.addWidget(self.btnThietlaphu)
        hbox2.addWidget(self.btnMucdoChitieu)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.groupbox1.setLayout(vbox)

    def lapkehoach_ACT(self):
        self.goi=Clapkehoach()
    def tietkiem_dautu_ACT(self):
        self.goi=CgiaodienTKDT()
    def thietlapngansach_ACT(self):
        self.goi=CThietLapHu()
    def mucdochitieu_ACT(self):
        self.goi=CnhapChiTieu()

if __name__ == '__main__':
    myapp=QApplication(sys.argv)

    window=CgiaodienTong()

    myapp.exec_()
    sys.exit()