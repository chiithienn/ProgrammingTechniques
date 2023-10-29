class xulyKD:
    def __init__(self,dth=0,cp=0,thue=''):
        self.dth=eval(dth)
        self.cp=eval(cp)
        self.thue=thue

    def phantram(self):
        s=self.thue
        if s.endswith('%'):
            s1=s.strip('%')
            s1=eval(s1)/100
        else:
            s1=eval(s)
        return s1
    def dautuKD(self): #Lợi nhuận = Doanh thu - Chi phí - Thuế thu nhập (Thuế * Doanh thu)
        thue=self.phantram()
        print(thue)
        ln = self.dth - self.cp - (thue*self.dth)
        return ln

    def xuatdautuKD(self):
        ln=self.dautuKD()
        cx = 'Tổng kết quả kinh doanh = ' + str(round(ln, 2))+'\n'
        if ln>0:
            kl='Đầu tư có lời'
        else:
            kl='Đầu tư thua lỗ'
        xuat=cx+kl
        return xuat
class xulyCK:
    def __init__(self,giaban=0,giamua=0,soluong=0,thue='',phigd=0):
        self.gb=eval(giaban)
        self.gm=eval(giamua)
        self.sl=eval(soluong)
        self.thue=thue
        self.phigd=eval(phigd)

    def phantram(self):
        s=self.thue
        if s.endswith('%'):
            s1=s.strip('%')
            s1=eval(s1)/100
        else:
            s1=eval(s)
        return s1

    def dautuCK(self):
        # Lợi nhuận = (Giá bán – Giá mua) * Số lượng cổ phiếu – (Thuế=(Thuế * Giá mua * Số lượng) + Phí giao dịch)
        thue=self.phantram()
        ln = (self.gb - self.gm) * self.sl - ((thue*self.gm*self.sl) + self.phigd)
        return ln

    #
    def xuatdautuCK(self):
        ln=self.dautuCK()
        cx = 'Tổng lợi nhuận đạt được = ' + str(round(ln, 2))+'\n'
        if ln>0:
            kl='Đầu tư có lời'
        else:
            kl='Đầu tư thua lỗ'
        xuat=cx+kl
        return xuat
