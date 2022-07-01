import requests
from tempfile import NamedTemporaryFile
from extractor import Extractor

MAX_PATH_LENGTH = 8
MAX_PATH_WIDTH = 2
JAR_PATH = '/data/git/code2vec/JavaExtractor/JPredict/target/JavaExtractor-0.0.1-SNAPSHOT.jar'


class Predictor:
    def __init__(self, config, model):
        model.predict([])
        self.model = model
        self.config = config
        self.path_extractor = Extractor(config,
                                        jar_path=JAR_PATH,
                                        max_path_length=MAX_PATH_LENGTH,
                                        max_path_width=MAX_PATH_WIDTH)

    def predict_java(self, code):
        with NamedTemporaryFile('wt') as tmp:
            tmp.write(code)
            tmp.flush()
            predict_lines, _ = self.path_extractor.extract_paths(tmp.name)
        raw_prediction_results = self.model.predict(predict_lines)
        for raw_prediction in raw_prediction_results:
            yield raw_prediction.code_vector
