#coding:utf-8
import xlrd

class readExcel(object):
    def __init__(self,path):
        self.path = path
    @property
    #获取索引
    def getSheet(self):
        xl = xlrd.open_workbook(self.path)
        sheet = xl.sheet_by_index(0)
        return sheet
    #获取行数
    @property
    def getRows(self):
        row = self.getSheet.nrows
        return row
    #获取列数
    @property
    def getCol(self):
        col = self.getSheet.ncols
        return col
    #获取每一列的值
    @property
    def getName(self):
        Testname = []
        for i in range(1,self.getRows):
            Testname.append(self.getSheet.cell_value(i,0))
        return Testname
    @property
    def getData(self):
        TestData = []
        for i in range(1, self.getRows):
            TestData.append(self.getSheet.cell_value(i, 1))
        return TestData

    @property
    def getUrl(self):
        TestUrl = []
        for i in range(1, self.getRows):
            TestUrl.append(self.getSheet.cell_value(i, 2))
        return TestUrl

    @property
    def getMethod(self):
        TestMethod = []
        for i in range(1, self.getRows):
            TestMethod.append(self.getSheet.cell_value(i, 3))
        return TestMethod

    '''@property
    def getUid(self):
        TestUid = []
        for i in range(1, self.getRows):
            TestUid.append(self.getSheet.cell_value(i, 4))
        return TestUid'''

    @property
    def getCode(self):
        TestCode = []
        for i in range(1, self.getRows):
            TestCode.append(self.getSheet.cell_value(i, 4))
        return TestCode

