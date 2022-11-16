import re
try:
	file = open("/usr/share/dict/words", "r")
	englishDictionary = set(re.sub("[^\w]", " ",  file.read()).split())
	file.close()
except (FileNotFoundError,IOError):
	from enchant import Dict
	englishDictionary=Dict("en_US")
instructions="This is a little program I wrote to help me come up with words I couldn't conjure for crosswords! It is going to continuously ask for new words with * in the locations where you don't know letters! Valid inputs look like **a*e or ai**. Type exit to exit!"

print(instructions, end="\n\n")
while True:
   known=re.sub("r[^a-z]","",input("-->").lower())
   if known=="exit":
      quit()
   alphabet=set("qwertyuiopasdfghjklzxcvbnm")

   if len(known)==1:
	   print("If you are on a unix operating system the dictionary I have lists all single characters as words so you are going to get nonsense but I'm gonna let you do you.")
   elif len(known)==0:
	   print("You gave me no input! Please try again!")
	   quit()
   def recur(prompt: str)->list:
	   out=[]
	   if prompt.count("*")==0: #something's gone very wrong or they've given us a string with no wildcards
		   return prompt
	   if prompt.count("*")==1:
		   wcloc=prompt.find("*") #only wildcard location
		   for char in alphabet:
			   proposed=prompt[0:prompt.find("*")]+char+prompt[prompt.find("*")+1:] #replace the * with each character in the alphabet
			   if proposed in englishDictionary :
				   out.append(proposed)
		   return out
	   else:
		   wcloc=prompt.find("*") #first wildcard location
		   for char in alphabet:
			   out+=(recur(prompt[0:prompt.find("*")]+char+prompt[prompt.find("*")+1:]))
		   return out

   print(recur(known))
