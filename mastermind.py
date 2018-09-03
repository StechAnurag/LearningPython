#! /usr/bin/python

print 'Content-Type: text/html'
print ''

import cgi
import random
form = cgi.FieldStorage()

reds = 0
whites = 0

if "answer" in form:
    answer = form.getvalue("answer")
else:
    answer = ""
    for i in range(4):
        answer += str(random.randint(0, 9))

if "guess" in form:
    guess = form.getvalue("guess")
    for key, digit in enumerate(guess):
        if digit == answer[key]:
            reds += 1
        else:
            for answerDigit in answer:
                if answerDigit == digit:
                    whites += 1
                    break
                    
else:
    guess = ""

if "NumberOfGuess" in form:
    NumberOfGuess = int(form.getvalue('NumberOfGuess')) + 1
else:
    NumberOfGuess = 0

if NumberOfGuess == 0:
  message = "I've chosen a 4 digit number. Can you guess it ?"
elif reds == 4:
  message = "Well done ! You got it in "+str(NumberOfGuess)+" number of guesses. <a href=''>PLAY AGAIN</a>"
else:
  message = "You've "+str(reds)+" correct digit(s) in right place and "+str(whites)+" correct digit(s) in wrong place.<br>You've had "+str(NumberOfGuess)+" number of guess(es)."

print '<center>'
print '<h1>Game : Mastermind</h1>'
print "<p>"+message+"</p>"
print '<form method="post">'
print '<input type="text" name="guess" value="'+guess+'">'
print '<input type="hidden" name="answer" value="'+answer+'">'
print '<input type="hidden" name="NumberOfGuess" value="'+str(NumberOfGuess)+'">'
print '<input type="submit" value="guess">'
print '</form>'
print '</center>'
