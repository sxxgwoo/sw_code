'''
Dota2 Senate

In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
You are given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".

Example 1:

Input: senate = "RRDDD"

Output: "Radiant"

Explanation:

The first 'R' takes the rights of the first 'D'.
THe second 'R' takes the rights of the second 'D'.
The next two 'D's have lost their rights.
The last 'D' takes the rights of the first 'R'.
The last remaining 'R' takes the rights of the last 'D'.
As only 'R' is left, he announces the victory.

Example 2:

Input: senate = "RDD"

Output: "Dire"
'''

# SH proof
def predictPartyVictory(senate: str) -> str:
    party = {"R" : 0, "D" : 0}

    for s in senate:
        if(s == "R"):
            party["R"] += 1
        else:
            party["D"] += 1
    
    for i in range(len(senate)):
        if(party["R"] == 0):
            return "Dire"
    
        if(party["D"] == 0):
            return "Radiant"

        if(senate[0] == "R"):
            for j in range(1, len(senate)):
                if(senate[j] == "D"):
                    senate = senate[1:j] + senate[j+1:] + "R"
                    party["D"] -= 1
                    break
        else:
            for j in range(1, len(senate)):
                if(senate[j] == "R"):
                    senate = senate[1:j] + senate[j+1:] + "D"
                    party["R"] -= 1
                    break

    if(party["R"] == 0):
        return "Dire"
    
    if(party["D"] == 0):
        return "Radiant"
    
# Greedy (Two Queues)
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

def predictPartyVictory(senate: str) -> str:
    D, R = Queue(), Queue()
    n = len(senate)

    # 각 상원의원의 인덱스를 큐에 삽입
    for i, c in enumerate(senate):
        if c == 'R':
            R.enqueue(i)
        else:
            D.enqueue(i)

    # 게임 진행
    while not D.is_empty() and not R.is_empty():
        dTurn = D.dequeue()
        rTurn = R.dequeue()

        if rTurn < dTurn:
            R.enqueue(rTurn + n)
        else:
            D.enqueue(dTurn + n)

    return "Radiant" if not R.is_empty() else "Dire"

# ============================
# Test Case "RRDDD" -> "Radiant"
# ============================
if __name__ == "__main__":
    res = predictPartyVictory("RRDDD")
    
    print(res)