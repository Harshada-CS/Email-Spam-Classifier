# 📧 Email Spam Classifier using Machine Learning

## 📌 Project Overview

This project is a Machine Learning-based web application that classifies emails/messages as **Spam** or **Not Spam (Ham)**. It uses Natural Language Processing (NLP) techniques to analyze text and make predictions.

---

## 🚀 Features

* Detect spam messages instantly 🚨
* User-friendly interface using Streamlit 🎨
* Displays spam probability
* Shows model accuracy 📊
* Confusion matrix visualization

---

## 🧠 Machine Learning Model

This project uses:

* **TF-IDF Vectorization** → Converts text into numerical features
* **Multinomial Naive Bayes** → Classification algorithm

### Why Naive Bayes?

* Works well for text data
* Fast and efficient
* High accuracy for spam detection

---

## 📊 Dataset

The dataset contains:

| Column  | Description       |
| ------- | ----------------- |
| label   | spam / ham        |
| message | Email or SMS text |

---

## 🛠️ Technologies Used

* Python 🐍
* Streamlit 🌐
* Pandas 📊
* Scikit-learn 🤖
* Matplotlib 📈

---

## 📂 Project Structure

```
EmailSpamClassifier/
 ├── app.py
 ├── spam.csv
 ├── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/your-username/email-spam-classifier.git
```

2. Navigate to project folder:

```
cd email-spam-classifier
```

3. Install dependencies:

```
pip install pandas scikit-learn streamlit matplotlib
```

---

## ▶️ Run the Project

```
python -m streamlit run app.py
```

---

## 📈 Output

* Predicts whether a message is spam or not
* Displays spam probability
* Shows confusion matrix

---

## 💡 Future Improvements

* Use deep learning models (LSTM, BERT)
* Add email integration
* Deploy on cloud 🌐

---

## 👩‍💻 Author

Harshada Shinde

---

## ⭐ Acknowledgement

This project is built for learning Machine Learning and NLP concepts and applying them to real-world problems.
