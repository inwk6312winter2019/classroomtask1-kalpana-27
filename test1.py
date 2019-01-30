import string
fin = open("word.txt","r")
for line in fin:
	word = line.split()
	word1= word.strip(string.punctuation)
	for i in word1:
		print(i)
