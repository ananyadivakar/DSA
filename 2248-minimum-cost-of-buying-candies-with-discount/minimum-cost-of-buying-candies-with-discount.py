class Solution:
    def minimumCost(self, cost):
        cost.sort(reverse=True)

        ans = 0

        for i in range(len(cost)):
            if i % 3 != 2:      # Pay for the 1st and 2nd candies
                ans += cost[i]  # Skip every 3rd candy (free)

        return ans