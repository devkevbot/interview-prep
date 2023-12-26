from collections import defaultdict
from heapq import heappop, heapify


class Twitter:
    def __init__(self):
        self.timestamp = 0
        self.user_tweets = defaultdict(list)
        self.user_following = defaultdict(set)

    def post_tweet(self, user_id: int, tweet_id: int):
        self.timestamp -= 1
        self.user_tweets[user_id].append((self.timestamp, tweet_id))

    def get_news_feed(self, user_id: int):
        """
        Let n = the number of tweets made by the user and who they're following.
        Let k = the number of tweets to retrieve.
        Time: O(k log n)
        Space: O(n)
        """

        news_feed = []
        news_feed.extend(self.user_tweets[user_id])

        for follower in self.user_following[user_id]:
            news_feed.extend(self.user_tweets[follower])

        # O(n)
        heapify(news_feed)
        result = []
        # O(k) iterations
        while news_feed and len(result) < 10:
            # O(log n)
            result.append(heappop(news_feed)[1])

        return result

    def follow(self, follower_id: int, followee_id: int):
        if follower_id != followee_id:
            self.user_following[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int):
        self.user_following[follower_id].discard(followee_id)
