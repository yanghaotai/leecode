'''
实现strStr()函数。

给你两个字符串haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回 -1 。

说明：

当needle是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当needle是空字符串时我们应当返回 0 。这与 C 语言的strstr()以及 Java 的indexOf()定义相符。

输入：haystack = "hello", needle = "ll"
输出：2

输入：haystack = "aaaaa", needle = "bba"
输出：-1

输入：haystack = "", needle = ""
输出：0
'''

'''
index()     查找子串substr第一次出现的位置，如果查找的子串不存在时，则抛出ValueError    
rindex()    查找子串substr最后一次出现的位置，如果查找的子串不存在时，则抛出ValueError    
find()      查找子串substr第一次出现的位置，如果查找的子串不存在时，则返回-1   
rfind()     查找子串substr最后一次出现的位置，如果查找的子串不存在时，则返回-1
'''

def strStr(haystack, needle):
    if needle:
        return haystack.find(needle)
    else:
        return 0

haystack = "hello"
needle = "el"
print(strStr(haystack,needle))