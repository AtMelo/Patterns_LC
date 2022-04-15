class Solution:
    def maxProfit(self, prices: list) -> int:
        left = 0
        right = 1
        max_prof = 0
        while right < len(prices):
            cur_pr = prices[right] - prices[left]
            if prices[right] < prices[left]:
                left = right
            else:
                if cur_pr > max_prof:
                    max_prof = cur_pr
            right += 1
        return max_prof

if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    sol = Solution()
    max_pr = sol.maxProfit(prices)
    print(max_pr)

