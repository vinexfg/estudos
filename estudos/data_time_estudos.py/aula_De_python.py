import calendar
import locale

locale.setlocale(locale.LC_ALL, '')

print(calendar.monthrange(2022, 12))
print(list(enumerate(calendar.day_name)))