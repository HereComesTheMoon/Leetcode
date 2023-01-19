class Twitter:
    def __init__(self):
        self.tweets: List[tuple[int, int]] = []
        self.follows: dict[int, Set[int]] = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.follows.get(userId, set())
        feed = []
        for (posterId, tweetId) in reversed(self.tweets):
            if posterId in following or posterId == userId:
                feed.append(tweetId)
                if len(feed) == 10:
                    return feed
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = { followeeId }
        else:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows.get(followerId, set()).discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)