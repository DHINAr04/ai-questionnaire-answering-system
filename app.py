import streamlit as st
import os
import tempfile
from rag_pipeline import generate_answer
from vector_store import create_vector_store
from export_doc import export_answers

st.set_page_config(page_title="AI Questionnaire System", layout="wide")

# ---------- LOGIN SESSION ----------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------- LOGIN PAGE ----------

if not st.session_state.logged_in:

    st.title("🤖 AI Questionnaire Answering System")

    st.info("""
Demo Credentials for Recruiter

Email: **admin@company.com**  
Password: **admin123**
""")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if email == "admin@company.com" and password == "admin123":
            st.session_state.logged_in = True
            st.rerun()

        else:
            st.error("Invalid credentials")

    st.stop()


# ---------- SIDEBAR ----------

st.sidebar.title("Menu")

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()


# ---------- HEADER ----------

st.title("🤖 AI Questionnaire Answering System")

st.write("""
Upload reference documents and paste a questionnaire.

The system retrieves relevant information from uploaded documents and
generates grounded answers with citations.
""")


# ---------- DOCUMENT UPLOAD ----------

st.subheader("Upload Reference Documents (PDF)")

uploaded_files = st.file_uploader(
    "Upload PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    paths = []

    for file in uploaded_files:

        temp_dir = tempfile.mkdtemp()
        path = os.path.join(temp_dir, file.name)

        with open(path, "wb") as f:
            f.write(file.getbuffer())

        paths.append(path)

    create_vector_store(paths)

    st.success("Documents indexed successfully!")


# ---------- QUESTION INPUT ----------

st.subheader("Paste Questionnaire (one question per line)")

questions_text = st.text_area("Questions", height=200)


# ---------- GENERATE ANSWERS ----------

if st.button("Generate Answers"):

    questions = [q.strip() for q in questions_text.split("\n") if q.strip()]

    results = []

    st.markdown("---")
    st.header("Generated Answers")

    for i, q in enumerate(questions):

        answer, snippet, citation, confidence = generate_answer(q)

        st.markdown(f"### Q{i+1}. {q}")

        edited_answer = st.text_area(
            "Answer",
            value=answer,
            key=f"answer_{i}"
        )

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Evidence Snippet**")
            st.info(snippet)

        with col2:
            st.markdown("**Citation**")
            st.write(citation)

            st.markdown("**Confidence**")
            st.progress(confidence/100)
            st.write(f"Confidence Score: {confidence}%")

        results.append({
            "question": q,
            "answer": edited_answer,
            "citation": citation,
            "confidence": confidence
        })


    # ---------- COVERAGE SUMMARY ----------

    total = len(results)
    answered = len([r for r in results if r["confidence"] > 0])
    not_found = total - answered

    coverage = (answered / total) * 100 if total > 0 else 0

    st.subheader("📊 Coverage Summary")

    c1, c2, c3 = st.columns(3)

    c1.metric("Total Questions", total)
    c2.metric("Answered", answered)
    c3.metric("Not Found", not_found)

    st.write(f"Coverage: {coverage:.1f}%")

    # ---------- EXPORT ----------

    file = export_answers(results)

    st.download_button(
        "Export Answers",
        file,
        file_name="answered_questionnaire.xlsx"
    )