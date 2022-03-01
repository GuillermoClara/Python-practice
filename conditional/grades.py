# A certain CS professor gives 5-point quizzes that are graded on the scale 5-A, 4-B, 3-C, 2-D, 1-F, 0-F.
# Write a program that accepts a quiz score as an input and uses a decision structure to calculate the corresponding grade.

grade = eval(input('Enter a grade from 5 to 0: '))
             
letter = ""

if grade == 5:
    letter = 'A'
elif grade == 4:
    letter = 'B'
elif grade == 3:
    letter = 'C'
elif grade == 2:
    letter = 'D'
elif grade <=1:
    letter = 'F'

print('The student got a '+letter)             
             
