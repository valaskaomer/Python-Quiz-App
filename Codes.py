class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    def checkAnswer(self,answer):
        return self.answer == answer
class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0
    def getQuestion(self):
        return self.questions[self.questionIndex]
    def displayQuestions(self):
        question=self.getQuestion()
        print(f"{self.questionIndex + 1}.Soru {question.text}")
        for q in question.choices:
            print(q)
            answer=input("Cevap:")
            self.guess(answer)
            self.loadQuestion()
    def guess(self,answer):
        question=self.getQuestion()
        if question.checkAnswer(answer):
            self.score+=1
        self.questionIndex+=1
    def loadQuestion(self):
        if len(self.questions)==self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestions()
    def showScore(self):
        print(f"Skorunuz {self.score}")
    def displayProgress(self):
        totalQuestion=len(self.questions)
        questionNumber=self.questionIndex +1
        if questionNumber> totalQuestion:
            print("Quiz bitti")
        else:
            print(f"Soru {questionNumber} of {totalQuestion}".center(100,"*"))
q1=Question("\nSORU 1",["A)\nB)\nC)\nD)\nE)"],"A")
q2=Question("\nSORU 2",["A)\nB)\nC)\nD)\nE)"],"B")
q3=Question("\nSORU 3",["A)\nB)\nC)\nD)\nE)"],"C")
q4=Question("\nSORU 4",["A)\nB)\nC)\nD)\nE)"],"D")
q5=Question("\nSORU 5",["A)\nB)\nC)\nD)\nE)"],"E")
questions=[q1,q2,q3,q4,q5]
quiz=Quiz(questions)
quiz.loadQuestion()
