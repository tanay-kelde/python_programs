# Using time module #
import time

start = time.time()

print(23*2.3)

end = time.time()
print(end - start)


# Using timeit module #
from timeit import default_timer as timer

start = timer()

print(23*2.3)

end = timer()
print(end - start)