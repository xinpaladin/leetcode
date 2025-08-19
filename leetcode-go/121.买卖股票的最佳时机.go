/*
 * @lc app=leetcode.cn id=121 lang=golang
 *
 * [121] 买卖股票的最佳时机
 */
// package main

// import "fmt"

// func main() {
// 	prices := []int{7, 1, 5, 3, 6, 4}
// 	res := maxProfit(prices)
// 	fmt.Println(res)
// }

// @lc code=start
func maxProfit(prices []int) (ans int) {
	minPrice := prices[0]
	for _, p := range prices {
		ans = max(ans, p-minPrice)
		minPrice = min(minPrice, p)
	}
	return
}

// @lc code=end
