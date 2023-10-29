class XulyFile:
    def luufile(self,path,data):
        file=open(path,'a',encoding='utf-8')
        file.writelines(data)
        file.writelines('\n')
        file.close()
    def xoads(self,path,data):
        file = open(path, 'w', encoding='utf-8')
        file.writelines(data)
        #file.writelines('\n')
        file.close()
    def docfile(self,path):
        arrSP=[]
        file=open(path,'r',encoding='utf-8')
        for line in file:
            arrSP.append(line)
        file.close()
        return arrSP