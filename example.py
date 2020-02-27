import argparse
import sys
sys.path.append('.')
from deposit import Deposit
from datetime import datetime, date
from sbi_rates import rate_history

deposits = []

deposits.append(Deposit(id="715", principal=391889.0, interval=4,
      rate=7.10, started="24/11/2018", duration=2))
deposits.append(Deposit(id="701", principal=914338.0, interval=4,
      rate=7.10, started="22/11/2018", duration=2))
deposits.append(Deposit(id="699", principal=979611.0, interval=4,
      rate=7.1, started="21/11/2018", duration=2))
deposits.append(Deposit(id="692", principal=653049.0, interval=4,
      rate=7.1, started="20/11/2018", duration=2))

#Year to get tax statement for
argparser = argparse.ArgumentParser()
argparser.add_argument("--year", default=(datetime.now().timetuple()[0] - 1), type=int)
args = argparser.parse_args()

# Renew any deposits if required
all_deposits = deposits[:]
for deposit in deposits:
  Deposit.renew_deposit(deposit=deposit, period_duration_lookup=rate_history, collector=all_deposits)

all_deposits.sort()

tax_sdate = date(args.year,1,1)
tax_edate = date(args.year,12,31)
for deposit in all_deposits:
   deposit_tax_statement = deposit.tax_statement(tax_sdate, tax_edate)
   if deposit_tax_statement is not None:
    print("{0}\t{1}".format(deposit, deposit_tax_statement))
