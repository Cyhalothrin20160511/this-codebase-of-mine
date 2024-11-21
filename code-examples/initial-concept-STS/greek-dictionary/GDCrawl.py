## GD Crawl
## This class is used to crawl Wikipedia information

# 第三方库Beautiful Soup, Python的第三方插件用来提取xml和HTML中的数据
# Third-party library Beautiful Soup, a Python third-party plug-in used to extract data from xml and HTML
# Βιβλιοθήκη Third-party Beautiful Soup, ένα πρόσθετο της Python το οποίο χρησιμοποιείται για εξαγωγή δεδομένων από XML και HTML
from bs4 import BeautifulSoup

class GDCrawl:
    def __init__(self):
        pass
    
    
    def crawlInformation(self, response):
        # 获取网页内容并解码
        # Get the web page content and decode it
        # Ανάκτηση περιεχομένου ιστοσελίδας και αποκωδικοποίηση
        html_doc = response.read().decode('utf-8')
        
        # 创建一个BeautifulSoup解析对象
        # Create a Beautiful Soup parsing object
        # Δημιουργία ενός αντικειμένου ανάλυσης Beautiful Soup
        soup = BeautifulSoup(html_doc, "html.parser")

        # 美化页面同时转为字符串
        # Beautify the page and convert it to a string
        # Ομορφοποίηση της σελίδας και μετατροπή της σε συμβολοσειρά
        # html_doc = soup.prettify()
        
        return soup
        
        