import pandas as pd
from pypdf import PdfReader


def parse_pdf(path):

    reader = PdfReader(path)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    questions = [
        q.strip()
        for q in text.split("\n")
        if len(q.strip()) > 10
    ]

    return questions


def parse_excel(path):

    df = pd.read_excel(path)

    questions = df.iloc[:, 0].dropna().tolist()

    return questions