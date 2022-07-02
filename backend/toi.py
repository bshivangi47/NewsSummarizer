from newspaper import Article
from pprint import pprint
from test import fetchArticles
import mysql.connector
import boto3
from database_connection import get_secret;

# import nltk
# import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

# nltk.download()


def storeToDB():
    remove_duplicates = fetchArticles()
    session = boto3.session.Session(
        aws_access_key_id="AKIAQXTBVLUAVYO7IV2C",
        aws_secret_access_key="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",
        region_name='us-east-1'
    )
    database=get_secret()
    username= database["username"]
    password= database["password"]
    print(username)
    print(password)

    client = session.client('comprehend')

    for i in remove_duplicates:
        try:
            url = i
            toi_article = Article(url, language="en")  # en for English
            toi_article.download()
            toi_article.parse()
            toi_article.nlp()

            print("Article's Summary:")
            print(toi_article.summary)
            
            response = client.detect_sentiment(
                Text=toi_article.summary,
                LanguageCode='en'
            )
            highest = 0
            for i in response['SentimentScore']:
                if highest < response['SentimentScore'].get(i):
                    highest = response['SentimentScore'].get(i)
            sentiment = (list(response['SentimentScore'].keys())[
                list(response['SentimentScore'].values()).index(highest)])

            conn = mysql.connector.connect(
                user=username, password=password, host='fd1q2uhgcs13m5h.cz7rsirlpbou.us-east-1.rds.amazonaws.com', database='project', port="3306", use_pure=True)
            cursor = conn.cursor()
            if toi_article.summary and toi_article.title:
                cursor.execute(
                    "Select * from project where Article_Summary = %s and Article_Title = %s and link = %s", (toi_article.summary, toi_article.title, url))

                if len(cursor.fetchall()) == 0:
                    cursor2 = conn.cursor()
                    sql = (
                        "INSERT INTO project(Article_Summary, Article_Title, link, sentiment)"
                        "VALUES (%s, %s, %s, %s)"
                    )
                    data = (toi_article.summary,
                            toi_article.title, url, sentiment)
                    cursor2.execute(sql, data)
                    conn.commit()
                conn.close()
            # print("Article's Keywords:")
            # print(toi_article.keywords)
        except Exception as e:
            print("error!!!!!!!!!!!!!!!!!"+str(e))
            continue
# storeToDB()
