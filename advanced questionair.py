import easygui as eg
import time

score = 0

print("Welcome to the storage quiz!")
print("\n")
print("There will be 10 questions on the types of storage.")
print("\n")

def ask_question(question, choices):
  answer = eg.buttonbox(question, choices=choices, title="Question")
  return answer

def check_answer(answer, correct_answer):
  global score
  if answer == correct_answer:
    print("Correct!")
    score += 1
  else:
    print("Incorrect.")

# Question 1
question1 = "RAM and ROM are types of main memory."
answer1 = ask_question(question1, ["True", "False"])
check_answer(answer1, "True")

# Question 2
question2 = "ROM stands for Read Only Memory."
answer2 = ask_question(question2, ["True", "False"])
check_answer(answer2, "True")

# ... (continue with the rest of the questions)

print("\n")
print("Your final score is:", score)

if score >= 10:
  print("You have passed the quiz!")
else:
  print("You have failed the quiz. Make sure to revise network and storage!")

# If the user failed, ask them a question about RAM
if score < 10:
  print("\n")
  print("What does RAM stand for?")
  answer_ram = ask_question("What does RAM stand for?", ["Random Access Memory", "Read Only Memory"])
  if answer_ram == "Random Access Memory":
    print("Correct!")
  else:
    print("Incorrect. RAM stands for Random Access Memory.")