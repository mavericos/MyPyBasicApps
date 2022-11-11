"""
A dictionary that stores questions and answers
have a variable that tracks the score of the player
loop through the dictionary using the key values pairs
display each question to the user and allow them to answer
tell them if they agree right or wrong
show the final result when quiz is completed
"""

quiz = {
    "question 1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question 2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question 3": {
        "question": "What is the capital of Italy ?",
        "answer": "Rome"
    },
    "question 4": {
        "question": "What is the capital of Bulgaria?",
        "answer": "Sofia"
    },
    "question 5": {
        "question": "What is the capital of Luxembueg?",
        "answer": "Luxemburg"
    },
    "question 6": {
        "question": "What is the capital of Portugal ?",
        "answer": "Lisabon"
    },
    "question 7": {
        "question": "What is the capital of Belgium?",
        "answer": "Bruxel"
    },
    "question 8": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question 9": {
        "question": "What is the capital of Switzerland ?",
        "answer": "Zurich"
    },
    "question 10": {
        "question": "What is the capital of Finland?",
        "answer": "Helsinki"
    },
    "question 11": {
        "question": "What is the capital of Slovenia?",
        "answer": "Ljubljana"
    },
    "question 12": {
        "question": "What is the capital of Lithuania ?",
        "answer": "Vilnius"
    },

}

score = 0

for key, value in quiz.items():
    print(value["question"])
    answer = input("Answer? ")

    if answer.lower() == value["answer"].lower():
        print("Correct")
        score = score + 1
        print("Your score is: " + str(score))
        print("")
        print("")

    else:
        print("Wrong!")
        print("The answer is : " + value["answer"])
        print("Your score is: " + str(score))
        print("")
        print("")

    print("You got " + str(score) + " out of 12 questions correctly")
    print("Your percentage is " + str(int(score/12 * 100)) + "%")