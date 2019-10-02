import requests
import operator

users = ("test", "henrikkol", "joesaunderson")

leaderBoard = {}

for user in users:
    req = requests.get('https://hacktoberfestchecker.jenko.me/prs?username=' + user.__str__())
    score = len(req.json()['prs'])
    userName = req.json()['username']
    leaderBoard.setdefault(userName, score)

sorted_x = sorted(leaderBoard.items(), key=operator.itemgetter(1), reverse=True)

for k, v in sorted_x:
    print(v, k)
