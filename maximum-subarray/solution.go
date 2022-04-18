func maxSubArray(nums []int) int {
    last := nums[0]
    maxi := nums[0]
    
    for _, v := range(nums[1:]) {
        if last <= 0 {
            last = v
        } else {
            last = last + v
        }
        if maxi < last {
            maxi = last 
        } 
    }
    return maxi
}