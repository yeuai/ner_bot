from os import makedirs
from os.path import dirname, join

import joblib
from languageflow.model.crf import CRF

from load_data import load_data
from models.custom_transformer import CustomTransformer
from models.features import template


if __name__ == '__main__':
    train_path = join(dirname(__file__), "data", "corpus", "train.txt")
    train_set = []
    train_set += load_data(train_path)
    print("Load data from file", train_path)
    transformer = CustomTransformer(template)
    X_train, y_train = transformer.transform(train_set)

    # train
    params = {
        'c1': 1.0,  # coefficient for L1 penalty
        'c2': 1e-3,  # coefficient for L2 penalty
        'max_iterations': 1000,  #
        # include transitions that are possible, but not observed
        'feature.possible_transitions': True
    }
    model_path = join(dirname(__file__), "models", "model_crf.bin")
    folder = dirname(model_path)
    try:
        makedirs(folder)
    except:
        pass
    estimator = CRF(params=params, filename=model_path)
    estimator.fit(X_train, y_train)
    transformer_path = join(dirname(__file__), "models", "transformer.bin")
    joblib.dump(transformer, transformer_path)
