from os.path import join, dirname

from underthesea import word_tokenize

from models.model_crf import CRFModel


def inverse_tokens(tokens):
    entities = []
    text = ""
    flag = 0
    for i in tokens:
        if i[1].startswith("B") and flag == 1:
            entities.append("<START:{}> {} <END>".format(type, text))
            # entities.append({"type": type, "text": text})
            text = i[0]
            type = i[1].split("B_")[1]
            flag = 1
        elif i[1].startswith("I") and flag == 1:
            text = text + " " + i[0]
        elif i[1].startswith("B"):
            text = i[0]
            type = i[1].split("B_")[1]
            flag = 1
        elif flag == 1 and not i[1].startswith("I"):
            entities.append("<START:{}> {} <END>".format(type, text))
            flag = 0
            text = ""
        else:
            text = 0
    return entities


def ner(sentence):
    model_path = join(dirname(__file__), "models", "model_crf.bin")
    tokens = word_tokenize(sentence)
    model = CRFModel.instance(model_path)
    output = model.predict(tokens)
    tokens = [token[0] for token in output]
    tags = [token[1] for token in output]
    output = []
    for tag, token in zip(tags, tokens):
        output.append((token, tag))
    text = inverse_tokens(output)
    return text
