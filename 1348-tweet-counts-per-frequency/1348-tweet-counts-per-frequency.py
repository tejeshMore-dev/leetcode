from bisect import insort, bisect_left, bisect_right

class TweetCounts:
    DURATIONS = {
        "minute": 60,
        "hour": 3600,
        "day": 86400
    }
    
    def __init__(self):
        self.tweet_records = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        insort(self.tweet_records[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        interval = self.DURATIONS[freq]

        bucket_size = ((endTime - startTime) // interval ) + 1
        buckets = [0] * bucket_size

        left = bisect_left(self.tweet_records[tweetName], startTime)
        right = bisect_right(self.tweet_records[tweetName], endTime)

        # for tweet_time in self.tweet_records[tweetName][left: right]:
        for i in range(left, right):
            tweet_time = self.tweet_records[tweetName][i]

            bucket = (
                tweet_time - startTime
            ) // interval

            buckets[bucket] += 1

        
        return buckets


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)