#N장의 카드에 써져 있는 숫자가 주어졌을 때,
#M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오

from itertools import combinations
n, m = map(int, input().split())
nums = list(map(int, input().split()))
comb_list = list(combinations(nums, 3)) # 컴비네이션으로 nums 숫자들 중 3개 선택
result = 0

for a, b, c in comb_list: # comb_list에서 3개 선택
    r = a + b + c
    if r <= m and r > result: # 3개의 합이 m 보다 작고 result보다 크면
        result = r # 3개의 합을 result에 넣는다
print(result)