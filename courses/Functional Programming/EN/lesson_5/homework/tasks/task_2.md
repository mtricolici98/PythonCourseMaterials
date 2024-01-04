# Countdown Application

Create a countdown application.

The application should let the user to type in a date and time in the following format as a single
string: `31/12/2023 23:59` (dd/mm/YYYY HH:MM).

The program should check if the date is not further than one year in the future. If the date is further, then show an
error message and let the user type in a new date and time.

The program should also let the user type in the event for the countdown: Example `New Iphone Releases`

After the input has been taken and validated the program should show time remaining until the desired date and time in
days, minutes and seconds: For example: `23 days 19 minutes 34 seconds left until New Iphone Releases` and should update
every second (Note: Use `time.sleep`)

```python
from datetime import datetime
import time

print(datetime.now())
time.sleep(1)  # Will wait 1 second
print(datetime.now())
```
