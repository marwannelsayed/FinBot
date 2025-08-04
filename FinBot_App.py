import streamlit as st
import pandas as pd

# Load and preprocess data
df = pd.read_csv('Key Financial Figures.csv')
df['Revenue Growth From Last Year (%)'] = df.groupby(['Company'])['Total Revenue'].pct_change() * 100
df['Net Income Growth From Last Year (%)'] = df.groupby(['Company'])['Net Income'].pct_change() * 100
df['Assets Growth From Last Year (%)'] = df.groupby(['Company'])['Total Assets'].pct_change() * 100
df['Liabilities Growth From Last Year (%)'] = df.groupby(['Company'])['Total Liabilities'].pct_change() * 100
df['Cash Flow Growth From Last Year (%)'] = df.groupby(['Company'])['Cash Flow from Operating Activities'].pct_change() * 100

# example of queries to use to ask the chatbot

# 1- What is the total revenue made by Apple?

# 2- What is the net income made by Tesla?

# 3- What is the total assets of Microsoft last year?

# 4- What is the cash flow of Apple in the previous year?

# 5- How has the total revenue changed over the last year? it wil ask you to specify the company

# 6- How has the net income changed over the last year in Microsoft?

# 7- What is the revenue growth percentage of Apple last year?

company_keywords = ['apple', 'microsoft', 'tesla']

def chatbot(query):
    matched_company = next((company for company in company_keywords if company in query.lower()), None)
    if not matched_company:
        return "Please specify a valid company (Apple, Microsoft, or Tesla)."

    company_name = matched_company.capitalize()
    company_df = df[df['Company'].str.contains(company_name, case=False, na=False)].sort_values('Fiscal Year', ascending=False)

    query = query.lower()

    if "total revenue" in query:
        if "change" in query or "growth" in query or "percentage" in query or "change" in query:
            growth = company_df['Revenue Growth From Last Year (%)'].iloc[-1]
            return f"The revenue growth percentage for {company_name} last year was {growth:.2f}%."
        elif "last year" in query or "previous year" in query:
            revenue = company_df['Total Revenue'].iloc[1]
            return f"The total revenue made by {company_name} last year was ${revenue:,}."
        else:
            revenue = company_df['Total Revenue'].iloc[0]
            return f"The total revenue made by {company_name} this year was ${revenue:,}."

    elif "net income" in query:
        if "change" in query or "growth" in query or "percentage" in query or "change" in query:
            growth = company_df['Net Income Growth From Last Year (%)'].iloc[-1]
            return f"The net income growth percentage for {company_name} last year was {growth:.2f}%."
        elif "last year" in query or "previous year" in query:
            income = company_df['Net Income'].iloc[1]
            return f"The net income made by {company_name} last year was ${income:,}."
        else:
            income = company_df['Net Income'].iloc[0]
            return f"The net income made by {company_name} this year was ${income:,}."
    elif "assets" in query:
        if "change" in query or "growth" in query or "percentage" in query:
            growth = company_df['Assets Growth From Last Year (%)'].iloc[-1]
            return f"The assets growth percentage for {company_name} last year was {growth:.2f}%."
        elif "last year" in query or "previous year" in query:
            assets = company_df['Total Assets'].iloc[1]
            return f"The total assets of {company_name} last year were ${assets:,}."
        else:
            assets = company_df['Total Assets'].iloc[0]
            return f"The total assets of {company_name} this year were ${assets:,}."
    elif "liabilities" in query:
        if "change" in query or "growth" in query or "percentage" in query:
            growth = company_df['Liabilities Growth From Last Year (%)'].iloc[-1]
            return f"The liabilities growth percentage for {company_name} last year was {growth:.2f}%."
        elif "last year" in query or "previous year" in query:
            liabilities = company_df['Total Liabilities'].iloc[1]
            return f"The total liabilities of {company_name} last year were ${liabilities:,}."
        else:
            liabilities = company_df['Total Liabilities'].iloc[0]
            return f"The total liabilities of {company_name} this year were ${liabilities:,}."
    elif "cash flow" in query:
        if "change" in query or "growth" in query or "percentage" in query:
            growth = company_df['Cash Flow Growth From Last Year (%)'].iloc[-1]
            return f"The cash flow growth percentage for {company_name} last year was {growth:.2f}%."
        elif "last year" in query or "previous year" in query:
            cash_flow = company_df['Cash Flow from Operating Activities'].iloc[1]
            return f"The cash flow from operating activities of {company_name} last year was ${cash_flow:,}."
        else:
            cash_flow = company_df['Cash Flow from Operating Activities'].iloc[0]
            return f"The cash flow from operating activities of {company_name} this year was ${cash_flow:,}."

    else:
        return "I'm sorry, I didn't understand your query."

# --- Streamlit UI ---
st.title("📊 Financial Chatbot")
st.write("Ask about financial figures for Apple, Microsoft, or Tesla.")

user_input = st.text_input("Enter your question:")

if user_input:
    response = chatbot(user_input)
    st.write("🤖", response)
