import random
import time
def ask_question():
    a = random.randint(1, 100)
    b = random.randint(1, 10)
    return a, b, a * b
def play_game():
    score = 0
    start = time. time ()
    time_limit = 10
    print(" + FAST MATH SHOT + ")
    print("Answer quickly! You have 10 seconds/n")
    while time.time() - start < time_limit:
          a, b, answer = ask_question()
          try:
              guess = int(input(f"{a} * {b} ="))
              if guess == answer:
                 score += 1
                 print("Correct!\n")
              else:
                 print("Wrong! \n")
          except ValueError:
              print("+ Numbers only!\n")

    print("Time up!")
    print("Final Score:", score)

play_game()
