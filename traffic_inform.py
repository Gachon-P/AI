import requests
import json

def getBusInform():
    bus_data = requests.get("http://172.16.239.139:8080/bus/busArrival?macId=E4:5F:01:D6:0F:91").json()
    bus_station = bus_data['stationName']
    bus_number = bus_data['lineNumber']
    bus_time = bus_data['arrivalInfo'][0]['predictTime1']
    if bus_time == "":
        bus_Time = "도착 정보가 없습니다."
    else:
        bus_Time = bus_time + "분 뒤 도착 예정입니다."
    paragraph = bus_station + "정거장에 " + bus_number + "번 버스가 " + bus_Time

    return paragraph
