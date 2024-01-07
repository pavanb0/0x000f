class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n != 1 and n not in visited:
            visited.add(n)
            n = self.sumcal(n)

        return n == 1

    def sumcal(self, num):
        sums = 0
        while num:
            digit = num % 10
            sums += digit ** 2
            num = num // 10
        return sums
