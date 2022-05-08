from class_question import Question

quiz_prompts = [
    "Question 1:\nThe capital of Finland is:\na) Oslo\nb) Helsinki\nc) Tampere",
    "Question 2:\nWhich of the islands is not Greek:\na) Crete\nb) Corfu\nc) Cyprus",
    "Question 3:\nThe capital of the Netherdlands is:\na) Amsterdam\nb) Roterdam\nc) Hague",
    "Question 4:\nThe capital of Peru is:\na) Lima\nb) Limassol\nc) Limon",
    "Question 5:\nMauritius island is located in which ocean:\na) Pacific\nb) Atlantic\nc) Indian"
]


questions = [
    Question(quiz_prompts[0], "b"),
    Question(quiz_prompts[1], "c"),
    Question(quiz_prompts[2], "a"),
    Question(quiz_prompts[3], "a"),
    Question(quiz_prompts[4], "c"),

]


def run_quiz(questions):
    score = 0
    for question in questions:
        print(question.prompt)
        answer = input()
        if answer == question.answer:
            score += 1

    print(f"You have scored {score} out of {len(questions)}!")

    if score == len(questions):
        print("Congrats!")


run_quiz(questions)