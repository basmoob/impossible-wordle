import random as r
import enchant
import wonderwords

class Style():
  RED = "\033[31m"
  GREEN = "\033[32m"
  BLUE = "\033[34m"
  RESET = "\033[0m"


'''
dictionary = ["apple", "house", "light", "bread", "plant", "water", "grass", "tiger", "chair", "table", "money", "sleep", "world", "cloud", "space", "sweet", "phone", "music", "heart", "green", "stone", "cloud", "river", "laugh", "happy", "angry", "truck", "horse", "apple", "dance", "quick", "swing", "party", "storm", "ocean", "sunny", "silver", "shadow", "peach", "tiger", "lucky", "kingf", "booky", "knife", "honey", "green", "blend", "floor", "peach", "radio", "blood", "heart", "media", "drunk", "grasp", "music", "water", "blend", "swift", "limey", "tree", "plants", "brick", "laugh", "waves", "witch", "stone", "court", "barky", "crisp", "lappy", "smart", "learn", "sound", "magic", "flaty", "turny", "fort", "sharp", "blaze", "cooly", "track", "bread", "hunt", "brand", "clear", "unite", "clean", "dream", "shift", "glass", "watch", "frost", "pasty", "drum", "alien", "clear", "sunny", "forest", "cloudy", "slice", "ship", "rock", "dirt", "clown", "wind", "honest", "worth", "sick", "loud", "raw", "edge", "wave", "party", "cricket", "link", "slice", "print", "chief", "beach"]
num = r.randint(0,100)
actual_word = list(reversed(dictionary [num]))'''

w = wonderwords.RandomWord()
actual_word = list(reversed(str(w.word(word_min_length=10,word_max_length=10))))
print(actual_word)

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
