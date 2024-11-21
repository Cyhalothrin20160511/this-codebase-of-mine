# Web Crawling in Python
# urllib 实现下载网页的三种方式

import urllib.request
import urllib.error
import ssl
import os

# 创建一个SSL上下文对象，并将下载的Mozilla CA证书集的路径传递给cafile参数
# Create an SSL context object and pass the path of the downloaded Mozilla CA certificate set to the cafile parameter
# Δημιουργία αντικειμένου πλαίσιο SSL και παράδοση της διαδρομής του σετ πιστοποιητικών Mozilla που έχει ληφθεί στην παράμετρο cafile
path = os.path.abspath("Web Crawling/cacert.pem")
ssl_context = ssl.create_default_context(cafile=path)

# 全局计数器 - 足够数量后停止爬取
# Global counter - stop crawling after reaching a sufficient number
# Καθολικός μετρητής - διακόπηκε αφού επιτεύχθηκε αρκετός αριθμός
count = 0

# 目标数量 - 由维基词典提供
# Target quantity - provided by Wiktionary
# Επιθυμητός αριθμός - παρέχεται από το Wiktionary
target = 341572

# 记录已经访问过的单词列表 - 用于去重
# Record the list of visited words - used for de-duplication
# Λίστα με τις λέξεις που έχουν επισκεφτεί - χρησιμοποιείται για αφαίρεση διπλοτύπων
visited_words = []

# 错误计数器，用于绕过维基词典的反爬虫机制
# Error counter, used to bypass Wiktionary's anti-crawling mechanism
# Μετρητής σφαλμάτων, χρησιμοποιείται για παράκαμψη του μηχανισμού αντι-κρατήσεων του Wiktionary
error_time = -1

def web_crawling(url):
    global count
    global last_word
    global visited_words
    global error_time
    
    print("Begin - ", count)

    # 使用上下文对象来发送HTTPS请求
    # Use the context object to send an HTTPS request
    # # Χρήση του αντικειμένου πλαισίου για την αποστολή ενός αιτήματος HTTPS
    response1 = urllib.request.urlopen(url, context=ssl_context)
    
    # print("第一种方法")
    
    # 获取状态码，200表示成功
    # Get the status code, 200 means success
    # # Παίρνουμε τον κωδικό κατάστασης, το 200 σημαίνει επιτυχία
    print(response1.getcode())
    
    # 获取网页内容并解码
    # Get the web page content and decode it
    # Ανάκτηση περιεχομένου ιστοσελίδας και αποκωδικοποίηση
    html_doc = response1.read().decode('utf-8')
    
    # print(len(html_doc))

    # print("第二种方法")
    # request = urllib.request.Request(url)
    # # 模拟Mozilla浏览器进行爬虫
    # request.add_header("user-agent", "Mozilla/5.0")
    # response2 = urllib.request.urlopen(request, context=ssl_context)
    # print(response2.getcode())
    # print(len(response2.read()))

    # print("第三种方法")
    # cookie = http.cookiejar.CookieJar()
    # # 加入urllib处理cookie的能力
    # opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    # urllib.request.install_opener(opener)
    # response3 = urllib.request.urlopen(url, context=ssl_context)
    # print(response3.getcode())
    # print(len(response3.read()))
    # print(cookie)
        
    # 嵌套递归函数来遍历多维列表并将元素添加到新列表
    # A nested recursive function is used to traverse the multidimensional list and add elements to a new list
    # Επίπεδη αναδρομική συνάρτηση για να διατρέξει τις πολυδιάστατες λίστες και προσθέσει τα στοιχεία σε μια νέα λίστα
    def flatten(visited_words):
        for item in visited_words:
            if isinstance(item, list):
                flatten(item)
            else:
                one_dim_list.append(item)

    # 第三方库Beautiful Soup, Python的第三方插件用来提取xml和HTML中的数据
    # Third-party library Beautiful Soup, a Python third-party plug-in used to extract data from xml and HTML
    # Βιβλιοθήκη Third-party Beautiful Soup, ένα πρόσθετο της Python το οποίο χρησιμοποιείται για εξαγωγή δεδομένων από XML και HTML
    from bs4 import BeautifulSoup
    
    # 创建一个BeautifulSoup解析对象
    # Create a Beautiful Soup parsing object
    # Δημιουργία ενός αντικειμένου ανάλυσης Beautiful Soup
    soup = BeautifulSoup(html_doc, "html.parser")

    # 美化页面同时转为字符串
    # Beautify the page and convert it to a string
    # Ομορφοποίηση της σελίδας και μετατροπή της σε συμβολοσειρά
    html_doc = soup.prettify()

    # 获取单词列表，提取其中有效部分（即网址）
    # Get the word list and extract the effective part (i.e., the URL)
    # Λήψη της λίστας των λέξεων και εξαγωγή του αποτελεσματικού μέρους (δηλαδή του URL)
    word_list = soup.find('div', {'id': 'mw-pages'})
    if word_list is None:
        error_time -= 1
        last_word = visited_words[error_time]
        return 0 
        
    word_groups = word_list.find_all('div', {'class': 'mw-category-group'})
            
    # print(word_groups)

    # 测试：网页能否正常保存至本地
    # with open('example.html', 'w', encoding='utf-8') as f:
    #     f.write(html_doc)
        
    # 两个列表用于存储网址信息
    # Two lists are used to store URL information
    # Χρησιμοποιούνται δύο λίστες για την αποθήκευση πληροφοριών URL
    multi_dim_list = []
    one_dim_list = []
        
    for group in word_groups:
        item = group.find_all('a')
        multi_dim_list.append(item)
    # print(multi_dim_list)
                
                
    # 调用递归函数并传入原始多维列表，将其转换为一维列表
    # Call the recursive function and pass in the original multidimensional list to convert it to a one-dimensional list
    # Κλήση της αναδρομικής συνάρτησης και μετάδοση της αρχικής πολυδιάστατης λίστας για να μετατραπεί σε μια μια διάσταση
    flatten(multi_dim_list)
    # print(one_dim_list)
    
    # 将单词和对应的URL写入本地文件
    # Write the word and corresponding URL to a local file
    # Εγγραφή της λέξης και του αντίστοιχου URL σε ένα τοπικό αρχείο
    with open('words_list2.html', 'a', encoding='utf-8') as f:
        for item in one_dim_list:
            href = item.get('href')
            title = item.get('title')
            
            # 如果单词已经访问过，则跳过
            # If the word has been visited, skip it
            # Αν η λέξη έχει ήδη επισκεφτεί, παραλείπεται
            if title in visited_words and len(visited_words) > 0:
                continue
            
            output = href + ' Chancenlos ' + title + '\n'
            f.write(output)
            count += 1
            last_word = title
            visited_words.append(title)
            
        # 这里傻了写了一个always true的语句，不过在爬取时确实起到了一个反制维基词典反爬取机制的功能
        # Here, a statement that is always true is written stupidly, but it does play a role in countering Wiktionary's anti-crawling mechanism during crawling
        # Εδώ, μια δήλωση που είναι πάντοτε αληθής γράφεται ανόητα, αλλά παίζει ένα ρόλο στο να αντιμετωπίζει το μηαντίσταση του Wiktionary κατά τη διάρκεια του web crawling
        if count == count:
            error_time -= 1
            last_word = visited_words[error_time]
            
        if error_time <= -50:
            error_time = -1
        
        print("End - ", count)


# 测试：寻找首先出现多次重复的单词
def acquire_url():
    global dict_check_error
    with open('test.html', 'r', encoding='utf-8') as f:
        l = f.readlines()
        for i in l:
            j = i.split(' Chancenlos ')
            j[1] = j[1][:-1]
            if str(j[1]) in dict_check_error:
                dict_check_error[str(j[1])] += 1
                if dict_check_error[str(j[1])] == 3:
                    print(str(j[1]))
                    return 0  
            else:
                dict_check_error[str(j[1])] = 1
                

# 测试：获取已经爬取的单词列表    
def acquire_visited_words():
    global visited_words
    with open('test.html', 'r', encoding='utf-8') as f:
        l = f.readlines()
        length = len(l)
        index = 40000 # 当时于40000左右中断
        while index < length:
            visited_words.append(l[index])
            index += 1


# 维基词典网址格式
# Wiktionary URL format
# Μορφή URL Λεξικού
model1 = "https://el.wiktionary.org/w/index.php?title=%CE%9A%CE%B1%CF%84%CE%B7%CE%B3%CE%BF%CF%81%CE%AF%CE%B1:%CE%9D%CE%AD%CE%B1_%CE%B5%CE%BB%CE%BB%CE%B7%CE%BD%CE%B9%CE%BA%CE%AC&pagefrom="
model2 = "#mw-pages"
last_word = ""

# 第一次中断：访问量过多被ban了，从这里另开一个进行爬取，最后去重
# First interruption: too many requests, switch to another IP address and continue crawling, then remove duplicates
# Πρώτη διακοπή: πολλές αιτήσεις, αλλαγή διεύθυνσης IP και συνέχιση ανάγνωσης, έπειτα αφαίρεση διπλοτύπων
count = 0
last_word = ""

# acquire_visited_words()

while last_word != "ϛ":
    # 对单词进行URL编码
    # URL encode the word
    # Κωδικοποίηση της λέξης στο URL
    encoded_last_word = urllib.parse.quote(last_word)
    url = model1 + encoded_last_word + model2
    print(url)
    web_crawling(url)

print("count: ", count, "    target: ", target)

# 结束条件没有正确判定，因为反制维基词典的反爬取机制时last_word并不为真，应改为"ϛ" not in visited_words
# 出乎意料的是，根据这一顺序总共爬取184432条网址，少于维基词典所标注的222992，存在问题

# 测试：于何处开始出现重复
# dict_check_error = {}
# acquire_url()
# sorted_dict = dict(sorted(dict_check_error.items(), key=lambda item: item[1]))
# print(sorted_dict)

# 无需另外爬取英文维基百科下所有现代希腊语条目URL，一一对应即可