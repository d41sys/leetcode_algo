class Solution:
    def customSortString(self, order: str, s: str) -> str:
        common = [w for w in s if w in set(order)]
        notcommon = [w for w in s if w not in set(order)]
        return ''.join(sorted(common, key=lambda x: order.index(x)) + list(notcommon))