import random

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def distance(point: list[int]) -> int:
            return point[0] ** 2 + point[1] ** 2

        left, right = 0, len(points) - 1
        target = k - 1

        while left <= right:
            pivot_index = random.randint(left, right)
            pivot_distance = distance(points[pivot_index])

            # Move the pivot to the end.
            points[pivot_index], points[right] = points[right], points[pivot_index]

            # Put all points no farther than the pivot before it.
            store = left
            for i in range(left, right):
                if distance(points[i]) < pivot_distance:
                    points[store], points[i] = points[i], points[store]
                    store += 1

            points[store], points[right] = points[right], points[store]

            if store == target:
                break
            elif store < target:
                left = store + 1
            else:
                right = store - 1

        return points[:k]
        