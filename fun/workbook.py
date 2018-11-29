'''
關於excel的操作
'''
import os
import xlwt
import xlrd
from xlutils.copy import copy

'''
自用表
'''
def new_file(file_name):    #--自用表,新增檔案--
    # new book
    wb = xlwt.Workbook()
    # sheet
    ws = wb.add_sheet('sheetName')
    # header
    styleBoldRed   = xlwt.easyxf('font: color-index red, bold on')
    headerStyle = styleBoldRed
    ws.write(0, 0, 'Url', headerStyle)
    ws.write(0, 1, 'Title', headerStyle)
    ws.write(0, 2, 'Price', headerStyle)
    ws.write(0, 3, 'Options', headerStyle) #單格存list
    for i in range (1, 9):
        ws.write(0, 3+i, 'Image'+str(i), headerStyle)
    ws.write(0, 13, 'id', headerStyle)
    # save
    wb.save(file_name)

def existed_file(file_name, url, Title, Price, Options, Image):    #--自用表,open existed xls file--
    # open
    oldWb = xlrd.open_workbook(file_name, formatting_info=True)
    # sheet index
    oldWbS = oldWb.sheet_by_index(0)
    # copy old detail
    newWb = copy(oldWb)
    newWs = newWb.get_sheet(0)
    # inser 1 row new data
    inserRowNo = 1
    newWs.write(inserRowNo, 0, url)
    newWs.write(inserRowNo, 1, Title)
    newWs.write(inserRowNo, 2, Price)
    newWs.write(inserRowNo, 3, ', '.join(Options))
    for i in range(0, len(Image)):
        newWs.write(inserRowNo, 4+i, Image[i])
    # write old detail
    for rowIndex in range(inserRowNo, oldWbS.nrows):
        for colIndex in range(oldWbS.ncols):
            newWs.write(rowIndex + 1, colIndex, oldWbS.cell(rowIndex, colIndex).value)
    # save
    newWb.save(file_name)
    print ('save with same name ok')

def Inser_file(file_name, url, Title, Price, Options, Image): #--自用表==
    if os.path.isfile(file_name): # 檔案存在
        pass
    else:                         # 檔案不存在
        new_file(file_name)
    existed_file(file_name, url, Title, Price, Options, Image)

def Dele_file(file_name):    #--刪除檔案--
    try:
        os.remove(file_name)
    except OSError as e:
        print(e)
    else:
        print("File is deleted successfully")


'''
上傳用
'''
def Up_file(file_name, Title, Price, Options, Image):  #--上傳用表--
    if os.path.isfile(file_name) == False: # 檔案不存在
        load_name = './fun/Upload_exmple.xlsx'
    else:
        load_name = file_name

    style = xlwt.easyxf('font: color-index red, bold on')
    oldWb = xlrd.open_workbook(load_name)
    oldWbS = oldWb.sheet_by_index(0)
    newWb = copy(oldWb)
    newWs = newWb.get_sheet(0)
    inserRowNo = 1
    newWs.write(inserRowNo, 1, Title, style)
    newWs.write(inserRowNo, 3, Price, style)

    # 選項
    if len(Options) > 20:
        newWs.write(1, 8, '選項超過20個', )
    Opid = list(range(10, 87, 4))
    for i in range(0, 20):
        if i >= len(Options):
            break
        newWs.write(1, Opid[i], Options[i], style)
        newWs.write(1, Opid[i]+1, Price, style)
        newWs.write(1, Opid[i]+2, 20)

    for im in range(1, 9):
        newWs.write(1, 88+im, Image[im], style)

    if os.path.isfile(file_name) == True :
        for rowIndex in range(inserRowNo, oldWbS.nrows):
            for colIndex in range(oldWbS.ncols):
                newWs.write(rowIndex + 1, colIndex, oldWbS.cell(rowIndex, colIndex).value)

    newWb.save(file_name)


if __name__ == '__main__':
    Title = 'diy相冊軟毛金屬油漆筆 手帳婚禮高光簽字筆照片黑卡紙塗鴉珠光筆'
    Price = '19.60'
    Options = ['广纳毛笔头金属笔【纸盒】12色', '硬头2mm加粗丙烯【15色】高档装']

    Inser_file(
            file_name = 'product.xls', 
            url = 'https://item.taobao.com/item.htm?ut_sk=1.WbomrgPmfPIDAEIfPlKIWoLg_21380790_1542969294953.TaoPassword-Weixin.1&id=568398343468&sourceType=item&price=19.6-42&suid=FAC11F6E-00BE-4637-A026-43113DA47A26&un=e1f6adf92ca26d12c078635431fc6d24&share_crt_v=1&sp_tk=77+lQXkzdGJrTW9lWHHvv6U=&cpp=1&shareurl=true&spm=a313p.22.w5.990087108870&short_name=h.3mSpjTu&app=chrome', 
            Title = Title,
            Price = Price, 
            Options = Options,
            Image = ['https://gd2.alicdn.com/imgextra/i2/2803025789/TB2XKXedWQoBKNjSZJnXXaw9VXa_!!2803025789.jpg_400x400.jpg', 'https://gd4.alicdn.com/imgextra/i4/2803025789/TB2TcKcfiCYBuNkHFCcXXcHtVXa_!!2803025789.jpg_400x400.jpg']
            )
    Up_file('tt.xls', Price, 199, Options, Image)