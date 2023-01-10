#달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.
#달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다.
#또, 정상에 올라간 후에는 미끄러지지 않는다.
#달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

import sys
import math
a, b, v = map(int, sys.stdin.readline().split())
# (a - b)를 day만큼 반복하고, 정상에 올라간 후는 미끄러지지않기때문에 마지막날은 a만큼만 더한다 
day = (v - a) / (a - b) #(a - b) * day + a = v 를 전개
print(math.ceil(day) + 1)