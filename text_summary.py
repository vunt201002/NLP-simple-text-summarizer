import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
import time
import math


text = """Samsung was founded by Lee Byung-chul in 1938 as a trading company. Over the next three decades, 
the group diversified into areas including food processing, textiles, insurance, securities, and retail. 
Samsung entered the electronics industry in the late 1960s and the construction and shipbuilding industries in 
the mid-1970s; these areas would drive its subsequent growth. Following Lee's death in 1987, Samsung was separated 
into five business groups – Samsung Group, Shinsegae Group, CJ Group and Hansol Group, and JoongAng Group.

Notable Samsung industrial affiliates include Samsung Electronics (the world's largest information technology company, 
consumer electronics maker and chipmaker measured by 2017 revenues), Samsung Heavy Industries 
(the world's second largest shipbuilder measured by 2010 revenues), and Samsung Engineering and Samsung C&T 
Corporation (respectively the world's 13th and 36th largest construction companies). Other notable subsidiaries 
include Samsung Life Insurance (the world's 14th largest life insurance company), Samsung Everland (operator of Everland Resort, 
the oldest theme park in South Korea) and Cheil Worldwide (the world's 15th largest advertising agency, as measured by 2012 revenues)"""


def summerizer(rowdocs):
    start_time = time.time()  # Record the start time

    stopwords = list(STOP_WORDS)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(rowdocs)

    token = [token.text for token in doc]

    wordFrequency = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in wordFrequency.keys():
                wordFrequency[word.text] = 1
            else:
                wordFrequency[word.text] += 1

    maxFrequency = max(wordFrequency.values())

    for word in wordFrequency.keys():
        wordFrequency[word] = wordFrequency[word] / maxFrequency

    sent_token = [sent for sent in doc.sents]

    sent_score = {}
    for sent in sent_token:
        for word in sent:
            if word.text in wordFrequency.keys():
                if sent not in sent_score.keys():
                    sent_score[sent] = wordFrequency[word.text]
                else:
                    sent_score[sent] += wordFrequency[word.text]

    select_len = int(len(sent_token) * 0.3)

    summary = nlargest(select_len, sent_score, key=sent_score.get)

    final_summary = [word.text for word in summary]
    summary_text = ' '.join(final_summary)

    end_time = time.time()  # Record the end time

    response_time = end_time - start_time  # Calculate the response time
    rounded_response_time = round(response_time, 2)  # Round to two decimal places

    return summary_text, rowdocs, len(rowdocs.split(' ')), len(summary_text.split(' ')), rounded_response_time




