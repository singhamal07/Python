class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = Counter(students)
        for sandwich in sandwiches:
            if count[sandwich] == 0:
                return count[0] + count[1]
            count[sandwich] -= 1
        return 0