# 存储网页到本地

import urllib.request
import urllib.error
import ssl
import os

# 创建一个SSL上下文对象，并将下载的Mozilla CA证书集的路径传递给cafile参数
# Create an SSL context object and pass the path of the downloaded Mozilla CA certificate set to the cafile parameter
# Δημιουργία αντικειμένου πλαίσιο SSL και παράδοση της διαδρομής του σετ πιστοποιητικών Mozilla που έχει ληφθεί στην παράμετρο cafile
path = os.path.abspath("Web Crawling/cacert.pem")
ssl_context = ssl.create_default_context(cafile=path)

# 计数器，用于记录保存的文件数量
# Counter to track the number of saved files
# Μετρητής για την καταγραφή του αριθμού των αποθηκευμένων αρχείων
count = 0

# 标志变量，用于判断是否成功读取网页内容
# Flag variable to indicate if the webpage content was successfully read
# Μεταβλητή σημαίας για να υποδείξει εάν το περιεχόμενο της ιστοσελίδας διαβάστηκε με επιτυχία
flag = 0

# 标志变量，用于判断是否未找到网页
# Flag variable to indicate if the webpage was not found
# Μεταβλητή σημαίας για να υποδείξει εάν η ιστοσελίδα δεν βρέθηκε
not_found = 0

# 实际计数器，后来简化为计数器的削减量，但还是产生了计数上的问题
# Actual counter, later simplified to the decrement of the counter, but still caused counting issues
# Πραγματικός μετρητής, αργότερα απλοποιήθηκε στη μείωση του μετρητή, αλλά παραμένει πρόβλημα με τη μέτρηση
real_count = 0

def save2local(html_doc, name):
    """
    将网页内容保存至本地文件
    :param html_doc: 网页内容
    :param name: 单词名称
    """
    """
    Save webpage content to a local file
    :param html_doc: Webpage content
    :param name: Word name
    """
    """
    Αποθηκεύει το περιεχόμενο της ιστοσελίδας σε ένα τοπικό αρχείο
    :param html_doc: Περιεχόμενο της ιστοσελίδας
    :param name: Όνομα λέξης
    """
    
    global real_count
    
    # 创建子文件夹
    # Create a subfolder
    # Δημιουργία υποφακέλου
    subfolder = 'saved_words'
    if not os.path.exists(subfolder):
        os.makedirs(subfolder)

    count_res = count + real_count
    encoded_name = urllib.parse.quote(name)
    index = str(count_res).zfill(6)
    name_temp = index + ".html"
    
    # 打开一个新文件，在子文件夹中创建
    # Open a new file and create it in the subfolder
    # Άνοιγμα ενός νέου αρχείου και δημιουργία του στον υποφάκελο
    file_name = os.path.join(subfolder, name_temp)
    
    # 将网页保存至本地
    # Save the webpage to the local file
    # Αποθήκευση της ιστοσελίδας στο τοπικό αρχείο
    if not os.path.exists(file_name):
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(html_doc)
            
        # 记录已爬取网址的单词及其index
        # Record the word and its index for the crawled webpage
        # Καταγραφή της λέξης και του δείκτη της για την ανακτημένη ιστοσελίδα
        with open('saved_words_list.html', 'a', encoding='utf-8') as f:
            context = index + " " + name + " " + encoded_name + '\n'
            f.write(context)


def try_response(url):
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
    
    from urllib.error import HTTPError
    global not_found
    
    # 尝试打开HTTPS连接
    # Try to open the HTTPS connection
    # Δοκιμή ανοίγματος της σύνδεσης HTTPS
    try:
        response = urllib.request.urlopen(url, context=ssl_context)
        # print(response.getcode())
        return response
        
    # 如果出现HTTPLError异常，则跳过这一单词（由于更新被维基词典清除的部分），优先级要高于urllib.error.URLError
    # If an HTTPError exception occurs, skip this word (due to parts cleared by WikiDict updates), prioritizing over urllib.error.URLError
    # Εάν προκύψει εξαίρεση HTTPError, παραλείπεται η συγκεκριμένη λέξη (λόγω τμημάτων που απομακρύνθηκαν από ενημερώσεις του WikiDict), με προτεραιότητα έναντι του urllib.error.URLError
    except HTTPError as e:
        print("Error occurred while opening url:", url)
        print("Error message:", e.reason)
        not_found = 1
        
    # 如果出现URLError异常，则进行错误处理
    # If a URLError exception occurs, handle the error
    # Εάν προκύψει εξαίρεση URLError, χειρίζεται το σφάλμα
    except urllib.error.URLError as e:
        print("Error occurred while opening url:", url)
        print("Error message:", e.reason)
        
        # 等待一段时间后重试
        # Wait for a while before retrying
        # Αναμονή για λίγο πριν επανάληψη
        import time
        time.sleep(10)
        
        # 递归调用自身进行重试 - 非必要不递归
        # Recursive call to retry - avoid unnecessary recursion
        # Αναδρομική κλήση για επανάληψη - αποφεύγεται η μη απαραίτητη αναδρομή
        # try_response(url)
        
    except Exception as e:
        print("Error: {}".format(e))
        
        # 等待一段时间后重试
        # Wait for a while before retrying
        # Αναμονή για λίγο πριν επανάληψη
        import time
        time.sleep(10)


def try_complete_read(response):
    """
    尝试完整读取响应对象的内容
    :param response: 网页响应对象
    :return: 网页内容
    """
    
    import http.client
    global html_doc
    global flag
    
    try:
        html_doc = response.read().decode('utf-8')
        flag = 1
        return html_doc
    
    except http.client.IncompleteRead as e:
        print("Error message: Incomplete Read")
        # 等待一段时间后重试
        import time
        time.sleep(10)


# 中途因网络问题、维基词典的反爬虫机制以及列表中遇到被清除的单词等错误而时常出现中断，因此必须重新设置起始点
# The process often gets interrupted due to network issues, anti-scraping measures of Wiktionary, and encountering deleted words in the list.
# Therefore, it is necessary to reset the starting point.
# Ο διαδικασία διακόπτεται συχνά λόγω προβλημάτων δικτύου, μέτρων αντι-κατακόρυφης προστασίας του Βικιλεξικού και αντιμετώπισης διαγραμμένων λέξεων στη λίστα.
# Επομένως, είναι απαραίτητο να επαναρυθμίσετε το αρχικό σημείο.
# 从125391开始，通过优化算法，使出现单词被维基词典清除的情况时不再手动删除原列表内对应单词
# The optimization algorithm ensures that when a word is removed from Wiktionary, it is not manually deleted from the original list.
# Ο αλγόριθμος βελτιστοποίησης εξασφαλίζει ότι όταν μια λέξη διαγράφεται από το Βικιλεξικό, δεν διαγράφεται χειροκίνητα από την αρχική λίστα.
start_index = 48390
# 小问题：924已被爬取却未记录进saved_words_list
# Minor issue: Word 924 was crawled but not recorded in the saved_words_list.
# Μικρό πρόβλημα: η λέξη 924 έχει ήδη ανακτηθεί αλλά δεν έχει καταγραφεί στη λίστα saved_words_list
# 由于相关语法不够严谨，从125391开始有些被清除的单词的下标由其它单词填充而非替代，因此会出现单词重复保存的问题
# Due to some inconsistencies in the syntax, starting from index 125391, there are cases where removed words are replaced by other words instead of being removed entirely. 
# This leads to the problem of duplicate word saving.
# Λόγω μη αυστηρής σύνταξης, από την αρχή του 125391 ορισμένες λέξεις που έχουν διαγραφεί από το Βικιλεξικό αντικαθίστανται από άλλες λέξεις αντί να τις αντικαταστήσουν.
# Επομένως μπορεί να προκύψει το πρόβλημα της αποθήκευσης διπλών λέξεων.

# 获取已经爬取的单词列表
# Acquire the list of visited words
# Απόκτηση της λίστας των επισκεφθέντων λέξεων
def acquire_visited_words():
    global count
    global start_index
    global not_found
    global real_count
    real_count = 0
    
    # 打开已爬取的单词列表文件
    # Open the file containing the list of visited words
    # Άνοιγμα του αρχείου που περιέχει τη λίστα των επισκεφθέντων λέξεων
    path = os.path.abspath("Web Crawling/words_list.html")
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            count += 1
            
            # 如果当前行数小于开始处理的行数索引，则跳过
            # If the current line number is less than the starting index, skip it
            # Εάν ο τρέχων αριθμός γραμμής είναι μικρότερος από το δείκτη έναρξης, παραλείπεται
            if count < start_index:
                    continue
                
            info_list = line.split(' Chancenlos ')
            url = "https://el.wiktionary.org" + info_list[0]
            name = info_list[1][:-1]
            
            # 处理单词的同时进行爬取
            # Process the word while performing scraping
            # Επεξεργασία της λέξης κατά την εκτέλεση της ανάκτησης
            print("Begin - ", count)
            not_found = 0
            response = try_response(url)
            
            # 如果请求失败，标志设为1，并跳过当前单词
            # If the request fails, set the flag to 1 and skip the current word
            # Εάν ο αίτημα αποτυγχάνει, ορίζεται η σημαία σε 1 και παραλείπεται η τρέχουσα λέξη
            if not_found == 1:
                real_count -= 1
                continue
            
            # 如果响应不完整，重新发起HTTP请求，直到响应完整为止
            # If the response is incomplete, resend the HTTP request until a complete response is received
            # Εάν η απόκριση είναι ανεπαρκής, επαναλαμβάνεται το αίτημα HTTP μέχρι να ληφθεί μια πλήρης απόκριση
            # 值 == 4 - 失败 值 == 55 - 成功
            # Value == 4 - Failed Value == 55 - Success
            # Τιμή == 4 - Αποτυχία Τιμή == 55 - Επιτυχία
            while len(str(response)) != 55:
                response = try_response(url)
            html_doc = try_complete_read(response)
            global flag
            while flag != 1:
                html_doc = try_complete_read(response)
            flag = 0
            
            # 将HTML文档保存到本地
            # Save the HTML document locally
            # Αποθήκευση του HTML εγγράφου τοπικά
            save2local(html_doc, name)
            print("End - ", count)
            

acquire_visited_words()