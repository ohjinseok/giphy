import requests, json, os, urllib
from pprint import pprint as pp

# 1단계 send_request로 함수화
def get_jjal(query):
    api_key = os.getenv('api_key')
    base_url = "http://api.giphy.com/v1/gifs/search?q={}&api_key={}&limit=12".format(query, api_key)
    res = requests.get(base_url)
    # url들을 대상으로 파일을 다운로드한다.
    return [(g.get('images').get('original').get('url'), g.get('slug')) for g in res.json().get('data')] 
    
def down_jjal(url):
    image = urllib.request.urlretrieve(url)
    
# 2단계 input()으로 사용자의 입력을 받아, send_request(입력값)를 실행

# down_jjal(urls[0])

def get_trend():
    api_key = os.getenv('api_key')
    base_url =  "http://api.giphy.com/v1/gifs/trending?api_key={}&limit=10".format(api_key)
    res = requests.get(base_url)
    return [g.get('images').get('original').get('url') for g in res.json().get('data')]
    
if __name__ == "__main__":
    query = input()
    urls= get_jjal(query)