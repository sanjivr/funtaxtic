from datetime import datetime, date, timedelta
import calendar

class Utils:
  '''
    @arg date_val : [datetime.date]
    @return       : [datetime.date] last day of month corresponding to date_val
  '''
  @classmethod
  def last_day_of_month(cls, date_val=datetime.today().date()):
    return date(date_val.year, date_val.month, calendar.monthrange(date_val.year, date_val.month)[1])
  
  '''
    generator method
    @arg sdate : [datetime.date] start date
    @arg edate : [datetime.date] end date
    @return    : [datetime.date] last day of each month between sdate and edate 
  '''
  @classmethod  
  def iterate_months(cls, sdate=None, edate=None):
    if sdate is None or edate is None:
      raise Exception("missing parameters")

    while True:
      cur_month_end=cls.last_day_of_month(sdate)
      if cur_month_end >= edate:
        yield(edate)
        break
      yield(cur_month_end)
      sdate = cur_month_end + timedelta(days=1)


