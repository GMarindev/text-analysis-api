import re
import pandas as pd

SENT_RE = re.compile(r"[.!?]+")

def word_count_df(df: pd.DataFrame) -> pd.Series:
    return df["word"].value_counts()

def top_words_df(df: pd.DataFrame, n: int = 30) -> pd.Series:
    return word_count_df(df).head(n)

def unique_words_df(df: pd.DataFrame) -> list[str]:
    return df["word"].unique().tolist()

def hapax_legomena_df(df: pd.DataFrame) -> list[str]:
    vc = word_count_df(df)
    return vc[vc == 1].index.tolist()

def lexical_diversity_df(df: pd.DataFrame) -> float:
    total = len(df)
    return (df["word"].nunique() / total) if total else 0.0



def sentence_count(text: str) -> int:
    sents = [s.strip() for s in SENT_RE.split(text) if s.strip()]
    return len(sents)

def avg_sentence_length(text: str) -> float:
    sents = [s.strip() for s in SENT_RE.split(text) if s.strip()]
    if not sents:
        return 0.0
    return sum(len(s.split()) for s in sents) / len(sents)

