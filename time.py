import time
count_repeat=input("Введите число запусков: ")
def time_this(num_runs):
    def time_wrap(func):
        def func_wrapper():
            #num_runs=10
            avg_time = 0
            for _ in range(num_runs):
                t0 = time.time()
                func()
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= num_runs
            return "Выполнение заняло %.5f секунд" % avg_time
        return func_wrapper
    return time_wrap

@time_this(int(count_repeat))
def f():
    for j in range(1000000):
        pass
print(f())