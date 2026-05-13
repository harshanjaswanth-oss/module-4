import random
import time

number=random.randint(1, 100)
def intro():
    print("may i ask your name")
    global name
    name=input()
    print(name +",we are going to play a game,i am thinking of a number between 1 and 100")
    if (number%2==0):
        x= 'even'
    else:
        x='odd'
    print("\nThis is an {} number" .format(x))
    time.sleep(.5)
    print("Go ahead, Guess!")
def pick():
        guesstaken=0
        while guesstaken <6:
            time.sleep(.25)
            enter=input("guess:")

            try:

                guess=int(enter)
                if guess<=100:
                    guesstaken=guesstaken+1
                    if guesstaken<6:
                        if guess<number:
                            print("The gueses that you have entered is too low")
                        if guess>number:
                            print("The number that you entered is too high")
                        if number!=number:
                            time.sleep(.5)
                            print("try again")
                        

                        if guess==number:
                            break

                        if guess>100 or guess<1:
                            print("silly goose, That number isn't in the range")
                            time.sleep(.25)
                            print("please enter  number between 1 and 100")
            except:
                print("i don't think that "+enter+" is a number. sorry")

        if guess == number:
            guesstaken = str(guesstaken)
            print('good job, {}!  you guessed my number in {} guesses'.format(name,guesstaken))
        if number!=number:
            print('nope. the number i was thinking of'+str(number))

playagain="yes"
while playagain == "yes" or playagain == "y" or playagain == 'Yes':
    intro()
    pick()
    print('do you want to play again')
    playagain=input()
                               

                    