'''
ThreadPoolExecutor线程池使用
'''
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
import time

def get_html(values):
    name, times = values
    time.sleep(times)
    if times == 7:
        raise RuntimeError("{0} run error!".format(name))
    print("线程:{0}get page {1} success".format(name, times))
    return name, times

if __name__ == "__main__":
    #使用submit提交
    with ThreadPoolExecutor(max_workers=3) as executor:
        tasks = []
        for sleep_time in [3, 7, 5]:
            name = "get_html_{}".format(sleep_time)
            task = executor.submit(get_html, (name, sleep_time))
            tasks.append(task)

        # for future in tasks:
        #     name, times = future.result()
        #     print("{0} 完成, 结果:{1}".format(name, times))

        # for future in as_completed(tasks):
        #     exception = future.exception()
        #     if exception:
        #         print(exception)
        #     else:
        #         name, times = future.result()
        #         print("{0} 完成, 结果:{1}".format(name, times))

        for future in wait(tasks).done:
            exception = future.exception()
            if exception:
                print(exception)
            else:
                name, times = future.result()
                print("{0} 完成, 结果:{1}".format(name, times))

    #使用map提交
    # with ThreadPoolExecutor(max_workers=3) as executor:
    #     args = []
    #     for sleep_time in [3, 7, 5]:
    #         name = "get_html_{}".format(sleep_time)
    #         times = sleep_time
    #         args.append((name, times))
    #     for result in executor.map(get_html, args):
    #         print(result)
