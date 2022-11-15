class QuizBrain:
    """Initialize the process for the game"""
    def __init__(self, question_list):
        """Initialize the attributes for class QuizBrain"""
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        """Returns a boolean according to the current question_number in relation to length of question_list"""
        return self.question_number <= len(self.question_list)-1

    def next_question(self):
        """checks the question_list and input the text for the user to answer"""
        question = self.question_list[self.question_number].text
        correct_answer = self.question_list[self.question_number].answer.lower()
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question} (True/False): ").lower()
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, answer_user, answer_correct):
        """Compares the user_answer to the correct answer and see if the user's right."""
        if answer_user == answer_correct:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {answer_correct}")
        if self.question_number == len(self.question_list):
            print("You've completed the quiz")
            print(f"Your final score was: {self.score}/{self.question_number}")
        else:
            print(f"Your current score is: {self.score}/{self.question_number}")
        print()
