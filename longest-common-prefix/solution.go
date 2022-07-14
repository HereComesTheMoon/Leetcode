func longestCommonPrefix(strs []string) string {
    prefix := strs[0]

    for k := 1; k < len(strs); k++ {
        for i := 0; i < len(prefix); i++ {
            if len(strs[k]) <= i || strs[k][i] != prefix[i] {
                prefix = prefix[:i]
                break
            }
        }
    }

    return prefix
}
