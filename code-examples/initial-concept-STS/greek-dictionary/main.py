## This is the main program, which is only expected to run locally.
import GDInput
import GDVisit
import GDCrawl
import GDProcess

gdv = GDVisit.GDVisit()
gdc = GDCrawl.GDCrawl()

def beautify_list(list):
    output = " ".join(list)
    return output

if __name__ == "__main__":
    # 定义一个GDInput类，存储单词以及对应语言
    # Define a GDInput class to store words and their corresponding languages
    # Ορίστε μια κλάση GDInput για την αποθήκευση λέξεων και των αντίστοιχων γλωσσών τους
    request = GDInput.GDInput()
    request.receiveInput()
    
    # 构造对应url
    # Construct the corresponding URL
    # Δημιουργία του αντίστοιχου URL
    url = gdv.constructURL(request.language, request.word)
    response = gdv.tryResponse(url)
    
    if response == False:
        print("False")
    else:
        html_doc = gdc.crawlInformation(response)
        word_info = GDProcess.GDProcess()
        
        word_info.processInformation(html_doc)
        
        with open('test.txt', 'w', encoding='utf-8') as file:
            file.write('etymology: ' + word_info.etymology + '\n\n')
            file.write('etymology_text: ' + word_info.etymology_text + '\n\n')
            file.write('pronunciation: ' + word_info.pronunciation + '\n\n')
            file.write('pronunciation_text: ' + word_info.pronunciation_text + '\n\n')
            
            file.write('elarthro: ' + word_info.elarthro + '\n\n')
            file.write('elarthro_text: ' + word_info.elarthro_text + '\n\n')
            file.write('elarthro_text_list: ' + beautify_list(word_info.elarthro_text_list) + '\n\n')
            file.write('elousiastiko: ' + word_info.elousiastiko + '\n\n')
            file.write('elousiastiko_text: ' + word_info.elousiastiko_text + '\n\n')
            file.write('elousiastiko_text_list: ' + beautify_list(word_info.elousiastiko_text_list) + '\n\n')
            file.write('elepitheto: ' + word_info.elepitheto + '\n\n')
            file.write('elepitheto_text: ' + word_info.elepitheto_text + '\n\n')
            file.write('elepitheto_text_list: ' + beautify_list(word_info.elepitheto_text_list) + '\n\n')
            file.write('elrima: ' + word_info.elrima + '\n\n')
            file.write('elrima_text: ' + word_info.elrima_text + '\n\n')
            file.write('elrima_boite: ' + word_info.elrima_boite + '\n\n')
            file.write('elmetochi: ' + word_info.elmetochi + '\n\n')
            file.write('elmetochi_text: ' + word_info.elmetochi_text + '\n\n')
            file.write('elmetochi_text_list: ' + beautify_list(word_info.elmetochi_text_list) + '\n\n')
            file.write('elepirrima: ' + word_info.elepirrima + '\n\n')
            file.write('elepirrima_text: ' + word_info.elepirrima_text + '\n\n')
            file.write('elepirrima_text_list: ' + beautify_list(word_info.elepirrima_text_list) + '\n\n')
            
            file.write('synonyms: ' + word_info.synonyms + '\n\n')
            file.write('synonyms_text: ' + word_info.synonyms_text + '\n\n')
            file.write('elekfraseis: ' + word_info.elekfraseis + '\n\n')
            file.write('elekfraseis_boite: ' + word_info.elekfraseis_boite + '\n\n')
            file.write('proverbs: ' + word_info.proverbs + '\n\n')
            file.write('proverbs_text: ' + word_info.proverbs_text + '\n\n')
            file.write('compoundwords: ' + word_info.compoundwords + '\n\n')
            file.write('compoundwords_text: ' + word_info.compoundwords_text + '\n\n')
            file.write('inflexions: ' + word_info.inflexions + '\n\n')
            file.write('inflexions_text: ' + word_info.inflexions_text + '\n\n')
            file.write('inflexions_text_list: ' + beautify_list(word_info.inflexions_text_list) + '\n\n')
            file.write('catlinks: ' + word_info.catlinks + '\n\n')
            file.write('catlinks_list: ' + beautify_list(word_info.catlinks_list) + '\n\n')
            
        print("True")
