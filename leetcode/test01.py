def plusOne(self, digits: List[int]) -> List[int]:
    return list(map(int, list(str(int(''.join(map(str, digits))) + 1))))
# 写一个加法函数，将列表转换为字符串，再转换为整数，加1后再转换为字符串，再转换为列表

plusOne([1, 2, 3])
