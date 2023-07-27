class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.c = (x_center, y_center)
        

    def randPoint(self) -> List[float]:
        x = float('inf')
        y = float('inf')
        while self.r**2 <= (x - self.c[0])**2 + (y - self.c[1])**2:
            x = random.uniform(self.c[0] - self.r, self.r + self.c[0])
            y = random.uniform(self.c[1] - self.r, self.r + self.c[1])
        return (x, y)

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()