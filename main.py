import random

answerlist = ["world", "hello", "supercalifragilisticexpialidocious", "illuminati", "turtle", "backpack"]
# randomizes the word list
random.shuffle(answerlist)
# picks out the word and separates the letters
answer = list(answerlist[0])

print(answer)

display = []
display.extend(answer)