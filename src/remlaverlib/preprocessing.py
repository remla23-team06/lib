import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


class Preprocessing:
    def __init__(self):
        self.porter_stemmer = PorterStemmer()
        self.all_stopwords = self._init_stopwords()
        nltk.download('stopwords')

    @staticmethod
    def _init_stopwords():
        all_stopwords = stopwords.words('english')
        all_stopwords.remove('not')
        return all_stopwords

    def process_input(self, review: str) -> str:
        """
        Preprocess the review data
        """
        equalized_review = re.sub('[^a-zA-Z]', ' ', review).lower().split()
        stemmed_review = " ".join(
            [self.porter_stemmer.stem(word) for word in equalized_review if
             word not in set(self.all_stopwords)])
        return stemmed_review
