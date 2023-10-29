from PySide2.QtWidgets import *
from PySide2.QtGui import *
import sys
from XulyFile import *

class CxemDS(QWidget):
    def __init__(self):
        super().__init__()

        self.setup()
        self.show()

    def setup(self):
        self.setWindowTitle('Danh sách các mục lập kế hoạch chi tiêu')
        self.setGeometry(300,200,650,600)
        self.setStyleSheet('background-color:#F7F7F7')

        self.Layout1()
        self.Layout2()
        self.Layout3()
        self.Layout4()
        self.Layout5()
        self.Layout6()
        self.Layout7()

        hbox = QHBoxLayout()
        vbox1=QVBoxLayout()
        vbox2=QVBoxLayout()
        vbox3=QVBoxLayout()

        space1=QLabel()
        space2=QLabel()
        space3=QLabel()
        space4=QLabel()
        space5=QLabel()

        vbox1.addWidget(self.groupbox1)

        vbox2.addWidget(self.groupbox2)
        vbox2.addWidget(space1)
        vbox2.addWidget(self.groupbox3)
        vbox2.addWidget(space2)
        vbox2.addWidget(self.groupbox4)

        vbox3.addWidget(self.groupbox5)
        vbox3.addWidget(space3)
        vbox3.addWidget(self.groupbox6)
        vbox3.addWidget(space4)
        vbox3.addWidget(self.groupbox7)

        hbox.addLayout(vbox1)
        hbox.addWidget(space5)
        hbox.addLayout(vbox2)
        hbox.addLayout(vbox3)

        self.setLayout(hbox)

    def Layout1(self):
        self.groupbox1=QGroupBox("Thiết yếu")
        self.groupbox1.setFont(QFont("#9Slide03 Cabin Bold",12))
        self.groupbox1.setStyleSheet('background-color:#FFA36C')
        hbox=QHBoxLayout()

        self.list1 = QListWidget()
        self.list1.setStyleSheet('background-color:#FCFAFA; border :1px solid black')

        file=XulyFile()
        arr=file.docfile('dsThietYeu.txt')
        for i in arr:
            self.list1.addItem(i)

        hbox.addWidget(self.list1)
        self.groupbox1.setLayout(hbox)

    def Layout2(self):
        self.groupbox2=QGroupBox("Giáo dục")
        self.groupbox2.setFont(QFont("#9Slide03 Cabin Bold", 10))
        self.groupbox2.setStyleSheet('background-color:#C4DDFF')
        hbox=QHBoxLayout()

        self.list2 = QListWidget()
        self.list2.setStyleSheet('background-color:#FCFAFA; border :1px solid black')

        file=XulyFile()
        arr=file.docfile('dsGiaoDuc.txt')
        for i in arr:
            self.list2.addItem(i)

        hbox.addWidget(self.list2)
        self.groupbox2.setLayout(hbox)

    def Layout3(self):
        self.groupbox3=QGroupBox("Tiết kiệm")
        self.groupbox3.setFont(QFont("#9Slide03 Cabin Bold", 10))
        self.groupbox3.setStyleSheet('background-color:#F7CCAC')
        hbox=QHBoxLayout()

        self.list3 = QListWidget()
        self.list3.setStyleSheet('background-color:#FCFAFA; border :1px solid black')

        file=XulyFile()
        arr=file.docfile('dsTietKiem.txt')
        for i in arr:
            self.list3.addItem(i)

        hbox.addWidget(self.list3)
        self.groupbox3.setLayout(hbox)

    def Layout4(self):
        self.groupbox4=QGroupBox("Hưởng thụ")
        self.groupbox4.setFont(QFont("#9Slide03 Cabin Bold", 10))
        self.groupbox4.setStyleSheet('background-color:#B4E197')
        hbox=QHBoxLayout()

        self.list4 = QListWidget()
        self.list4.setStyleSheet('background-color:#FCFAFA; border :1px solid black')

        file=XulyFile()
        arr=file.docfile('dsThietYeu.txt')
        for i in arr:
            self.list4.addItem(i)

        hbox.addWidget(self.list4)
        self.groupbox4.setLayout(hbox)

    def Layout5(self):
        self.groupbox5=QGroupBox("Thiện tâm")
        self.groupbox5.setFont(QFont("#9Slide03 Cabin Bold", 10))
        self.groupbox5.setStyleSheet('background-color:#FF8080')
        hbox=QHBoxLayout()

        self.list5 = QListWidget()
        self.list5.setStyleSheet('background-color:#FCFAFA; border :1px solid black')

        file=XulyFile()
        arr=file.docfile('dsThienTam.txt')
        for i in arr:
            self.list5.addItem(i)

        hbox.addWidget(self.list5)
        self.groupbox5.setLayout(hbox)

    def Layout6(self):
        self.groupbox6=QGroupBox("Thu nhập")
        self.groupbox6.setFont(QFont("#9Slide03 Cabin Bold", 10))
        self.groupbox6.setStyleSheet('background-color:#FBCAFF')
        hbox=QHBoxLayout()

        self.list6 = QListWidget()
        self.list6.setStyleSheet('background-color:#FCFAFA; border :1px solid black')

        file=XulyFile()
        arr=file.docfile('dsThuNhap.txt')
        for i in arr:
            self.list6.addItem(i)

        hbox.addWidget(self.list6)
        self.groupbox6.setLayout(hbox)

    def Layout7(self):
        self.groupbox7=QGroupBox("Hưởng thụ")
        self.groupbox7.setFont(QFont("#9Slide03 Cabin Bold", 10))
        self.groupbox7.setStyleSheet('background-color:#FFFEB7')
        hbox=QHBoxLayout()

        self.list7 = QListWidget()
        self.list7.setStyleSheet('background-color:#FCFAFA; border :1px solid black')

        file=XulyFile()
        arr=file.docfile('dsThietYeu.txt')
        for i in arr:
            self.list7.addItem(i)

        hbox.addWidget(self.list7)
        self.groupbox7.setLayout(hbox)

if __name__ == '__main__':
    myapp=QApplication(sys.argv)

    window=CxemDS()

    myapp.exec_()