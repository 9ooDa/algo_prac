class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        stu = students.copy()
        sea = seats.copy()
        for i in range(len(students)):
            if students[i] in sea:
                sea.remove(students[i])
                stu.remove(students[i])

        students.sort()
        seats.sort()

        count = 0
        for i in range(len(students)):
            count += abs(students[i]-seats[i])

        return count