# https://leetcode.com/problems/defuse-the-bomb/

def decrypt(code: list[int], k: int) -> list[int]:
        lc = len(code)
        new_code = [0] * lc
        if k > 0:
            for i in range(lc):
                for j in range(1, k + 1):
                    new_code[i] += code[(i + j) % lc]
        elif k < 0:
            for i in range(lc):
                for j in range(1, -k + 1):
                    new_code[i] += code[(i - j) % lc]
        return new_code
