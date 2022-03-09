# https://leetcode.com/problems/k-closest-points-to-origin/submissions/

from typing import List

class Solution:
    def get_distance(self, a: list) -> float:
        """
        distance from point 'a' to the origin
        """
        dist_x = a[0] ** 2
        dist_y = a[1] ** 2
        return (dist_x + dist_y) ** 0.5
    
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # answers: list = [[] for i in range(k)]
        # answers_dist: list = [0 for i in range(k)]
        points_dists = []
        
        for point in points:
            distance = self.get_distance(point)
            points_dists.append(tuple((point, distance))) 
            
        sorted_points_dists = sorted(points_dists, key=lambda x: x[1])

        return [point for point, dist in sorted_points_dists][:k]


class Solution_alt:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        
        return points[:k]


from scipy import spatial
class Solution_2:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        tree = spatial.KDTree(points)
		# x is the origin, k is the number of closest neighbors, p=2 refers to choosing l2 norm (euclidean distance)
        distance, idx = tree.query(x=[0,0], k=K, p=2) 
        return [points[i] for i in idx] if K > 1 else [points[idx]]

"""
Why set distance to negative?

Good Q. Python's heapq is implemented as min heap.

However, what we actually want is a max heap where when we 'pop' an element from the max heap, we get the largest element currently in the heap.

Let's take example of points = [[1,3],[-2,2]], K = 1.
If we were to push both [1,3] and [2,2] to heap by their Euclidean distance, then our heap would have [(10, 1, 3), (8, -2, 2)].
When we "pop" an element, we want to pop (10, 1, 3), which is how max heap works.

Since Python's heapq is implemeneted as min heap, we would actually get (8,-2,2) which is not what we want.
To use Python's heapq as Max heap, I just reversed sign of Euclidean distance.
"""
import heapq
class Solution_3:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        heap = []
        
        for (x, y) in points:
            dist = -(x*x + y*y)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        
        return [(x,y) for (dist,x, y) in heap]


class Solution_4:
    def kClosest(self, points, K):
        return heapq.nsmallest(K, points, key=lambda x: x[0] ** 2 + x[1] ** 2)


"""
QuickSelect: variation of quicksort
It partially sort the first K

Read the last solution: https://leetcode.com/problems/k-closest-points-to-origin/solution/
    Time complexity: O(N), worst case O(N^2)
    Space complexity: O(1)

Quicksort uses logN space for recursion stack, but
    quickselect solves this with no recursion, and thus making O(1)
"""
class Solution_5:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.quick_select(points, k)
    
    def quick_select(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Perform the QuickSelect algorithm on the list"""
        left, right = 0, len(points) - 1
        pivot_index = len(points)
        while pivot_index != k:
            # Repeatedly partition the list
            # while narrowing in on the kth element
            pivot_index = self.partition(points, left, right)
            if pivot_index < k:
                left = pivot_index
            else:
                right = pivot_index - 1
        
        # Return the first k elements of the partially sorted list
        return points[:k]
    
    def partition(self, points: List[List[int]], left: int, right: int) -> int:
        """Partition the list around the pivot value"""
        pivot = self.choose_pivot(points, left, right)
        pivot_dist = self.squared_distance(pivot)
        while left < right:
            # Iterate through the range and swap elements to make sure
            # that all points closer than the pivot are to the left
            if self.squared_distance(points[left]) >= pivot_dist:
                points[left], points[right] = points[right], points[left]
                right -= 1
            else:
                left += 1
        
        # Ensure the left pointer is just past the end of
        # the left range then return it as the new pivotIndex
        if self.squared_distance(points[left]) < pivot_dist:
            left += 1
        return left
    
    def choose_pivot(self, points: List[List[int]], left: int, right: int) -> List[int]:
        """Choose a pivot element of the list"""
        return points[left + (right - left) // 2]
    
    def squared_distance(self, point: List[int]) -> int:
        """Calculate and return the squared Euclidean distance."""
        return point[0] ** 2 + point[1] ** 2