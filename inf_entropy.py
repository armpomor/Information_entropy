from string import printable
from collections import Counter
from math import log2


class Entropy:
    def __init__(self, text=''):
        self.text = text
        self.counter = Counter()
        self.entropy = 0
        
    def symbols(self):
        """
        Возвращает printable + русский алфавит
        """
        rus_alphabet = [chr(i) for i in range(ord('а'), ord('а')+ 32)]
        return printable + ''.join(rus_alphabet)
    
    def analyze_text(self) -> dict:
        """
        Считаем количество каждого символа в тексте
        """
        for i in range(len(self.text) - 1):
            self.counter[self.text[i]] += 1
        return self.counter
    
    def inf_entropy(self):
        self.analyze_text()
        for i in self.symbols():
            if i in self.counter:
                probability = self.counter[i] / sum(self.counter.values())
                self.entropy += -probability * log2(probability)
     
    
if __name__ == '__main__':
    with open('crack_doom.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        
    entropy = Entropy(text)
    
    entropy.inf_entropy()
    print(entropy.entropy)
