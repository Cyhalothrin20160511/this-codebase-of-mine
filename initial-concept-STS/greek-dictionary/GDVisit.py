## GD Visit
## This class is used to visit Wiktionary

import ssl
import urllib.request
from urllib.error import HTTPError

# 创建一个SSL上下文对象，并将下载的Mozilla CA证书集的路径传递给cafile参数
# Create an SSL context object and pass the path of the downloaded Mozilla CA certificate set to the cafile parameter
# Δημιουργία αντικειμένου πλαίσιο SSL και παράδοση της διαδρομής του σετ πιστοποιητικών Mozilla που έχει ληφθεί στην παράμετρο cafile
ssl_context = ssl.create_default_context(cafile="F:/Megali Idea/Web Crawling/cacert.pem")

class GDVisit:
    def __init__(self):
        self.part1 = "https://"
        self.part2 = ".wiktionary.org/wiki/"
        
    def constructURL(self, language, word):
        url = self.part1 + language + self.part2 + word
        return url
    
    
    def tryResponse(self, url):
        """
        尝试打开网页连接并返回响应对象
        :param url: 网页URL
        :return: 网页响应对象
        """
        """
        Attempt to open the webpage connection and return the response object
        :param url: Webpage URL
        :return: Webpage response object
        """
        """
        Προσπαθεί να ανοίξει τη σύνδεση με την ιστοσελίδα και επιστρέφει το αντικείμενο απόκρισης
        :param url: URL ιστοσελίδας
        :return: Αντικείμενο απόκρισης ιστοσελίδας
        """
    
        # 尝试打开HTTPS连接
        # Try to open the HTTPS connection
        # Δοκιμή ανοίγματος της σύνδεσης HTTPS
        try:
            response = urllib.request.urlopen(url, context=ssl_context)
            return response
            
        except:
            return False
        
        
