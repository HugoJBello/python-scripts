
#https://quentin.pradet.me/blog/javascript-promises-are-equivalent-to-pythons-asyncio.html
#https://stackoverflow.com/questions/43325501/how-do-i-write-a-sequence-of-promises-in-python
#https://www.blog.pythonlibrary.org/2016/07/26/python-3-an-intro-to-asyncio/
import asyncio
import logging
logging.basicConfig(level=logging.INFO)

async def some_coroutine():
    await asyncio.sleep(1)
    await asyncio.sleep(0.01)
    print("we are in tcouroutine 1 ")
    try:
        await some_coroutine_handler("blabla")
    except:
        print("hoooo")
    return await some_coroutine_handler("blabla")

async def some_coroutine_handler(input):
    await asyncio.sleep(1)
    result = "this is from coroutine 1 " + input
    print(result)
    return result


loop = asyncio.get_event_loop()
task1 = loop.create_task(some_coroutine())


loop.run_until_complete(asyncio.wait([task1]))

print("aaa")