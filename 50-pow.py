#1回目
#TIME LIMIT　 答えを見て計算量を考え直す

class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = x
        # なぜかabs(n//2)だと、abs(-3//2)が2を返したので先にnを正に変換
        halfn = abs(n)//2

        if n == 0:
            return 1
        

        #２分割でループ
        #切り捨て除算：　"//"
        if abs(n) > 1:
            for i in range(halfn - 1):
                ans = ans * x
            ans = ans * ans

            if abs(n)%2 != 0:
                ans = ans * x
        
        if n < 0:
            return 1 / ans
        
        return ans