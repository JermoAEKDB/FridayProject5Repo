import sqlite3
import random
Right = 0
Wrong = 0
print("Welcome to my Super Bowl Trivia!")

Questions = {
    'Will Travis Kelce score a touchdown?(Yes/No)':'Yes',
    'Did Red, Blue, or Orange gatorade get dumped on the winning coach?' : 'Red',
    'How many touchdowns did Patrick Mahomes throw for?' : '3',
    'Was Taylor Swift shown atleast seven times on television?(Yes/No)':'Yes',
    'How many receptions did Brandon Aiyuk have?':'6'
    }

for leg in Questions:
    print(leg)
    answer = input("Choose Wisely: ")
    if answer == Questions[leg]:
        print("Great Job your parlay is saved!")
        Right +=1
    else:
        print("You busted your parlay and lost!")
        Wrong +=1
        print("The right choice is: ", Questions[leg])

print("Here are your final scoring totals (Right:Wrong) - ", Right ,":", Wrong ,)