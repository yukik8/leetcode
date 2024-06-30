from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        #defaultdictはdictの組み込みサブクラス
        #要素を追加できる空の辞書を宣言
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        return list(anagram_map.values())
    
print(Solution().groupAnagrams(strs=["eat","tea","tan","ate","nat","bat"]))