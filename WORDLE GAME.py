import random

def give_instructions():
    print('''\nWordle is a word guessing game.
    You have 5 attempts.
    🗸 means the letter is in the word and correct position.
    x means the letter is in the word but in the wrong position.
    _ means the letter is not in the word.
          
    Best of luck''')

words=["this","five","help","take","pink","cats"]

hidden_word=random.choice(words)


def check_word(guess):
    if hidden_word==guess:
        print("Congrats!! You did it.")
        return True
    else:
        result=""
        for i,j in zip(guess, hidden_word):
            if i==j:
                result=result+"(🗸)"  #zip function uses the inexes so the c is at the correct position
            elif i in hidden_word:
                result=result+"(x)"
            else:
                result=result+"(_)"
        print(result)
        return False
    
def main():
    attempts=5
    while attempts>0:
        guess=input("Enter four letter word: ")
        if check_word(guess):
            break
        else:
            attempts-=1
            if attempts!=1:
                print(f"You have {attempts} attempts left")
            else:
                print(f"You have {attempts} attempt left")


    else:
        print("Game over")

main()