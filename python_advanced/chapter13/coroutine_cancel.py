import asyncio
import time

async def get_html(sleep_times):
    print("wating {0} times".format(sleep_times))
    await asyncio.sleep(sleep_times)
    print("done after {}s".format(sleep_times))

if __name__ == "__main__":
    task_1 = get_html(3)
    task_2 = get_html(2)
    task_3 = get_html(4)
    tasks = [task_1, task_2, task_3]
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:
        all_task = asyncio.Task.all_tasks()
        for task in all_task:
            print("cancel task")
            print(task.cancel())
        loop.stop()
        loop.run_forever()
    finally:
        loop.close()