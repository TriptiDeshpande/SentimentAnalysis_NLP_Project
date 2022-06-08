#!/usr/bin/env python
# coding: utf-8

# In[75]:


import streamlit as st
import spacy
from textblob import TextBlob
from textblob.np_extractors import ConllExtractor

st.set_page_config(layout='wide', initial_sidebar_state='expanded',page_icon="smiley")
st.title('Text Sentiment Analysis')

st.markdown('Type a sentence in the below text box and choose the desired option in the adjacent menu.')
side = st.sidebar.selectbox("Select an option below", ("Sentiment", "Name Entity Recognizer"))
Text = st.text_input("Enter the sentence")

def sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity < 0:
        return ("Negative with a score of : ", analysis.sentiment.polarity)
    elif analysis.sentiment.polarity==0:
        return " Waiting ..... "
    else:
        return ("Positive with a score of : ", analysis.sentiment.polarity)

def ner(sentence):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)
    ents = [(e.text, e.label_) for e in doc.ents]
    return ents
def run():
    if side == "Sentiment":
        st.write(sentiment(Text))    
    if side == "Name Entity Recognizer":
        st.write(ner(Text))
if __name__ == '__main__':
    run()


# In[ ]:





# In[ ]:




