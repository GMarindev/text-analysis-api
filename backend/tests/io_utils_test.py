from backend.app.io_utils import read_file, dataframer

def test_read_file(tmp_path):
    p = tmp_path / "example.txt"
    content = "example content"
    p.write_text(content, encoding="utf-8")
    assert read_file(p) == content

def test_dataframer():
    df = dataframer("Hola hola mundo")
    assert df["word"].tolist() == ["hola", "hola", "mundo"]