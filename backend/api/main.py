from fastapi import FastAPI, UploadFile, File, HTTPException, Query
from pydantic import BaseModel
from backend.app.io_utils import dataframer
from backend.app.text_utils import (
    word_count_df, top_words_df, unique_words_df, hapax_legomena_df,
    lexical_diversity_df, sentence_count, avg_sentence_length
)
class WordCount(BaseModel):
    word: str
    count: int

class AnalysisResponse(BaseModel):
    top_words: list[WordCount]
    hapax_legomena: list[str]
    sentence_count: int
    avg_sentence_length: float
    lexical_diversity: float
    unique_words: int
    total_tokens: int

app = FastAPI()

@app.post("/analyze/file", response_model=AnalysisResponse)
async def analyze_file(
    file: UploadFile = File(..., description="Plain text file"),
    top_n: int = Query(30, ge=1, le=200),
    encoding: str = Query("utf-8")
):
    try:
        raw = await file.read()
        text = raw.decode(encoding, errors="ignore")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Cannot read file: {e}")

    if not text.strip():
        raise HTTPException(status_code=400, detail="Empty or unreadable file.")

    df = dataframer(text)

    counts = word_count_df(df)
    top_series = counts.head(top_n)

    return AnalysisResponse(
        top_words=[WordCount(word=w, count=int(c)) for w, c in top_series.items()],
        hapax_legomena=hapax_legomena_df(df),
        sentence_count=sentence_count(text),
        avg_sentence_length=avg_sentence_length(text),
        lexical_diversity=lexical_diversity_df(df),
        unique_words=len(unique_words_df(df)),
        total_tokens=len(df),
    )