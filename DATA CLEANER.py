#WRITE A FUNCTION THAT TAKES IN ROUGH AND UNORGANIZED DATA, THEN IT 
# SORTS IT ACCORDINGLY BY IT RUNNING THE DATA THROUGH VARIOUS FUNCTIONS.


info = """2026-04-05T08:48:34.543+02:00;Wager;-21;648281706
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
2026-04-03T12:29:31.803+02:00;Blu Voucher Deposit;15;Blu Voucher Deposit
2026-04-03T12:14:07.617+02:00;Wager;-200;641739786
2026-04-03T12:06:31.657+02:00;OTT Voucher Deposit;200;OTT Voucher Deposit
2026-04-02T21:22:45.02+02:00;Wager;-10;640452816
2026-04-02T21:22:14.03+02:00;OTT Voucher Deposit;10;OTT Voucher Deposit
2026-04-02T12:01:11.937+02:00;Wager;-50;639087455
2026-04-02T01:09:32.78+02:00;OTT Voucher Deposit;50;OTT Voucher Deposit
2026-04-01T18:56:27.873+02:00;Wager;-53;637723922
2026-04-01T18:47:36.1+02:00;OTT Voucher Deposit;50;OTT Voucher Deposit
2026-04-01T01:04:59.523+02:00;Wager;-60;636143362
2026-04-01T01:01:46.353+02:00;Wager;-100;636141684
2026-03-31T22:03:16.623+02:00;Wager;-50;635914713
2026-03-31T19:55:10.083+02:00;Wager;-100;635443379
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
2026-04-03T12:29:31.803+02:00;Blu Voucher Deposit;15;Blu Voucher Deposit
2026-04-03T12:14:07.617+02:00;Wager;-200;641739786
2026-04-03T12:06:31.657+02:00;OTT Voucher Deposit;200;OTT Voucher Deposit
2026-04-02T21:22:45.02+02:00;Wager;-10;640452816
2026-04-02T21:22:14.03+02:00;OTT Voucher Deposit;10;OTT Voucher Deposit
2026-04-02T12:01:11.937+02:00;Wager;-50;639087455
2026-04-02T01:09:32.78+02:00;OTT Voucher Deposit;50;OTT Voucher Deposit
2026-04-01T18:56:27.873+02:00;Wager;-53;637723922
2026-04-01T18:47:36.1+02:00;OTT Voucher Deposit;50;OTT Voucher Deposit
2026-04-01T01:04:59.523+02:00;Wager;-60;636143362
2026-04-01T01:01:46.353+02:00;Wager;-100;636141684
2026-03-31T22:03:16.623+02:00;Wager;-50;635914713
2026-03-31T19:55:10.083+02:00;Wager;-100;635443379
2026-03-31T12:39:55.4+02:00;Wager;-10;633840369
2026-03-31T12:33:34.09+02:00;Wager;-10;633823117
2026-03-31T12:29:02.903+02:00;Wager;-10;633810447
2026-03-31T12:20:52.847+02:00;Wager;-100;633788127
2026-03-30T22:45:49.92+02:00;Payout;133;631399394
2026-03-30T11:08:46.697+02:00;Wager;-50;631399394
2026-03-29T23:04:58.077+02:00;Payout;214.02;630518556
2026-03-29T23:04:58.073+02:00;Win Boost Cash Payout;4.28;630518556
2026-03-29T20:38:08.3+02:00;Wager;-100;630518556
2026-03-29T18:14:58.093+02:00;Payout;135;629814917
2026-03-29T17:31:52.683+02:00;Wager;-45;630021789
2026-03-29T16:18:56.143+02:00;Wager;-45;629814917
2026-03-29T14:37:26.597+02:00;Payout;49.3;629406019
2026-03-29T14:02:29.553+02:00;Wager;-29;629406019
2026-03-29T14:01:40.793+02:00;Wager;-25;629403307
2026-03-29T10:56:47.867+02:00;Wager;-75;628828917
2026-03-28T22:46:28.637+02:00;Payout;270.81;627776589
2026-03-28T22:46:28.633+02:00;Win Boost Cash Payout;5.42;627776589"""

import pandas as pd
df = pd.DataFrame(records)
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
    date = date.replace("T", " @ ").replace("+02:00", "")
    print("Date & Time:", date)

    action = segments[1]
    print("Bet Type:", action)

    amount = segments[2]
    signed_amount = float(amount) # keep the sign intact

    record = {
    "date": date,
    "type": action,
    "amount": signed_amount
    }

    if action == "Rewards Cash Award" or action == "Win Boost Cash Payout" or action == "Payout":
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

    print(f"\nDeposits: {deposits} | Wagers: {wagers} | Wins: {wins}")
    print(f"\nTotal Deposited Amount: {round(deposits_sum,2)} | Total Wagered Amount: {round(wagers_sum,2)} | Total Amount Won: {round(wins_sum,2)}")
        
        #print(info[i])
        
info_len(info, deposits, deposits_sum, wagers, wagers_sum, wins, wins_sum)




    

    


