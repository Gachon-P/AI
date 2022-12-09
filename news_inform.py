import json
import requests

def getNews():
    news_data = requests.get("http://172.16.239.139:8080/news/getNews?category=all").json()
    news_result = json.loads(news_data['result'])
    paragraph = []
    
    paragraph.append(f"첫번째 소식입니다. {news_result['articles'][0]['title']}")
    paragraph.append(f"두번째 소식입니다. {news_result['articles'][1]['title']}")
    paragraph.append(f"세번째 소식입니다. {news_result['articles'][2]['title']}")
    paragraph.append(f"네번째 소식입니다. {news_result['articles'][3]['title']}")
    paragraph.append(f"다섯번째 소식입니다. {news_result['articles'][4]['title']}")

    return paragraph

    
