from collections import deque
a = int(input())
b = deque([i for i in range(1, a + 1)])
while len(b) > 1:

    b.popleft()
    b.append(b.popleft())
    
print(b[0])