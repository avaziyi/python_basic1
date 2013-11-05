# -*- coding: utf-8 -*-
'''
import urllib2  
req = urllib2.Request('http://music.douban.com/subject_search?search_text=%E9%80%86%E5%85%89&cat=1003')  
response = urllib2.urlopen(req)  
html = response.read() 
print html
'''
import urllib2  
  
class RedirectHandler(urllib2.HTTPRedirectHandler):  
    def http_error_403(self, req, fp, code, msg, headers):  
        pass  
    def http_error_302(self, req, fp, code, msg, headers):  
        pass  

user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'  
headers = { 'User-Agent' : user_agent, 'Connection': 'keep-alive','Accept-Encoding': 'gzip,deflate,sdch'}  
data = ""
url = 'http://music.douban.com/subject_search?search_text=%E9%80%86%E5%85%89&cat=1003'    
req = urllib2.Request(url=url, headers=headers)  
response = urllib2.urlopen(req)  
the_page = response.read()
print the_page