from spellchecker import SpellChecker 
class spellcheckerAPP:
    def __init__(self):
        self.spell = SpellChecker()

    def check_correct(self,text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
                print(f"correcting words '{word}' to '{corrected_word}'")
                corrected_words.append(corrected_word)
            else:
                corrected_words.append(word)
                    

        return ' '.join(corrected_words)
    
    def runapp(self):
        print("\n spell cheker")
        while True:
         inp = input("Enter the text ot type exit to quite =")
         if inp.lower() == "exit":
             print("closing the app")
             break
         corect = self.check_correct(inp)
         print(f"corrected text is : {corect}")         

if __name__ == "__main__":
    spellcheckerAPP().runapp()

            
