#!/usr/bin/python3

import datetime as date
from random import randint
from pymongo import MongoClient
import pprint
import argparse


def printCollection(collection):
        for elt in collection.find():
            pprint.pprint(elt)

HOST = ''
PORT = 27017
client = MongoClient(HOST,PORT)

parser = argparse.ArgumentParser(description="Gestion base mongodb")
parser.add_argument("-D",'--db', help="Base de donnée", default="apiwatchTest", metavar='Base')
parser.add_argument("-p", help="Affiche la collections indiquée",metavar="COLLECTION")
parser.add_argument("-i", "--insert", help="Insert DailyRecordTH Document", metavar='ID')
parser.add_argument("-c","--collection", action="store_true", help="Affiche les collections de la base")
parser.add_argument("--dbs", action="store_true", help="Affiche les bases")
args = parser.parse_args()


if(args.dbs and args.db):
	dbs = client. database_names()
	for elt in dbs:
		print("-> "+elt)

if(args.p):
    if(args.db):
        db = client[args.db]
        collection = db[args.p]
        printCollection(collection)

if(args.collection and args.db):
    db = client[args.db]
    collectionList = db.collection_names()
    for collect in collectionList:
        print(collect)
        
if(args.insert):
    db = client[args.db]
    collection = db.DailyRecordsTH
    id = args.insert
    new_dailyRecord = [{
        "recordDate" : date.datetime.now(),
        "humidity_int_max" : randint(30,60),
        "humidity_int_min" : randint(20,55),
        "temp_int_max" : randint(10,35),
        "temp_int_min" : randint(15,33),
        "temp_int_mean" : randint(20,35),
        "temp_int_stddev" : 0.704536,
        "sensorRef" : "42:13:1A",
        "idHive"  : id,
        "health_status" : "A",
        "health_trend" : "I"
    }]
    result = collection.insert_many(new_dailyRecord)
    result.inserted_ids
    print(result)
