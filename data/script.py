from os.path import join, dirname
import re


def text2conll(news, matched):
    text = news.split("-")[1].strip()
    for match in matched:
        sent = text.replace(match[1], "[{}/{}]".format(match[1], match[0]))
    return 0


def convert(text):
    words = ""
    possition = 0
    pattern = r"<START:(?P<tag>\w*)>\s(?P<token>[\w\s]+)\s<END>"
    for match in re.finditer(pattern, text, re.MULTILINE):
        start_tag, end_tag = match.regs[0]
        tag = text[start_tag:end_tag]
        words += text[possition:start_tag]
        if tag.startswith("<START"):
            tag_match = re.match(pattern, tag)
            tag_word = tag_match.group("token")
            words = words + tag_word
        possition = end_tag
    news = words + text[possition:len(text)]
    matched = re.findall(pattern, text)
    tokens = text2conll(news, matched)
    return tokens


path = join(dirname(__file__), "news", "vntrans.2.0.txt")
with open(path) as f:
    news = f.read().split("\n")
for post in news:
    sentences = convert(post)
