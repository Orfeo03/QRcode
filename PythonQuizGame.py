# Python quiz game

questions = ("How many elements are in the periodic table?:",
             "Which animal lays the largest eggs?:",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?:",
             "Which planet in the solar system is the hottest?: ")  #First we need a tuple of options

options = (("A. 116","B. 117","C. 118","D. 119"),
           ("A. Whale","B. Crocodile","C. Elephant ","D. Ostruch"),
           ("A. Nitrogen","B. Oxygen ","C. Carbon-Dioxide","D. Hydrogen"),
           ("A. 206","B. 207","C. 208 ","D. 209 "),
           ("A. Mercury","B. Venus ","C. Earth ","D. Mars "))

answers = ("C","D","A","A","B") #Then a tuple of answers
guesses = [] #We will be appending guesses to our list.That's why we're using
#a list rather than a tuple
score = 0
question_num = 0

for question in questions:
    print("-------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D):").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score = score + 1
    else:
        print("Wrong Answer")
        print(f"{answers[question_num]} is the correct answer")
    question_num +=1

print("------------------")
print("      RESULTS       ")
print("-------------------")

print("answers:",end="")
for answer in answers:
    print(answer,end=" ")
print()

print("guesses:",end="")
for guess in guesses:
    print(guess,end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your final score is: {score} %")
print("-------------------")
print("Congratulations!")











