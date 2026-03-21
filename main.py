import random
fulldeck=[]
multideck=[]
deck="Deck"
with open(deck,'r',encoding='utf-8') as file:
    for line in file:
        content= line.strip()
        tempcardinfo=content.split(",")
        tempcardinfo[2]=int(tempcardinfo[2])
        tempcardinfo[3] = int(tempcardinfo[3])
        fulldeck.append(tempcardinfo)
decnum=int(input("How many decks for a game?: "))
for num in range(decnum):
    multideck.extend(fulldeck)
random.shuffle(multideck)
input1="0"
input2="0"
maxvalue=21
p1score=0
p2score=0
while input1!="1":
    currentcard=multideck.pop(0)
    print(f"Your card is: {currentcard[0]} of {currentcard[1]}. ")
    if currentcard[2]!=currentcard[3]:
        choice=input(f"What value do you choose? [{currentcard[2]}] or [{currentcard[3]}]")
        p1score+=int(choice)
    else:
        p1score+=currentcard[2]
    print(f"Score: {p1score}")
    if p1score>21:
        break
    if input("")=="Enough":
        break
while input2!="1":
    currentcard=multideck.pop(0)
    print(f"Your card is: {currentcard[0]} of {currentcard[1]}. ")
    if currentcard[2]!=currentcard[3]:
        choice=input(f"What value do you choose? [{currentcard[2]}] or [{currentcard[3]}]")
        p2score+=int(choice)
    else:
        p2score+=currentcard[2]
    print(f"Score: {p2score}")
    if p2score>21:
        break
    if input("")=="Enough":
        break
if p2score>21:
    print("Player 1 wins")
elif p1score>21:
    print("Player 2 wins")
elif p1score>p2score:
    print("Player 1 wins")
else:
    print("Player 2 wins")
