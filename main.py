import random

answerlist = ["world", "hello", "supercalifragilisticexpialidocious", "illuminati", "turtle", "backpack"]
# randomizes the word list
random.shuffle(answerlist)
# picks out the word and separates the letters
answer = list(answerlist[0])

display = []
display.extend(answer)

for i in range (len(display)):
    display=[i] = '-'
print(' '.join(display))
print()

count = 0

while count 