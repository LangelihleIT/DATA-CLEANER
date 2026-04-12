#WRITE A FUNCTION THAT TAKES IN ROUGH AND UNORGANIZED DATA, THEN IT 
# SORTS IT ACCORDINGLY BY IT RUNNING THE DATA THROUGH VARIOUS FUNCTIONS.



info = """Date;Type;Amount;Transaction ID
2026-04-10T10:08:05.04+02:00;Wager;-40;663471562
2026-04-09T22:03:36.463+02:00;Wager;-33;662758595
2026-04-09T21:58:30.653+02:00;Early Cashout Payout;73.23;661327497
2026-04-09T15:10:08.51+02:00;Wager;-49;661327497
2026-04-09T14:44:45.133+02:00;Blu Voucher Deposit;49;Blu Voucher Deposit
2026-04-08T19:17:40.4+02:00;Wager;-95;659410257
2026-04-08T19:15:14.967+02:00;Blu Voucher Deposit;95;Blu Voucher Deposit
2026-04-07T09:50:50.53+02:00;Wager;-58;654476242
2026-04-07T09:50:11.533+02:00;OTT Voucher Deposit;58;OTT Voucher Deposit
2026-04-06T14:17:25.81+02:00;Wager;-3;652399308
2026-04-06T14:17:02.45+02:00;Wager;-45;652397709
2026-04-06T14:16:05.3+02:00;OTT Voucher Deposit;48;OTT Voucher Deposit
2026-04-05T08:48:34.543+02:00;Wager;-21;648281706
2026-04-04T22:49:02.907+02:00;Rewards Cash Award;4.91;8481caea-979a-4d87-67f8-08de28375189
2026-04-04T20:33:07.583+02:00;Wager;-200;647472408
2026-04-04T20:30:09.27+02:00;OTT Voucher Deposit;200;OTT Voucher Deposit
2026-04-04T18:30:42.207+02:00;Wager;-300;647009638
2026-04-04T05:40:59.497+02:00;Wager;-20;644025173
2026-04-04T05:36:05.82+02:00;Wager;-200;644022086
2026-04-03T23:38:23.883+02:00;Payout;454.94;641739786
2026-04-03T23:38:23.877+02:00;Win Boost Cash Payout;6.71;641739786
2026-04-03T18:33:13.473+02:00;Payout;71.6;641851791
2026-04-03T18:33:13.47+02:00;Win Boost Cash Payout;2.86;641851791
2026-04-03T12:46:48.02+02:00;Wager;-15;641851791
2026-04-03T12:29:31.803+02:00;Blu Voucher Deposit;15;Blu Voucher Deposit"""


import pandas as pd
import matplotlib.pyplot as plt
import sqlite3 
import os 
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def parse_to_list(info: str) -> list:
    return [line.strip() for line in info.strip().splitlines() if line.strip()]

info = parse_to_list(info)
info = info[1:]  # skip the header row

deposits = 0
wagers = 0
wins = 0

deposits_sum = 0
wagers_sum = 0
wins_sum = 0


def cleaning(transaction, deposits, deposits_sum, wagers, wagers_sum, wins, wins_sum):
    segments = transaction.split(";")

    date = segments[0]
    date = date.replace("T", " ").replace("+02:00", "")
    print("Date & Time:", date)

    action = segments[1]
    print("Bet Type:", action)

    amount = segments[2]
    signed_amount = float(amount) # keep the sign intact

    #RECORD --> PANDAS
    record = {
    "date": date,
    "type": action,
    "amount": signed_amount
    }

    if action == "Rewards Cash Award" or action == "Win Boost Cash Payout" or "Payout" in action:
        print("Amount Won:", amount)
        wins_sum += float(amount)
        wins += 1
    elif "-" in str(amount):
        clean_amount = amount.replace("-", "")
        print(f"YOU LOST: {clean_amount}")
        wagers += 1
        wagers_sum += float(clean_amount)
    else:
        print("Amount Deposited:", amount)
        deposits += 1
        deposits_sum += float(amount)

    code = segments[3]
    print("Bet Code:", code)

    return record, deposits, deposits_sum, wagers, wagers_sum, wins, wins_sum  # <-- this was missing
    

def info_len(info, deposits, deposits_sum, wagers, wagers_sum, wins, wins_sum):
    info_len = len(info)
    print("Number of Transaction Entries: ",info_len)
    print("<---------------TRANSACTION SUMMARIES----------->")
    transaction = []
    records = []
    for i in range(info_len):
        transaction = info[i]
        print(f"<<<<<<<TRANSACTION INFO {i+1}>>>>>>>>")
        record, deposits, deposits_sum, wagers, wagers_sum,  wins, wins_sum = cleaning(transaction, deposits, deposits_sum, wagers, wagers_sum, wins, wins_sum)
        records.append(record)
    
    net_profit = round(wins_sum + deposits_sum - wagers_sum, 2)
    
    

    print(f"\nDeposits: {deposits} | Wagers: {wagers} | Wins: {wins}")
    print(f"\nTotal Deposited Amount: {round(deposits_sum,2)} | Total Wagered Amount: {round(wagers_sum,2)} | Total Amount Won: {round(wins_sum,2)}")
    print(f"Net Profit: {net_profit}")
    
    betting_pnl = round(wins_sum - wagers_sum, 2)
    print(f"\nBetting P&L (DEPOSITS EXCLUDED): R{betting_pnl}")
    print(f"Deposit Reliance: R{round(deposits_sum,2)}")
    
    if betting_pnl >= 0:
        print("Verdict: GOOD NEWS!")
        print("You are Profitable")
    else:
        print(f"Verdict: Without Cash Injections, TOTAL LOSSES = R{abs(betting_pnl)}")
        
    #SQL CODE
    df = pd.DataFrame(records)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date").reset_index(drop=True)
    conn = sqlite3.connect("transactions.db")
    df.to_sql("transactions", conn, if_exists="replace", index=False)
    print("Database Connection: Succesful. Data Writtent to -> transactions.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions LIMIT 2")
    rows = cursor.fetchall()
    print("\n<--- DATABASE VERIFICATION --->")
    for row in rows:
        print(row)
        
    conn.close()
    
    df["bankroll"] = df["amount"].cumsum()
    df["hour"] = df["date"].dt.hour
    df["day"] = df["date"].dt.day_name
    df["month"] = df["date"].dt.month
    
    wager_df = df[df["type"] == "Wager"].copy()
    
    print("\n<--- LOSSES BY HOUR --->")
    print(wager_df.groupby("hour")["amount"].sum().sort_values())

    print("\n<--- LOSSES BY DAY --->")
    print(wager_df.groupby("day")["amount"].sum().sort_values())
    print(df)
    
    betting_df = df[(df["type"] != "OTT Voucher Deposit") & (df["type"] != "Blu Voucher Deposit")].copy()
    betting_df["betting_pnl"] = betting_df["amount"].cumsum()
    
    print(betting_df)
    
    #Plotting & Visualisation 
    plt.figure(figsize=(12,5))
    plt.plot(df["date"], df["bankroll"], color="green", linewidth=1.5, label="Account Balance")
    plt.plot(betting_df["date"], betting_df["betting_pnl"], color="red", linewidth=1.5, label="Betting P&L (Deposits Excluded)")
    plt.axhline(y=0, color="grey", linestyle="--", linewidth=1)
    plt.title("Bankroll Over Time")
    plt.xlabel("Date --> Time")
    plt.ylabel("Balance (R) --> Bankroll")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    
def query(sql):
    conn = sqlite3.connect("transactions.db")
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    return rows

# these live outside the function, at the bottom of the file
info_len(info, deposits, deposits_sum, wagers, wagers_sum, wins, wins_sum)

print("\n<--- WAGERS --->")
print(query("SELECT * FROM transactions WHERE type = 'Wager'"))

print("\n<--- TOTAL WAGERED --->")
print(query("SELECT SUM(amount) FROM transactions WHERE amount < 0"))

print("\n<--- BIGGEST SINGLE LOSS --->")
print(query("SELECT MIN(amount) FROM transactions"))
