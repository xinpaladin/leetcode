/*
 * @lc app=leetcode.cn id=78 lang=golang
 *
 * [78] 子集
 */
package main

import "fmt"

func main() {
	nums := []int{1, 2, 3}
	res := subsets(nums)
	fmt.Println(res)
}

// @lc code=start
func subsets(nums []int) [][]int {
	// ans := make([][]int, 0)
	// n := len(nums)
	// for mask := 0; mask < 1<<n; mask++ {
	// 	set := []int{}
	// 	for i, v := range nums {
	// 		// mask 第i位是否为1
	// 		if mask>>i&1 > 0 {
	// 			set = append(set, v)
	// 		}
	// 	}
	// 	ans = append(ans, append([]int(nil), set...))
	// }
	// return ans

	ans := make([][]int, 1<<len(nums))
	for i := range ans { // 枚举全集 U 的所有子集 i
		for j, x := range nums {
			if i>>j&1 == 1 { // j 在集合 i 中
				ans[i] = append(ans[i], x)
			}
		}
	}

	return ans
}

// @lc code=end
