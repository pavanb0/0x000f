strs = ["eat","tea","tan","ate","nat","bat"]

def GroupAnagram(strings):
    out = {}
    for word in strings:
        sortedword = ''.join(sorted(word))
        if sortedword in out:
            out[sortedword].append(word)
        else:
            out[sortedword] = [word]
    return out.values()
print(GroupAnagram(strs)) 
  