class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[1 if not p else 0 for p in image[i][::-1]] for i in range(len(image))]