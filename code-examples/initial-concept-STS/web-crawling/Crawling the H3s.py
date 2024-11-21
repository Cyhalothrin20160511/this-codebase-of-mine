from bs4 import BeautifulSoup

# 随机挑选的测试用单词 - καίριος
# Randomly chosen test word - καίριος
# Τυχαία επιλεγμένη λέξη για δοκιμή - καίριος
# 对应网址：https://el.wiktionary.org/wiki/%CE%BA%CE%B1%CE%AF%CF%81%CE%B9%CE%BF%CF%82
# Corresponding URL: https://el.wiktionary.org/wiki/%CE%BA%CE%B1%CE%AF%CF%81%CE%B9%CE%BF%CF%82
# Αντίστοιχη διεύθυνση URL: https://el.wiktionary.org/wiki/%CE%BA%CE%B1%CE%AF%CF%81%CE%B9%CE%BF%CF%82
# 在这里发现23万个单词只爬取到18万个确实是出了问题，像κάνω这样常用的单词反而没有被爬取下来
# It was found that only 180,000 words were crawled out of 230,000, which was indeed a problem as commonly used words like κάνω were missed
# Παρατηρήθηκε ότι από τις 230.000 λέξεις, μόνο 180.000 ανακτήθηκαν, πράγμα που αντιπροσωπεύει πρόβλημα, καθώς λέξεις όπως το κάνω που χρησιμοποιούνται συχνά δεν ανακτήθηκαν
id = 68536
name = str(id).zfill(6)
path = "saved_words/" + name + ".html"

# 定义保存H3s词频与定义的字典
# Define dictionaries to save H3 frequencies and definitions
# Ορισμός των λεξικών για την αποθήκευση της συχνότητας των H3 και των ορισμών
h3s_frequency = dict()
h3s_definition = dict()

def update_h3s_dicts(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        parser_output = soup.find('div', class_ = 'mw-parser-output')
        
        # 获取所有H3标签
        # Get all H3 tags
        # Παίρνουμε όλα τα H3 tags
        # 有些单词如γλειφιντζούρι是其它单词的另一形式，第二层可以为空
        # Some words like γλειφιντζούρι are alternative forms of other words, and the second layer can be empty
        # Ορισμένες λέξεις όπως το γλειφιντζούρι είναι εναλλακτικές μορφές άλλων λέξεων και η δεύτερη στρώση μπορεί να είναι κενή
        try:
            h3_tags = parser_output.find_all('span', class_ = 'mw-headline')
        except:
            return 0
        
        # 标记是否进入了希腊语部分，比起bool形我更喜欢用int
        # Flag to indicate whether it has entered the Modern Greek section, I prefer using int instead of bool
        # Σημείωνουμε αν έχουμε μπει στο τμήμα της Νέας Ελληνικής, προτιμώ να χρησιμοποιήσω ακέραιο αντί για λογική μεταβλητή
        flag = 0
        
        for h3_tag in h3_tags:
            h3_name = h3_tag.text.replace(' ', '')
            
            # 不想花太多时间在灵活运用BeautifulSoup的语法上，因此尽可能用简单方法实现对现代希腊语标签的提取
            # I don't want to spend too much time on flexible use of BeautifulSoup syntax, so I try to achieve the extraction of Modern Greek tags with simple methods
            # Δεν θέλω να ξοδέψω πολύ χρόνο στην ευέλικτη χρήση της σύνταξης του BeautifulSoup, οπότε προσπαθώ να εξάγω τα tags της Νέας Ελληνικής με απλούς τρόπους
            # 判断是否进入了现代希腊语部分
            # Check if it has entered the Modern Greek section
            # Ελέγχουμε αν έχουμε μπει στο τμήμα της Νέας Ελληνικής
            if '(' in h3_name and ')' in h3_name:
                if "(el)" in h3_name:
                    flag = 1
                else:
                    flag = 0
                    
            # 如果进入了希腊语部分，更新词频字典和定义字典
            # If it has entered the Modern Greek section, update the frequency and definition dictionaries
            # Αν βρισκόμαστε στο τμήμα της Νέας Ελληνικής, ενημερώνουμε το λεξικό με την συχνότητα και τον ορισμό
            if flag == 1:
                if h3_name in h3s_frequency:
                    h3s_frequency[h3_name] += 1
                else:
                    h3s_frequency[h3_name] = 1
                    h3s_definition[h3_name] = str(h3_tag)


# 遍历所有文件进行更新字典操作
# Iterate through all files to update the dictionaries
# Διατρέχουμε όλα τα αρχεία για να ενημερώσουμε τα λεξικά
for id in range(1, 184411):
    name = str(id).zfill(6)
    path = "saved_words/" + name + ".html"
    update_h3s_dicts(path)
    print(id)

import json

# 按照词频对词典进行排序
# Sort the dictionaries based on frequency
# Ταξινομούμε τα λεξικά με βάση τη συχνότητα
h3s_frequency = sorted(h3s_frequency.items(), key=lambda x: x[1], reverse=True)
# 按照词频排序后的顺序对定义字典进行排序
# Sort the definitions based on the frequency order
# Ταξινομούμε τους ορισμούς με βάση τη σειρά της συχνότητας
h3s_definition = sorted(h3s_definition.items(), key=lambda x: [item[0] for item in h3s_frequency].index(x[0]))

# 将字典转化为格式化后的JSON文本，indent参数控制缩进，使用ensure_ascii=False来保持希腊语文本不编码
# Convert the dictionaries to formatted JSON texts
# Μετατρέπουμε τα λεξικά σε μορφοποιημένα κείμενα JSON, το παράμετρος indent ελέγχει την εσοχή, το ensure_ascii=False χρησιμοποιείται για να διατηρήσει το κείμενο στα ελληνικά ακέραιο
frequency_json = json.dumps(h3s_frequency, ensure_ascii=False, indent=4)
definition_json = json.dumps(h3s_definition, ensure_ascii=False, indent=4)

# 将JSON文本写入文件，用html格式单纯是因为发现先前保存的文件不知为何都用了这一格式
# Write the JSON texts to a file, using the HTML format simply because it was found that the previously saved files were all in this format
# Γράφουμε τα κείμενα JSON σε ένα αρχείο, χρησιμοποιούμε τη μορφή HTML απλά επειδή παρατηρήθηκε ότι τα προηγούμενα αποθηκευμένα αρχεία είχαν αυτήν τη μορφή
with open("H3s_dic.html", 'w', encoding='utf-8') as f:
    f.write(frequency_json)
    f.write("\n")
    f.write(definition_json)
