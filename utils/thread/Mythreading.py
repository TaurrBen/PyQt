# Mythreading.py 文件名
import time

from PyQt5.QtCore import QThread, pyqtSignal

class RunThread(QThread):

    counter_value = pyqtSignal(int)

    def __init__(self, target, args, name=""):
        QThread.__init__(self)
        self.target = target
        self.args = args
        self.is_running = True

    def run(self):
        #print("starting",self.name, "at:",ctime())
        self.res = self.target(*self.args)

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
    