from nltk.corpus import words
import random


class User_Progress():

    def __init__(self,n):
        self.letters = ['_']*n
    
    def status(self):
        return ''.join(self.letters)


class Health_Bar():

    def __init__(self, lives):
        self.hearts = ['<3']*lives
        self.current_health = lives-1
        self.is_empty = False
    
    def damage(self):

        if self.is_empty == True:
            print("Health already empty, game over!")

        else:
            self.hearts[self.current_health] = 'X'
            self.current_health -= 1
            if self.current_health == -1:
                self.is_empty = True

    def status(self):
        return ' '.join(self.hearts)


if __name__ == '__main__':
    words_list = words.words()
    vocab_size = len(words_list)

    target_word = words_list[random.randint(0,vocab_size-1)].lower()
    target_word_length = len(target_word)

    user_letters = User_Progress(target_word_length)

    lives = input("How many lives would you like? ")
    
    try:
        lives = int(lives)

    except:
        print("Looks like you did not input a valid number... defaulting to 5.")
        lives = 5

    health = Health_Bar(lives)

    print(health.status())
    print(user_letters.status())
        
    alive = True

    while alive:

        guess = input("Guess a Letter: ")

        if guess == 'exit':
            alive = False

        wrong_guess = True
        for i, char in enumerate(target_word):
            if guess == char:
                wrong_guess = False
                user_letters.letters[i] = guess 
            
        if wrong_guess == True:
            health.damage()
        
        print("")
        print("Health: ", health.status())
        print("")
        print("Answer: ", user_letters.status())
        print("")

        if health.is_empty:
            print("Game Over!")
            print("The word was: ", target_word)
            alive = False
        
        if user_letters.status() == target_word:
            print("You Won!")
            print("The word was: ", target_word)
            alive = False

                

    
    