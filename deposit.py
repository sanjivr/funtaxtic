#!/usr/bin/python
from datetime import datetime, date, timedelta
import calendar
from pprint import pprint

class PeriodDuration(object):
  def __init__(self, **kwargs):
    self.duration_rate = []
    for key, value in kwargs.items():
      if hasattr(self, key):
          setattr(self, key, value)
      else:
          raise Exception("Unknown property [" + key +"]")

  @property
  def start(self):
    try:
      return self._start
    except AttributeError:
      return None

  @start.setter
  def start(self, value):
    if isinstance(value, str):
      self._start = datetime.strptime(value, "%d/%m/%Y").date()
    elif isinstance(value, date):  
      self._start = value

  @property
  def end(self):
    try:
      return self._end
    except AttributeError:
      return None

  @end.setter
  def end(self, value):
    if isinstance(value, str):
      self._end= datetime.strptime(value, "%d/%m/%Y").date()
    elif isinstance(value, date):  
      self._end= value

  @property
  def duration_rate(self):
    try:
      return self._duration_rate 
    except AttributeError:
      return []

  @duration_rate.setter
  def duration_rate(self, value):
      self._duration_rate = value
    
  def __eq__(self, other):
    return self.start <= other and other < self.end

  def __str__(self):
    return "(%s %s %s)" %(self.start, self.end, self.duration_rate)

  def __repr__(self):
    return str(self)

class DurationRate(object):
  def __init__(self, **kwargs):
    for key, value in kwargs.items():
      if hasattr(self, key):
          setattr(self, key, value)
      else:
          raise Exception("Unknown property [" + key +"]")

  def __eq__(self, other):
    return self.min <= other and other < self.max

  @property
  def min(self):
    try:
      return self._min
    except AttributeError:
      return None

  @min.setter
  def min(self, value):
      self._min = int(value)

  @property
  def max(self):
    try:
      return self._max
    except AttributeError:
      return None

  @max.setter
  def max(self, value):
      self._max= int(value)


  @property
  def rate(self):
    try:
      return self._rate
    except AttributeError:
      return None
      
  @rate.setter
  def rate(self, value):
      self._rate = float(value)

  def __str__(self):
    return "(%d %d %f)" %(self.min, self.max, self.rate)

  def __repr__(self):
    return str(self)

class Utils:
  @classmethod
  def last_day_of_month(cls, date_val=datetime.today().date()):
    return date(date_val.year, date_val.month, calendar.monthrange(date_val.year, date_val.month)[1])
  
  @classmethod  
  def iterate_months(cls, sdate=None, tdate=None):
    if sdate is None or tdate is None:
      raise Exception("missing parameters")

    while True:
      cur_month_end=cls.last_day_of_month(sdate)
      if cur_month_end >= tdate:
        yield(tdate)
        break
      yield(cur_month_end)
      sdate = cur_month_end + timedelta(days=1)

  @classmethod
  def renew_deposit(cls, deposit=None, period_duration_lookup=None, collector=[]):
    if deposit is None:
      return 
    today = datetime.now().date()   
    if deposit.matures() < deposit.closed or (deposit.matures() == deposit.closed and deposit.matures() < today): 
      id = deposit.id
      interval = deposit.interval
      duration_days = deposit.duration_days
      duration = deposit.duration
      started = deposit.matures() + timedelta(days = 1)
      principal = deposit.principal + (0.9 * deposit.compound())
      #Lookup
      rate = deposit.rate
      if deposit.matures() != deposit.closed:
        closed = deposit.closed
      else:  
         closed = None
      renewed_deposit = Deposit(id=id, interval=interval, duration_days=duration_days, duration=duration, started=started, principal=principal, closed = closed, rate=rate)
      renewed_deposit.reset(period_duration_lookup=period_duration_lookup)
      collector.append(renewed_deposit)
      if not renewed_deposit.premature:
        Utils.renew_deposit(deposit=renewed_deposit, period_duration_lookup=period_duration_lookup, collector=collector)
    else:
      return 


#Has to derive from object inorder to use property annotation
class Deposit(object):

  def __init__(self, **kwargs):
    for key, value in kwargs.items():
        #Calls the property
        if hasattr(self, key):
          setattr(self, key, value) 
        else:
          raise Exception("Unknown property [" + key +"]")
    if self.closed is None:
       self.closed = self.matures()   

  @property
  def id(self):
    try:
      return self._id
    except AttributeError:
      return None

  @id.setter
  def id(self, value):
    self._id = value

  @property
  def principal(self):
    try:
      return self._principal
    except AttributeError:
      return None

  @principal.setter
  def principal(self, value):
    self._principal = float(value)

  @property
  def rate(self):
    try:
      return self._rate * 100
    except AttributeError:
      return None
  
  @rate.setter
  def rate(self, value):
    self._rate = float(value)/100
  
  @property
  def interval(self):
    #icici, sbi - compounded quarterly
    try:
      return self._interval
    except AttributeError:
      return None

  @interval.setter
  def interval(self, value):
    self._interval = int(value)

  @property
  def started(self):
    try:
      return self._started
    except AttributeError:
      return None

  @started.setter
  def started(self, value):
    if isinstance(value, str):
      self._started = datetime.strptime(value, "%d/%m/%Y").date()
    elif isinstance(value, date):  
      self._started = value

  @property
  def closed(self):
    try:
      return self._closed
    except AttributeError:
      return None


  @closed.setter
  def closed(self, value):
    if isinstance(value, str):
      self._closed = datetime.strptime(value, "%d/%m/%Y").date()
    elif isinstance(value, date):  
      self._closed = value

  
  @property
  def premature(self):
    try:
      return self._premature
    except AttributeError:
      return False

  @premature.setter
  def premature(self, value):
    self._premature = value

  @property  
  def duration(self):
    try:
      return self._duration
    except AttributeError:
      return None
  
  @duration.setter
  def duration(self, value):
    self._duration = float(value)
    if self.duration_days is None:
      setattr(self, 'duration_days', value * 365)

  @property
  def duration_days(self):
    try:
      return self._duration_days
    except AttributeError:
      return None

  @duration_days.setter
  def duration_days(self, value):
    self._duration_days = int(value)
    #Set duration in years
    if self.duration is None:
     setattr(self, 'duration', float(value)/365)
  
 
  def matures(self):
    days = None
    if self.duration_days is None:
      days = timedelta(int (365 * self.duration))
    else:  
      days = timedelta(self.duration_days)
    return self.started + days   

  def tax_statement(self, sdate=None, edate=None):
    if sdate is None or edate is None:
      raise Exception("Missing parameters")
    if sdate > edate :
      raise Exception("Start date should precede end date")
      

    print "Calculating Income for tax period {0} {1} ".format(sdate, edate)
    if sdate > self.matures() or sdate > self.closed :
      print "Already Matured"
      return
  
    print max(sdate, self.started), self.compound(target_date = max(sdate,
          self.started))   
    print min(edate, self.matures(), self.closed), self.compound(target_date = min(edate,
          self.matures(), self.closed))

  def returns(self):
    for year in range(self.started.year, min(self.closed, self.matures()).year+1):
      sdate = date(year, 1, 1)
      edate = date(year, 12, 31)
      self.tax_statement(sdate=sdate, edate=edate)
    for year in range(self.started.year, min(self.closed, self.matures()).year+2):
      sdate = date(year, 4, 1)
      edate = date(year+1, 3, 31)
      self.tax_statement(sdate=sdate, edate=edate)
      
    
      
  def statement(self):
    for month_end in Utils.iterate_months(sdate = self.started, 
        tdate = min(self.matures(), self.closed)):
      print month_end, self.compound(target_date=month_end)

  def compound(self, target_date=None):
    duration = None
    if target_date is None:
      duration = self.duration
    elif isinstance(target_date, str):
      duration = float((datetime.strptime(target_date, "%d/%m/%Y").date() - self.started).days)/365
    elif isinstance(target_date, date):  
      duration = float((target_date - self.started).days)/365
    else:  
      raise Exception("Unsupported parameter type")
    
    if duration > self.duration:
      duration = self.duration
    return self.principal * ((1+ self._rate/self.interval))**(self.interval * duration) - self.principal

  def reset(self, period_duration_lookup=None):
    if self.closed < self.matures():
       #use self.started to figure out period duration lookup entry
       duration_rate_lookup = period_duration_lookup[period_duration_lookup.index(self.started)].duration_rate
       self.duration = float(self.duration_days)/365
       self.duration_days = (self.closed - self.started).days
       self.rate = duration_rate_lookup[duration_rate_lookup.index(self.duration_days)].rate - 0.5
       self.premature = True
    else:
      pass

def main():
  a = Deposit(closed="28/12/2012", rate=8.5, principal= 400000.0, interval=4, duration_days=555, started="26/05/2012")
  pprint(vars(a))
  a.returns()
  a.statement()

if __name__ == "__main__":
  main()
