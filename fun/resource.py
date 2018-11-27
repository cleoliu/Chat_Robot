class taobao(object):
    TITLE = '//*[@id="J_Title"]/h3'                                 #標題
    PRICE = '//*[@id="J_StrPrice"]/em[2]'                           #價格
    ISKU = '//*[@id="J_isku"]/div/dl[1]/dd/ul/li'                   #多顏多尺區塊
    OPTION = '//*[@class ="J_TSaleProp tb-img tb-clearfix"]/li'     #選項
    IMAGE = '//div[@class="tb-gallery"]/ul/li'                      #主圖數量
    IMAGE_SUB = './div/a/img/@data-src'                             #單主圖
    DESCIMAGE = '//div[@id="J_DivItemDesc"]//descendant::img/@src'  #描述圖

class tmall(object):
    TITLE = '//*[@class="tb-detail-hd"]/h1'
    PRICE = '//*[@class="tm-promo-price"]/span[1]'
    ISKU = '//*[@class="tb-prop tm-sale-prop tm-clear tm-img-prop "]'
    OPTION = '//*[@class="tm-clear J_TSaleProp tb-img     "]/li'
    IMAGE = '//*[@id="J_UlThumb"]/li'
    IMAGE_SUB = './a/img/@src'
    DESCIMAGE = '//*[@id="description"]//descendant::img/@src'