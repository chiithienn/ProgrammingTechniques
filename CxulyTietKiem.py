class CtienTK:
    def __init__(self,von=0,money=0,time=0,num=0):
        self.von=von
        self.tien=money
        self.thoigian=time
        self.num=num
    #
    def boheo(self):
        for i in range(self.thoigian):
            self.von+=self.tien
        self.von2=format(self.von,",.0f")
        return self.von2
    #
    def xuatTK(self):
        kq=self.boheo()
        if self.num==1:
            tg='Kết quả sau {0} ngày:'.format(self.thoigian)+'\n'
        if self.num==2:
            tg='Kết quả sau {0} tháng:'.format(self.thoigian)+'\n'
        if self.num==3:
            tg='Kết quả sau {0} năm:'.format(self.thoigian)+'\n'
        cx='Tổng tiền tiết kiệm = '+str(kq)+' vnđ'
        xuat=tg+cx
        return xuat
class CguiNH:
    def __init__(self,von=0,money=0,time=0,r=0,num=0):
        self.von=von
        self.tien=money
        self.thoigian=time
        self.laisuat=r
        self.num=num

    def phantram(self):
        s = self.laisuat
        if s.endswith('%'):
            s1 = s.strip('%')
            s1 = eval(s1) / 100
        else:
            s1 = eval(s)
        return s1
    def guiNH(self): #S=A*(1+r)^n
        laisuat=self.phantram()
        self.von=self.tien*(1+laisuat)**self.thoigian
        self.s0=self.von-self.tien
        self.von2=format(self.von,",.2f")
        self.s02=format(self.s0,",.2f")
        return self.von2
    def guidinhky(self):#Sn=(A/r)*((1+r)^n-1)*(1+r)
        laisuat = self.phantram()
        self.von=(self.tien/laisuat)*(((1+laisuat)**self.thoigian)-1)*(1+laisuat)
        self.s0=self.von - self.tien * self.thoigian
        self.von2 = format(self.von, ",.2f")
        self.s02 = format(self.s0, ",.2f")
        return self.von2
    #
    def xuatTKNH(self):
        kq=self.guiNH()
        if self.num==2:
            tg='Kết quả sau {0} tháng:'.format(self.thoigian)+'\n'
        if self.num==3:
            tg='Kết quả sau {0} năm:'.format(self.thoigian)+'\n'
        cx = 'Tổng tiền tiết kiệm = ' + str(kq) + ' vnđ'
        ln='Lãi nhận được = '+str(self.s02) + ' vnđ'
        xuat=tg+cx+'\n'+ln
        return xuat
    def xuatTKDK(self):
        kq=self.guidinhky()
        if self.num==2:
            tg='Kết quả sau {0} tháng:'.format(self.thoigian)+'\n'
        if self.num==3:
            tg='Kết quả sau {0} năm:'.format(self.thoigian)+'\n'
        cx='Tổng tiền tiết kiệm = '+str(kq) + ' vnđ'
        ln='Lãi nhận được = '+str(self.s02) + ' vnđ'
        xuat = tg + cx + '\n' + ln
        return xuat
