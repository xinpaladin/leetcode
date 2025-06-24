/*
 * @lc app=leetcode.cn id=121 lang=golang
 *
 * [121] 买卖股票的最佳时机
 */

// @lc code=start
func maxProfit(prices []int) int {
	minPrice := prices[0]
	maxProfit := 0
	for _, price := range prices {
		fmt.Println(price, minPrice)
		maxProfit = max(price-minPrice, maxProfit)
		minPrice = min(price, minPrice)
	}
	return maxProfit
}

// @lc code=end

