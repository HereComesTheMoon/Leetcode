class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [ [None for _ in range(n)] for _ in range(n) ]
        x, y = 0, 0
        dx, dy = 1, 0
        def change_dir(dx, dy):
            match (dx, dy):
                case (1, 0):
                    return (0, 1)
                case (0, 1):
                    return (-1, 0)
                case (-1, 0):
                    return (0, -1)
                case (0, -1):
                    return (1, 0)
                case _:
                    assert False

        def is_invalid(x, y, dx, dy):
            if not (0 <= x + dx < n):
                return True
            if not (0 <= y + dy < n):
                return True
            if matrix[y + dy][x + dx] is not None:
                return True
            return False

        for k in range(1, n ** 2 + 1):
            matrix[y][x] = k
            if is_invalid(x, y, dx, dy):
                dx, dy = change_dir(dx, dy)
            x += dx
            y += dy
        return matrix
            
            



             