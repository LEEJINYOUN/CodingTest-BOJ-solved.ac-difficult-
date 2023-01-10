#“a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다”
#아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

t = int(input())
for _ in range(t):
    a = int(input())
    b = int(input())
    man = [i for i in range(1, b + 1)]  # 0층의 1부터 b호까지 사람 수
    
    for x in range(a):
        for y in range(1, b):
            man[y] += man[y - 1] #man의 y 인덱스는 y - 1 인덱스를 더한 값
    print(man[-1])