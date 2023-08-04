import requests
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "590MEM9PT9AHTFAC"
NEWS_API_KEY = "d0f719048c8e480eb6ca92ba33f0501a"
account_sid = "ACf20dacd10b969a9cf2e69ed463dfd542"
auth_token = "17468fd02dd412f7e96e06ce090863d7"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

now =dt.datetime.now()
current_date = now.date()
current_day = now.weekday()
yesterday = now.replace(day=now.day - 2)
yesterday_date = yesterday.date()
day_before_yesterday = now.replace(day=now.day - 3)
day_before_yesterday_date = day_before_yesterday.date()


response = requests.get(url="https://www.alphavantage.co/query", params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
yesterday_data = data[f"{yesterday_date}"]
yesterday_price = float(yesterday_data["4. close"])
day_before_yesterday_data = data[f"{day_before_yesterday_date}"]
day_before_yesterday_price = float(day_before_yesterday_data["4. close"])
price_difference = (yesterday_price - day_before_yesterday_price)
if price_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
diff_percent = round((price_difference/yesterday_price) * 100)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

news_params = {
        "q": "tesla",
        "from": day_before_yesterday_data,
        "apikey": NEWS_API_KEY,

    }

response = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
news_data = response.json()["articles"]
three_articles = news_data[:3]

if abs(diff_percent) > 1:

    formatted_articles = [f"{STOCK}: {up_down}{diff_percent}% \nHeadline: {article['title']}."
                          f"\nBrief: {article['description']}." for article in three_articles]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages \
            .create(
            body=article,
            from_='+17624754351',
            to='+918360664411'
        )
        print(message.status)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

