
import functools
import sched, time

s = sched.scheduler(time.time, time.sleep)

def setInterval(sec):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*argv, **kw):
            setInterval(sec)(func)
            func(*argv, **kw)

        s.enter(sec, 1, wrapper, ())
        return wrapper

    s.run()
    return decorator
