from os.path import join, dirname

import joblib
import pycrfsuite
from sklearn_crfsuite import metrics

from load_data import load_data

if __name__ == '__main__':
    test_path = join(dirname(__file__), "data", "corpus", "test.txt")
    test_set = []
    test_set += load_data(test_path)
    transformer_path = join(dirname(__file__), "models", "transformer.bin")
    transformer = joblib.load(transformer_path)
    X_test, y_test = transformer.transform(test_set)

    model_path = join(dirname(__file__), "models", "model_crf.bin")
    estimator = pycrfsuite.Tagger()
    estimator.open(model_path)
    y_pred = [estimator.tag(x) for x in X_test]
    f1_score = metrics.flat_f1_score(y_test, y_pred, average='weighted')
    print(round(f1_score, 3))
