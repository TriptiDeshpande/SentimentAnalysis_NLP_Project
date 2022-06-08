# SentimentAnalysis_NLP_Project
## Business Problem
To perform Sentimental Analysis on a Amazon product 

## Objective 
The objective of the analysis is to get daily Analysis of a product such as emotions, sentiment etc. using Amazon data of our choice. 

## Data Insights 
The product chosen for our Data extraction for Sentimental Analysis is Redmi Note 8. The dataset contains over 3000 product reviews from Amazon.com along with their corresponding rating stars and usernames of the customers . 

## Project Flow - 
1. Data Extraction - More than 3000 reviews were extracted using the BeautifulSoup tool 
2. Data pre-processing - Data cleaning, Tokenization, POS Tagging, Lemmatization
3. EDA 
4. Sentiment Analysis - this was done to calculate the sentiment score using the VADER SentimentIntensityAnalyser
5. Feature Engineering and Model Building - 7 different models were build using both feature engineering methods namely TF-IDF and Bag of Words(Count Vectorizer)
6. Deployment - The deployment was done on streamlit cloud for the sentiment analysis using the TextBlob Sentiment Analyser
Live app link - https://share.streamlit.io/triptideshpande/sentimentanalysis_nlp_project/main/Final_Deployment.py!




