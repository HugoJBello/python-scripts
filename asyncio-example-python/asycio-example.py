
#https://quentin.pradet.me/blog/javascript-promises-are-equivalent-to-pythons-asyncio.html
#https://stackoverflow.com/questions/43325501/how-do-i-write-a-sequence-of-promises-in-python
#https://www.blog.pythonlibrary.org/2016/07/26/python-3-an-intro-to-asyncio/
import asyncio


async def some_coroutine1():
    await asyncio.sleep(1)
    await asyncio.sleep(0.01)        
    return 'done1'
async def some_coroutine2():
    await asyncio.sleep(1)
    return 'done2'

def process_result(future):
    print('Task returned:', future.result())


loop = asyncio.get_event_loop()
task1 = loop.create_task(some_coroutine1())
task1.add_done_callback(process_result)

task2 = loop.create_task(some_coroutine2())
task2.add_done_callback(process_result)
loop.run_until_complete(asyncio.wait([task1,task2]))

print("aaa")