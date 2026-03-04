import pandas as pd
import io

def export_answers(results):

    data = []

    for r in results:

        data.append({
            "Question": r["question"],
            "Answer": r["answer"],
            "Citation": r["citation"],
            "Confidence": r["confidence"]
        })

    df = pd.DataFrame(data)

    buffer = io.BytesIO()

    df.to_excel(buffer, index=False)

    buffer.seek(0)

    return buffer