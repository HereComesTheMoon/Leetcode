func longestCommonPrefix(strs []string) string {
    prefix := strs[0]
    for k := 0; k < len(prefix); k++ {
        for _, s := range(strs) {
            if len(s) <= k || s[k] != prefix[k] {
                return prefix[:k]
            }
        }
    }
    return prefix
}
