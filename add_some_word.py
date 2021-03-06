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

x, y = load_data('dataset/laura1w_p3.txt')
x_2, y_2 = load_data('dataset/laura3w_t1.txt')
# print(f)

def write_data(data ,part):
    with open(part, 'w', encoding='utf-8-sig') as f:
        for sen, label in data:
            for i in range(8):
                if i == 1:
                    f.writelines(sen[i] + " " + label[i] + "\n")
                if i == 3:
                    f.writelines(sen[i] + " " + "B-START" + "\n")
                if i == 5:
                    f.writelines(sen[i] + " " + "B-DEST" + "\n")
                if i == 7:
                    f.writelines(sen[i] + " " + "B-PRICE" + "\n")
            j = random.randrange(len(x_2)-1)
            for i in range(4,7):
                f.writelines(x_2[j][i] + " " + y_2[j][i] + "\n")
            f.writelines('\n')

write_data(zip(x, y) ,'dataset/some_word4.txt')