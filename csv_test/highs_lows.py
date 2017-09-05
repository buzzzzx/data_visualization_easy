import csv

from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    dates = []
    lows = []
    for row in reader:
        try:
            high = int(row[1])
            date = datetime.strptime(row[0], "%Y-%m-%d")
            low = int(row[3])

        except ValueError:
            print(date, "missing data")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(date)

# 绘制图像
fig = plt.figure(dpi=128, figsize=(10, 6))

plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title("Daily high and low temperatures, 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()