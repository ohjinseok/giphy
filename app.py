from flask import Flask, render_template, request
import giphy

app = Flask(__name__)

# index 페이지 : 검색어를 입력 받음
@app.route('/')
def index():
    return render_template('index.html')
    
# seach 페이지:
# 1. 입력 받은 검색어로 giphy 요청을 보내 짤방 정보를 받아옴
# 2. 받아온 정보(짤방 주소)를 보여줌
@app.route('/search')
def search():
    query = request.args.get('query')
    # 1. jjals에는 검색을 통해 받아온 짤들을 리스트로 저장한다.
    jjals = giphy.get_jjal(query)
    
    # 2. jjals를 template(search.html)에서 보여준다.
    return render_template('search.html', query=query, jjals=jjals)
    
    
@app.route('/trending')
def trending():
    # 인기짤을 모아 놓은 페이지를 만든다.
    # API -> trending
    # search와는 다른 부트스트램 컴포넌트를 활용한다.
    jjals = giphy.get_trend()
    
    return render_template('trending.html', jjals=jjals)

@app.route('/block')
def block():
    return render_template('block.html')