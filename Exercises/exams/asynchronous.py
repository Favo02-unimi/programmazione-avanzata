from threading import Thread

class NotYetDoneException(Exception):
    def __init__(self, message):
        self.message = message

class asynchronous:
    def __init__(self, f):
        self.f = f

    def start(self, n):

        def wrapped_f():
            self.result = self.f(n)

        self.thread = Thread(target=wrapped_f)
        self.thread.start()
        return self

    def is_done(self):
        return not self.thread.is_alive()

    def get_result(self):
        if not self.is_done():
            raise NotYetDoneException("the call has not yet completed its task")
        return self.result

if __name__ == '__main__':
    import time

    @asynchronous
    def long_process(num):
        time.sleep(10)
        return num * num

    result = long_process.start(12)

    for i in range(20):
        time.sleep(1)

        if result.is_done():
            print("[{1}]: result {0}".format(result.get_result(), i))
        else: print("[{0}]: not ready yet".format(i))

    result2 = long_process.start(13)

    try:
        print("result2 {0}".format(result2.get_result()))
    except NotYetDoneException as ex:
        print(ex.message)
