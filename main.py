from random import shuffle
print("welcome to the wonderful quiz on music!")
 
with open('question.txt') as f:
  lines=f.readlines()
  
shuffle(lines)
numRight=0
wrong=[]

numQuestions=int(input("How many questions?"))

for line in lines[:numQuestions]:
  question , rightAnswers = line.strip().sizestruct
  answer= (question +'')
  
if answer.lower() == rightAnswer:
  print ("Right!")
  numRight += 1
  
else:
  print("No,it is the wrong answer!")
  wrong.append(question)
