import requests
import operator

users = ("test", "henrikkol", "joesaunderson")

leaderBoard = {}

for user in users:
    req = requests.get('https://hacktoberfestchecker.jenko.me/prs?username=' + user.__str__())
    score = len(req.json()['prs'])
    userName = req.json()['username']
    leaderBoard.setdefault(userName, score)
    print(userName + ' ' + score.__str__())

print(leaderBoard.get('henrikkol'))

sorted_x = sorted(leaderBoard.items(), key=operator.itemgetter(1), reverse=True)

print("sorted list: ")
print(sorted_x.pop(1))
#
# leaderBoardSorted = sorted(leaderBoard, key=leaderBoard.get, reverse=True)
#
# for i in leaderBoardSorted:
#     print(leaderBoardSorted)
#
# # print(leaderBoardSorted.__getitem__(1))