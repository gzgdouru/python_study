'''
python多进程使用
'''
import multiprocessing
import time

def get_html(n):
    time.sleep(n)
    print("get html {}.html success.".format(n))
    return "get {0}.html compalte!".format(n)

def show(arg):
    print(arg)

if __name__ == "__main__":
    # process = multiprocessing.Process(target=get_html, args=(10,))
    # process.start()
    # print(process.pid)
    # process.join()

    # pool = multiprocessing.Pool(4)
    # for i in range(10):
    #     pool.apply_async(func=get_html, args=(2,), callback=show)
    #
    # pool.close()
    # pool.join()

    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # for result in pool.imap(get_html, [1, 5, 3]):
    #     print("{} sleep success".format(result))

    for result in pool.imap_unordered(get_html, [1, 5, 3]):
        print("{} sleep success".format(result))

