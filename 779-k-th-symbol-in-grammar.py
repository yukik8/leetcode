class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return 0
        #xはn-1行目の数字の個数（n行目の数字の個数の半数）
        x = 2 ** (n-2)
        #kはn行目の答えの番地を指す
        #kがxよりも大きい場合n行目の後半部分に位置しているのでn-1行目の該当地点に移動
        if k>x:
            #この文法？
            return 1 ^ self.kthGrammar(n - 1, k - x)
        return self.kthGrammar(n - 1, k)
