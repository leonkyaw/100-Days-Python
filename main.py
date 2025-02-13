from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]["text"], question_data[i]["answer"]))

# print(question_bank[0].text)  # access attribute 'text' of item in a list

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_question()

print("You have completed the quiz")
print(f"Your final score was {quiz_brain.score}/{quiz_brain.question_no}")


