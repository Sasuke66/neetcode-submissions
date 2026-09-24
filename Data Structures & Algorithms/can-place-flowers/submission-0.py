class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        run = 1
        count = 0
        for flower in flowerbed:
          if flower == 0:
            run += 1
          else:
            count += (run - 1) // 2
            run = 0
        count += run//2
        return count >= n