from collections import defaultdict
class Solution:
    def topKFrequent(self, nums, k) :
        freq_dict = defaultdict(int)
        result = []
        freq_list = []

        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1

        for freq in freq_dict.values():
            freq_list.append(freq)

        freq_list.sort()
        freq_list = freq_list[-k:]

        for freq in freq_list[:k]:
            for num in freq_dict:
                if freq_dict[num] == freq and num not in result:
                    result.append(num)

        return result