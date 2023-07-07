from datetime import datetime
import pytz

# Parse the datetime string to a datetime object
datetime_obj_utc = datetime.strptime("13:34:52.312918", "%H:%M:%S.%f")

# Attach the UTC timezone to the datetime object
datetime_obj_utc = datetime_obj_utc.replace(tzinfo=pytz.UTC)

# Convert to CST
datetime_obj_cst = datetime_obj_utc.astimezone(pytz.timezone("America/Chicago"))

print(datetime_obj_cst.time())
