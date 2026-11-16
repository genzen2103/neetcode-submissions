class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        # Count how many students prefer each sandwich type.
        preferences = [students.count(0), students.count(1)]

        for sandwich in sandwiches:
            if preferences[sandwich] == 0:
                # No remaining student wants the top sandwich.
                return sum(preferences)
            preferences[sandwich] -= 1

        return 0