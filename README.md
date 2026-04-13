Author
Langelihle — [@LangelihleIT](https://github.com/LangelihleIT)
BetAnalytics — Personal Betting Data Processor
A data processor that takes in raw transaction data and makes it meaningful.
Why It Exists
Most betting platforms give you a transaction history but no real insight.
Numbers without context are just noise. This project turns that noise into
honest, actionable analysis, including the uncomfortable parts.
Key Questions It Answers
- What is my true betting P&L excluding deposits?
- What hour and day of the week do I lose the most?
- How many times have I chased losses?
- What is my maximum drawdown from peak bankroll?
- How often have I bet more than 20% of my available balance
What It Does: [Explained In 5 Phases]
Phase 1: Foundation
Parses raw semicolon-delimited transaction data, classifies each entry
(Wager, Deposit, Payout), and computes running totals.

Phase 2: Analysis Layer
Loads data into a pandas -> DataFrame, handles DateTime conversion,
sorts chronologically, computes cumulative bankroll and plots it over time.

Phase 3 : Truth Metrics
Separates betting performance from cash deposits. Answers the question:
"If I stopped depositing today, would I still be alive?"



Phase 4: Storage
Writes structured data to a SQLite database. Enables persistent storage
and advanced SQL queries against transaction history.
Phase 5: Behavioural Insights
Identifies loss patterns by hour and day, detects chasing behaviour,
calculates maximum drawdown, flags overbetting instances, and renders
a four-panel dashboard visualisation.
Tech Stack
- Python 3.12
- pandas
- matplotlib
- sqlite3 (built-in)
- os (built-in)
INSTRUCTIONS
1. Clone the repository
2. Install dependencies
3. REPLACE THE DATA IN “info =…”, with your own and ensure this sequence:
info = """YOUR csv data"""and then Paste your exported transaction data into the `info` variable. 

   in `DATA CLEANER.py`
4. Run the file.
Sample Output >>>
Total Deposited Amount: 465.0
 Total Wagered Amount: 1079.0 
Total Amount Won: 614.25
 Net Profit: 0.25
Betting P&L (DEPOSITS EXCLUDED): R-464.75 
Deposit Reliance: R465.0 
Verdict: Without Cash Injections, TOTAL LOSSES = R464.75
Chasing instances detected: 6 
Maximum Drawdown: R536.09
 Overbetting instances (>20% of bankroll): 4

