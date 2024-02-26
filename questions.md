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

## Q: Flask-Migrate 如何使用？ #124

## Q: 如何使用 SQLAlchemy 下 Raw SQL？ #125

## Q: 如何用土炮的方式建立 Table？ #126

## Q: 什麼是密碼雜湊？如何使用 Python 實現？ #129