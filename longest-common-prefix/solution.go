func longestCommonPrefix(strs []string) string {
    length := len(strs[0])
    for _, s := range(strs) {
        if len(s) < length {
            length = len(s)
        }
    }

    for k := 0; k < length; k++ {
        for _, s := range(strs) {
            if s[k] != strs[0][k] {
                return strs[0][:k]
            }
        }
    }

    return strs[0][:length]
}
