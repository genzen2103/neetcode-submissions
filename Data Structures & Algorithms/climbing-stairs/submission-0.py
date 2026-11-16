class Solution:
    mem = {1:1,2:2}
    def climbStairs(self, n: int) -> int:
        if n in self.mem:  return self.mem[n]
        result = self.climbStairs(n-1)+self.climbStairs(n-2)
        self.mem[n] = result
        return result