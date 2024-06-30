#1回目
# class Solution:
#     def intersection(self, nums1, nums2):
#         # setは引数の中の重複を削除した集合を返す組み込み関数
#         # list()で集合をlistに直す
#         sorted_nums1 = list(set(nums1))
#         # sort()はリストを昇順に並べてNoneを返す組み込みメソッド
#         #（sorted()は昇順に並べたリストを返す組み込み関数）
#         sorted_nums1.sort()
#         return [i for i in sorted_nums1 if i in nums2]
    
#答え
# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         return set(nums1) & set(nums2)

# setなのに演算するとList[int]として捉えていい？
# sort機能がsetに入っている？

#２回目（答えを踏まえて）
class Solution:
    def intersection(self, nums1, nums2):
        #setは集合だから和集合などの演算ができる
        return sorted(list(set(nums1) & set(nums2)))