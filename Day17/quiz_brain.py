class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def stil_has_Qusetion(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer =input(f"q: {self.question_number}: {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("You got it wrong")
        print(f"The correct answer was: {current_answer}")  
        print(f"Your current score is:{self.score} / {self.question_number} ")
        print("\n")
  

