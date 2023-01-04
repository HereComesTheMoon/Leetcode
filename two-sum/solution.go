func twoSum(nums []int, target int) []int {
    d := make(map[int]int)
    for i, v := range nums {
        if j, ok := d[target - nums[i]]; ok {
            return []int{i, j}
        }
        d[v] = i
    }

    return []int{}
}