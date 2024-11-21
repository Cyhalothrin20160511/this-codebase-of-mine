## GD Input
## This class is used to receive user input

import urllib.request

class GDInput:
    def __init__(self):
        self.word = "no_word"
        self.language = "el"
        
    
    def receiveInput(self):
        self.word = str(input().strip())
        
        # 暂时只考虑希腊语的情况
        # For now only the Greek case will be considered
        # Προς το παρόν θα εξεταστεί μόνο η ελληνική περίπτωση
        if self.language == "el":
            self.word = self.word.lower()
            
        # 编码对于希腊语单词是有必要的
        # Encoding is necessary for Greek words
        # Η κωδικοποίηση είναι απαραίτητη για τις ελληνικές λέξεις
        self.word = self.encodeWord(self.word)
        
    
    def encodeWord(self, word):
        encoded_word = urllib.parse.quote(word)
        return encoded_word
