import requests
import json
import datetime

def getWeather():
    data = requests.get("http://172.16.239.139:8080/weather/getWeather?macId=E4:5F:01:D6:0F:91").json()
    city = data['city']
    weatherInfo = json.loads(data['weatherInfo'])
    current = weatherInfo['current']
    
    #Weather Indicator
    daily_weather = weatherInfo['daily'][0]['weather'][0]['main']
    daily_min = round(weatherInfo['daily'][0]['temp']['min'], 1)
    daily_max = round(weatherInfo['daily'][0]['temp']['max'], 1)
    
    clear_weather = 'Clear'
    snow_weather = 'Snow'
    cloud_weather = 'Clouds'
    rain_weather = ['Drizzle', 'Rain', 'Thunderstorm']
    mist_weather = ['Mist', 'Smoke', 'Haze', 'Dust', 'Fog', 'Sand', 'Dust', 'Ash', 'Squall', 'Tornado']
    
    #Weather Information Paragraph
    paragraph = f"현재 {city}의 기온은 {round(current['temp'], 1)}도이며, 체감온도는 {round(current['feels_like'], 1)}도입니다. 오늘의 최고기온은 {daily_max}도로 예상되고, 오늘의 최저기온은 {daily_min}도로 예상됩니다. 날씨는 전반적으로 {current['weather'][0]['description']}이 예상됩니다. "
    if abs(daily_max-daily_min) >= 10:
        temp_diff_paragraph = f"일교차가 큰 날이에요. 겉옷을 챙겨나가는걸 추천드릴게요. "
        paragraph += temp_diff_paragraph
        
    if daily_weather == clear_weather:
        clear_paragraph = f"오늘은 맑은 날씨가 예상되는 하루에요. 가벼운 산책 어떠세요?"
        paragraph += clear_paragraph
    elif daily_weather == snow_weather:
        snow_paragraph = f"눈이 오는 날, 미끄러운 도로를 조심하셔야 합니다!"
        paragraph += snow_paragraph
    elif daily_weather in rain_weather:
        rain_paragraph = f"오늘은 비가 예상되니, 우산을 꼭 챙기세요!"
        paragraph += rain_paragraph
    elif daily_weather in mist_weather:
        mist_paragraph = f"안개가 예상되는 날씨, 운전을 하신다면 서행하셔야 합니다!"
        paragraph += mist_paragraph
    elif daily_weather == cloud_weather:
        cloud_paragraph = f"구름이 많은 날이에요. 혹시 모를 비를 주의하세요!"
        paragraph += cloud_paragraph
    

    return paragraph

def main():
    print(getWeather())
    
if __name__ == "__main__":
    main()
