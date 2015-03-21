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

