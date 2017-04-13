from os import system

import random
import sys
import datetime

raw_file_name = "raw_file.txt"
out_file_name = str(datetime.datetime.now()).replace('-', '_').replace(':', '_')

def keyListMaker(k):
	randList = [0]*52

	i = 0
	j = 65

	while i <= 25:
		randList[i] = j
		i += 1
		j += 1

	j = 97

	while i < 52:
		randList[i] = j
		i += 1
		j += 1

	i = 0
	while i < 26:
		r = random.randint(i,25)
		aux = randList[i]
		randList[i] = randList[r]
		randList[r] = aux
		i += 1

	while i < 52:
		r = random.randint(i,51)
		aux = randList[i]
		randList[i] = randList[r]
		randList[r] = aux
		i += 1

	return randList

def encrypt(keyList, char):
	if (ord(char) >= 65 and ord(char) <= 90):
		return chr(keyList[ord(char) - 65])
	elif (ord(char) >= 97 and ord(char) <= 122):
		return chr(keyList[ord(char) - 71])
	elif (char == ' '):
		return '+'
	elif (char == '\n'):
		return '-'
	else:
		return char

def main():
	arqOld = open(raw_file_name,'rt')
	arqNew = open(out_file_name,'w')
	arqKey = open(out_file_name + '_decrypter.py','w')

	content = arqOld.read()
	newContent = ''
	keyList = keyListMaker(25)
	i = 0

	while i < len(content):
		newContent += encrypt(keyList,content[i]);
		i+=1

	arqNew.write(newContent)
	arqNew.close()

	i = 65
	decryptedProg = 'dicKey = {'

	while i <= 90:
		decryptedProg += str(i) + ':' + str(keyList.index(i) + 65) + ','
		i += 1

	i = 97
	while i <= 122:
		decryptedProg += str(i) + ':' + str(keyList.index(i) + 71) + ','
		i += 1

	decryptedProg = decryptedProg + '43:32,45:10}\n'
	decryptedProg += "import sys\n"
	decryptedProg += "arq = open('" + out_file_name + "','r')\n"
	decryptedProg += "content = arq.read()\n"
	decryptedProg += "arq.close()\n"
	decryptedProg += "newContent = ''\n"
	decryptedProg += "i = 0\n"
	decryptedProg += "while i < len(content):\n"
	decryptedProg += "\taux = ord(content[i])\n"
	decryptedProg += "\tif ((aux >= 65 and aux <= 90) or (aux >= 97 and aux <= 122)):\n"
	decryptedProg += "\t\tnewContent += chr(dicKey[aux])\n"
	decryptedProg += "\telif (aux == 43 or aux == 45):\n"
	decryptedProg += "\t\tnewContent += chr(dicKey[aux])\n"
	decryptedProg += "\telse:\n"
	decryptedProg += "\t\tnewContent += content[i]\n"
	decryptedProg += "\ti += 1\n"
	decryptedProg += "if len(sys.argv) > 1 and sys.argv[1] == '--save':\n"
	decryptedProg += "\tarqNew = open('decrypted_file.txt','w')\n"
	decryptedProg += "\tarqNew.write(newContent)\n"
	decryptedProg += "\tarqNew.close()\n"
	decryptedProg += "else:\n"
	decryptedProg += "\tprint(newContent)"

	arqKey.write(decryptedProg)
	arqKey.close()

if __name__ == '__main__':
	if len(sys.argv) > 1:
		raw_file_name = sys.argv[1]

	if len(sys.argv) > 2:
		out_file_name = sys.argv[2]

	main()