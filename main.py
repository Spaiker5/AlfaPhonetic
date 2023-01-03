import pandas as pd

alfa_file = "alfa_file.csv"

data = pd.read_csv(alfa_file)
phonetic = {row.letter: row.code for (index, row) in data.iterrows()}

tekst = input("Wklej tekst:").upper()

przeliterowane = [phonetic[letter] for letter in tekst]

print("-".join(przeliterowane))