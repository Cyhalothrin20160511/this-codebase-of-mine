# Schule tou Shu, MEIN λεξικό
import sys
import urllib.request
import ssl
from bs4 import BeautifulSoup
import os
import json

# All functions from here on 
def STS_lexiko():
    while True:
        # Initialize Variables
        flag_dict = {
            0: "EL",        # language_code, ελληνικά ως προεπιλογή αλλά είναι μην διαθέσιμος ο κωδικός
            1: "QW",        # target_command
            2: "Schloss"    # word_request
        }
        
        # I kept this initial sentence because it was originally a German learning dictionary
        print("Willkommen! Was ist Ihre Wahl?")
        
        
        # Phase Zero: Choose a Language
        # Programmer Humor: START FROM ZERO
        print("Please enter your target language code:")
        # Actually it could be all available but I just don't want to start overwhelmed
        print("(Currently available: JA - 日本語; DE - Deutsch; TR - Türkçe)")
        
        # 0 stands for language_code
        get_input(0, flag_dict)
        
        while check_input(0, flag_dict[0]) == 0:
            if politely_ask_if_start_over():
                print("Please enter your target language code again:")
                get_input(0, flag_dict)
        
        
        # Phase One: Choose a Purpose
        print("※ Input QW for querying a word")
        print("※ Input QWW for querying a word from Wiktionary")
        print("※ Input QWL for querying a word from local")
        print("※ Input BYE for ending the program without a reason")
        
        # 1 stands for target_command
        get_input(1, flag_dict)
        
        while check_input(1, flag_dict[1]) == 0:
            if politely_ask_if_start_over():
                print("Please input your command code again:")
                get_input(1, flag_dict)
        

        # Branch One - Querying a Word
        # Phase Two: Choose a Word
        print("Please enter the word you want to query:")
        
        # 2 stands for word_request
        get_input(2, flag_dict)
        
        # Phase Three: Try to find it from local
        # pass
        
        # Phase Four: Crawl the Wiktionary
        url = construct_url(flag_dict[2])
        
        while try_response(url) == 0:
            if politely_ask_if_start_over():
                print("Please enter the word you want to query again:")
                get_input(2, flag_dict)
        
        # Phase Five: Get Information
        soup = make_soup(try_response(url))
        get_information(flag_dict[0], flag_dict[2], soup)
        
        print("Ende")
        return 0
    
    # Auto restart if not meet the real ending point
    STS_lexiko()
    
    
def get_input(flag, dict):
    input_text = str(input().strip())
    
    # Auto Uppercase
    if flag == 1:
        input_text = input_text.upper()
    
    dict[flag] = input_text
    
    
def check_input(flag, input):
    language_list = ["JA", "DE", "TR"]
    command_list = ["QW", "QWW", "QWL"]
    
    if flag == 0 and input in language_list:
        return 1
    
    elif flag == 1:
        if input == "BYE":
            say_goodbye()
        elif input in command_list:
            return 1
            
    else:
        for i in range(3):
            print("INVALID OPTION!!!")
        print("-" * 64)
        return 0
    
    
def say_goodbye():
    rick_astley = """
*******,,,************////////*///****,****/////////////////****
,,,.....,,,,.,.,.....,,,,,.,.,*,,.......,,,,,,,,****,,,.......,.
.....  ...   .   ......,.,,,,,,,,....   .,,,,,,,.,,,,,... .   ..
   .....     ......  ....,,....,,,.    ... ...,,.,,,..,,,,.    .
      .. .....    .  .....(#######(((,...  .  ..,,,,. ,,...,.   
     .....  ...  .  ....,,/##%##((((##... ..  ..,,,,,,,,....,...
      .  .. .  ..    ...,/**/****,,*(#,,,.....,,,,,,.. .,,,,. ,,
  .......  ..        ... ,,(/(/*//***(...,,,,,,..,,,.. ... .,,. 
..  ...   ....   .   ....*.////***,***,...,....,,,,,,..,   .,,,,
.  .    ... . ........., .*///*******..,,,.,,,...,,,.,,,....  ,.
..  . ...,,,,,,,.......,,,,,//**,,**,,,,.   .,,.,,,,,...,,,,,.,,
...,,,,,,. ..,.,,.. .,,,..,,//////***/........,,,,,,,,..,,,,..,,
,,....,... .,, .,,,..,,,,/(,//*(//**,/##%%%(*,,..,,,,..,,,.,..  
......,,,.  ...,,.,,*/#%%%%*,,/***/,.,#%%%%%%%%%%#,,,.,,,...,.  
,...,,,.,,,,,,,,/(#%%%%%%&&(*,.,**,.,%%%%%%%%%%%%%#,,,,,,,,.,. .
.,,,,....,,,,,./%%%%%%%%%%&&&%##/#%&%%%%%%%%%%%%%%%,,,,....,,,..
.,,,......,,. .(%%%%&%%%%%%&%%%%(%%%%%%%%%%%%%%%%%%/,,,,,,,,,,,.
.,,,......,,,,.#%&&&&&%%%%%%%%#(/#(#/*//*#%%%%%&&%%#,,,,...,,,. 
.,,,......,,..,#%&&&&&&%%&&&&&%*/*/////*/#%%%&&&&%%(,,.,,,,..,. 
,,,,...,..,,..,#%&&&&&&&&&&&&&&///#%@#(//#%%&&&&&%%%,,,,,,...,,.
.,,,...,..,,,,,%%&&&&&&&&&&&&&&%(%&@&@@&%&%%%%%&%&&%%,,,,,,,.,,.
.,,.......,,,,**/%&&@&&&@&%%%&&&(%%%%&&@&&#%%%%%%%&&&%,,...,,,,.
,,,,,,,,,.,,/*,***(%&&&&&@&%%%&%(%%%&%%@@&&&&&&&%%&%*,,,,,,,,,,,
,,,,,,,,,,,,,/****/%&@&&&@@&%%&%(%&&&&%%%@@@&&&&&%/,,,,,,,,,,,,,
********,,,,,,(%&&&&@@@@%@@@&&&&(%#&@&%%%%%%%,,,,,,,,,,,,,,,,,,,
*****************#&@@@@@@@@@@&@#(//(##&&&&&&%***,***************
"""
    print("-" * 64)
    print(rick_astley)
    print("-" * 64)
    for i in range(3):
        print("AUF WIEDERSEHEN!!!")
    sys.exit()
    
    
def politely_ask_if_start_over():
    print("Would you like to retype? (Y/N)")
    yes_or_no = str(input().strip()).upper()
    if yes_or_no == "Y":
        return 1
    else:
        sys.exit()
    

def construct_url(word):
    encoded_word = urllib.parse.quote(word)
    url = "https://en.wiktionary.org/wiki/" + encoded_word
    return url


def try_response(url):
    # 創建一個SSL上下文對象，并將下載的Mozilla CA證書集的路徑傳遞給cafile參數
    # Create an SSL context object and pass the path of the downloaded Mozilla CA certificate set to the cafile parameter
    # Δημιουργία αντικειμένου πλαίσιο SSL και παράδοση της διαδρομής του σετ πιστοποιητικών Mozilla που έχει ληφθεί στην παράμετρο cafile
    # Codes are from the old dictionary project so the annotation has three languages
    # Unfortunately the codes of that project are too complicated (programming horror) so I might simply abandon that one and raise its successor here
    current_dir = os.path.dirname(__file__)
    cacert_path = os.path.join(current_dir, "cacert.pem")
    ssl_context = ssl.create_default_context(cafile=cacert_path)
    
    try:
        response = urllib.request.urlopen(url, context=ssl_context)
        return response
    except:
        return 0


def make_soup(response):
    html_doc = response.read().decode('utf-8')
    soup = BeautifulSoup(html_doc, "html.parser")
    return soup


def get_information(language, word, soup):
    # Words that have passed the test: 
    word_info = {
        "word": "",
        "language": "",
        "alternative_forms": "",
        "etymology": "",
        "pronunciation": "",
        "noun": "",
        "declension": "",
        "hyponyms": "",
        "derived_terms": "",
        "related_terms": "",
    }
    # In order to make the program simple and understandable, from here on I will not simplify the function
    word_info["word"] = word
    
    # Language
    id_to_language = {
        "JP": "Japanese",
        "DE": "German",
        "TR": "Turkish",
    }
    word_info["language"] = id_to_language[language]
    
    starting_tag = soup.find(id=word_info["language"])
    current_tag = starting_tag.parent.find_next_sibling()
    current_status = ""
    
    while True:
        print(current_tag)
        while True:
            if current_tag == None or current_tag.name.startswith("h2"):
                pass
            
            elif current_tag.name.startswith("h"):
                span_tag = current_tag.find("span")
                current_status = span_tag.get("id").lower()
                
            elif not current_tag.name.startswith("h"):
                for key in word_info.keys():
                    if key in current_status:
                        text = beautify_text(current_tag.get_text())
                        word_info[key] = word_info[key] + " " + text
                        
            break
            
        if current_tag == None or current_tag.name.startswith("h2"):
            break
        
        current_tag = current_tag.find_next_sibling()
            
    json_data = json.dumps(word_info, ensure_ascii=False, indent=4)
    with open('test.txt', 'w', encoding='utf-8') as file:
        file.write(json_data)
    
    
def beautify_text(text):
    text = text.replace("\n", "\n ")
    return text


if __name__ == "__main__":
    # I can write endless functions, but the main program is absolutely simple
        STS_lexiko()

