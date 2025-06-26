/*
 * @lc app=leetcode.cn id=46 lang=golang
 *
 * [46] 全排列
 */
package main

import "fmt"

func main() {
	nums := []int{1, 2, 3}
	res := permute(nums)
	fmt.Println(res)
}

// @lc code=start
func permute(nums []int) [][]int {
	n := len(nums)
	path := make([]int, n)
	onPath := make([]bool, n)
	ans := make([][]int, 0)
	var dfs func(int)
	dfs = func(i int) {
		if i == n {
			ans = append(ans, append([]int(nil), path...))
			return
		}
		for j, on := range onPath {
			if !on {
				path[i] = nums[j]
				onPath[j] = true
				dfs(i + 1)
				onPath[j] = false
			}
		}
	}
	dfs(0)
	return ans

}

// @lc code=end
