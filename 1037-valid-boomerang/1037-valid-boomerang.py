class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        def get_area(x,y):
            return 0.5*(abs((x[0]*(y[1]-y[2])) + (x[1]*(y[2]-y[0])) + (x[2]*(y[0]-y[1]))))
        x, y = [point[0] for point in points], [point[1] for point in points]
        print(x)
        print(y)
        print(get_area(x, y))
    
        return get_area(x, y) != 0