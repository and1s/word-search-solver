import numpy as np
import string

WORDLIST_FILENAME = "words.txt"

def split(word):
	return [char for char in word]

def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

wordlist = load_words()

# Put in word search letter row by row below
letters = ['AWAKIIHTOHSLDQTEAUSP', 'YGSSDFCOFIREGUEKTLGU', 'ASAOLZRFSERILWTHSIUS', 'LBCZJELTFAIDDTLNIHPI', 'TAOSBLMCSIHCAEOONJNZ', 'PLAAICHSSESDOOIPAOEU', 'INWEDTIGWXMSAEHEYEWE', 'OSRIZWSEIHANDERSSWAO', 'LAOAHALCHITLTFFHVOYE', 'EITEQKPNIBHBTNISTAAB', 'EOMTLAIHUDSEIBOSDDSR', 'WEMEHITCINNVLNUSCNUE', 'AJGAIZHANEBTAATCSAEI', 'UGGLTADIUSSIMBLTLHIH', 'UDRRLSIOKNRESIEQSIOV', 'PEESTHENBAYOCHNTOPOE', 'IAETUILEXECDLIEEVODS', 'AUPIODOEGREBMEALFSSE', 'TLMIHYOUMCCGDLGLNTAE', 'UIEARDODRSSEVTPSOZLE']
cross = []

for string in letters:
	string = string.lower()
	cross.append(split(string))

print(*cross, sep = "\n")

wordright = ""
wordleft = ""
worddown = ""
wordup = ""
wordupright = ""
wordupleft = ""
worddownright = ""
worddownleft = ""

#length of words to find
for length in range(3,11):
	#length of words to find
	lenword = length
	for num in range(20):
		for num2 in range(20):
			wordright = ""
			worddown = ""
			wordleft = ""
			wordup = ""
			wordupleft = ""
			wordupright = ""
			worddownleft = ""
			worddownright = ""
			for num3 in range(0,lenword):
				try:
					wordright += cross[num][num2 + num3]
				except:
					pass
				try:
					worddown += cross[num + num3][num2]
				except:
					pass
				try:
					worddownright += cross[num + num3][num2+num3]
				except:
					pass
				if(num-lenword+1 >= 0):
					wordup += cross[num-num3][num2]
				if(num2-lenword+1 >= 0):
					wordleft += cross[num][num2-num3]
				if(num-lenword+1 >= 0 and num2-lenword+1 >= 0):
					wordupleft += cross[num-num3][num2-num3]
				try:
					if(num2-lenword+1 >= 0):
						wordupright += cross[num-num3][num2+num3]
				except:
					pass
				try:
					if(num2-lenword+1 >= 0):
						worddownleft += cross[num+num3][num2-num3]
				except:
					pass
			if(len(wordright)==lenword):
				if(wordright in wordlist):
					print(wordright)
					print(num,num2)
				#pass
			if(len(worddown)==lenword):
				if(worddown in wordlist):
					print(worddown)
					print(num,num2)
				#pass
			if(len(worddownright)==lenword):
				if(worddownright in wordlist):
					print(worddownright)
					print(num,num2)
				#pass
			if(wordup != ""):
				if(wordup in wordlist):
					print(wordup)
					print(num,num2)
				#pass
			if(wordleft != ""):
				if(wordleft in wordlist):
					print(wordleft)
					print(num,num2)
				#pass
			if(wordupleft != ""):
				if(wordupleft in wordlist):
					print(wordupleft)
					print(num,num2)
				#pass
			if(len(wordupright)==lenword and wordupright != ""):
				if(wordupright in wordlist):
					print(wordupright)
					print(num,num2)
				#pass
			if(len(worddownleft)==lenword and worddownleft != ""):
				if(worddownleft in wordlist):
					print(worddownleft)
					print(num,num2)
				#pass



















