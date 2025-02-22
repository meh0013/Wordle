#Wordle
import os
import random
os.system('color')
import nltk
from nltk.corpus import words,wordnet
from termcolor import colored

#Download required datasets
nltk.download("words")
nltk.download("wordnet")
	
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
    word_list=[word.lower() for word in words.words() if len(word)==5]
    answer=random.choice(word_list)
    
    def get_word_meaning(word):
        synsets=wordnet.synsets(word)
        if synsets:
            return synsets[0].definition()
        return "Meaning not found"
    
    #answer=random.choice(open("fiveletterwords_final.txt","r").read().split())
    while flag==0:
        guess=input("_ _ _ _ _\n").lower()
        print("_ _ _ _ _")
        if len(guess)==5:
            
            if len(guess_list)==5:
                print("You lost! The word was: ",answer)
                print("Meaning of your word: ",get_word_meaning(answer))
                break
            
            if guess not in open("fiveletterwords_final.txt","r").read().split():
                print("Given word does not exist...please try again")
                continue
            
            result=word_compare(guess,answer)
            guess_list.append(result)
            
            if guess==answer:
                print("Congratulations! You've guessed the word!")
                flag=1
            
            for previous_guess in guess_list:
                print(previous_guess)

                   
        else:
            print("Please enter a valid 5-letter word.")
            
wordle()




