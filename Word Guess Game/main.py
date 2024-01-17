import random
name=input("Enter your Name : ")
print("Good Luck",name)

words=['books','rainbow','snake','library','earth','bag']

word=random.choice(words)

print("Guess the Character : ")

guesses=''

turns=10

while(turns>0):
    fail=0

    for i in words:
        if i in guesses:
            print(i,end="")
        else:
            print("_")
            fail+=1
    
    if fail==0:
        print("YOU WIN!!!")
        print("The Word is",words)
        break  
    print()
    guess=input("Guess the character : ")

    guesses+=guess

    if guess not in word:
        turns-=1
        print("Wrong Character!")

        print("You have",+turns,"More Guesses")

        if turns==0:
            print("BOOO!!1 You Loosed!")
