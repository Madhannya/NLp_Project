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

f = load_data('NLp_Project/laura0.txt')
# print(f)

def write_data(data ,part):
    with open(part, 'w', encoding='utf-8-sig') as f:
        for j, sentence in enumerate(data):
            for word in sentence:
                for i in range(6):
                    if i == 4:
                        f.writelines('กลับ O\n')
                    else :
                        f.writelines(word[i] + " " + data[1][j][i] + "\n")
                f.writelines('\n')

write_data(f ,'NLp_Project/some_word1.txt')