import random 

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    guess = random.randint(low,high)
    while feedback != 'c' :
        if low!=high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (h) , too low (l), or correctly (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1


    print(f'Yay! The computer guessed your number, {guess}, correctly!!')

computer_guess(100)