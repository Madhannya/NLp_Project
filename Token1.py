import deepcut
openfile = open("./Project/NLp_Project/sentence1.txt","r", encoding='utf-8-sig')
opendict = open("./Project/NLp_Project/Destination.txt","r",encoding='utf-8-sig')
openout = open("./Project/NLp_Project/laura1.txt","w",encoding='utf-8-sig')
opendict.readline()
dict = []
for line in opendict:
    for word in line.rstrip().split(','):
        dict.append(word)
dataset = [line.strip() for line in openfile]
word = [[w for w in deepcut.tokenize(data, dict + ['ไป'])]for data in dataset]
for w in word :
    if len(w)!= 6 :
        print(w)
for x in word :
    for i,y in enumerate(x):
        if i == 3 :
            openout.writelines(y + " " + "B-START"+"\n")
        elif i == 5 :
            openout.writelines(y +" " + "B-DEST"+"\n")
        else :
            openout.writelines(y + " " + "O"+"\n") 
    openout.writelines('\n')
