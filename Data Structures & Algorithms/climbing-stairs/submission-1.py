class Solution:
    def climbStairs(self, n: int) -> int:
        one_step_before = 1  # ways to reach the previous step
        two_steps_before = 1 # ways to reach the step before that

        for _ in range(n-1):
            # New count is the sum of the previous two counts.
            one_step_before, two_steps_before = (
                one_step_before + two_steps_before,
                one_step_before,
            )

        return one_step_before