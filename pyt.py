from datetime import datetime
from pytz import timezone
import pytz
utc = pytz.utc
print(utc.zone)
# 'UTC'
eastern = timezone('US/Eastern')
print(eastern.zone)
# 'US/Eastern'
amsterdam = timezone('Europe/Amsterdam')
print(amsterdam.zone)

fmt = '%Y-%m-%d %H:%M:%S %Z%z'


loc_dt = eastern.localize(datetime(2022, 2, 24, 21, 0, 0))
print(loc_dt.strftime(fmt))
# 2002-10-27 06:00:00 EST-0500

ams_dt = loc_dt.astimezone(amsterdam)
print(ams_dt.strftime(fmt))
# '2002-10-27 12:00:00 CET+0100'
