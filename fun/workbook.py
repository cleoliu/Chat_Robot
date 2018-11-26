import os
import xlwt
import xlrd
from xlutils.copy import copy

def new_file(file_name):    #--新增檔案--
    # new book
    wb = xlwt.Workbook()
    # sheet
    ws = wb.add_sheet('sheetName')
    # header
    styleBoldRed   = xlwt.easyxf('font: color-index red, bold on')
    headerStyle = styleBoldRed
    ws.write(0, 0, "網址", headerStyle)
    ws.write(0, 1, "商品名稱", headerStyle)
    ws.write(0, 2, "價格", headerStyle)
    ws.write(0, 3, "選項", headerStyle) #單格存list
    ws.write(0, 4, "圖片", headerStyle)
    # save
    wb.save(file_name)

def existed_file(file_name, NewUrl, Item, Price, Option, Image):    #--open existed xls file--
    # open
    oldWb = xlrd.open_workbook(file_name, formatting_info=True)
    # sheet index
    oldWbS = oldWb.sheet_by_index(0)
    # copy old detail
    newWb = copy(oldWb)
    newWs = newWb.get_sheet(0)
    # inser 1 row new data
    inserRowNo = 1
    newWs.write(inserRowNo, 0, NewUrl)
    newWs.write(inserRowNo, 1, Item)
    newWs.write(inserRowNo, 2, Price)
    newWs.write(inserRowNo, 3, ', '.join(Option))
    for i in range(0, len(Image)):
        newWs.write(inserRowNo, 4+i, Image[i])
    # write old detail
    for rowIndex in range(inserRowNo, oldWbS.nrows):
        for colIndex in range(oldWbS.ncols):
            newWs.write(rowIndex + 1, colIndex, oldWbS.cell(rowIndex, colIndex).value)
    # save
    newWb.save(file_name)
    print ("save with same name ok")

def Inser_file(file_name, NewUrl, Item, Price, Option, Image):
    if os.path.isfile(file_name): # 檔案存在
        pass
    else:                         # 檔案不存在
        new_file(file_name)
    existed_file(file_name, NewUrl, Item, Price, Option, Image)

def Dele_file(file_name):    #--刪除檔案--
    try:
        os.remove(file_name)
    except OSError as e:
        print(e)
    else:
        print("File is deleted successfully")

if __name__ == '__main__':
    Inser_file(
            file_name='product.xls', 
            NewUrl='https://item.taobao.com/item.htm?ut_sk=1.WbomrgPmfPIDAEIfPlKIWoLg_21380790_1542969294953.TaoPassword-Weixin.1&id=568398343468&sourceType=item&price=19.6-42&suid=FAC11F6E-00BE-4637-A026-43113DA47A26&un=e1f6adf92ca26d12c078635431fc6d24&share_crt_v=1&sp_tk=77+lQXkzdGJrTW9lWHHvv6U=&cpp=1&shareurl=true&spm=a313p.22.w5.990087108870&short_name=h.3mSpjTu&app=chrome', 
            Item='diy相冊軟毛金屬油漆筆 手帳婚禮高光簽字筆照片黑卡紙塗鴉珠光筆', 
            Price='19.60', 
            Option=['广纳毛笔头金属笔【纸盒】12色', '硬头2mm加粗丙烯【15色】高档装'],
            Image=['https://gd2.alicdn.com/imgextra/i2/2803025789/TB2XKXedWQoBKNjSZJnXXaw9VXa_!!2803025789.jpg_400x400.jpg', 'https://gd4.alicdn.com/imgextra/i4/2803025789/TB2TcKcfiCYBuNkHFCcXXcHtVXa_!!2803025789.jpg_400x400.jpg']
            )
