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
    wb.save(file_name)

def existed_file(file_name, url, Title, Price, Options, Image):    #--自用表,open existed xls file [product.xls]--
    # open
    oldWb = xlrd.open_workbook(file_name, formatting_info=True)
    # currently row count
    inserRowNo = oldWb.sheets()[0].nrows
    # copy old detail
    newWb = copy(oldWb)
    newWs = newWb.get_sheet(0)

    # **inser new data**
    newWs.write(inserRowNo, 0, url)                 #網址
    newWs.write(inserRowNo, 1, Title)               #品名
    newWs.write(inserRowNo, 2, Price)               #價格
    newWs.write(inserRowNo, 3, ', '.join(Options))  #選項
    for i in range(0, len(Image)):                  #圖片
        newWs.write(inserRowNo, 4+i, Image[i])

    # save
    newWb.save(file_name)
    print ('[%s] save with same name ok' %file_name)

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
        print("File [%s] is deleted successfully" %file_name)


'''
上傳用
'''
def Up_file(file_name, Title, Price, Options, Image):  #--上傳用表 [upload.xls]--
    if os.path.isfile(file_name) == False: #檔案不存在
        load_name = './fun/Upload_exmple.xlsx'
    else:
        load_name = file_name
    
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
    newWs.write(inserRowNo, 1, Title, style)            #品名
    newWs.write(inserRowNo, 2, oldWbS.cell_value(1, 2)) #文宣
    newWs.write(inserRowNo, 3, Price, style)            #售價
    newWs.write(inserRowNo, 4, oldWbS.cell_value(1, 4)) #數量
    newWs.write(inserRowNo, 6, oldWbS.cell_value(1, 6)) #出貨日

    # **選項**
    if len(Options) > 20:
        newWs.write(1, 8, '選項超過20個', )
    Opid = list(range(10, 87, 4))
    for ps_variation in range(0, 20):
        if ps_variation >= len(Options):
            break
        newWs.write(inserRowNo, Opid[ps_variation], Options[ps_variation], style)
        newWs.write(inserRowNo, Opid[ps_variation]+1, Price, style)
        newWs.write(inserRowNo, Opid[ps_variation]+2, 20)

    # **圖片** 89~97
    for ps_img in range(1, 10):
        if ps_img >= len(Image):
            break
        newWs.write(inserRowNo, 88+ps_img, Image[ps_img], style)

    # **運送條件** 99~108
    for channel in range(1, 11):
        newWs.write(inserRowNo, 98+channel, oldWbS.cell_value(1, 98+channel))

    # save
    newWb.save(file_name)
    print ('[%s] save with same name ok' %file_name)



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