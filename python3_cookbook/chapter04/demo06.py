'''
带有外部状态的生成器函数
'''
from collections import deque


class LineHistory:
    def __init__(self, lines, maxlen=3):
        self._lines = lines
        self._history = deque(maxlen=maxlen)

    def __iter__(self):
        for lineno, line in enumerate(self._lines, 1):
            self._history.append((lineno, line))
            yield line

    def clear(self):
        self._history.clear()


if __name__ == "__main__":
    with open("demo05.py", "r", encoding="utf-8") as f:
        lines = LineHistory(f)
        for line in lines:
            if "name" in line:
                for lineno, line in lines._history:
                    print(f"{lineno}:{line}")

