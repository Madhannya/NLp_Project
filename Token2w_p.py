import deepcut
dataset = []
for i in range(4):            
    openfile = open("./NLp_Project/sentence2w_p" + str(i)+".txt","r", encoding='utf-8-sig')
    dataset.append([line.strip() for line in openfile])
opendict = open("./NLp_Project/Destination.txt","r",encoding='utf-8-sig')
opendict.readline()
dict = []
for line in opendict:
    for word in line.rstrip().split(','):
        dict.append(word)

word = [[[w for w in deepcut.tokenize(data, dict + ['ไป', 'ราคา'])]for data in line]for line in dataset]
# for line in word[0]:
#     print(line)    
for w in word[0]:
    if len(w)!= 6 :
        print(w)
for w in word[1] :
    if len(w)!=6 :
        print(w)
for w in word[2] :
    if len(w)!=9 :
        print(w)
for w in word[3] :
    if len(w)!=7 :
        print(w)


for j, x in enumerate(word):
    openout = open("./NLp_Project/laura2w_p"+str(j)+".txt","w",encoding='utf-8-sig')
    for z in x:  
        for i,y in enumerate(z):
            if i == 1 :
                openout.writelines(y + " " + "B-START"+"\n")
            elif i == 3 :
                openout.writelines(y +" " + "B-DEST"+"\n")
            elif i < 4 :
                openout.writelines(y + " " + "O"+"\n") 

            if i == 4:
                openout.writelines(y + " " + "B-PRICE"+"\n")
            if i > 4 :
                openout.writelines(y + " " + "I-PRICE"+"\n")

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


