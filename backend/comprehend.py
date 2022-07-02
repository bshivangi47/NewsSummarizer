
from pprint import pprint
import boto3

session = boto3.session.Session(
    aws_access_key_id="AKIAQXTBVLUAVYO7IV2C",
    aws_secret_access_key="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",
    region_name='us-east-1'
)

client = session.client('comprehend')

response = client.detect_sentiment(
    Text='"Hello Zhang Wei, I am John. Your AnyCompany Financial Services, LLC credit card account 1111-0000-1111-0008 has a minimum payment of $24.53 that is due by July 31st. Based on your autopay settings, we will withdraw your payment on the due date from your bank account number XXXXXX1111 with the routing number XXXXX0000. \n\nYour latest statement was mailed to 100 Main Street, Any City, WA 98121. \nAfter your payment is received, you will receive a confirmation text message at 206-555-0100. \nIf you have questions about your bill, AnyCompany Customer Service is available by phone at 206-555-0199 or email at support@anycompany.com.",',
    LanguageCode='en'
)
highest = 0
# pprint(response)
# pprint(response['SentimentScore'])
for i in response['SentimentScore']:
    # pprint(response['SentimentScore'].get(i))
    if highest < response['SentimentScore'].get(i):
        highest = response['SentimentScore'].get(i)
print(list(response['SentimentScore'].keys())[
      list(response['SentimentScore'].values()).index(highest)])
