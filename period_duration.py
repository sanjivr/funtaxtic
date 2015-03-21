from datetime import datetime, date

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

