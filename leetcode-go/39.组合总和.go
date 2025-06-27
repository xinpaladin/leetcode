/*
 * @lc app=leetcode.cn id=39 lang=golang
 *
 * [39] 组合总和
 */
package main

import (
	"fmt"
)

func main() {
	candidates := []int{2, 3, 6, 7}
	target := 7
	res := combinationSum(candidates, target)
	fmt.Println(res)
}

// @lc code=start

func combinationSum(candidates []int, target int) [][]int {
	var combinations = make([][]int, 0)
	combination := []int{}
	var dfs func(index, target int)
	dfs = func(index int, target int) {
		if index == len(candidates) {
			return
		}
		if target == 0 {
			combinations = append(combinations, append([]int(nil), combination...))
			return
		}
		dfs(index+1, target)

		if target >= candidates[index] {
			combination = append(combination, candidates[index])
			dfs(index, target-candidates[index])
			combination = combination[:len(combination)-1]
		}

	}
	dfs(0, target)
	return combinations
}

// @lc code=end
