
class Quizbrain():
    def __init__(self, q_list):
        self.qnumber = 0
        self.question_list = q_list
        self.score = 0
    
    def check_answer(self, question, answer):
        if question.answer.lower() == answer.lower():
            print("You got right")
            self.score +=1
        else:
            print("You got wrong")
        print(f"The Correct answer is: {question.answer}")
        print(f"Your Current Score is: {self.score}/{self.qnumber}")
        print("\n")
        
        

    def next_question(self):
        current_question = self.question_list[self.qnumber]
        self.qnumber +=1
        answer = input(f"Q.{self.qnumber} : {current_question.text} (True/False): ")
        self.check_answer(current_question, answer=answer)

    def still_questions_avaliable(self):
        return self.qnumber < len(self.question_list)
        # Above single line of code will perform same task
        # if self.qnumber < len(self.question_list):
        #     return True
        # else: 
        #     return False
    
  
        


