from multiprocessing import connection
from app import create_app
from toi import storeToDB
import mysql.connector
import json
import requests

from flask import request
import requests

import collections
from database_connection import get_secret;
app = create_app()

database_secret=get_secret()

@app.route("/storeNewsArticles", methods=["GET"])
def fetchNewsArticles():
    try:
        storeToDB()
        return {"message": "Stored", "success": "true"}, 200
    except Exception as e:
        return {"error": str(e)}, 400

@app.route("/callinglambda")
def calling_lambda():
    EXTERNAL_URL='https://mzi0vth5xi.execute-api.us-east-1.amazonaws.com/default/cloud-project-1'
    res = requests.get(EXTERNAL_URL)
    print(res.text)
    return {"message":res.text},200

@app.route("/fetchNews")
def fetchNews():
    database=get_secret()
    username= database["username"]
    password= database["password"]
    page = int(request.args.get('page'))
    print(page)
    print(database_secret)
    connection = mysql.connector.connect(
        user=username, password=password, host='fd1q2uhgcs13m5h.cz7rsirlpbou.us-east-1.rds.amazonaws.com', database='project', port="3306", use_pure=True)
    cursor = connection.cursor()
    cursor2 = connection.cursor()
    page = (page-1)*15
    print(page)

    sql_select_Query = "select * from project limit 15 offset " + str(page)
    sql_totalRows_Query = "select count(*) from project "
    cursor2.execute(sql_totalRows_Query)
    total = cursor2.fetchone()
    print(total)
    cursor.execute(sql_select_Query)

    # get all records
    records = cursor.fetchall()

    news_info = []
    for row in records:
        items = {
            "id": row[0],
            "Article_Summary": row[1],
            "Article_Title": row[2],
            "link": row[3],
            "sentiment": row[4],
        }
        news_info.append(items)

    return {"message": news_info, "total": total}, 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
