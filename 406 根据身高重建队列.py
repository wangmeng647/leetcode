
class Solution:
    def reconstructQueue(self, people):
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        que = []
        que.append(people[0])
        for word in people[1:]:
            que.insert(word[1], word)
        return que

s = Solution()
people = [[7,1],[4,4],[7,0],[5,0],[6,1],[5,2],[7,2]]
print(s.reconstructQueue(people))