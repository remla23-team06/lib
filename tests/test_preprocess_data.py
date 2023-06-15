"""Tests for preprocess_data.py"""
import re

import pytest

from src.remlaverlib.preprocessor import Preprocessor


@pytest.fixture
def preprocessor():
    pre_proc = Preprocessor()
    return pre_proc


def test_stopwords(preprocessor):
    assert len(preprocessor.all_stopwords) > 0
    assert "not" not in preprocessor.all_stopwords


def test_process_input(preprocessor):
    review = "The food was delicious!"
    processed_review = preprocessor.process_input(review)
    assert processed_review.islower() or processed_review == ""
    assert not re.match("[^a-zA-Z]", processed_review)
