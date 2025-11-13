# To-Do List & Habit Tracker App

A simple and interactive **To-Do List & Habit Tracker** built with **Streamlit**, designed for both **Google Colab testing** and **Hugging Face Spaces deployment**.  
This app helps you stay productive by managing daily tasks and tracking habits with progress charts — all in one clean interface.

---

## 🌐 Live Demo

🚀 **Try it now on Hugging Face Spaces:**  
👉 [To-Do List & Habit Tracker App – Hugging Face Demo](https://huggingface.co/spaces/nareen99/To-DoList-Habit-Tracker)

---

## 🧠 Features

### To-Do List
- Add new tasks with titles and optional descriptions  
- Mark tasks as complete/incomplete  
- Delete tasks easily  
- View total and completed tasks  
- Data saved locally in JSON for persistence  

### Habit Tracker
- Add daily habits (e.g., Drink Water, Exercise)  
- Mark completion for today  
- Track ongoing streaks automatically  
- View streak progress via a bar chart  

### Extra
- Works fully offline (JSON-based storage)  
- Streamlit-powered responsive interface  
- Ready for Colab testing and Hugging Face deployment  

---

## ⚙️ Installation (Google Colab)

You can test and run the app directly in **Google Colab** before deployment.

### 1️⃣ Install Dependencies
```bash
!pip install streamlit streamlit-option-menu matplotlib pandas
````

### 2️⃣ Upload `app.py`

Upload your `app.py` file in Colab’s file explorer.

### 3️⃣ Run Streamlit App

```bash
!streamlit run app.py --server.port 6006 & npx localtunnel --port 6006
```

After a few seconds, you’ll get a public **URL** (from LocalTunnel).
Click it to open the Streamlit app in your browser.

---

## 🚀 Deployment on Hugging Face Spaces

1. Go to **[Hugging Face Spaces](https://huggingface.co/spaces)**
2. Click **“Create new Space”**
3. Choose:

   * **SDK:** Streamlit
   * **Visibility:** Public (or Private)
4. Upload the following files:

   * `app.py`
   * `requirements.txt`
5. Click **“Commit changes”**
6. Wait for the build to finish — your app will be live shortly!

---

## 📦 Requirements

Add this to your `requirements.txt` file:

```
streamlit
streamlit-option-menu
matplotlib
pandas
```

---

## 🧩 Project Structure

```
├── app.py
├── requirements.txt
└── README.md
```

---

## 🧠 How It Works

* The app uses **JSON files** (`todos.json` and `habits.json`) to store user data.
* You can add, complete, or delete tasks and habits anytime — the data persists locally.
* The habit tracker automatically counts streaks based on daily completions.
* A bar chart visualizes your progress using Matplotlib and Pandas.

---

## 🪄 Example Usage

1. Navigate to the **To-Do List** tab → Add and check off daily tasks.
2. Switch to the **Habit Tracker** tab → Add habits and mark them “Done Today.”
3. View your streak chart to stay motivated!

---

## 🧰 Tech Stack

| Tool                    | Purpose                 |
| ----------------------- | ----------------------- |
| **Python**              | Core logic              |
| **Streamlit**           | Front-end UI            |
| **Matplotlib / Pandas** | Habit tracking charts   |
| **JSON**                | Local data persistence  |
| **Hugging Face Spaces** | App deployment platform |

---

## 🖌️ Acknowledgements

* Built using [Streamlit](https://streamlit.io/)
* Deployed on [Hugging Face Spaces](https://huggingface.co/spaces)
* Inspired by minimal productivity tools and notebook-style UIs
