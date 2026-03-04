#!/bin/bash
# 天气播报 - 扬中

curl -s "https://api.open-meteo.com/v1/forecast?latitude=32.24&longitude=119.82&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Asia%2FShanghai&forecast_days=3" | python3 -c "
import json, sys
data = json.load(sys.stdin)
print('📍 江苏省扬中市 未来三天天气：')
for i in range(3):
    date = data['daily']['time'][i]
    max_temp = data['daily']['temperature_2m_max'][i]
    min_temp = data['daily']['temperature_2m_min'][i]
    rain = data['daily']['precipitation_sum'][i]
    print(f'{date}: {min_temp}°C ~ {max_temp}°C, 降雨 {rain}mm')
"
