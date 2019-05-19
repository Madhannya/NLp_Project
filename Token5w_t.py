import deepcut
dataset = []
for i in range(6):            
    openfile = open("./NLp_Project/sentence5w_t" + str(i)+".txt","r", encoding='utf-8-sig')
    dataset.append([line.strip() for line in openfile])
opendict = open("./NLp_Project/Destination.txt","r",encoding='utf-8-sig')
opendict.readline()
dict = []
for line in opendict:
    for word in line.rstrip().split(','):
        dict.append(word)

word = [[[w for w in deepcut.tokenize(data, dict + ['ไป','ราคา','-','โมงเช้า','ประมาณ','ออก','เช้า','มืด'])]for data in line]for line in dataset]
# for line in word[0]:
#     print(line)    
for w in word[0]:
    if len(w)!= 8 :
        print(w)
for w in word[1] :
    if len(w)!= 6 :
        print(w)
for w in word[2] :
    if len(w)!= 6 :
        print(w)
for w in word[3] :
    if len(w)!= 5 :
        print(w)
for w in word[4] :
    if len(w)!= 5 :
        print(w)
for w in word[5] :
    if len(w)!= 5  :
        print(w)


for j, x in enumerate(word):
    openout = open("./NLp_Project/laura5w_t"+str(j)+".txt","w",encoding='utf-8-sig')
    for z in x:  
        for i,y in enumerate(z):
            if i == 0 :
                openout.writelines(y + " " + "B-START"+"\n")
            elif i == 2 :
                openout.writelines(y +" " + "B-DEST"+"\n")
            elif i < 2 :
                openout.writelines(y + " " + "O"+"\n") 

            if i == 3:
                openout.writelines(y + " " + "B-TIME"+"\n")
            if i > 3 :
                openout.writelines(y + " " + "I-TIME"+"\n")

            # if j < 2:
            #     if i == 6:
            #         openout.writelines(y + " " + "B-PRICE"+"\n")
            #     if i == 7:
            #         openout.writelines(y + " " + "I-PRICE"+"\n")
            # elif j == 2:
            #     if i == 6:
            #         openout.writelines(y + " " + "B-PRICE"+"\n")
            #     if i > 6 :
            #         openout.writelines(y + " " + "I-PRICE"+"\n")
            # elif j == 3:
            #     if i == 6:
            #         openout.writelines(y + " " + "B-PRICE"+"\n")
            #     if i > 6 :
            #         openout.writelines(y + " " + "I-PRICE"+"\n")
        
        openout.writelines('\n')


