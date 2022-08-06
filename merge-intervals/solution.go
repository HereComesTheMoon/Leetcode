func merge(v [][]int) [][]int {
    sort.Slice(v, func(i,j int) bool { return v[i][0] < v[j][0] })

    lower := v[0][0]
    upper := v[0][1]
    
    results := make([][]int, 0, len(v))

    for _, iv := range v[1:] {
        if iv[0] <= upper {
            if upper < iv[1] {
                upper = iv[1]
            }
        } else {
            results = append(results, []int{lower, upper})
            lower = iv[0]
            upper = iv[1]
        }
    }
    results = append(results, []int{lower, upper})

    return results
}



