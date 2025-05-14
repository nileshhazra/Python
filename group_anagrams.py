def group_anagrams(strs):
    hashtable = {}
    for string in strs:
        ss = "".join(sorted(string))
        if ss in hashtable:
            hashtable[ss].append(string)
        else:
            hashtable[ss] = [string]
    return list(hashtable.values())


result = group_anagrams(["ab", "ba", "aabb", "aaa", "bb", "bba", "cc", "bbaa"])
print(type(result))
print(result)
