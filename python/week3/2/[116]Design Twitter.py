'''
Design Twitter
Implement a simplified version of Twitter which allows users to post tweets, follow/unfollow each other, and view the 10 most recent tweets within their own news feed.

Users and tweets are uniquely identified by their IDs (integers).

Implement the following methods:

Twitter() Initializes the twitter object.
void postTweet(int userId, int tweetId) Publish a new tweet with ID tweetId by the user userId. You may assume that each tweetId is unique.
List<Integer> getNewsFeed(int userId) Fetches at most the 10 most recent tweet IDs in the user's news feed. Each item must be posted by users who the user is following or by the user themself. Tweets IDs should be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId follows the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId unfollows the user with ID followeeId.
Example 1:

Input:
["Twitter", "postTweet", [1, 10], "postTweet", [2, 20], "getNewsFeed", [1], "getNewsFeed", [2], "follow", [1, 2], "getNewsFeed", [1], "getNewsFeed", [2], "unfollow", [1, 2], "getNewsFeed", [1]]

Output:
[null, null, null, [10], [20], null, [20, 10], [20], null, [10]]

Explanation:
Twitter twitter = new Twitter();
twitter.postTweet(1, 10); // User 1 posts a new tweet with id = 10.
twitter.postTweet(2, 20); // User 2 posts a new tweet with id = 20.
twitter.getNewsFeed(1);   // User 1's news feed should only contain their own tweets -> [10].
twitter.getNewsFeed(2);   // User 2's news feed should only contain their own tweets -> [20].
twitter.follow(1, 2);     // User 1 follows user 2.
twitter.getNewsFeed(1);   // User 1's news feed should contain both tweets from user 1 and user 2 -> [20, 10].
twitter.getNewsFeed(2);   // User 2's news feed should still only contain their own tweets -> [20].
twitter.unfollow(1, 2);   // User 1 follows user 2.
twitter.getNewsFeed(1);   // User 1's news feed should only contain their own tweets -> [10].
'''
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.time = 0  # 타임스탬프 증가용
        self.followMap = defaultdict(set)  # 팔로우 관계
        self.tweetMap = defaultdict(list)  # 유저 별 트윗 저장

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        feed = self.tweetMap[userId][:]  # 자신의 트윗 포함
        for followeeId in self.followMap[userId]:
            feed.extend(self.tweetMap[followeeId])  # 팔로우한 유저의 트윗 추가
        feed.sort(key=lambda x: -x[0])  # 시간 기준 정렬 (최신순)
        return [tweetId for _, tweetId in feed[:10]]  # 최신 10개 트윗 ID 반환

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)

# 실행 예시
if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 10)              # User 1 posts tweet 10
    twitter.postTweet(2, 20)              # User 2 posts tweet 20
    print(twitter.getNewsFeed(1))         # [10]
    print(twitter.getNewsFeed(2))         # [20]
    twitter.follow(1, 2)                  # User 1 follows User 2
    print(twitter.getNewsFeed(1))         # [20, 10]
    print(twitter.getNewsFeed(2))         # [20]
    twitter.unfollow(1, 2)                # User 1 unfollows User 2
    print(twitter.getNewsFeed(1))         # [10]
    