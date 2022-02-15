import random
capital=1000

def win():
    global capital
    capital+=50

def lose():
    global capital
    capital-=50

rounds=0
win_count=0
lose_count=0

while capital:
    rounds+=1
    if random.randint(0,1):
        win()
        win_count+=1
        print(f'round:{rounds}\tcaptical:{capital}\twin_count:{win_count}\tlose_count:{lose_count}')
    else:
        lose()
        lose_count+=1
        print(f'round:{rounds}\tcaptical:{capital}\twin_count:{win_count}\tlose_count:{lose_count}')

print('you finally lost your captical')
