from flask import Flask, render_template
from dotenv import load_dotenv
app = Flask(__name__)
load_dotenv()

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Toby'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Portland 的天氣真好！'
        },
        {
            'author': {'username': 'Susan'},
            'body': '復仇者聯盟電影真的很酷！'
        }
    ]
    return render_template('index.html', title = '首頁', user=user, posts=posts)

if __name__ == '__main__':
    app.run()