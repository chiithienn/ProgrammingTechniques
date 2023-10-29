from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtCharts import *
import sys
from XulyFile import *

class CbieudoBar(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setup()
        self.show()

    def setup(self):
        self.setWindowTitle("Biểu đồ Bar về mức chi so với giới hạn ngân sách")
        self.setGeometry(820, 200, 800, 650)
        self.setStyleSheet('background-color:grey')

        self.create_bar()

    def create_bar(self):
        set0 = QtCharts.QBarSet("Ngân sách")
        set0.setBrush(QColor('#6BCB77'))
        set1 = QtCharts.QBarSet("Chi tiêu")
        set1.setBrush(QColor('#FF6B6B'))

        file=XulyFile()
        arr=file.docfile('Gia_tri_cac_hu.txt')
        list=file.docfile('DS_chi_tieu.txt')

        set0 << eval(arr[0]) << eval(arr[1]) << eval(arr[2]) << eval(arr[3]) << eval(arr[4]) << eval(arr[5])
        set1 << eval(list[0]) << eval(list[1]) << eval(list[2]) << eval(list[3]) << eval(list[4]) << eval(list[5])

        series = QtCharts.QBarSeries()
        series.append(set0)
        series.append(set1)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setTitle("BIỂU ĐỒ SO SÁNH CHI TIÊU SO VỚI NGÂN SÁCH")
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        categories = ["Thiết yếu", "Giáo dục", "Tiết kiệm", "Hưởng thụ", "Đầu tư", "Thiện tâm"]
        axis = QtCharts.QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartView = QtCharts.QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chartView)

if __name__ == '__main__':
    myapp=QApplication(sys.argv)

    window=CbieudoBar()

    myapp.exec_()
    sys.exit()