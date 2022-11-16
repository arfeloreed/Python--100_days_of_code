from quiz_brain import QuizBrain
from question_model import Question
from data import question_data


question_bank = []
for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))

question = QuizBrain(question_bank)
while question.still_has_question():
    question.next_question()
