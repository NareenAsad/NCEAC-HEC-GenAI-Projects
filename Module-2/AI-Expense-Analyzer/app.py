import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from groq import Groq
from datetime import datetime

# Groq LLM Setup
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Streamlit Page Setup
st.set_page_config(page_title="AI Expense Analyzer", layout="wide")
st.title("AI Expense Analyzer (Groq + Streamlit)")

st.markdown(
    """
    This app lets you log your expenses, visualize spending patterns, and get **AI insights** powered by **Groq (LLaMA 3.3 70B)**.
    """
)

# Initialize Session State
if "expenses" not in st.session_state:
    st.session_state.expenses = pd.DataFrame(
        columns=["Date", "Category", "Amount", "Description"]
    )

# Expense Entry Form
st.header("Add a New Expense")

with st.form("expense_form"):
    col1, col2 = st.columns(2)
    with col1:
        date = st.date_input("Date", datetime.now())
        category = st.selectbox(
            "Category",
            [
                "Food",
                "Transport",
                "Entertainment",
                "Bills",
                "Shopping",
                "Health",
                "Other",
            ],
        )
    with col2:
        amount = st.number_input("Amount (in USD)", min_value=0.0, step=0.1)
        description = st.text_area("Description")

    submitted = st.form_submit_button("Add Expense")

if submitted:
    new_expense = pd.DataFrame(
        [[date, category, amount, description]],
        columns=["Date", "Category", "Amount", "Description"],
    )
    st.session_state.expenses = pd.concat(
        [st.session_state.expenses, new_expense], ignore_index=True
    )
    st.success("Expense added successfully!")

# Display Expenses Table
if not st.session_state.expenses.empty:
    st.header("Expense History")
    st.dataframe(st.session_state.expenses, use_container_width=True)

    # Visualization
    st.header("Expense Visualizations")

    total_by_category = (
        st.session_state.expenses.groupby("Category")["Amount"].sum().sort_values()
    )

    col1, col2 = st.columns(2)

    # Bar Chart
    with col1:
        st.subheader("Spending by Category")
        fig, ax = plt.subplots()
        total_by_category.plot(kind="bar", ax=ax)
        ax.set_ylabel("Amount ($)")
        st.pyplot(fig)

    # Pie Chart
    with col2:
        st.subheader("Expense Distribution")
        fig2, ax2 = plt.subplots()
        total_by_category.plot(kind="pie", ax=ax2, autopct="%1.1f%%")
        ax2.set_ylabel("")
        st.pyplot(fig2)

    # Trend Chart
    st.subheader("Spending Over Time")
    expenses_over_time = (
        st.session_state.expenses.groupby("Date")["Amount"].sum().reset_index()
    )
    fig3, ax3 = plt.subplots()
    ax3.plot(expenses_over_time["Date"], expenses_over_time["Amount"], marker="o")
    ax3.set_xlabel("Date")
    ax3.set_ylabel("Total Spending ($)")
    st.pyplot(fig3)

    # AI Insights (Groq LLM)
    st.header("AI Expense Insights")

    expense_summary = ""
    for _, row in st.session_state.expenses.iterrows():
        expense_summary += f"- {row['Date']}: ${row['Amount']} on {row['Category']} ({row['Description']})\n"

    prompt = f"""
    You are an AI financial assistant. Here is my recent expense history:
    {expense_summary}

    Analyze the spending trends and provide:
    1. Key spending insights (where I spend the most)
    2. Times I spent unusually high amounts
    3. Suggestions to better manage or optimize expenses
    4. General financial health summary
    """

    if st.button("Generate AI Insights"):
        with st.spinner("Analyzing your spending with Groq AI..."):
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile",
            )
            ai_response = chat_completion.choices[0].message.content

        st.markdown("### Groq AI Recommendations:")
        st.write(ai_response)

else:
    st.info("Please add some expenses to get started.")
