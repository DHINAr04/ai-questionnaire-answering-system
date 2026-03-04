# 🤖 AI Questionnaire Answering System

An AI-powered tool that automatically answers structured questionnaires using internal reference documents.

This project demonstrates how **Retrieval-Augmented Generation (RAG)** can be used to extract grounded answers from enterprise documentation while providing **evidence snippets, citations, and confidence scores**.

---

# 🚀 Live Demo

Live Application
https://shareappio-m2rafsteasu6fcapu7dzjb.streamlit.app/

GitHub Repository
https://github.com/DHINAr04/ai-questionnaire-answering-system

---

# 🔑 Demo Login Credentials

Email: [admin@company.com](mailto:admin@company.com)
Password: admin123

---

# 🏢 Industry

Cloud SaaS Infrastructure

---

# 🏢 Fictional Company

**TechNova Cloud Solutions**

TechNova Cloud Solutions is a fictional SaaS infrastructure provider that offers scalable cloud hosting, data security, and compliance solutions for enterprise applications. The platform helps organizations deploy, monitor, and secure cloud workloads while maintaining high availability and industry compliance standards.

---

# 📌 Problem

Organizations frequently receive structured questionnaires such as:

* Security assessments
* Vendor risk questionnaires
* Compliance forms
* Operational audits

These questionnaires must be answered using internal documentation, which is usually a **manual and time-consuming process**.

This system automates that workflow using AI.

---

# ⚙️ System Workflow

1. User logs into the system
2. User uploads internal reference documents (PDF)
3. User pastes questionnaire questions
4. System retrieves relevant content using semantic search
5. AI extracts the most relevant answers from the documents
6. Each answer includes:

* Evidence snippet
* Citation
* Confidence score

7. User reviews or edits answers
8. Completed questionnaire can be exported

---

# 🧠 AI Architecture (RAG Pipeline)

The system uses a **Retrieval-Augmented Generation (RAG)** approach.

Steps:

1. Reference documents are loaded and converted into text
2. Text is split into smaller chunks
3. Sentence embeddings are generated using **Sentence Transformers**
4. Embeddings are stored in a **Chroma vector database**
5. When a question is asked:

* The question is converted to an embedding
* Vector similarity search retrieves relevant document chunks

6. The system extracts the most relevant sentence as the answer.

This ensures answers are **grounded in reference documents**.

---

# ✨ Features

## Core Features

* User authentication
* Upload questionnaire
* Upload reference documents
* AI-generated answers
* Grounded citations from documents

## Nice-to-Have Features Implemented

* Confidence score for each answer
* Evidence snippets from documents
* Coverage summary dashboard

---

# 📊 Coverage Summary Example

Total Questions: 8
Answered: 8
Not Found: 0
Coverage: 100%

---

# 📄 Example Output

Question
Where is customer data stored?

Answer
Customer data is stored in managed AWS services including Amazon RDS and Amazon S3.

Citation
infrastructure_overview.pdf

Confidence
82%

---

# 📁 Reference Documents

The system uses fictional internal documents as the **source of truth**.

infrastructure_overview.pdf
security_policy.pdf
compliance_standards.pdf

These documents include:

* cloud infrastructure architecture
* security policies
* encryption standards
* monitoring practices
* compliance certifications
* disaster recovery processes

---

# 🧾 Example Questionnaire

Where is customer data stored?
How is system availability ensured?
What framework does the company follow for information security?
How is data encrypted?
What backup strategy does the company use?
Does the company support multi-factor authentication?
How does the company monitor system security?
What compliance standards does the company follow?

---

# ⚖️ Assumptions

* Uploaded documents are considered the **source of truth**
* Answers must be grounded in the uploaded documents
* If no relevant information is found, the system returns:

Not found in references.

---

# ⚠️ Trade-offs

To keep the project lightweight and reproducible:

* Sentence-transformer embeddings are used instead of large LLMs
* Answers are extracted from evidence rather than fully generated
* ChromaDB is used as a local vector database

These choices make the system **fast, simple, and easy to deploy**.

---

# 🔮 Future Improvements

With more time the system could include:

* LLM-based answer synthesis
* retrieval re-ranking
* smarter document chunking
* partial answer regeneration
* version history for questionnaire runs
* improved UI dashboard
* cloud vector database

---

# 🛠 Tech Stack

Python
Streamlit
Sentence Transformers
ChromaDB
LangChain
Pandas

---

# ▶️ Run Locally

Install dependencies

pip install -r requirements.txt

Run the application

streamlit run app.py

---

# 📌 Assignment Context

This project was built as part of the **GTM Engineering Internship Assignment for Almabase**.

The goal was to build a practical AI system that automates answering structured questionnaires using internal documentation.

---

# 👨‍💻 Author

Dhinagaran M
