count = 0
limit = 5
secret_number = 7

while secret_number == 7:
    guess = int(input("Guess number: "))
    count += 1
    if guess > 7:
        print("Too high, try again")
        remaining = limit - count
        print(f"You have {remaining} tries left.")
    elif guess < 7:
        print("Too low, try again")
        remaining = limit - count
        print(f"You have {remaining} tries left.")
    else:
        print(f"Correct! You guessed it in {count} tries.")
        break

    if count == 5:
        print("Game over")
        break
