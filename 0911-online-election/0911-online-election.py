from collections import defaultdict
import bisect

class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leaders = []

        self.votes = defaultdict(int)
        self.max_votes = 0
        self.leader = None

        for person in persons:
            self.votes[person] += 1

            if self.votes[person] >= self.max_votes:
                self.leader = person
                self.max_votes = self.votes[person]
            
            self.leaders.append(self.leader)

    def q(self, t: int) -> int:
        i = bisect.bisect_right(self.times, t) - 1
        return self.leaders[i]


    # def __init__(self, persons: List[int], times: List[int]):
    #     self.votes = defaultdict(list)
    #     self.unique_persons = set()

    #     for person, time in zip(persons, times):
    #         self.votes[person].append(time)
    #         self.unique_persons.add(person)

    # def q(self, t: int) -> int:

    #     def count(person, target):
    #         voting_list = self.votes[person]
    #         l = 0
    #         r = len(voting_list)

    #         while l < r:
    #             mid = l + (r - l) // 2
            
    #             if voting_list[mid] > target:
    #                 r = mid
    #             else:
    #                 l = mid + 1

    #         return l, voting_list[l - 1]
        
    #     ans = None
    #     max_votes = 0
    #     for person in self.unique_persons:
    #         vote_count, last_vote = count(person, t)
    #         if vote_count > max_votes:
    #             ans = (person, last_vote)
    #             max_votes = vote_count
    #         elif vote_count == max_votes and last_vote > ans[1]:
    #             ans = (person, last_vote)
    #             max_votes = vote_count
        
        # return ans[0]

        
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)