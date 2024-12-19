import enchant
import wonderwords

class Style():
  RED = "\033[31m"
  GREEN = "\033[32m"
  BLUE = "\033[34m"
  RESET = "\033[0m"

w = wonderwords.RandomWord()
actual_word = list(reversed(str(w.word(word_min_length=10,word_max_length=10))))
d = enchant.Dict("en_US")


counter = 0
while counter != 6 :   #checks if guess incorrect
    correction = ["-","-","-","-","-"]
    guess = list(input(""))
    

    if len(guess) == len(actual_word) and d.check(map(guess)) == True:
        for x in guess:
            
            if x in actual_word:
                accIndex = actual_word.index(x)
                guessIndex = guess.index(x)
                
                if accIndex == guessIndex:
                    correction[guessIndex] = f"{Style.GREEN}{x}{Style.RESET}"
                else:
                    correction[guessIndex] = x
        print("".join(correction))
        counter+=1
    else:
        print(f"{len(actual_word)} characters only and real words only")

print("".join(actual_word))
