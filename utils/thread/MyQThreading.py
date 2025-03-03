# MyQThreading.py 文件名
import asyncio
import time
from asyncio import AbstractEventLoop
from threading import Thread

from PyQt5.QtCore import QThread, pyqtSignal

class RunThread(QThread):

    counter_value = pyqtSignal(int)

    def __init__(self, target, args=None, name=""):
        QThread.__init__(self)
        self.target = target
        self.args = args
        self.is_running = True

    def run(self):
        #print("starting",self.name, "at:",ctime())
        if self.args:
            self.res = self.target(*self.args)
        else:
            self.res = self.target()

    def stop(self):
        # 负责停止线程
        self.terminate()
class async_RunThread(QThread):

    counter_value = pyqtSignal(int)

    def __init__(self, target, args=None, name=""):
        QThread.__init__(self)
        self.target = target
        self.args = args
        self.is_running = True
        self.loop = None


    def run(self):
        #print("starting",self.name, "at:",ctime())
        # asyncio.run(self.target())
        asyncio.create_task(self.target())
        # print(1111)
        # asyncio.set_event_loop(self.loop)

        # 运行异步任务
        try:
            self.loop = asyncio.get_event_loop()
        except Exception as e:
            self.loop = asyncio.new_event_loop()
            self.loop.run_in_executor(None,self.target())
        # self.loop.run_until_complete(self.target())
        # self.loop.close()

    async def stop(self):
        # 负责停止线程
        self.terminate()

class AsyncioThread(QThread):
    def __init__(self, loop: AbstractEventLoop):
        super().__init__()
        self._loop = loop
        self.daemon = True
    def run(self) -> None:
        self._loop.run_forever()

    def stop(self):
        # 负责停止线程
        self.terminate()

def _start_thread(self, a, b):
    print("*****运行打印*****")
    print(a,b)
    print("%s" % (time.strftime('<%H:%M:%S>', time.localtime())))
    print("*****运行打印*****")

if __name__ == "__main__":
    # 多线程的引用
    start_func = RunThread(target=_start_thread, args=(1, 2))
    # 多线程启动
    start_func.start()
    