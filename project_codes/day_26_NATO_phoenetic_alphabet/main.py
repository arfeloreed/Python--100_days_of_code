import pandas


nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

# create a dictionary out of the csv file
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

# create a list of the phonetic code words from a word that the user inputs
word = input("Enter a word: ").upper()
word = [letter for letter in word]
code_words = [nato_alphabet_dict[letter] for letter in word if letter in nato_alphabet_dict.keys()]
print(code_words)
