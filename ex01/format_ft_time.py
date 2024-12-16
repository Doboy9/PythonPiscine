import time
from datetime import date


time_raw = time.time()

time_float = f"{time_raw:,.4f}"
time_exp = f"{time_raw:.2e}"



today = date.today()

today_str = today.strftime("%B %d %Y")

print("Seconds since January 1, 1970:", time_float, "or", time_exp, "in scientific notation")
print(today_str)