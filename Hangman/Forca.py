secretWord = "avocado"
types = []
chances = 3

while True:
    if chances <= 0:
        print("You Lose!\n")
        break

    guess = input("\nSay a letter: ")
    types.append(guess)

    if len(guess) > 1:
        print("\nJust one letter!")
        continue

    if guess in secretWord:
        print("\nCongratulations, you get a letter\n")        
    else:
        print("\nYou missed, try again!\n")
        types.pop()
        chances -= 1

    gets = ''
    for letra in secretWord:
        if letra in types:
            gets += letra
        else:
            gets += '*'

    if gets == secretWord:
        print(f"\nCongratulations, YOU WON!! The word was: {secretWord}\n")
        break
    else:
        print(f"gets: {gets}")

    print(f"There are still {chances} chances.")
