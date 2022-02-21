#创建线程需要使用到thread的模块
from threading import Thread
'''方案一'''
# def func():
#     for i in range(1,1000):
#         print("子线程",i)
#
# if __name__ == '__main__':
#     t=Thread(target=func);
#     t.start();
#
#     for i in range(1,1000):
#         print("主线程",i)

'''方案二：接口回调'''

# class MyThread(Thread):
#     def run(self):
#         for i in range(1, 1000):
#              print("子线程",i)
#
# if __name__ == '__main__':
#     t=MyThread();
#     t.start();
#
#     for i in range(1, 1000):
#         print('主线程',i)

'''线程池：一次开辟一批的线程，我们用户直接给线程池子提交任务，任务的调度由线程池来完成'''

from concurrent.futures import ThreadPoolExecutor;
# class MyThread(Thread):
#     def __init__(self,name):
#         self._name=name
#     def run(self):
#         for i in range(1000):
#             print(self._name,i);
def fn(name):
    for i in range(1000):
        print(name,i)
if __name__ == '__main__':
    #创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(fn,name=f'name{i}')



