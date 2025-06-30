/*
 * @lc app=leetcode.cn id=22 lang=golang
 *
 * [22] 括号生成
 */
package main

import (
	"fmt"
	"strings"
)

func main() {
	n := 3
	ans := generateParenthesis(n)
	fmt.Println(ans)
}

// @lc code=start
func generateParenthesis(n int) []string {
	var ans []string
	var path = make([]string, 0, 2*n)
	var backtrace func(path []string, left, right int)
	backtrace = func(path []string, left, right int) {
		if len(path) == 2*n {
			ans = append(ans, strings.Join(path, ""))
			return
		}
		if left > 0 {
			backtrace(append(path, "("), left-1, right)
		}
		if right > left {
			backtrace(append(path, ")"), left, right-1)
		}

	}
	backtrace(path, n, n)
	return ans

}

// @lc code=end
