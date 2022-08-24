func myPow(a float64, n int) float64 {
    if n == 0 {
        return 1;
    }

    bit := 1
    res := 1.0
    neg := n < 0
    if neg {
        n = -n
    }

    for {
        if n & bit != 0 {
            res *= a
        }
        bit = bit << 1
        if bit > n {
            if neg {
                return 1 / res
            }
            return res
        }
        a = a*a
    }
}
