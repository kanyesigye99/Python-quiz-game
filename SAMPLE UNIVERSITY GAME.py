#```python
import time

# 20 quiz questions
questions = [
    {
        "question": "What is the main purpose of a hypothesis?",
        "options": [
            "A. To state a testable prediction",
            "B. To prove a theory automatically",
            "C. To list all research sources",
            "D. To replace collected evidence"
        ],
        "correct": "A",
        "explanation": "A hypothesis is a prediction that can be tested using evidence."
    },
    {
        "question": "Which source is most suitable for checking an academic claim?",
        "options": [
            "A. An anonymous comment",
            "B. A peer-reviewed journal article",
            "C. An uncredited advertisement",
            "D. A social media rumor"
        ],
        "correct": "B",
        "explanation": "Peer review provides an additional check on research methods and claims."
    },
    {
        "question": "In a spreadsheet, what does a formula usually begin with?",
        "options": [
            "A. A hashtag (#)",
            "B. A question mark (?)",
            "C. An equals sign (=)",
            "D. A slash (/)"
        ],
        "correct": "C",
        "explanation": "Spreadsheet formulas typically begin with an equals sign."
    },
    {
        "question": "What does a percentage represent?",
        "options": [
            "A. A value out of ten",
            "B. A value out of one thousand",
            "C. A measurement in seconds",
            "D. A value out of one hundred"
        ],
        "correct": "D",
        "explanation": "Percent means 'per hundred.'"
    },
    {
        "question": "Which action best demonstrates critical thinking?",
        "options": [
            "A. Comparing evidence before reaching a conclusion",
            "B. Accepting the first answer without checking",
            "C. Ignoring conflicting evidence",
            "D. Repeating an unsupported claim"
        ],
        "correct": "A",
        "explanation": "Critical thinking involves evaluating evidence and alternatives."
    },
    {
        "question": "What is the independent variable in an experiment?",
        "options": [
            "A. The result measured",
            "B. The factor deliberately changed",
            "C. The researcher's final grade",
            "D. A value that cannot be recorded"
        ],
        "correct": "B",
        "explanation": "The independent variable is the factor the researcher changes."
    },
    {
        "question": "Which chart is generally best for showing a trend over time?",
        "options": [
            "A. Pie chart",
            "B. Venn diagram",
            "C. Line chart",
            "D. Flowchart"
        ],
        "correct": "C",
        "explanation": "A line chart makes changes across successive time points easy to see."
    },
    {
        "question": "What is plagiarism?",
        "options": [
            "A. Editing your own work",
            "B. Summarizing with a citation",
            "C. Quoting with attribution",
            "D. Using someone else's work without proper credit"
        ],
        "correct": "D",
        "explanation": "Plagiarism presents another person's words or ideas without appropriate attribution."
    },
    {
        "question": "What should a clear presentation introduction do?",
        "options": [
            "A. State the topic and purpose",
            "B. Include every detail of the conclusion",
            "C. Avoid mentioning the audience",
            "D. Replace all supporting evidence"
        ],
        "correct": "A",
        "explanation": "A good introduction orients the audience to the topic and purpose."
    },
    {
        "question": "Which number is the median of 3, 5, and 9?",
        "options": [
            "A. 3",
            "B. 5",
            "C. 6",
            "D. 9"
        ],
        "correct": "B",
        "explanation": "The median is the middle value when the numbers are in order."
    },
    {
        "question": "What is a primary source?",
        "options": [
            "A. A summary written decades later",
            "B. An encyclopedia overview",
            "C. An original record or firsthand account",
            "D. A list of unrelated websites"
        ],
        "correct": "C",
        "explanation": "Primary sources provide original or firsthand evidence."
    },
    {
        "question": "Why should research findings cite sources?",
        "options": [
            "A. To make writing longer",
            "B. To avoid reading originals",
            "C. To guarantee every claim is correct",
            "D. To let readers verify the evidence"
        ],
        "correct": "D",
        "explanation": "Citations help readers trace and evaluate supporting evidence."
    },
    {
        "question": "What does the mean of a set of numbers describe?",
        "options": [
            "A. Its arithmetic average",
            "B. Its largest value only",
            "C. Its middle letter",
            "D. Its number of categories"
        ],
        "correct": "A",
        "explanation": "The mean is calculated by dividing the total by the number of values."
    },
    {
        "question": "Which is an example of constructive feedback?",
        "options": [
            "A. This is bad.",
            "B. Your introduction is clear; add evidence to support the second point.",
            "C. Don't bother revising.",
            "D. Everyone else did better."
        ],
        "correct": "B",
        "explanation": "Constructive feedback identifies a strength and a specific improvement."
    },
    {
        "question": "What is the purpose of a control group?",
        "options": [
            "A. To select the final answer",
            "B. To change every variable",
            "C. To provide a comparison",
            "D. To guarantee a positive result"
        ],
        "correct": "C",
        "explanation": "A control group provides a baseline against which results can be compared."
    },
    {
        "question": "Which practice improves online account security?",
        "options": [
            "A. Reusing one password everywhere",
            "B. Sharing passwords by email",
            "C. Ignoring software updates",
            "D. Using unique, strong passwords"
        ],
        "correct": "D",
        "explanation": "Unique, strong passwords reduce the risk of one breach affecting multiple accounts."
    },
    {
        "question": "What does a conclusion in an evidence-based report do?",
        "options": [
            "A. Summarize findings and their implications",
            "B. Introduce unrelated claims",
            "C. Hide limitations",
            "D. Replace the methods section"
        ],
        "correct": "A",
        "explanation": "A conclusion brings the findings together and explains their significance."
    },
    {
        "question": "How many degrees are in a right angle?",
        "options": [
            "A. 45",
            "B. 90",
            "C. 180",
            "D. 360"
        ],
        "correct": "B",
        "explanation": "A right angle measures 90 degrees."
    },
    {
        "question": "Which approach helps make group work effective?",
        "options": [
            "A. Leaving tasks undefined",
            "B. Keeping progress secret",
            "C. Agreeing on roles and deadlines",
            "D. Avoiding communication"
        ],
        "correct": "C",
        "explanation": "Clear roles and deadlines make coordination and accountability easier."
    },
    {
        "question": "What is the most appropriate response to an unexpected result?",
        "options": [
            "A. Delete it without a record",
            "B. Change the prediction afterward",
            "C. Assume the equipment was perfect",
            "D. Check the method and investigate possible causes"
        ],
        "correct": "D",
        "explanation": "Unexpected results should be examined rather than ignored or concealed."
    }
]


# Store players' scores
high_scores = []


def grade_for(percentage):
    if percentage >= 70:
        return "First Class"
    elif percentage >= 60:
        return "Second Class Upper"
    elif percentage >= 50:
        return "Second Class Lower"
    elif percentage >= 40:
        return "Third Class"
    else:
        return "Fail"


def play_quiz(player_name):

    score = 0
    correct_count = 0

    print("\n====================================")
    print("         QUIZ MILLIONAIRE")
    print("====================================")
    print("You have 15 seconds for each question.")
    print("Each correct answer gives you 10 points.\n")

    for number, item in enumerate(questions, start=1):

        print("------------------------------------")
        print(f"Question {number} of {len(questions)}")
        print("------------------------------------")

        print(item["question"])

        for option in item["options"]:
            print(option)

        start_time = time.time()

        answer = input("\nYour answer (A/B/C/D): ").upper()

        end_time = time.time()

        # Calculate time used
        time_used = end_time - start_time

        if time_used > 15:
            print("\nTime's up! +0 points")
            print(f"Correct answer: {item['correct']}")
            print(item["explanation"])
            continue

        if answer == item["correct"]:
            score += 10
            correct_count += 1

            print("\nCorrect! +10 points")

        else:
            print("\nNot quite. +0 points")
            print(f"Correct answer: {item['correct']}")

        print(item["explanation"])

    # Calculate final results
    percentage = round((score / 200) * 100)
    grade = grade_for(percentage)

    # Store score
    record = {
        "name": player_name,
        "score": score,
        "percentage": percentage,
        "grade": grade
    }

    high_scores.append(record)

    # Sort highest score first
    high_scores.sort(
        key=lambda x: (x["score"], x["percentage"]),
        reverse=True
    )

    # Keep only top 10
    high_scores[:] = high_scores[:10]

    # Display results
    print("\n====================================")
    print("           FINAL RESULTS")
    print("====================================")

    print(f"Player: {player_name}")
    print(f"Score: {score} / 200")
    print(f"Correct answers: {correct_count} / 20")
    print(f"Percentage: {percentage}%")
    print(f"Grade: {grade}")

    show_leaderboard()


def show_leaderboard():

    print("\n====================================")
    print("          TOP 10 SCORES")
    print("====================================")

    for position, player in enumerate(high_scores, start=1):

        print(
            f"{position}. {player['name']} - "
            f"{player['score']}/200 - "
            f"{player['percentage']}% - "
            f"{player['grade']}"
        )


def main():

    print("====================================")
    print("         QUIZ MILLIONAIRE")
    print("====================================")

    player_name = input("Enter your name: ").strip()

    if player_name == "":
        print("Please enter your name.")
        return

    while True:

        play_quiz(player_name)

        again = input("\nDo you want to play again? (Y/N): ").upper()

        if again != "Y":
            print("\nThank you for playing Quiz Millionaire!")
            break


# Start the program
main()
#```
