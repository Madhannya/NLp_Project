import random
des =open("./NLp_Project/Destination.txt","r",encoding = 'utf-8')
sen =open("./NLp_Project/sentance.txt","r",encoding = 'utf-8')
complete = []
fplane = []
Alldes=[]
Allsen=[]
Allprize=[]
Alltime=[]
count = des.readline()
for x in range(int(count)):
    c1=des.readline().strip()
    c2=c1.split(',')
    Alldes.append(c2)
count = sen.readline()
print(count)
for x in range(int(count)):
    Allsen.append(sen.readline().strip())
for a in Allsen:
    print(a)
count = sen.readline()
print(count)
for x in range(int(count)):
    Allprize.append(sen.readline().strip())
count = sen.readline()
print(count)
for x in range(int(count)):
    Alltime.append(sen.readline().strip())
# for re in range(len(Alldes)):
#     print(Alldes[re])
number = 0
bb = 0
sen.close()
for a3 in range(len(Allsen)-1):
    complete.append([])
    for a2 in range(len(Allprize)) :
        complete[bb].append([])
        for a in range(len(Alldes)-1):
            for b in range(len(Alldes)):
                for c in range(len(Alldes[a])-1):
                    for d in range(len(Alldes[b])-1):
                        if Alldes[a][c] != Alldes[b][d]:
                            Alls = Allsen[a3].replace('des1',Alldes[a][c])
                            Alls = Alls.replace('des',Alldes[b][d])
                            if a2 <= 1 :
                                complete[bb][a2].append(Alls + Allprize[a2])
                            else :
                                rand = random.randint(5,50)
                                complete[bb][a2].append(Alls + Allprize[a2] + str(rand*100) + "บาท")

                        #     if (rand == 1 and rand1 == 1) or rand ==2:
                        #         randsen= random.randint(0,5)
                        #         rand1 = random.randint(0,11)
                        #         rand2 = random.randint(0,3)
                        #         if randsen <= 1 :
                        #             if rand2 == 0 and rand1 <= 11 :
                        #                 Alls = Alls + Alltime[randsen] + str(rand1) + "เช้า"
                        #             if rand2 == 1 and rand1 >= 1 and rand1 <= 3:
                        #                 Alls = Alls + Alltime[randsen] + "บ่าย"+str(rand1) 
                        #             if rand2 == 2 and rand1 >= 1 and rand1 <= 5 :
                        #                 Alls = Alls + Alltime[randsen] + str(rand1) + "ทุ่ม"
                        #             if rand2 == 3 and rand1 >= 1 and rand1 <= 5 :
                        #                 Alls = Alls + Alltime[randsen] + "ตี"+str(rand1) 
                        #             else :
                        #                 continue
                        #         else :
                        #             Alls = Alls + Alltime[randsen]
                        # print(Alls)
                        # complete[bb].append(Alls)
                        number = number +1
    
    bb = bb +1 
des.close()
print(number)
for i, data in enumerate(complete):
    for j , data2 in enumerate(data):
        fileout = open("./Project/NLp_Project/sentence"+str(i)+"w_p"+str(j)+".txt","w", encoding='utf-8-sig')
        for line in data2:
            fileout.writelines(line+"\n")




