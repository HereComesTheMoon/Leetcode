func maxArea(height []int) int {
    l := 0 // lower
    u := len(height) - 1// upper
    maxi := min(height[l], height[u]) * u
    for l < u {
        if height[l] <= height[u] {
            l++
        } else {
            u--
        }
        maxi = max(maxi, (u-l) * min(height[l], height[u]))
    }

    return maxi
}

func min(a int, b int) int {
    if a < b {
        return a
    }
    return b
}

func max(a int, b int) int {
    if a > b {
        return a
    }
    return b
}
