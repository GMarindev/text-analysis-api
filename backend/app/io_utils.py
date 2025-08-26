from pathlib import Path
import pandas as pd
import re
from pathlib import Path
import string

def read_file(path: Path, encoding: str = "utf-8") -> str:
    return path.read_text(encoding=encoding)

def dataframer(text: str) -> pd.DataFrame:
    tokens = clean_and_split(text)
    return pd.DataFrame({"word": tokens})

def clean_and_split(text: str) -> list[str]:
    clean_txt = re.sub(f"[{re.escape(string.punctuation)}]", "", text.lower())
    return clean_txt.split()