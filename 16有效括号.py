"""
给定一个只包括'(',‘)','{',‘}’,'[',']’的字符串s,判断字符串是否有效。
有效字符串需满足:
1.左括号必须用相同类型的右括号闭合。
2.左括号必须以正确的顺序闭合。
3. 每个右括号都有一个对应的相同类型的左括号。
示例1:
输入:s="()"
输出:true

示例2:
输入:s = "()[]{}"
输出:true
"""
def solution(s: str) -> bool:
    mat = []
    match = {")":"(","}":"{","]":"["}
    for i in s:
        if i in ["(","{","["]:
            mat.append(i)
        else:
            if not mat:
                return False
            if mat[-1] == match[i]:
                mat.pop()
            else:
                return False
    return len(mat)==0
print(solution("({{}})"))