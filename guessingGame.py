secretNum = 8
guessCount = 0
guessLimit = 3
while guessCount < guessLimit:
    guess = int(input('Guess: '))
    guessCount += 1
    if guess ==secretNum:
         print("Winner winner chicken dinner!")
         break 
    else:
        print("Guess again!")
else: 
    print("You lost :( womp womp wommmmmp")
