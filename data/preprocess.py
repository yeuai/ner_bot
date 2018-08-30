import string
from os.path import join, dirname
import re


def normalize(news):
    pattern = r"\(\s.*?\s\)\s[\-\–\*]"
    text = re.sub(pattern, "", news).strip()
    return text


def transform(token):
    output = []
    output.append((token[0].split()[0], "B_{}".format(token[1].upper())))
    for i in token[0].split()[1:]:
        output.append((i, "I_{}".format(token[1].upper())))
    return output


def convert(news):
    text = normalize(news)
    words = []
    tokens = []
    possition = 0
    pattern = r"<START:(?P<tag>\w*)>(?P<token>.*?)<END>"
    for match in re.finditer(pattern, text, re.MULTILINE):
        start_tag, end_tag = match.regs[0]
        tag = text[start_tag:end_tag]
        word = text[possition:start_tag]
        words.append(word)
        if tag.startswith("<START"):
            tag_match = re.match(pattern, tag)
            tag_word = tag_match.group("token").strip()
            tag_name = tag_match.group("tag")
            words.append((tag_word, tag_name))
        possition = end_tag
    last_words = text[possition:len(text)]
    words.append(last_words)
    for word in words:
        if type(word) is str:
            tokens.append([(item, "0") for item in word.split()])
        else:
            if len(word[0].split()) == 1:
                word = (word[0], "B_{}".format(word[1].upper()))
                tokens.append([word])
            else:
                word = transform(word)
                tokens.append(word)
    tokens = [item for sublist in tokens for item in sublist]
    return tokens


def to_conll(token):
    output = '\n'.join('\t'.join(i for i in row) for row in token)
    return output


def save_corpus(tokens):
    corpus = join(dirname(__file__), "corpus")
    split_size = 0.8
    train_size = int(len(tokens) * split_size)
    train_text = '\n\n'.join(to_conll(token) for token in tokens[:train_size])
    test_text = '\n\n'.join(to_conll(token) for token in tokens[train_size:])
    with open(join(corpus, "train.txt"), "w") as tf:
        tf.write(train_text)
    with open(join(corpus, "test.txt"), "w") as tf:
        tf.write(test_text)


path = join(dirname(__file__), "news", "vntrans.2.0.txt")
with open(path) as f:
    news = f.read().split("\n")
tokens = [convert(post) for post in news]
save_corpus(tokens)
