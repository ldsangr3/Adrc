import math
import numpy as np
import datetime

current_hour = 18
        
if current_hour >= 16:
    Time_ = current_hour -16
elif current_hour < 10:
    Time_ = current_hour + 8
else:
    Time_ = 0
        
print("time", Time_)
schedule = abs(math.sin(((Time_ - 18) / 18) * 3.14159))

print("schedule", schedule)
a=-50
print("Interpolating", np.interp(a, [0, 100], [0, 5])
)
