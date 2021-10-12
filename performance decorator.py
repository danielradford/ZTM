# Performance decorator.
# Demonstration of how to impiment the decorator pattern.
# The decorator pattern allows one to modify the behaviour of a function.


from time import time
def performance(fn):
  def wrapper(*args, **kwargs):
    t1 = time()
    result = fn(*args, **kwargs)
    t2 = time()
    print(f'took {t2-t1}')
    return result
  return wrapper

@performance
def long_time():
    for i in range(10000):
        i*5

long_time()
