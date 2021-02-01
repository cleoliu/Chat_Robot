'''
關於excel的操作
'''
import os
import xlwt
import xlrd
from xlutils.copy import copy

'''
自用表 [product.xls]
'''
def __NewFile(fileName):                                            #--新增自用表(product.xls)--
    # new book
    wb = xlwt.Workbook()
    # sheet
    ws = wb.add_sheet('sheetName')

    # **header**
    styleBoldRed   = xlwt.easyxf('font: color-index red, bold on')
    headerStyle = styleBoldRed
    ws.write(0, 0, 'id', headerStyle)
    ws.write(0, 1, 'Url', headerStyle)
    ws.write(0, 2, 'Title', headerStyle)
    ws.write(0, 3, 'Price', headerStyle)
    ws.write(0, 4, 'Options', headerStyle) #單格存list
    for i in range (1, 10):
        ws.write(0, 4+i, 'Image'+str(i), headerStyle)

    # save
    wb.save(fileName)

def __ExistedFile(fileName, url, title, price, options, image):    #--寫自用表(product.xls)--
    # open
    oldWb = xlrd.open_workbook(fileName, formatting_info=True)
    # currently row count
    inserRowNo = oldWb.sheets()[0].nrows
    # copy old detail
    newWb = copy(oldWb)
    newWs = newWb.get_sheet(0)

    # **inser new data**
    newWs.write(inserRowNo, 1, url)                 #網址
    newWs.write(inserRowNo, 2, title)               #品名
    newWs.write(inserRowNo, 3, price)               #價格
    newWs.write(inserRowNo, 4, ', '.join(options))  #選項
    for i in range(0, len(image)):                  #圖片
        newWs.write(inserRowNo, 5+i, image[i])

    # save
    newWb.save(fileName)
    print ('[%s] save with same name ok' %fileName)

def InserFile(fileName, url, title, price, options, image):         #--判斷是否已有自用表 或 建立新自用表(product.xls)==
    if os.path.isfile(fileName): # 檔案存在
        pass
    else:                         # 檔案不存在
        __NewFile(fileName)
    __ExistedFile(fileName, url, title, price, options, image)


'''
上傳用 [upload.xls]
'''
def UpFile(fileName, userName, title, price, options, image):       #--寫上傳用表(upload.xls)--
    if os.path.isfile(fileName) == False: #檔案不存在
        load_name = './Common/Template/Upload_{}_Template.xlsx'.format(userName)
    else:
        load_name = fileName
    
    # open
    oldWb = xlrd.open_workbook(load_name)
    # currently row count
    inserRowNo = oldWb.sheets()[0].nrows
    # copy old detail
    newWb = copy(oldWb)
    newWs = newWb.get_sheet(0)
    oldWbS = oldWb.sheet_by_index(0)

    # **inser new data**
    style = xlwt.easyxf('font: color-index red, bold on')
    newWs.write(inserRowNo, 0, oldWbS.cell_value(1, 0)) #分類
    newWs.write(inserRowNo, 1, title, style)            #品名
    newWs.write(inserRowNo, 2, oldWbS.cell_value(1, 2)) #文宣
    newWs.write(inserRowNo, 3, price, style)            #售價
    newWs.write(inserRowNo, 4, oldWbS.cell_value(1, 4)) #數量
    newWs.write(inserRowNo, 6, oldWbS.cell_value(1, 6)) #出貨日

    # 選項
    if len(options) > 20:
        newWs.write(1, 8, '選項超過20個', )
    opid = list(range(10, 87, 4))
    for psVariation in range(0, 20):
        if psVariation >= len(options):
            break
        newWs.write(inserRowNo, opid[psVariation], options[psVariation], style)
        newWs.write(inserRowNo, opid[psVariation]+1, price, style)
        newWs.write(inserRowNo, opid[psVariation]+2, 20)

    # 圖片 89~97
    for psImg in range(0, 9):
        if psImg >= len(image):
            break
        newWs.write(inserRowNo, 89+psImg, image[psImg], style)

    # 運送條件 99~108
    for channel in range(0, 10):
        newWs.write(inserRowNo, 99+channel, oldWbS.cell_value(1, 99+channel))

    # save
    newWb.save(fileName)
    print ('[%s] save with same name ok' %fileName)


'''
共用類
'''
def DeleFile(fileName):                                             #--刪除檔案--
    try:
        os.remove(fileName)
    except OSError as e:
        print(e)
    else:
        print("File [%s] is deleted successfully" %fileName)


if __name__ == '__main__':
    InserFile(
            fileName = 'product.xls', 
            url = 'https://item.taobao.com/item.htm?ut_sk=1.WbomrgPmfPIDAEIfPlKIWoLg_21380790_1542969294953.TaoPassword-Weixin.1&id=568398343468&sourceType=item&price=19.6-42&suid=FAC11F6E-00BE-4637-A026-43113DA47A26&un=e1f6adf92ca26d12c078635431fc6d24&share_crt_v=1&sp_tk=77+lQXkzdGJrTW9lWHHvv6U=&cpp=1&shareurl=true&spm=a313p.22.w5.990087108870&short_name=h.3mSpjTu&app=chrome', 
            title = 'diy相冊軟毛金屬油漆筆 手帳婚禮高光簽字筆照片黑卡紙塗鴉珠光筆',
            price = '19.60', 
            options = ['广纳毛笔头金属笔【纸盒】12色', '硬头2mm加粗丙烯【15色】高档装'],
            image = ['https://gd2.alicdn.com/imgextra/i2/2803025789/TB2XKXedWQoBKNjSZJnXXaw9VXa_!!2803025789.jpg_400x400.jpg', 'https://gd4.alicdn.com/imgextra/i4/2803025789/TB2TcKcfiCYBuNkHFCcXXcHtVXa_!!2803025789.jpg_400x400.jpg']
            )
    UpFile('tt.xls', price, 199, options, image)