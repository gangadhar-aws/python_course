from data import question_data
from question_model import Question
from quiz_brain import Quizbrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    quesiton_answer = question["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=quesiton_answer)
    question_bank.append(new_question)


quiz = Quizbrain(question_bank)

while quiz.still_questions_avaliable():
    quiz.next_question()
