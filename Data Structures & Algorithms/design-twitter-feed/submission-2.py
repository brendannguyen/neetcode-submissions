class Twitter:

    def __init__(self):
        self.count = 0
        self.following = {} # (userId, [followees])

        self.tweets = {} # (userId, [(id, tweet)])

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        if userId in self.tweets:
            self.tweets[userId].append((self.count, tweetId))
        else:
            self.tweets[userId] = [(self.count, tweetId)] 

    def getNewsFeed(self, userId: int) -> List[int]:
        # add user to own following set
        if userId in self.following:
            self.following[userId].add(userId)
        else:
            self.following[userId] = {userId}

        maxHeap = []
        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                count, tweetId = self.tweets[followeeId][-1]
                maxHeap.append((count, tweetId, followeeId, index-1))
        heapq.heapify_max(maxHeap)
        

        newsFeed = []
        while maxHeap and len(newsFeed) < 10:
            count, tweetId, followeeId, nextIndex = heapq.heappop_max(maxHeap)
            newsFeed.append(tweetId)

            if nextIndex >= 0:
                count, tweetId = self.tweets[followeeId][nextIndex]
                heapq.heappush_max(maxHeap, (count, tweetId, followeeId, nextIndex-1))

        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].add(followeeId)
        else:
            self.following[followerId] = {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
