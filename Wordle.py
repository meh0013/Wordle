#Wordle

'''
Strings are guessed and updated to a 5x5 matrix(guesser function) 
 -> filter the wordlist to 5 letter words only 
Positional verification function(green - right word right place, yellow - right word wrong place, red - wrong word) 
 -> how to give colour to text on command line? -> can use termcolor but that doesn't allow comparision
 -> alternative: use ANSI sequences, which allow comparision
	-> Instead of applying it to each word individually, create a class that does just that
	-> each string+it's ANSI color code becomes an object, allowing comparision between them
	-> but compare method must be specified else it'll not work -> operator overloading

BACKGROUND_RED = '\033[41m'
BACKGROUND_GREEN = '\033[42m'
BACKGROUND_YELLOW = '\033[43m' # orange on some systems
'''
'''class ColoredText:
    def __init__(self, text, color):
        self.text = text
        self.color = color  # Store the color name or code

    def __repr__(self):
        color_code = {
            "red": "\033[31m",
            "green": "\033[32m",
            "blue": "\033[34m",
            "reset": "\033[0m"
        }
        return f"{color_code.get(self.color, '')}{self.text}{color_code['reset']}" #(coloring start)(text)(end coloring)
    
    def __iter__(self):
        # Yield the attributes in sequence
        yield self.text
        yield self.color

    def compare(self, other):
        return self.text == other.text and self.color == other.color
		#only if both are true, returns true
		#don't really need to check the text, but it's better to have there as a failsafe'''


'''import os
import random
os.system('color')
from termcolor import colored


	
def word_compare(guess, answer):
	result=""
	for i in range(5): 
		if guess[i]==answer[i]: 
			result+=colored(guess[i],"green")
		elif guess[i] in answer:
			result+=colored(guess[i],"yellow")
		else:
			result+=colored(guess[i],"red")	

	return result


def wordle():
	global flag,guess,answer,guess_list
	flag=0
	answer=random.choice(open("fiveletterwords.txt","r").read().split())
	print(answer)
	while flag==0:
		guess_list=[]		
		guess=str(input("_ _ _ _ _\n"))
		guess_list.append(word_compare(guess.lower(), answer))
		print(*guess_list, sep="\n")
		if guess==answer: flag=1

wordle()'''




import os
import random
os.system('color')
from termcolor import colored


	
def word_compare(guess, answer):
	result=""
	for i in range(5): 
		if guess[i]==answer[i]: 
			result+=colored(guess[i],"green")
		elif guess[i] in answer:
			result+=colored(guess[i],"yellow")
		else:
			result+=colored(guess[i],"red")	

	return result


def wordle():
	global flag,guess,answer,guess_list
	flag=0
	guess_list=[]
	
	answer=random.choice(open("fiveletterwords.txt","r").read().split())
	print(answer)
	
	while flag==0:
		guess = input("_ _ _ _ _\n").lower()
		print("_ _ _ _ _")
		if len(guess) == 5:  
            		result = word_compare(guess, answer)
            		guess_list.append(result)  

            		
            		for previous_guess in guess_list:
                		print(previous_guess)

            		if guess == answer:
                		print("Congratulations! You've guessed the word.")
                		flag = 1
		else:
            		print("Please enter a valid 5-letter word.")

wordle()

