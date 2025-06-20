# 📱 SMS Spam Detection Web App (Streamlit + Machine Learning)

This is a simple and interactive **SMS Spam Detection System** built using **Machine Learning models**. The app predicts whether a given SMS message is **SPAM or HAM (Not Spam)** based on its text content.

## 📌 Features

- Built using **Multinomial Naive Bayes** models.
- Text preprocessing with **TF-IDF Vectorizer**.
- Interactive **Streamlit-based frontend**.
- Predicts in real-time whether the SMS is **Spam or Not Spam**.
- Clean and user-friendly UI.

## 🛠️ Tech Stack

| Area             | Tools & Libraries                            |
|------------------|----------------------------------------------|
| **Frontend**     | Streamlit                                    |
| **Backend/ML**   | Scikit-learn, Pandas                         |

## 📂 Project Structure

├── app.py # Streamlit web app  
├── SMS_Spam_Detection_Model.ipynb # Model building Jupyter notebook  
├── spam_model.pkl # Trained model (TF-IDF + classifier)  
├── requirements.txt # Python dependencies  
└── README.md # Project description  

## ⚙️ Installation (For Local Run)

1. Clone the repository:
`
git clone https://github.com/Soumodeep084/SMS-Spam-Detection-System-ML.git
cd fake-news-app-ml-project
`


2. Create a virtual environment (recommended):  
`python -m venv venv`  
`source venv/bin/activate # For Linux/Mac`  
`venv\Scripts\activate # For Windows`


3. Install the required libraries:
`pip install -r requirements.txt`


4. Run the Streamlit app:
`streamlit run app.py`


## 📝 Model Details
1. Text Representation: TF-IDF Vectorizer with N-grams (1,2)
2. Features Used: TF-IDF word features
3. Classifier Used: Multinomial Naive Bayes


## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License
This project is licensed under the MIT License.
