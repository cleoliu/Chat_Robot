class Taobao(object):
    TITLE = '//*[@id="J_Title"]/h3'                                 #標題
    PRICE = '//*[@id="J_StrPrice"]/em[2]'                           #價格
    ISKU = '//*[@id="J_isku"]/div/dl[1]/dd/ul/li'                   #多顏多尺區塊
    OPTION = '//*[@class ="J_TSaleProp tb-img tb-clearfix"]/li'     #選項
    OPTION_TEXT = './a//span'
    IMAGE = '//div[@class="tb-gallery"]/ul/li'                      #主圖數量
    IMAGE_SUB = './div/a/img/@data-src'                             #單主圖
    IMG_SIZE = '50x50'
    DESCIMAGE = '//div[@id="J_DivItemDesc"]//descendant::img/@src'  #描述圖

class Tmall(object):
    TITLE = '//*[@class="tb-detail-hd"]/h1'
    PRICE = '//*[@class="tm-promo-price"]/span[1]'
    ISKU = '//*[@class="tb-prop tm-sale-prop tm-clear tm-img-prop "]'
    OPTION = '//*[@class="tm-clear J_TSaleProp tb-img     "]/li'
    OPTION_TEXT = './a//span'
    IMAGE = '//*[@id="J_UlThumb"]/li'
    IMAGE_SUB = './a/img/@src'
    IMG_SIZE = '60x60'
    DESCIMAGE = '//*[@id="description"]//descendant::img/@src'

class Qr1688(object):
    TITLE = '//*[@id="mod-detail-title"]/h1'
    PRICE = '//*[@class="price-discount-sku"]/span[2]'
    ISKU = '//*[@class="obj-leading"]'
    OPTION = '//*[@class="mod-detail-purchasing mod-detail-purchasing-multiple "]/div'
    OPTION_TEXT = '/div/div/div/table/tbody/tr/@data-sku-config'
    IMAGE = '//*[@id="d-swipe"]/div/div[1]'
    IMAGE_SUB = './img/@swipe-lazy-src'
    IMG_SIZE = ''
    DESCIMAGE = '//*[@id="description"]//descendant::img/@src'