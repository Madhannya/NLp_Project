import random

def load_data(part):
    sents, labels = [], []
    words, tags = [], []
    with open(part, 'r', encoding='utf-8-sig') as f:
        for line in f:
            line = line.rstrip()
            if line:
                word, tag = line.split()
                words.append(word)
                tags.append(tag)
            else:
                sents.append(words)
                labels.append(tags)
                words, tags = [], []
                
    return sents, labels

x, y = load_data('./Project/NLp_Project/laura1w_t3.txt')
x_2, y_2 = load_data('./Project/NLp_Project/laura2w_p0.txt')
# print(f)

def write_data(data ,part):
    with open(part, 'w', encoding='utf-8-sig') as f:
        for sen, label in data:
            f.writelines(str(random.randint(1,99)) + "00 " + "B-PRICE" + "\n") 
            # f.writelines("ตั๋ว O\n")
            rand = random.randint(1,24)
            rand1 = random.randint(0,1)
            rand2 = random.randint(1,59)
            if rand1 == 0 :
                word = "AM"
            else : 
                word = "PM"
            if rand2 <= 9:
                rand2 = "0"+str(rand2)
            f.writelines(str(rand) + " " + "B-TIME" + "\n")
            f.writelines("." + " " + "I-TIME" + "\n")
            f.writelines(str(rand2) + " " + "I-TIME" + "\n")
            f.writelines(word + " " + "I-TIME" + "\n") 
            # f.writelines(str(random.randint(1,99)) + "00 " + "B-PRICE" + "\n") 
            for i in range(8):
                if i ==3:
                    f.writelines(sen[i] + " " + "B-DEST" + '\n')
                # if i ==5:
                #     f.writelines(sen[i] + " " + "B-DEST" + '\n')
            # rand = random.randint(1,24)
            # rand1 = random.randint(0,1)
            # rand2 = random.randint(1,59)
            # f.writelines(str(random.randint(1,99)) + "00 " + "B-PRICE" + "\n") 
            # if rand1 == 0 :
            #     word = "AM"
            # else : 
            #     word = "PM"
            # if rand2 <= 9:
            #     rand2 = "0"+str(rand2)
            # f.writelines(str(rand) + " " + "B-TIME" + "\n")
            # f.writelines("." + " " + "I-TIME" + "\n")
            # f.writelines(str(rand2) + " " + "I-TIME" + "\n")
            # f.writelines(str(random.randint(1,99)) + "00 " + "B-PRICE" + "\n")
            # f.writelines(word + " " + "I-TIME" + "\n") 
            # f.writelines(str(random.randint(1,99)) + "00 " + "B-PRICE" + "\n") 
            # j = random.randrange(len(x_2)-1)
            # # for i in range(4,7):
            # f.writelines(x_2[j][4] + " " + "B-PRICE" + "\n")
            # for i in range(5,9):
            #     f.writelines(x_2[j][i] + " " + "I-PRICE" + "\n")
            f.writelines('\n')

write_data(zip(x, y) ,'./Project/NLp_Project/chain15.txt')