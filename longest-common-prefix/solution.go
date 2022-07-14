func longestCommonPrefix(strs []string) string {
    prefix := strs[0]
    for _, s := range(strs) {
        if len(s) < len(prefix) {
            prefix = s
        }
    }

    for k := 0; k < len(strs); k++ {
        for i := 0; i < len(prefix); i++ {
            if strs[k][i] != prefix[i] {
                prefix = prefix[:i]
                break
            }
        }
    }

    return prefix
}
