import pandas as pd
import pytest
from backend.app.text_utils import (
    word_count_df, top_words_df, unique_words_df,
    hapax_legomena_df, lexical_diversity_df,
    sentence_count, avg_sentence_length,
)

@pytest.fixture
def df_simple():
    return pd.DataFrame({"word": ["a", "b", "a", "c", "b", "a", "d"]})

def test_word_count_df(df_simple):
    counts = word_count_df(df_simple)
    assert counts.to_dict() == {"a": 3, "b": 2, "c": 1, "d": 1}

def test_top_words_df(df_simple):
    top = top_words_df(df_simple, n=2)
    assert top.index.tolist() == ["a", "b"]
    assert top.tolist() == [3, 2]

def test_unique_words_df_preserva_orden(df_simple):
    assert unique_words_df(df_simple) == ["a", "b", "c", "d"]

def test_hapax_legomena_df(df_simple):
    hap = hapax_legomena_df(df_simple)
    assert set(hap) == {"c", "d"}

def test_lexical_diversity_df(df_simple):
    assert lexical_diversity_df(df_simple) == pytest.approx(4 / 7)

def test_sentence_count_basico():
    text = "Hola. ¿Qué tal? Bien!"
    assert sentence_count(text) == 3

def test_avg_sentence_length_basico():
    text = "Uno dos tres. Cuatro cinco."
    assert avg_sentence_length(text) == pytest.approx(2.5)

def test_texto_vacio():
    assert sentence_count("") == 0
    assert avg_sentence_length("") == 0.0