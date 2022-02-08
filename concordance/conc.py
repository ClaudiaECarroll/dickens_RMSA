import sys
import os
import io
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

files_path = sys.argv[1]
textfile_dictionary = sys.argv[2]

rmsa_words = ["face", "countenance", "manner", "look", "expression", "appearance"]

for filename in os.listdir(files_path):
    if filename.endswith(".txt"):

        file = open(os.path.join(files_path, filename), "rt")
        text = file.read()      

        words = word_tokenize(text)

        words = [word.lower() for word in words if word.isalpha()]

        stops = stopwords.words("english")

        tokens = [word for word in words if word not in stops]
        tokens.insert(0, "pad")

        conc_words = []
        i=[]
               
        for word in rmsa_words:        
            i += [x for x, token in enumerate(tokens) if token == word]
        for number in i:
                conc_words = conc_words + [tokens[number-1], tokens[number+1], tokens[number+2]]
        print(conc_words)
          
        ps = PorterStemmer()

        conc_stems = []
        
        for word in conc_words:
            conc_stems.append(ps.stem(word))
        print(conc_stems)

        file = io.open(textfile_dictionary, mode="r", encoding="utf8")
        dictionaryread = file.read()
        dictionary = dictionaryread.split()
        print(dictionary)

        dictionary_stems = []
        for word in dictionary:
            dictionary_stems.append(ps.stem(word))
        print(dictionary_stems)

        rmsa_count = 0

        for element in dictionary_stems:
            for w in conc_stems:
                if w == element:
                    rmsa_count = rmsa_count + 1

        print(filename, len(tokens), rmsa_count) 
            
    
