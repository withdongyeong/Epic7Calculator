import pickle
import gzip
import sys
from TextRecognitionDataGenerator.trdg.generators.from_dict import GeneratorFromDict

sys.path("../")
sys.path("../TextRecognitionDataGenerator")

def makeDict():
    dict = {
        'a':0
    }
    # save and compress dict
    with gzip.open('epicDict.pickle', 'wb') as f:
        pickle.dump(dict, f, pickle.HIGHEST_PROTOCOL)


def loadDict():
    # load and uncompress dict
    with gzip.open('epicDict.pickle', 'rb') as f:
        dict = pickle.load(f)
    return dict

makeDict()
generator = GeneratorFromDict(
)



