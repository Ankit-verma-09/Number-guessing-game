import random
# class game:
def decorator(func):
    def call():
        print("!!! Welcome to number guessing game !!!".center(145," "))
        print("!!! you have only 10 attemps to guess!!!".center(145," "))
        func()
    return call
@decorator
def guess_game():
    ## to take random value by system
    print("!!!Do you want to play game right now.!!!".center(145," "))
    ask=input("".rjust(73," "))
    ask1=ask.lower()
    if ask=="yes":
        targetValue = random.randint(1,100)
        # print(targetValue)
        #assigning values to print number of attempts
        attempt=10
        attempt_count=0
        #while loop with concition checking
        while attempt_count<=attempt:
            try:
                print("Guess a value: ".rjust(80," "),end=(""))
                q=input()
                n=int(q)
                attempt_count+=1
                if attempt_count>=attempt:
                    print(f"no. of attempts:{attempt_count} your guess is wrong".center(145," "))
                    print("you taken too many attempts".center(145," "))
                    break
                elif n==targetValue:
                    print(f"no. of attempts:{attempt_count} your guess is right".center(145," "))
                    break
                elif n>targetValue:
                    m=n-targetValue
                    print(f"no. of attempts:{attempt_count} your guess is high".center(145," "))            
                else:
                    m=targetValue-n
                    print(f"no. of attempts:{attempt_count} your guess is low".center(145," "))        
            except ValueError:
                q.lower()
                if q=="end" or "quit" or "exit":
                    print("Thank you for playing. Visit again!".center(145," "))
                    return 0
                else:
                    print("Invalid value: Enter Correct Integer Value".center(145," "))
    else:
        print("Thank you for coming. Visit again!".center(145," "))
guess_game()


