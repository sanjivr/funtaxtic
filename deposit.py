#!/usr/bin/python
from datetime import datetime, date, timedelta
import calendar
from pprint import pprint

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
    self._started = datetime.strptime(value, "%d/%m/%Y").date()

  @property  
  def duration(self):
    try:
      return self._duration
    except AttributeError:
      return None
  
  @duration.setter
  def duration(self, value):
    self._duration = float(value)

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
    #if getattr(self, 'duration') is None:
    setattr(self, 'duration', float(value)/365)
  
 
  def matures(self):
    days = None
    if self.duration_days is None:
      days = timedelta(int (365 * self.duration))
    else:  
      days = timedelta(self.duration_days)
    return self.started + days   

      
  def statement(self):
    for month_end in Utils.iterate_months(sdate = self.started, 
        tdate = self.matures()):
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

    return self.principal * ((1+ self._rate/self.interval))**(self.interval * duration) - self.principal

def main():
  a = Deposit(rate=9, principal=750000.0, interval=4, duration=2, started = "21/11/2014")
  pprint(vars(a))
  a.statement()

if __name__ == "__main__":
  main()