/*
 * @lc app=leetcode.cn id=20 lang=golang
 *
 * [20] 有效的括号
 */
package main

// @lc code=start
// func isValid(s string) bool {
// 	l := len(s)
// 	if l%2 == 1 {
// 		return false
// 	}
// 	d := map[string]string{
// 		")": "(",
// 		"}": "{",
// 		"]": "[",
// 	}
// 	var stack = make([]string, 0, l/2+1)

// 	seq := strings.Split(s, "")

// 	for _, v := range seq {
// 		value, ok := d[v]
// 		if ok {
// 			if len(stack) == 0 || stack[len(stack)-1] != value {
// 				return false
// 			} else {
// 				stack = stack[:len(stack)-1]
// 			}
// 		} else {
// 			stack = append(stack, v)
// 		}
// 	}
// 	return len(stack) == 0
// }

func isValid(s string) bool {
	n := len(s)
	if n%2 == 1 {
		return false
	}
	pairs := map[byte]byte{
		')': '(',
		']': '[',
		'}': '{',
	}
	stack := []byte{}
	for i := 0; i < n; i++ {
		if pairs[s[i]] > 0 {
			if len(stack) == 0 || stack[len(stack)-1] != pairs[s[i]] {
				return false
			}
			stack = stack[:len(stack)-1]
		} else {
			stack = append(stack, s[i])
		}
	}
	return len(stack) == 0
}

// @lc code=end
