from os.path import join, dirname

path = join(dirname(__file__), "news", "vntrans.2.0.txt")
with open(path) as f:
    news = f.read()
tags = ["vehicle", "loc", "dame", "time", "reason"]
result = ["{}: {}".format(tag, news.count(tag)) for tag in tags]
with open("real_tags.txt", "w") as f:
    f.write("\n".join(i for i in result))
