from flask import Flask, render_template, request
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')

app = Flask(__name__)

@app.route('/',methods=['GET'])
def solve():
    return render_template("home.html")

@app.route('/swiggy',methods=['POST'])
def swiggy():
     return computeSwiggy()

@app.route('/zomato',methods=['POST'])
def zomato():
     return computeZomato()

def computeSwiggy():
    dfs=pd.read_excel('/Users/Rishita Kalluri/Downloads/Swiggy2.xlsx',engine='openpyxl')
    sid=SentimentIntensityAnalyzer()
    for data in dfs:
        ss=sid.polarity_scores(data)
    return ss

def computeZomato():
    dfs=pd.read_excel('/Users/Rishita Kalluri/Downloads/Zomato1.xlsx',engine='openpyxl')
    sid=SentimentIntensityAnalyzer()
    for data in dfs:
        ss=sid.polarity_scores(data)
    return ss


if __name__ == '__main__':
	app.run(debug=True)