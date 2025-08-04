# 📊 Financial Chatbot using Streamlit

This project is a chatbot that allows users to query key financial data for major companies using natural language. It supports queries about:

- **Total Revenue**
- **Net Income**
- **Total Assets**
- **Total Liabilities**
- **Cash Flow from Operating Activities**
- **Year-over-Year Growth Percentages**

---

## 🏢 Supported Companies

- Apple  
- Microsoft  
- Tesla  

---

## ⚙️ Features

- 🧠 Intelligent chatbot interface built with **Streamlit**
- Parses natural language to extract financial intent
- Handles queries like:
  - "What is the total revenue of Apple last year?"
  - "How did Tesla's net income change?"
  - "Show the cash flow of Microsoft this year"

---

## 🗃️ Dataset Format

The chatbot uses a CSV file called `Key Financial Figures.csv` that contains annual financial data for Apple, Microsoft, and Tesla.

Each record includes:

| Fiscal Year | Company       | Total Revenue | Net Income | Total Assets | Total Liabilities | Cash Flow from Operating Activities |
|-------------|----------------|---------------|------------|--------------|--------------------|--------------------------------------|
| 2025        | Apple Inc.     | 281724        | 96250      | 352755       | 287491             | 110543                               |
| 2024        | Microsoft Corp | 232085        | 72720      | 303657       | 183007             | 87000                                |
| 2023        | Tesla Inc.     | 81462         | 12583      | 94973        | 41031              | 14000                                |

The following growth columns are calculated automatically:

- Revenue Growth From Last Year (%)
- Net Income Growth From Last Year (%)
- Assets Growth From Last Year (%)
- Liabilities Growth From Last Year (%)
- Cash Flow Growth From Last Year (%)

---

## 🧠 How the Chatbot Works

- ✅ Detects the company mentioned in the user query
- ✅ Checks for financial metric keywords (like "revenue", "net income", "assets")
- ✅ Identifies time-based context ("this year", "last year", or "change")
- ✅ Retrieves the relevant value from the dataset
- ✅ Responds with a natural language message

---

## 💻 Example Queries

Try asking:

1. What is the total revenue made by Apple?
2. What is the net income made by Tesla?
3. What is the total assets of Microsoft last year?
4. What is the cash flow of Apple in the previous year?
5. How has the total revenue changed over the last year?
6. How has the net income changed over the last year in Microsoft?
7. What is the revenue growth percentage of Apple last year?

---

## 🚀 Getting Started

### 1. Install Dependencies

Make sure you have Python 3 installed, then install the required packages:

pip install streamlit pandas

### 2. Run the Chatbot App

streamlit run chatbot_app.py

## ❗ Limitations

- Only supports Apple, Microsoft, and Tesla
- Only responds to simple queries about revenue, income, assets, liabilities, and cash flow
- No advanced NLP or fuzzy matching

## 📄 License

This project is for educational purposes only.

Made with ❤️ by Marwan