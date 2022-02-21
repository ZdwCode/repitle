#协程就类似与一个批处理操作系统
import asyncio

# #加了async之后函数就变成了一个异步协程函数  调用的话返回的是一个异步协程对象<coroutine object func at 0x000001F2B9DC5548>
# #asyncio.run() 传入一个协程对象
# async def func():
#     print("你好，我叫赛利亚")
#
# if __name__ == '__main__':
#     asyncio.run(func())#



# import time
# async def func1():
#     print('hello,i am huang');
#     await asyncio.sleep(2) #await 挂起并保存上下文
#     print('hello,i am huang');
#
#
# async def func2():
#     print('hello,i am zhang');
#     await asyncio.sleep(3)
#     print('hello,i am zhang');
#
#
# async def func3():
#     print('hello,i am luo');
#     await asyncio.sleep(4)
#     print('hello,i am luo');
#
# if __name__ == '__main__':
#     f1=func1();
#     f2=func2();
#     f3=func3();
#     tasks=[
#         f1,f2,f3
#     ]
#
#     t1=time.time();
#     #一次性启动多个任务
#     asyncio.run(asyncio.wait(tasks))
#     t2=time.time();
#     print(t2-t1);

import time
async def func1():
    print('hello,i am huang');
    await asyncio.sleep(2) #await 挂起并保存上下文
    print('hello,i am huang');


async def func2():
    print('hello,i am zhang');
    await asyncio.sleep(3)
    print('hello,i am zhang');


async def func3():
    print('hello,i am luo');
    await asyncio.sleep(4)
    print('hello,i am luo');

async def main():
    f1=func1();
    f2=func2();
    f3=func3();
    tasks=[
        f1,f2,f3
    ]
    #???
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())