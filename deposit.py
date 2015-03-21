#!/usr/bin/python
import sys
sys.path.append('.')
from datetime import datetime, date, timedelta
from pprint import pprint
from utils import Utils
from period_duration import PeriodDuration
from duration_rate import DurationRate

#Has to derive from object inorder to use property annotation
class Deposit(object):

  def __init__(self, **kwargs):
    for key, value in kwargs.items():
        #Calls the property
        if hasattr(self, key):
          setattr(self, key, value) 
        else:
          raise Exception("Unknown property [" + key +"]")
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

  def is_closed(self):
      return self.closed is not None
  
  def ended(self):
    if self.is_closed():
      return min(self.matures(), self.closed)
    else:
      return self.matures()

  def __cmp__(self, other):
    if self.id == other.id:
      if self.started < other.started:
        return -1
      elif self.started == other.started:
        return 0
      else:
        return 1
    else: 
      if self.id < other.id:
        return -1
      else:
        return 1

  def __repr__(self):
    return "{0} {1} {2} {3} {4} {5}".format(self.id, self.started, self.ended(), self.duration_days, self.rate, int(self.principal))

  def should_renew(self):
    # Closed Account
    if self.is_closed():
      # Parent Node - True (parent account, maturity date < close date)
      # Leaf Node - False  (leaf account, maturity date >= close date)
      return self.matures() < self.closed
    # Open Account
    else:  
      # Parent Node - True (parent account, maturity date < today)
      # Leaf Node - False  (active account, maturity date >= today)
      return self.matures()  < datetime.now().date()
      
  def tax_statement(self, sdate=None, edate=None):
    if sdate is None or edate is None:
      raise Exception("Missing parameters")
    if sdate > edate :
      raise Exception("Start date should precede end date")
      

    #print "Calculating Income for tax period {0} {1} ".format(sdate, edate)
    if sdate > self.ended():
      #  print "Already Matured"
      return
    calc_sdate = max(sdate, self.started)
    calc_edate = min(edate, self.ended())
    interest_earned = self.compound(target_date = calc_edate) - \
                      self.compound(target_date = calc_sdate)
    return "[{0} - {1}]: {2}".format(calc_sdate, calc_edate, int(interest_earned))

  def returns(self):
    for year in range(self.started.year, self.ended().year+1):
      sdate = date(year, 1, 1)
      edate = date(year, 12, 31)
      self.tax_statement(sdate=sdate, edate=edate)
    for year in range(self.started.year, self.ended().year+2):
      sdate = date(year, 4, 1)
      edate = date(year+1, 3, 31)
      self.tax_statement(sdate=sdate, edate=edate)
      
  def statement(self):
    for month_end in Utils.iterate_months(sdate = self.started, tdate = self.ended()):
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
    duration_rate_lookup = period_duration_lookup[period_duration_lookup.index(self.started)].duration_rate
    if self.closed < self.matures():
       #use self.started to figure out period duration lookup entry
       self.duration_days = (self.closed - self.started).days
       self.duration = float(self.duration_days)/365
       # Premature closure penalty = 0.5 %
       self.rate = duration_rate_lookup[duration_rate_lookup.index(self.duration_days)].rate - 0.5
       self.premature = True
    else:
       self.rate = duration_rate_lookup[duration_rate_lookup.index(self.duration_days)].rate 

  """
    @arg deposit : [Deposit] First Deposit
    @arg period_duration_lookup : 
    @arg collector: [List[Deposit]] List of renewed deposits till date
  """
  @classmethod
  def renew_deposit(cls, deposit=None, period_duration_lookup=None, collector=[]):
    if deposit is None:
      return 
    if deposit.should_renew():
      id = deposit.id
      interval = deposit.interval
      duration_days = deposit.duration_days
      duration = deposit.duration
      started = deposit.matures() + timedelta(days = 1)
      # 10% TDS
      principal = deposit.principal + (0.9 * deposit.compound())
      rate = deposit.rate
      closed = deposit.closed
      renewed_deposit = Deposit(id=id, interval=interval, duration_days=duration_days, duration=duration, started=started, principal=principal, closed = closed, rate=rate)
      # Reset Attributes of New Deposit
      renewed_deposit.reset(period_duration_lookup=period_duration_lookup)
      collector.append(renewed_deposit)
      if not renewed_deposit.premature:
        Deposit.renew_deposit(deposit=renewed_deposit, period_duration_lookup=period_duration_lookup, collector=collector)
    else:
      return 

