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
while input1!="1":
    currentcard=multideck.pop(0)
    print(currentcard,end="")
    input1=input()