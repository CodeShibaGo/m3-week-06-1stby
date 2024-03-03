# Questions

## Q: 使用 `virtualenv` 建立虛擬環境 #116
    'virtualenv'是用來建立一個虛擬環境,
    可以在這個環境中安裝所需的套件或是函式庫。

    安裝virtualenv
    ```
    pip install virtualenv
    ```
    建立虛擬環境
    ```
    python3 -m venv venv
    ```
    使用虛擬環境
    ```
    source ./venv/bin/activate
    ```

## Q: python-dotenv 如何使用？ #119
安裝python-dotenv
    
    ```
    pip install python-dotenv
    ```

在資料夾裡新增.env檔
(.env 文件通常用於存儲應用程序的配置信息，如敏感數據、API 密鑰、資料庫連接信息等。它是一個純文本文件，使用鍵值對的形式存儲配置。)

在app.py加入

    ```
    from dotenv import load_dotenv
    load_dotenv()
    ```

    說出 .env 跟 .flaskenv 的差別是？
.env 文件是一個通用的用於配置應用程序的文件，不僅限於 Flask。

.flaskenv 文件是 Flask 專用的配置文件，它用於設置 Flask 應用程序的環境變量。

flaskenv 文件通常用於設置 Flask 相關的變量，如 FLASK_APP（指定 Flask 應用程序的入口點）和 FLASK_ENV（指定 Flask 應用程序的運行環境）。
## Q: 如何使用 Flask-SQLAlchemy 連接上 MySQL？ #123
安裝Flask-SQLAlchemy套件\安裝MySQL\安裝PyMySQL

SQLALCHEMY_DATABASE_URI 設定

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@localhost:{os.getenv('DB_HOST_PORT')}/{os.getenv('DB_NAME')}"

username：資料庫的使用者名稱。
password：資料庫的使用者密碼。
server：資料庫所在位置為localhost:3306。
db：資料庫的名稱。


把重要資訊存在.env
## Q: Flask-Migrate 如何使用？ #124
安裝Flask-Migrate
初始化Flask-Migrate

在專案內加入
from flask_migrate import Migrate
migrate = Migrate(app, db)

接下來就是要使用flask_migrate的指令來初始化設定檔以及設定資料庫等資訊
flask db init
這指令會依據Model的結構產生初始化設定並放置於migrations資料夾內。

flask db migrate
透過這指令可以產生資料庫內容，而不用去寫SQL語法建立Table以及設定DB Schema。

flask db upgrade
當Model的結構有異動時要自動更新資料庫的話首先先執行此指令，接下來再執行flask db migrate，如此即可更新資料庫以符合Model資料結構。
## Q: 如何使用 SQLAlchemy 下 Raw SQL？ #125
使用Text模組
    from sqlalchemy.sql import text
創建sql查詢
    sql = text("SELECT * FROM users WHERE username = :username")
執行
    with db_engine.connect() as connection:
    result = connection.execute(sql, username='example_user')
    user = result.fetchone()
列印結果
    print(user)
## Q: 如何用土炮的方式建立 Table？ #126

## Q: 什麼是密碼雜湊？如何使用 Python 實現？ #129