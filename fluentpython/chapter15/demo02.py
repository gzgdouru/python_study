'''
使用@contextmanager
'''
import sys
import contextlib


@contextlib.contextmanager
def looking_glass():
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write

    msg = ""
    try:
        yield "JABBERWOCKY"
    except ZeroDivisionError:
        msg = "please do not divide by zero!"
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)


if __name__ == "__main__":
    with looking_glass() as what:
        print("Alice, Kitty and Snowdrop")
        print(what)

    print(what)
    print("back to normal")
