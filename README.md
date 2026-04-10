
🚀 Project Overview  
This project is an AI-powered chatbot built using Rasa Open Source + Python + SQLite + Pandas.  
It performs real-world business analytics such as sales tracking, revenue analysis, profit calculation, employee statistics, chart generation, and automated report exporting (CSV & Excel).

---

📂 Project Structure  
rasa-project/  
│  
├── actions/  
│   └── actions.py  
│  
├── database/  
│   └── db.py  
│  
├── data/  
│   ├── nlu.yml  
│   ├── stories.yml  
│   ├── rules.yml  
│  
├── charts/  
│   ├── bar_chart.png  
│   ├── pie_chart.png  
│  
├── reports/  
│   ├── sales_report.csv  
│   ├── sales_report.xlsx  
│  
├── config.yml  
├── domain.yml  
├── endpoints.yml  
├── credentials.yml  
├── app.py  

---

⚙️ How to Run Project  

pip install rasa==3.6.20 rasa-sdk pandas matplotlib openpyxl sqlite3  
python app.py  
python -m rasa train  
python -m rasa run actions  
python -m rasa shell  

---

📌 TASKS (52–89) EXPLANATION  

🗄️ 52. SQLite Database Connection  
Connect chatbot with SQLite for storing sales data.

📊 53. Create Sales Table  
Creates structured table for revenue, expense, employee, city, month.

➕ 54. Insert Sample Data  
Adds dummy sales records for testing analytics.

📥 55. Fetch All Rows  
Reads complete dataset from database.

💰 56. Total Revenue Query  
Calculates SUM(revenue) from database.

📉 57. Monthly Revenue Query  
Fetches revenue based on selected month.

👨‍💼 58. Employee Count by Department  
Groups employees department-wise using SQL.

🏙️ 59. Top City by Sales  
Finds highest revenue-generating city.

⚙️ 60. SQL in Python Action  
Runs SQLite queries inside Rasa custom actions.

👋 61. Greeting Rule  
Handles user greetings (hi/hello).

👋 62. Goodbye Rule  
Handles farewell messages.

📊 63. Profit Intent Story  
Returns revenue - expense calculation.

💸 64. Expense Intent Story  
Calculates total expenses.

👨‍💼 65. Employee Count Story  
Returns department-wise employee stats.

🔁 66. Multi-step Story (3 intents)  
Handles sequential user queries.

🔄 67. Retrain Model  
Retrains chatbot after updates in data.

🐞 68. Debug Mode Testing  
Runs chatbot with debug logs.

📈 69. Intent Confidence Check  
Analyzes prediction confidence.

🧠 70. Improve Low Confidence Intent  
Adds better training examples.

📚 71. Add 20 Training Phrases  
Improves dataset for sales intent.

✍️ 72. Spelling Mistake Handling  
Handles typos like "saless", "revenu".

⌨️ 73. Short Form Inputs  
Handles queries like "sales?"

📝 74. Long Sentence Inputs  
Handles full sentence queries.

🌐 75. Tamil-English Mixed Inputs  
Supports Hinglish / Tanglish chatbot inputs.

📊 76. Show Chart Intent  
Triggers visualization actions.

📊 77. Bar Chart Generation  
Creates city vs revenue bar chart.

🥧 78. Pie Chart Generation  
Creates revenue distribution chart.

💾 79. Save Chart Image  
Stores charts in project folder.

📁 80. Display Chart Path  
Returns saved image location to user.

📊 81. Pandas DataFrame Report  
Creates tabular report from SQL data.

🧾 82. Convert DataFrame to String  
Formats table output for chatbot.

📋 83. Formatted Table Response  
Displays structured chatbot response.

⬇️ 84. Download Report Intent  
Triggers file export action.

📤 85. Export Excel File  
Saves sales report as .xlsx file.

📤 86. Export CSV File  
Saves sales report as .csv file.

📁 87. Create Reports Folder  
Auto-creates folder for storing outputs.

💾 88. Save Reports Automatically  
Stores generated files inside reports/.

🧠 89. Final Integrated Chatbot System  
Combines SQLite + Rasa + Charts + Reports into a complete AI chatbot system.

---

🧠 Technologies Used  
Python  
Rasa Open Source  
SQLite Database  
Pandas  
Matplotlib  
OpenPyXL  

---

🎯 Features  
✔ AI Chatbot  
✔ SQL-based Analytics  
✔ Revenue & Profit Calculation  
✔ Employee Analysis  
✔ Chart Generation  
✔ Excel & CSV Export  
✔ Folder Automation  
✔ Debug Mode Support  

---

💡 Example Output  

User: total revenue  
Bot: 📊 Total Revenue: 310000  

User: profit  
Bot: 💰 Total Profit: 180000  

User: show chart  
Bot: 📈 Chart saved in charts folder  

User: download report  
Bot: 📁 Report saved in reports folder  

---

🔥 TASK 52–89 Rasa Chatbot Project
