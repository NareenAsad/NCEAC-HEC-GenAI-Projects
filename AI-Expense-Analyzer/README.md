# 💸 AI Expense Analyzer (Groq + Streamlit)

An **AI-powered Expense Analyzer** built using **Streamlit**, **Groq LLM (LLaMA 3.3 70B)**, and **Matplotlib**.  
This app allows users to enter expenses with descriptions, visualize their spending habits through charts, and get **personalized AI insights** on how to manage money better.

---

## 🌐 Live Demo

🚀 **Try it now on Hugging Face Spaces:**  
👉 [AI Expense Analyzer – Hugging Face Demo](https://huggingface.co/spaces/nareenasad/ai-expense-analyzer)

---

## 🧠 Features

* Add and manage daily expenses (date, category, amount, and description)  
* Visualize spending patterns with bar and pie charts  
* Analyze expense trends over time  
* Get AI-generated financial insights powered by **Groq LLaMA 3.3 70B**  
* Simple and interactive UI built with **Streamlit**  
* Ready to run locally, on **Google Colab**, or on **Hugging Face Spaces**

---

## 🛠️ Tech Stack

- **Frontend/UI**: [Streamlit](https://streamlit.io/)
- **AI Engine**: [Groq API](https://groq.com/)
- **Language Model**: LLaMA 3.3 70B Versatile
- **Data Visualization**: Matplotlib
- **Data Handling**: Pandas

---

## 📦 Project Structure

```

├── app.py              # Main Streamlit application
├── requirements.txt    # Required dependencies
└── README.md           # Project documentation

````

---

## ⚙️ Installation (Local Setup)

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-expense-analyzer.git
cd ai-expense-analyzer
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Groq API Key

Create a `.env` file in your project root and add:

```
GROQ_API_KEY=your_api_key_here
```

Or export it in your terminal:

```bash
export GROQ_API_KEY="your_api_key_here"
```

### 4. Run the Application

```bash
streamlit run app.py
```

Visit `http://localhost:8501` in your browser 🎉

---

## 🚀 Running on Google Colab

If you prefer to test it on **Google Colab**, follow these steps:

### 1. Install Dependencies

```python
!pip install streamlit pandas matplotlib groq python-dotenv
```

### 2. Create `app.py`

```python
%%writefile app.py
# Paste full app.py code here
```

### 3. Set Your API Key

```python
import os
os.environ["GROQ_API_KEY"] = "your_api_key_here"
```

### 4. Run Streamlit App via LocalTunnel

```python
!wget -q -O - ipv4.icanhazip.com
!streamlit run app.py & npx localtunnel --port 8501
```

After a few seconds, Colab will print a **public URL** like:

```
your-url.loca.lt
```

Click it to open the Streamlit app in your browser.

---

## 🧾 Example Use

1. Enter your expenses:

   * Date: `2025-11-03`
   * Category: `Food`
   * Amount: `15.50`
   * Description: `Lunch with colleagues`

2. View automatic visualizations:

   * Bar chart of category-wise spending
   * Pie chart of total expense distribution
   * Line chart showing spending over time

3. Click **“🔍 Generate AI Insights”**

   * The app will summarize your spending and generate smart financial advice using **Groq LLM**.

---

## 🧮 Sample Output

**AI Insights Example:**

> You tend to spend most of your budget on Food and Entertainment.
> Your expenses spike on weekends.
> Consider setting a weekly limit for discretionary spending and moving recurring bills to one day for better control.

---

## 🧰 Requirements

```
streamlit
pandas
matplotlib
groq
python-dotenv
```

---

## 📈 Future Enhancements

* Persistent storage (CSV or database)
* Monthly summaries and budgeting goals
* Income tracking and savings analysis
* PDF/Excel export of expense reports
* Authentication for multiple users

---

## ❤️ Credits

Developed by **Nareen Asad**
Powered by **Groq LLaMA 3.3 70B** and **Streamlit**