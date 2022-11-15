import re
try:
	file = open("/usr/share/dict/words", "r")
	englishDictionary = re.sub("[^\w]", " ",  file.read()).split()
	file.close()
except (FileNotFoundError,IOError):
	from enchant import Dict
	englishDictionary=Dict("en_US")
instructions="This is a little program I wrote to help me come up with words I couldn't conjure for wordle! Its going to ask you for three things.\nFirst it will ask for  the letters you know the places of. It wants this as a string (of any length) of all lower case letters and asterisks (*) wherever you don't know the location of letters (for example a string might look like a*bd* or *ddsd). I recommend no more than 3 asterisks. The remaining options are optional! So feel free to ignore them if you prefer (just enter nothing).\nThe other two are (in order) letters you know are good but don't know the location of and letters you know are bad. Both of these just want letters so really any format will do but a single word of just letters (like apftg) is best. Note that the dictionaries used are intentionally extremely loose! Don't just trust this (or any program) blindly!"

print(instructions, end="\n\n")

known=re.sub("r[^a-z]","",input("Green letters! Use * as wildcards and use all lowercase letters please!\n-->").lower())
unknown=set(re.sub("r[^a-z]","",input("Yellow letters! Just lower case letters here!\n-->").lower()))
bad=set(re.sub("r[^a-z]","",input("Grey letters! Again, just lower case here.\n-->").lower()))

alphabet=set("qwertyuiopasdfghjklzxcvbnm")-bad

if len(known)==1:
	print("If you are on a unix operating system the dictionary I have lists all single characters as words so you are going to get nonsense but I'm gonna let you do you.")
elif len(known)==0:
	print("You gave me no input for the green letters! If you are trying (inadvisably) to get me to list all the 5 letter words the input you want is *****. Please Try again!")
	quit()
def recur(prompt: str)->list:
	out=[]
	if prompt.count("*")==0: #something's gone very wrong or they've given us a string with no wildcards
		return prompt
	if prompt.count("*")==1:
		wcloc=prompt.find("*") #only wildcard location
		for char in alphabet:
			proposed=prompt[0:prompt.find("*")]+char+prompt[prompt.find("*")+1:] #replace the * with each character in the alphabet
			if proposed in englishDictionary and (len(set(proposed))== len(set(proposed).union(unknown))): #that last bit is checking if all the yellow letters are included in the string. 
				out.append(proposed)
		return out
	else:
		wcloc=prompt.find("*") #first wildcard location
		for char in alphabet:
			out+=(recur(prompt[0:prompt.find("*")]+char+prompt[prompt.find("*")+1:]))
		return out

print(recur(known))