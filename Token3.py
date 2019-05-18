import deepcut
openfile = open("./NLp_Project/sentence3.txt","r", encoding='utf-8-sig')
opendict = open("./NLp_Project/Destination.txt","r",encoding='utf-8-sig')
openout = open("./NLp_Project/laura3.txt","w",encoding='utf-8-sig')
opendict.readline()
dict = []
for line in opendict:
    for word in line.rstrip().split(','):
        dict.append(word)
dataset = [line.strip() for line in openfile]
word = [[w for w in deepcut.tokenize(data, dict + ['ไป'])]for data in dataset]
for w in word :
    if len(w)!= 4 :
        print(w)
for x in word :
    for i,y in enumerate(x):
        if i == 1 :
            openout.writelines(y + " " + "B-DEST"+"\n")
        elif i == 3 :
            openout.writelines(y +" " + "B-START"+"\n")
        else :
            openout.writelines(y + " " + "O"+"\n") 
    openout.writelines('\n')


