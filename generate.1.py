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

x, y = load_data('dataset/laura5w_p2.txt')
x_2, y_2 = load_data('dataset/laura3w_t1.txt')
# print(f)

def write_data(data ,part):
    with open(part, 'w', encoding='utf-8-sig') as f:
        for sen, label in data:
            p = str(random.randrange(1,99)) + '00'
            f.writelines(str(random.randint(0,24)) + " " + "B_TIME" + "\n")
            f.writelines(". I_TIME\n")
            f.writelines(str(random.randint(0,5)) + '0' + " I_TIME" + "\n")
            f.writelines(p + " " + "B-PRICE" + '\n')
            f.writelines("ไป O\n")
            f.writelines(sen[random.sample([0,2],1)[0]] + " " + "B_DEST" + "\n")
            
            f.writelines('\n')


write_data(zip(x, y) ,'dataset/some_word8.txt')