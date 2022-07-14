func romanToInt(s string) int {
    conv := map[byte]int {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    conv2 := map[string]int {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }

    num := 0
    k := 1
    for ; k < len(s) ; k++ {
        if val, ok := conv2[s[k-1:k+1]]; ok {
            num += val
            k++
        } else {
            num += conv[s[k-1]]
        }
    }
    if k == len(s) {
        num += conv[s[len(s)-1]]
    }
    return num
}
