import time

# 20 quiz questions stored in a list
questions = [
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Processing Unit", "B. Computer Personal Unit",
                    "C. Central Program Utility", "D. Computer Processing User"],
        "answer": "A"
    },
    {
        "question": "Which language are we using for this quiz?",
        "options": ["A. Java", "B. Pxython", "C. C++", "D. HTML"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used to start a comment in Python?",
        "options": ["A. //", "B. /*", "C. #", "D. --"],
        "answer": "C"
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": ["A. display()", "B. output()", "C. print()", "D. show()"],
        "answer": "C"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. String", "B. Integer", "C. Float", "D. Boolean"],
        "answer": "D"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. def", "C. fun", "D. define"],
        "answer": "B"
    },
    {
        "question": "Which operator is used for exponentiation in Python?",
        "options": ["A. ^", "B. ^^", "C. **", "D. //"],
        "answer": "C"
    },
    {
        "question": "Which function is used to get input from a user?",
        "options": ["A. get()", "B. input()", "C. read()", "D. scan()"],
        "answer": "B"
    },
    {
        "question": "Which of these is a Python collection?",
        "options": ["A. List", "B. Folder", "C. Processor", "D. Compiler"],
        "answer": "A"
    },
    {
        "question": "What is the extension of a Python file?",
        "options": ["A. .c", "B. .java", "C. .py", "D. .html"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to make a decision in Python?",
        "options": ["A. if", "B. check", "C. decide", "D. when"],
        "answer": "A"
    },
    {
        "question": "Which loop is commonly used to repeat through a list?",
        "options": ["A. repeat", "B. for", "C. loop", "D. repeat-for"],
        "answer": "B"
    },
    {
        "question": "Which operator means 'equal to' in Python?",
        "options": ["A. =", "B. ==", "C. !=", "D. ==="],
        "answer": "B"
    },
    {
        "question": "What does len() do in Python?",
        "options": ["A. Deletes data", "B. Finds the length",
                    "C. Creates a list", "D. Converts data"],
        "answer": "B"
    },
    {
        "question": "Which one is an integer?",
        "options": ["A. 12.5", "B. '12'", "C. 12", "D. True"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to create a loop over a condition?",
        "options": ["A. while", "B. during", "C. repeat", "D. loop"],
        "answer": "A"
    },
    {
        "question": "Which symbol is used for multiplication?",
        "options": ["A. x", "B. *", "C. ××", "D. #"],
        "answer": "B"
    },
    {
        "question": "Which statement stops a loop immediately?",
        "options": ["A. stop", "B. exit", "C. break", "D. end"],
        "answer": "C"
    },
    {
        "question": "Which data type stores text?",
        "options": ["A. Integer", "B. String", "C. Boolean", "D. Float"],
        "answer": "B"
    },
    {
        "question": "What is the result of 10 // 3 in Python?",
        "options": ["A. 3", "B. 3.33", "C. 1", "D. 4"],
        "answer": "A"
    }
]


# Grade calculation
def get_grade(score):
    percentage = (score / 200) * 100

    if percentage >= 80:
        return "First Class"
    elif percentage >= 70:
        return "Second Class Upper"
    elif percentage >= 60:
        return "Second Class Lower"
    elif percentage >= 50:
        return "Pass"
    else:
        return "Fail"


# Save score to scores.txt
def save_score(name, score):
    with open("scores.txt", "a") as file:
        file.write(f"{name} - {score}\n")


# Display previous high scores
def show_scores():
    try:
        with open("scores.txt", "r") as file:
            scores = file.readlines()

        if scores:
            print("\n===== HIGH SCORES =====")
            for score in scores:
                print(score.strip())
        else:
            print("\nNo scores recorded yet.")

    except FileNotFoundError:
        print("\nNo scores recorded yet.")


# Main game
def play_game():
    print("\n===================================")
    print("\n=======GROUP C UNIVERSITY GAME=====")
    print("   WHO WANTS TO BE A PYTHON STAR?")
    print("===================================\n")

    name = input("Enter your name: ")

    score = 0

    print("\nYou have 15 seconds for each question.")
    print("Correct answer = +10 points")
    print("Wrong answer / timeout = 0 points")

    input("\nPress Enter to start...")

    for number, question in enumerate(questions, start=1):

        print("\n-----------------------------------")
        print(f"Question {number} of {len(questions)}")
        print("-----------------------------------")

        print(question["question"])

        for option in question["options"]:
            print(option)

        start_time = time.time()

        answer = input("\nYour answer (A/B/C/D): ").upper().strip()

        end_time = time.time()

        elapsed_time = end_time - start_time

        if elapsed_time > 15:
            print("TIME'S UP! You get 0 points.")

        elif answer == question["answer"]:
            score += 10
            print("Correct! +10 points")

        else:
            print("Wrong answer! +0 points")
            print(f"The correct answer was {question['answer']}.")

        print(f"Current score: {score}")

    # Final results
    grade = get_grade(score)

    print("\n===================================")
    print("          QUIZ FINISHED")
    print("===================================")
    print(f"Player: {name}")
    print(f"Final Score: {score}/200")
    print(f"Grade: {grade}")

    save_score(name, score)

    print("\nYour score has been saved to scores.txt.")


# Program menu
while True:

    print("\n========== MAIN MENU ==========")
    print("1. Start Quiz")
    print("2. View High Scores")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        play_game()

    elif choice == "2":
        show_scores()

    elif choice == "3":
        print("Thank you for playing!")
        break

    else:
        print("Invalid choice. Please select 1, 2 or 3.")