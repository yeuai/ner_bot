from collections import Counter
from os.path import join, dirname


def read(path):
    sentences = []
    with open(path) as file:
        data = file.read().split("\n")
        for token in data:
            words = token.split("\t")
            sentences.append(words)
    return sentences


def count_tag(tokens):
    tags = [i[1] for i in tokens]
    count_tag = Counter(tags)
    output = [i for i in count_tag.most_common() if i[0].startswith("B_")]
    output = [(i[0].replace("B_", "").lower(), i[1]) for i in output]
    return output


if __name__ == '__main__':
    token_tag = []
    train_path = join(dirname(__file__), "corpus", "train.txt")
    test_path = join(dirname(__file__), "corpus", "test.txt")
    data = read(train_path) + read(test_path)
    for item in data:
        try:
            if item[1] != '0':
                token_tag.append(item)
        except:
            pass
    tags = count_tag(token_tag)
    result = '\n'.join(': '.join(map(str, row)) for row in tags)
    with open("eda.txt", "w") as ed:
        ed.write(result)
