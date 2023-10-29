from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtCharts import *
import sys

class giaodienPCCT(QMainWindow):
    def __init__(self,a1,a2,a3,a4,a5,a6):
        super().__init__()
        self.a1=a1
        self.a2=a2
        self.a3=a3
        self.a4=a4
        self.a5=a5
        self.a6=a6

        self.setWindowTitle("Phân chia chi tiêu")
        self.setGeometry(770, 200, 850, 600)
        self.setStyleSheet('background-color:grey')

        self.create_piechart(self.a1,self.a2,self.a3,self.a4,self.a5,self.a6)

        self.show()

    def create_piechart(self,a1,a2,a3,a4,a5,a6):
        series=QtCharts.QPieSeries()
        s=(100/(a1+a2+a3+a4+a5+a6))
        text1 = 'Thiết yếu ' + str(round(a1*s,2)) + '%'
        text2 = 'Giáo dục ' + str(round(a2*s,2)) + '%'
        text3 = 'Tiết kiệm ' + str(round(a3*s,2)) + '%'
        text4 = 'Hưởng thụ ' + str(round(a4*s,2)) + '%'
        text5 = 'Đầu tư ' + str(round(a5*s,2)) + '%'
        text6 = 'Thiện tâm ' + str(round(a6*s,2)) + '%'

        series.append(text1,a1)
        series.append(text2,a2)
        series.append(text3, a3)
        series.append(text4, a4)
        series.append(text5, a5)
        series.append(text6, a6)

        #tách bánh
        #slice=QtCharts.QPieSlice()

        slice = series.slices()[0]
        slice.setExploded(True)
        slice.setLabelVisible(True)
        slice.setPen(QPen(Qt.black, 3))
        slice.setBrush(QColor('#40DFEF'))

        slice = series.slices()[1]
        slice.setExploded(True)
        slice.setLabelVisible(True)
        slice.setPen(QPen(Qt.black, 3))
        slice.setBrush(QColor('#B9F8D3'))

        slice = series.slices()[2]
        slice.setExploded(True)
        slice.setLabelVisible(True)
        slice.setPen(QPen(Qt.black, 3))
        slice.setBrush(QColor('#FFFBE7'))

        slice = series.slices()[3]
        slice.setExploded(True)
        slice.setLabelVisible(True)
        slice.setPen(QPen(Qt.black, 3))
        slice.setBrush(QColor('#E78EA9'))

        slice = series.slices()[4]
        slice.setExploded(True)
        slice.setLabelVisible(True)
        slice.setPen(QPen(Qt.black, 3))
        slice.setBrush(QColor('#A85CF9'))

        slice = series.slices()[5]
        slice.setExploded(True)
        slice.setLabelVisible(True)
        slice.setPen(QPen(Qt.black, 3))
        slice.setBrush(QColor('#FF7777'))

        chart=QtCharts.QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        chart.setTitle("THIẾT LẬP CÁC HŨ")
        #chart.setFont(QFont('#9Slide03 HelvetIns',1000000))
        chart.setTitleFont(QFont('#9Slide03 HelvetIns',20))

        chartview=QtCharts.QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chartview)


if __name__ == '__main__':
    myapp=QApplication(sys.argv)

    window=giaodienPCCT(30,20,20,70,50,10)

    myapp.exec_()
    sys.exit()