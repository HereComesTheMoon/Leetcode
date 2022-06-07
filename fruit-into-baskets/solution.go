func totalFruit(fruits []int) int {
    k := 1
    for k < len(fruits) && fruits[0] == fruits[k] {
        k++
    }

    if k == len(fruits) {
        return k
    }

    prev := fruits[0]
    curr := fruits[k]
    startWindow := 0
    startCurrentStreak := k
    maxFruits := 1

    k++
    for ; k < len(fruits); k++ {
        if fruits[k] == fruits[k - 1] {
            continue
        }

        if fruits[k] != prev {
            if k - startWindow > maxFruits {
                maxFruits = k - startWindow
            }
            startWindow = startCurrentStreak
        }

        startCurrentStreak = k
        prev = curr
        curr = fruits[k]
    }
    if len(fruits) - startWindow > maxFruits {
        maxFruits = len(fruits) - startWindow
    }

    return maxFruits
}
