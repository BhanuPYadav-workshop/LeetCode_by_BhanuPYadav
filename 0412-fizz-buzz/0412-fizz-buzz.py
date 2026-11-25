class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result = []
        for i in range(1,n+1):
            word=('Fizz' if i%3==0 else "") + ('Buzz' if i%5==0 else "")
            result.append(word or str(i))
        return result