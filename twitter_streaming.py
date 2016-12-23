from tweepy.streaming import StreamListener

from tweepy import OAuthHandler

from tweepy import Stream

import json

import tweepy

import pymongo

access_token = "444602782-Fv2XfiBxOeU26ILqypJynemKfgPrWtlDGzuDvr98"

access_token_secret = "h4P6eJHcFaCZP3uPp12cvmiHcPjoeYiXnktDtQKYbfgwo"

consumer_key = "B4XQ6SH3zDZ1v1LszacYa60Av"

consumer_secret = "lmHAf5zRspFUWZHsvBXxHHOafvklqFujQBwg7BoASeRFmSzkdp"

 

# Defining listener class for getting the streamingclass 
# Defining listener class for getting the streaming
class StdOutListener(StreamListener):
	def on_data(self, testdata2):           

#Retrieving the details like Id, tweeted text and created at.

		tweet=json.loads(testdata2)

		created_at = tweet["created_at"]

		id_str = tweet["id_str"]

		text = tweet["text"]

		obj = {"created_at":created_at,"id_str":id_str,"text":text,}

		tweetind=collection.insert_one(obj).inserted_id

		print obj

		return True

	def on_error(self, status):

        	print status


if __name__ == '__main__':


#This handles Twitter authetification and the connection to Twitter Streaming AP

    l = StdOutListener()

    auth = OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)

 

 # Below code  is for making connection with mongoDB

    from pymongo import MongoClient   

    client = MongoClient()

    client = MongoClient('localhost', 27017)

    db = client.coletas_twitter

    collection = db.collection_trabalho

#This line filter Twitter Streams to capture data by the keywords: 'India'

    stream.filter(track=['Futebol','Ferias','Jogos','Dados','Comercio','Minas Gerais','Brasil'])
