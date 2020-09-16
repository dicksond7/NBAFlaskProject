import matplotlib.pyplot as plt
import pandas as pd
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

NBADatabase = client['NBADatabase']

NBACollectionPerGame = NBADatabase['NBAPLAYERS']

NBACollectionAdvanced = NBADatabase['NBAPLAYERSADVANCED']

AllStats = NBACollectionAdvanced.find({})

df = pd.DataFrame(list(AllStats))

Names = df["name"].to_list()



