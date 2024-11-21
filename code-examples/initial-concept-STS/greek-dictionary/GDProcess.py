## GD Process
## This class is used to process information

# 第三方库Beautiful Soup, Python的第三方插件用来提取xml和HTML中的数据
# Third-party library Beautiful Soup, a Python third-party plug-in used to extract data from xml and HTML
# Βιβλιοθήκη Third-party Beautiful Soup, ένα πρόσθετο της Python το οποίο χρησιμοποιείται για εξαγωγή δεδομένων από XML και HTML
from bs4 import BeautifulSoup

class GDProcess:
    def __init__(self):
        self.etymology = "Ετυμολογία"
        self.etymology_text = "NO_ETYMOLOGY_TEXT"
        self.pronunciation = "Προφορά"
        self.pronunciation_text = "NO_PRONUNCIATION_TEXT"
        
        self.elarthro = "Άρθρο"
        self.elarthro_text = "NO_ELARTHRO_TEXT"
        self.elarthro_text_list = []
        self.elousiastiko = "Ουσιαστικό"
        self.elousiastiko_text = "NO_ELOUSIASTIKO_TEXT"
        self.elousiastiko_text_list = []
        self.elepitheto = "Επίθετο"
        self.elepitheto_text = "NO_EPITHETO_TEXT"
        self.elepitheto_text_list = []
        self.elrima = "Ρήμα"
        self.elrima_text = "NO_ELRIMA_TEXT"
        self.elrima_boite = "NO_ELRIMA_BOITE"
        self.elmetochi = "Μετοχή"
        self.elmetochi_text = "NO_ELMETOCHI_TEXT"
        self.elmetochi_text_list = []
        self.elepirrima = "Επίρρημα"
        self.elepirrima_text = "NO_ELEPIRRIMA_TEXT"
        self.elepirrima_text_list = []
        
        self.synonyms = "Συνώνυμα"
        self.synonyms_text = "NO_SYNONYMS_TEXT"
        self.elekfraseis = "Εκφράσεις"
        self.elekfraseis_boite = "NO_ELEKFRASEIS_BOITE"
        self.proverbs = "Παροιμίες"
        self.proverbs_text = "NO_PROVERBS_TEXT"
        self.compoundwords = "Σύνθετα"
        self.compoundwords_text = "NO_COMPOUNDWORDS_TEXT"
        self.inflexions = "Κλίση"
        self.inflexions_text = "NO_INFLEXIONS_TEXT"
        self.inflexions_text_list = []
        self.catlinks = "catlinks" # Κατηγορίες: Οι σημαντικότερες
        self.catlinks_list = []
        
            
    def processInformation(self, html):
        # 我不知道其它语言是否有这些标签，这只是预设
        # I don't know if other languages have these tags, this is just the default
        # Δεν ξέρω αν άλλες γλώσσες έχουν αυτές τις ετικέτες, αυτή είναι απλώς η προεπιλογή
        self.processEtymology(html)
        self.processPronunciation(html)
        
        self.processElarthro(html)
        self.processElousiastiko(html)
        self.processElepitheto(html)
        self.processElrima(html)
        self.processElmetochi(html)
        self.processElepirrima(html)
        
        self.processSynonyms(html)
        self.processElekfraseis(html)
        self.processProverbs(html)
        self.processCompoundwords(html)
        self.processInflexions(html)
        self.processCatlinks(html)
        
    
    def processEtymology(self, html):
        etymology_tag = html.find(id=self.etymology)
        etymology_text_tag = etymology_tag.find_next("dl")
        self.etymology = etymology_tag.get_text(strip=True)
        self.etymology_text = etymology_text_tag.get_text()
    
    
    def processPronunciation(self, html):
        pronunciation_tag = html.find(id=self.pronunciation)
        
        if pronunciation_tag == None:
            self.pronunciation = "PRONUNCIATION NOT FOUND"
            return 0
        
        pronunciation_text_tag = pronunciation_tag.find_next("dl")
        self.pronunciation = pronunciation_tag.get_text(strip=True)
        self.pronunciation_text = pronunciation_text_tag.get_text().rstrip()


    def processElarthro(self, html):
        elarthro_tag = html.find(id=self.elarthro)
        
        if elarthro_tag == None:
            self.elarthro = "ARTHRO NOT FOUND"
            return 0
        
        self.elarthro_text_list = []
        current_tag = elarthro_tag.find_next()
        while current_tag and not current_tag.name.startswith("h"):
            self.elarthro_text_list.append(current_tag.get_text())
            current_tag = current_tag.find_next()
            
        self.elarthro = elarthro_tag.get_text(strip=True)
        self.elarthro_text = "".join(self.elarthro_text_list)
        
        
    def processElousiastiko(self, html):
        elousiastiko_tag = html.find(id=self.elousiastiko)
        
        if elousiastiko_tag == None:
            self.elousiastiko = "OUSIASTIKO NOT FOUND"
            return 0
        
        self.elousiastiko_text_list = []
        current_tag = elousiastiko_tag.find_next()
        while current_tag and not current_tag.name.startswith("h"):
            self.elousiastiko_text_list.append(current_tag.get_text())
            current_tag = current_tag.find_next()
         
        self.elousiastiko = elousiastiko_tag.get_text(strip=True)
        self.elousiastiko_text = "".join(self.elousiastiko_text_list)
        
        
    def processElepitheto(self, html):
        elepitheto_tag = html.find(id=self.elepitheto)
        
        if elepitheto_tag == None:
            self.elepitheto = "EPITHETO NOT FOUND"
            return 0
        
        self.elepitheto_text_list = []
        current_tag = elepitheto_tag.find_next()
        while current_tag and not current_tag.name.startswith("h"):
            self.elepitheto_text_list.append(current_tag.get_text())
            current_tag = current_tag.find_next()
         
        self.elepitheto = elepitheto_tag.get_text(strip=True)
        self.elepitheto_text = "".join(self.elepitheto_text_list)


    def processElrima(self, html):
        elrima_tag = html.find(id=self.elrima)
        
        if elrima_tag == None:
            self.elrima = "RIMA NOT FOUND"
            return 0
        
        elrima_text_tag = elrima_tag.find_next("p")
        elrima_boite_tag = elrima_text_tag.find_next_sibling()
        self.elrima = elrima_tag.get_text(strip=True)
        self.elrima_text = elrima_text_tag.get_text().rstrip()
        self.elrima_boite = elrima_boite_tag.get_text().strip()
        
        
    def processElmetochi(self, html):
        elmetochi_tag = html.find(id=self.elmetochi)
        
        if elmetochi_tag == None:
            self.elmetochi = "METOCHI NOT FOUND"
            return 0
        
        self.elmetochi_text_list = []
        current_tag = elmetochi_tag.find_next()
        while current_tag and not current_tag.name.startswith("h"):
            self.elmetochi_text_list.append(current_tag.get_text())
            current_tag = current_tag.find_next()
         
        self.elmetochi = elmetochi_tag.get_text(strip=True)
        self.elmetochi_text = "".join(self.elmetochi_text_list)
        
        
    def processElepirrima(self, html):
        elepirrima_tag = html.find(id=self.elepirrima)
        
        if elepirrima_tag == None:
            self.elepirrima = "EPIRRIMA NOT FOUND"
            return 0
        
        self.elepirrima_text_list = []
        current_tag = elepirrima_tag.find_next()
        while current_tag and not current_tag.name.startswith("h"):
            self.elepirrima_text_list.append(current_tag.get_text())
            current_tag = current_tag.find_next()
         
        self.elepirrima = elepirrima_tag.get_text(strip=True)
        self.elepirrima_text = "".join(self.elepirrima_text_list)


    def processSynonyms(self, html):
        synonyms_tag = html.find(id=self.synonyms)
        
        if synonyms_tag == None:
            self.synonyms = "SYNONYMS NOT FOUND"
            return 0
        
        synonyms_text_tag = synonyms_tag.find_next("ul")
        self.synonyms = synonyms_tag.get_text(strip=True)
        self.synonyms_text = synonyms_text_tag.get_text()
        
        
    def processElekfraseis(self, html):
        elekfraseis_tag = html.find(id=self.elekfraseis)
        
        if elekfraseis_tag == None:
            self.elekfraseis = "EKFRASEIS NOT FOUND"
            return 0
        
        elekfraseis_boite_tag = elekfraseis_tag.find_next("ul")
        self.elekfraseis = elekfraseis_tag.get_text(strip=True)
        self.elekfraseis_boite = elekfraseis_boite_tag.get_text()
        
        
    def processProverbs(self, html):
        proverbs_tag = html.find(id=self.proverbs)
        
        if proverbs_tag == None:
            self.proverbs = "PROVERBS NOT FOUND"
            return 0
        
        proverbs_text_tag = proverbs_tag.find_next("ul")
        self.proverbs = proverbs_tag.get_text(strip=True)
        self.proverbs_text = proverbs_text_tag.get_text()
        
        
    def processCompoundwords(self, html):
        compoundwords_tag = html.find(id=self.compoundwords)
        
        if compoundwords_tag == None:
            self.compoundwords = "COMPOUNDWORDS NOT FOUND"
            return 0
        
        compoundwords_text_tag = compoundwords_tag.find_next("ul")
        self.compoundwords = compoundwords_tag.get_text(strip=True)
        self.compoundwords_text = compoundwords_text_tag.get_text()
        
        
    def processInflexions(self, html):
        inflexions_tag = html.find(id=self.inflexions)
        
        if inflexions_tag == None:
            self.inflexions = "INFLEXIONS NOT FOUND"
            return 0
        
        self.inflexions_text_list = []
        current_tag = inflexions_tag.find_next()
        while current_tag and not current_tag.name.startswith("h"):
            self.inflexions_text_list.append(current_tag.get_text())
            current_tag = current_tag.find_next()
         
        self.inflexions = inflexions_tag.get_text(strip=True)
        self.inflexions_text = "".join(self.inflexions_text_list)
        
        
    def processCatlinks(self, html):
        catlinks_tag = html.find(id=self.catlinks)
        
        if catlinks_tag == None:
            self.catlinks = "CATLINKS NOT FOUND"
            return 0
        
        # NOT NEEDED
        # self.catlinks = catlinks_tag.get_text(strip=True)
        self.catlinks_list = [li.get_text(strip=True) for li in catlinks_tag.find_all("li")]
        
        
        