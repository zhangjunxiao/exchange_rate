# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json

url = 'http://apis.baidu.com/apistore/currencyservice/currency?fromCurrency=USD&toCurrency=CNY&amount=2'


req = urllib2.Request(url)

req.add_header("apikey", "4eea02ae3804de24c47ac1988bc907e0")

resp = urllib2.urlopen(req)
content = resp.read()
if content:
    print(content)
