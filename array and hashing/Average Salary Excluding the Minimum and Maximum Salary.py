class Solution:
    def average(self, salary: List[int]) -> float:
        salary_sum = sum(salary)
        min_s = min(salary)
        max_s = max(salary)
        ent = len(salary) - 2
        return (salary_sum - (min_s + max_s))/ent
        