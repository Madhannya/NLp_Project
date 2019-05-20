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

x, y = load_data('dataset/laura4w_p2.txt')
x_2, y_2 = load_data('dataset/laura3w_t1.txt')
# print(f)

def write_data(data ,part):
    with open(part, 'w', encoding='utf-8-sig') as f:
        for sen, label in data:
            f.writelines("ตั๋ว O\n")
            for i in range(8):
                if i < 3:
                    f.writelines(sen[i] + " " + label[i] + "\n")
                if i ==6:
                    f.writelines(sen[i] + " " + "B-PRICE" + '\n')
            j = random.randrange(len(x_2)-1)
            # for i in range(4,7):
            f.writelines(x_2[j][5] + " " + "B-TIME" + "\n")
            f.writelines(x_2[j][6] + " " + "I-TIME" + "\n")
            f.writelines('\n')

write_data(zip(x, y) ,'dataset/some_word5.txt')