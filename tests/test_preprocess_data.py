"""Tests for preprocess_data.py"""
import re


def test_stopwords(preprocessor):
    """
    Test if stopwords have been downloaded and "not" does not appear in stopwords
    :param preprocessor:
    :return: void
    """
    assert len(preprocessor.all_stopwords) > 0
    assert "not" not in preprocessor.all_stopwords


def test_process_input(preprocessor):
    """
    Test if input has been processed properly
    :param preprocessor:
    :return: void
    """
    review = "The food was delicious!"
    processed_review = preprocessor.process_input(review)
    assert processed_review.islower() or processed_review == ""
    assert not re.match("[^a-zA-Z]", processed_review)
