'''
上下文管理器和with块
'''
import sys


class LookingGlass:
    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return "JABBERWOCKY"

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print("please Do not divide by zero!")
            return True

if __name__ == "__main__":
    with LookingGlass() as what:
        print("Alice, Kitty and Snowdrop")
        print(what)

    print(what)
    print("back to normal")
