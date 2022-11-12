import threadpool
import asyncio
import time


async def do_work_one(name):
    """
    定义一个协程对象
    :return:
    """
    time.sleep(0.5)
    print(name, 'do_work_one',"\n")


async def do_work_two(name):
    """
    定义一个协程对象
    :return:
    """
    time.sleep(0.5)
    print(name, 'do_work_two',"\n")


def task_do_work(name):
    """
    1、每一个线程里面会有多个协程对象
    2、协程的运行是由顺序的，只是在IO交互的时候，不用等待IO交互完成
    3、多线程中使用协程的时候必须新建loop对象
    :return:
    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    coroutine1 = do_work_one(name)
    coroutine2 = do_work_two(name)

    tasks = [asyncio.ensure_future(coroutine1), asyncio.ensure_future(coroutine2)]
    loop.run_until_complete(asyncio.wait(tasks))
    return 'success'


def call_back(param, result):
    #print('回调', param, result)
    pass


if __name__ == '__main__':
    jobs = []
    pool = threadpool.ThreadPool(10)
    work_requests = []
    for i in range(1000):
        work_requests.append(threadpool.WorkRequest(task_do_work, args=('线程:{0}'.format(i), ), callback=call_back, exc_callback=call_back))
    [pool.putRequest(req) for req in work_requests]
    pool.wait()
    print('end')
