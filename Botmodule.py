import random
def oppchoice(multideck,p1score,p2score,maxvalue):
    if p1score <= maxvalue:
        countlist=[0,0,0,0,0,0,0,0,0,0,0,0,0]
        place=0
        while True:
            try:
                card=multideck[place]
            except IndexError:
                break
            checkcard=card[0]
            match checkcard:
                case "Ace":
                    countlist[0]+=1
                case "Two":
                    countlist[1]+=1
                case "Three":
                    countlist[2]+=1
                case "Four":
                    countlist[3]+=1
                case "Five":
                    countlist[4]+=1
                case "Six":
                    countlist[5]+=1
                case "Seven":
                    countlist[6]+=1
                case "Eight":
                    countlist[7]+=1
                case "Nine":
                    countlist[8]+=1
                case "Ten":
                    countlist[9]+=1
                case "Jack":
                    countlist[10]+=1
                case "Queen":
                    countlist[11]+=1
                case "King":
                    countlist[12]+=1
                case _:
                    break
            place+=1
        print(countlist)


