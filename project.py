from random import seed
from turtle import color
from numpy import size, where
import pandas as pd
import seaborn as sns
from matplotlib import colors, figure, pyplot as plt
from pyparsing import col

data = pd.read_csv("matches.csv")
winners = data["winner"].value_counts()[:3]

# plt.figure(figsize=(20,20))

plt.subplot(5,2,1)
plt.bar(winners.keys(),winners.values ,color = ["skyblue","orange","pink"])
plt.title("Maximum wins")
plt.xlabel("Teams")
plt.ylabel("Wins")

temp1 = data[data["toss_winner"]==data["winner"]]
toss_match_winner = temp1["winner"].value_counts()[:5]
plt.title("Teams winning toss and match")
plt.subplot(5,2,2)
plt.pie(toss_match_winner,labels=toss_match_winner.keys(),radius=2,colors=['skyblue','pink','yellow','orange','grey'],autopct="%0.1f%%")

temp2 = data[data["win_by_wickets"]>5]
max_win_bat_second = temp2["win_by_wickets"].value_counts()
plt.subplot(5,2,5)
plt.plot(max_win_bat_second.keys(),max_win_bat_second)
plt.title("Wins with more than 5 wickets")
plt.xlabel("No. of wickets")
plt.ylabel("No. of matches")

umpires = data["umpire1"].value_counts()[:5]
plt.subplot(5,2,9)
plt.barh(umpires.keys(),umpires)
plt.title("Umpires")
plt.xlabel("Umpires with maximum no. of matches")
plt.ylabel("No. of matches")

no_of_matches = data["season"].value_counts()
plt.subplot(5,2,6)
plt.scatter(no_of_matches.keys(),no_of_matches)
plt.xlabel("Season")
plt.ylabel("No. of matches")

temp3 = data[data["win_by_runs"]>0]
motm_bat_first = temp3["player_of_match"].value_counts()[:5]

plt.subplot(5,2,10)
plt.bar(motm_bat_first.keys(),motm_bat_first,color=["pink","orange","grey","yellow","skyblue"])
plt.xlabel("Player")
plt.ylabel("No. of man of the match")
plt.title("Player with max. awards batting first")

plt.show()
