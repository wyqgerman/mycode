def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again ")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ", answer)
      
score = 0

name = input("May I have your name?  ")

print("Guess the Animal")

guess1 = input("Which animal lives at the North Pole?\n 1. polar bear \n 2. Leopard \n 3. Blue Whale \n Your Answer : ")
check_guess(guess1, "1")

guess2 = input("Which is the fastest land animal?\n 1. polar bear \n 2. Leopard \n 3. Blue Whale \n Your Answer : ")
check_guess(guess2, "2")

guess3 = input("Which is the larget animal?\n 1. polar bear \n 2. Leopard \n 3. Blue Whale \n Your Answer : ")
check_guess(guess3, "3")

print("Mr. ",name)
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 3) * 100) + "% correct.")
