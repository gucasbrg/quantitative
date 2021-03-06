# coding=utf-8
'''
@author: ElegyPrincess
'''
import json
from django.http import HttpResponse
import HistData as HD

def display_hist_hs300_price(request):
    if 'date' in request.GET:
        date=request.GET['date']+' 00:00:00'
        stock="hs300"
        data=HD.histPrice(date,stock)
        if data == ():
            return HttpResponse("isNone")
        else:
            jsondatar = json.dumps(data, ensure_ascii=False)
            return HttpResponse(jsondatar, content_type='application/json')
    else:
        print "未获取到数据"


def display_hist_hs300(request):
        stock = "hs300"
        data = HD.histData(stock)
        # 使用json.dumps将数据转换为json格式，json.dumps方法默认会输出成这种格式"\u5377\u76ae\u6298\u6263"，加ensure_ascii=False，则能够防止中文乱码。
        # JSON采用完全独立于语言的文本格式，事实上大部分现代计算机语言都以某种形式支持它们。这使得一种数据格式在同样基于这些结构的编程语言之间交换成为可能。
        # json.dumps()是将原始数据转为json（其中单引号会变为双引号），而json.loads()是将json转为原始数据。
        jsondatar = json.dumps(data, ensure_ascii=False)
        return HttpResponse(jsondatar,content_type='application/json')

