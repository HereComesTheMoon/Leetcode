func merge(v [][]int) [][]int {
    sort.Slice(v, func(i,j int) bool { return v[i][0] < v[j][0] })

    results := make([][]int, 0, len(v))
    p := v[0]

    for _, iv := range v[1:] {
        if iv[0] <= p[1] {
            if p[1] < iv[1] {
                p[1] = iv[1]
            }
        } else {
            results = append(results, p)
            p = iv
        }
    }
    results = append(results, p)

    return results
}






