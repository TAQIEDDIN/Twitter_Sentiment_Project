# 🐦 Twitter Sentiment Analysis AI Dashboard
<img width="1877" height="862" alt="analiz" src="https://github.com/user-attachments/assets/43a9723f-38e1-4b35-a6b0-0e2b1c7565a0" />

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-05998b?style=for-the-badge&logo=fastapi)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.4-f7931e?style=for-the-badge&logo=scikitlearn)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-3.0-38B2AC?style=for-the-badge&logo=tailwind-css)

A high-performance, professional sentiment analysis web application. This project uses Machine Learning to classify tweets/text into **Positive** or **Negative** sentiments with a modern, responsive Glassmorphism UI.

---

## 🚀 Overview

This project moves away from standard data science notebooks into a **Production-Ready** environment. Instead of basic tools like Streamlit, it features a custom-built Backend using **FastAPI** and a premium Frontend designed with **Tailwind CSS**.

### Key Features:
- **Real-time Prediction**: Instant sentiment analysis using a pre-trained Logistic Regression model.
- **Advanced NLP Pipeline**: Custom text preprocessing including Stemming and Stopwords removal.
- **Modern UI/UX**: Dark mode Glassmorphism interface with Lucide icons and smooth animations.
- **Production Architecture**: Organized folder structure ready for deployment on platforms like Render or AWS.

---

## 🏗️ Project Structure

```text
Twitter_Sentiment_Project/
├── main.py              # FastAPI Backend & NLP Logic
├── requirements.txt     # Project Dependencies
├── .gitignore           # Files to be ignored by Git (venv, CSV, etc.)
├── model/               # Trained ML Models
│   ├── model.pkl        # Logistic Regression Model
│   └── vectorizer.pkl   # TF-IDF Vectorizer
├── templates/           # Frontend HTML Files
│   └── index.html       # Professional Dashboard UI
└── static/              # Static assets (CSS/JS/Images)



🧠 Machine Learning Details
The Dataset
The model was trained on the Sentiment140 dataset, which contains 1,600,000 tweets extracted using the Twitter API.

Preprocessing Pipeline:
Cleaning: Removal of special characters and numbers using RegEx.

Tokenization: Breaking down sentences into individual words.

Stopwords Removal: Filtering out common words (the, is, at, etc.) that don't carry sentiment.

Stemming: Reducing words to their root form using NLTK's PorterStemmer.

Vectorization: Converting text to numerical data using TF-IDF.

Model:
Algorithm: Logistic Regression.

Accuracy: Optimized for high-speed inference in web environments.

💻 Tech Stack
Backend: FastAPI (Python)

Frontend: HTML5, Tailwind CSS, JavaScript (Fetch API)

ML/NLP: Scikit-Learn, NLTK, Pickle, Pandas

Server: Uvicorn (ASGI)

🛠️ Installation & Setup
Clone the Repository

Bash
git clone [https://github.com/TAQIEDDIN/Twitter_Sentiment_Project.git](https://github.com/TAQIEDDIN/Twitter_Sentiment_Project.git)
cd Twitter_Sentiment_Project
Create Virtual Environment

Bash
python -m venv venv
# Activate it:
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
Install Dependencies

Bash
pip install -r requirements.txt
Run the Application

Bash
uvicorn main:app --reload
Open your browser at http://127.0.0.1:8000.

🧪 Example Tests
Try these sentences in the dashboard:

Positive: "I'm so excited about the future of Artificial Intelligence!"

Negative: "The service was extremely slow and the staff was rude."

Sarcastic: "Oh great, another bug to fix. Exactly what I wanted."

📝 License
Distributed under the MIT License. See LICENSE for more information.

Developed with ❤️ by TAQIEDDIN

