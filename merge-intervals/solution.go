type ivs [][]int

func (v ivs) Len() int {
    return len(v)
}

func (v ivs) Swap(i, j int) {
    v[i], v[j] = v[j], v[i]
}

func (v ivs) Less(i, j int) bool {
    return v[i][0] < v[j][0]
}


func merge(v [][]int) [][]int {
    var w ivs = v
    sort.Sort(w)

    lower := w[0][0]
    upper := w[0][1]
    
    results := make([][]int, 0, len(w))

    for _, iv := range w[1:] {
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

