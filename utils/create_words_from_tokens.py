import random

lines = open("/home/shubham/Documents/MTP/SyntheticDetectionTextGenration/SynthText/data/tokens/tokens_HI.txt").readlines()

tokens=[]
digits =[]
for line in lines:
	t, count  = line.split(":")
	
	if "०" <= t <= "९":
		digits.append(t)
		
	if int(count) >= 10:
		tokens.append(t)

f = open("/home/shubham/Documents/MTP/SyntheticDetectionTextGenration/SynthText/data/newsgroup/rand_text/newsgroup_HI"
         ".txt", "w")

p = len(tokens) -1

num_words = 1000
words=[]
for i in range(0, num_words):
	len = random.randint(2, 10)
	word=""
	for j in range(0, len):
		x = random.randint(0 ,3)
		if x ==2 :
			k = random.randint(0 , 9 )
			word+=digits[k]
		else:
			k =random.randint(0, p)
			word+=tokens[k]
	words.append(word)
	
	f.write(word)
	f.write(" ") if i%100 ==0 else f.write("\n")
	


