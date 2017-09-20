# coding=gbk
import threading, time
from threading import RLock, Lock, Condition, Event

count = 0

def print_hello(*args, **kwargs):
    print(args, kwargs)


class TimerCircle(threading.Timer):
    def run(self):
        while True:
            self.finished.wait(self.interval)
            # if not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            # self.finished.set()

t = TimerCircle(1, print_hello, 'hello')
t.start()

# t = threading.Timer(1, print_hello, 'hello')
# t.start()


class Counter(threading.Thread):

    def __init__(self, lock, threadName):
        super(Counter, self).__init__(name=threadName)
        self.lock = lock

    def run(self):
        global count
        self.lock.acquire()
        for _ in range(10000):
            count = count + 1
        self.lock.release()


lock = threading.Lock()
for i in range(5):
    Counter(lock, "thread-" + str(i)).start()

print(count)
time.sleep(10)

lock1 = threading.Lock()
def conter(*args):
    print(args)
    global count, lock1
    lock1.acquire()
    for _ in range(10000):
        count = count + 1
    lock1.release()
for i in range(5):
    t = threading.Thread(target=conter, name="thread-"+str(i), args=(1, 2))
    t.start()

"""
threading : �е�4����

t = threading.Lock()
t.acquire(blocking=True, timeout=-1)  ��ȡ����t���ͷ�ǰһֱ����
t.release()                           �ͷ�t


t = threading.RLock()
t.acquire(blocking=True, timeout=-1)    ��ȡ���ڵ�ǰ�߳��Ѿ���������������������������
t.release()                             �ͷ���
��ͬһ���߳��У�acquire��release������ͬ�����acquire����release����ǰ�߳�һ����ȡ���������߳��޷���ȡ����




threading.Event

t = threading.Condition()
t.acquire(*args)    ��ȡ�ײ���
t.release()         �ͷŵײ���
t.wait(timeout=None)  
�ȴ�֪ͨ��ֱ��������ʱ����������߳��ڵ��ô˷���ʱ��δ��ȡ�����������RuntimeError���÷����ͷŵײ�����Ȼ��������ֱ��������һ���߳��е���
ͬ����������notify������notify_all�������û��ѣ�����ֱ����ѡ�ĳ�ʱ������һ�����ѻ�ʱ���������»�ȡ���������ء�
t.wait_for()
t.notify(n=1)
Ĭ������£�����һ���̵߳ȴ��������������еĻ����� ��������߳��ڵ��ô˷���ʱ��δ��ȡ�����������RuntimeError��
�÷�����໽�ѵȴ������������߳�n��; ���û���߳����ڵȴ���������Ч�ġ�
���������n���߳����ڵȴ�����ǰ��ʵ�ֽ����û���n���̡߳� ���ǣ�����������Ϊ�ǲ���ȫ�ġ� δ�����Ż���ʵ�ֿ���ż���ỽ�ѳ���n���̡߳�
ע�⣺һ�����ѵ��߳�ʵ���ϲ������wait�������÷��أ�ֱ�����������»�ȡ������ ����notify�������ͷ������������Ӧ�á�

t.notify_all()
"""


