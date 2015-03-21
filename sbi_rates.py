import sys
sys.path.append('.')
from period_duration import PeriodDuration
from duration_rate import DurationRate
from datetime import datetime

#https://www.sbi.co.in/portal/documents/36873/53953/1403695699641_RETAIL_TERM_DEPOSIT_INTEREST_RATES.pdf/3f68fe5f-8b81-4205-90bf-67a825a42556
rate_history = []
rate_history.append(PeriodDuration(start="14/2/2011", end="12/5/2011",
      duration_rate = [
        DurationRate(min=0, max=7, rate=0.0),
        DurationRate(min=7, max=15, rate=4.0),
        DurationRate(min=15, max=46, rate=5.0),
        DurationRate(min=46, max=91, rate=5.5),
        DurationRate(min=91, max=181, rate=6.0),
        DurationRate(min=181, max=366, rate=7.75),
        DurationRate(min=366, max=555, rate=8.25),
        DurationRate(min=555, max=556, rate=9.25)
      ]))

rate_history.append(PeriodDuration(start="12/5/2011", end="11/7/2011",
      duration_rate = [
        DurationRate(min=0, max=7, rate=0.0),
        DurationRate(min=7, max=15, rate=6.25),
        DurationRate(min=15, max=46, rate=6.25),
        DurationRate(min=46, max=91, rate=6.25),
        DurationRate(min=91, max=181, rate=7.0),
        DurationRate(min=181, max=366, rate=7.75),
        DurationRate(min=366, max=555, rate=8.25),
        DurationRate(min=555, max=556, rate=9.25)
      ]))

rate_history.append(PeriodDuration(start="11/7/2011", end="13/8/2011",
      duration_rate = [
        DurationRate(min=0, max=7, rate=0.0),
        DurationRate(min=7, max=91, rate=7.0),
        DurationRate(min=91, max=180, rate=7.25),
        DurationRate(min=180, max=241, rate=6.5),
        DurationRate(min=241, max=365, rate=7.75),
        DurationRate(min=365, max=556, rate=9.25)
      ]))

rate_history.append(PeriodDuration(start="13/8/2011", end="28/3/2012",
      duration_rate = [
        DurationRate(min=0, max=7, rate=0.0),
        DurationRate(min=7, max=91, rate=7.0),
        DurationRate(min=91, max=180, rate=7.25),
        DurationRate(min=180, max=241, rate=7.0),
        DurationRate(min=241, max=365, rate=7.75),
        DurationRate(min=365, max=556, rate=9.25)
      ]))

rate_history.append(PeriodDuration(start="28/3/2012", end="24/4/2012",
      duration_rate = [
        DurationRate(min=0, max=7, rate=0.0),
        DurationRate(min=7, max=91, rate=8.0),
        DurationRate(min=91, max=180, rate=8.0),
        DurationRate(min=180, max=181, rate=7.0),
        DurationRate(min=181, max=241, rate=8.0),
        DurationRate(min=241, max=365, rate=8.0),
        DurationRate(min=365, max=556, rate=9.25)
      ]))

rate_history.append(PeriodDuration(start="24/4/2012", end="08/6/2012",
      duration_rate = [
        DurationRate(min=0, max=7, rate=0.0),
        DurationRate(min=7, max=91, rate=7.25),
        DurationRate(min=91, max=180, rate=7.25),
        DurationRate(min=180, max=181, rate=7.25),
        DurationRate(min=181, max=241, rate=7.5),
        DurationRate(min=241, max=365, rate=7.5),
        DurationRate(min=365, max=556, rate=9.0)
      ]))

rate_history.append(PeriodDuration(start="8/6/2012", end="07/9/2012",
      duration_rate = [
        DurationRate(min=0, max=7, rate=0.0),
        DurationRate(min=7, max=91, rate=7.0),
        DurationRate(min=91, max=180, rate=7.0),
        DurationRate(min=180, max=181, rate=7.0),
        DurationRate(min=181, max=241, rate=7.25),
        DurationRate(min=241, max=365, rate=7.5),
        DurationRate(min=365, max=556, rate=9.0)
      ]))

rate_history.append(PeriodDuration(start="7/9/2012", end="01/3/2013",
      duration_rate = [
        DurationRate(min=0, max=7, rate=0.0),
        DurationRate(min=7, max=91, rate=6.5),
        DurationRate(min=91, max=180, rate=6.5),
        DurationRate(min=180, max=181, rate=6.5),
        DurationRate(min=181, max=241, rate=6.5),
        DurationRate(min=241, max=365, rate=6.5),
        DurationRate(min=365, max=556, rate=8.5)
      ]))

rate_history.append(PeriodDuration(start="1/3/2013", end="19/9/2013",
      duration_rate = [
        DurationRate(min=0, max=7, rate=0.0),
        DurationRate(min=7, max=91, rate=6.5),
        DurationRate(min=91, max=180, rate=6.5),
        DurationRate(min=180, max=181, rate=6.5),
        DurationRate(min=181, max=241, rate=6.5),
        DurationRate(min=241, max=365, rate=6.5),
        DurationRate(min=365, max=556, rate=8.75)
      ]))

rate_history.append(PeriodDuration(start="19/9/2013", end="20/9/2013",
      duration_rate = [
        DurationRate(min=0, max=7, rate=0.0),
        DurationRate(min=7, max=91, rate=7.5),
        DurationRate(min=91, max=180, rate=7.5),
        DurationRate(min=180, max=211, rate=6.5),
        DurationRate(min=211, max=365, rate=6.5),
        DurationRate(min=365, max=556, rate=9.0)
      ]))

rate_history.append(PeriodDuration(start="20/9/2013", end="1/11/2013",
      duration_rate = [
        DurationRate(min=0, max=7, rate=0.0),
        DurationRate(min=7, max=91, rate=7.5),
        DurationRate(min=91, max=180, rate=7.5),
        DurationRate(min=180, max=211, rate=6.8),
        DurationRate(min=211, max=365, rate=7.5),
        DurationRate(min=365, max=556, rate=9.0)
      ]))

rate_history.append(PeriodDuration(start="1/11/2013", end=datetime.now().date(),
      duration_rate = [
        DurationRate(min=0, max=7, rate=0.0),
        DurationRate(min=7, max=91, rate=7.5),
        DurationRate(min=91, max=180, rate=7.5),
        DurationRate(min=180, max=211, rate=7.0),
        DurationRate(min=211, max=365, rate=7.5),
        DurationRate(min=365, max=556, rate=9.0)
      ]))
