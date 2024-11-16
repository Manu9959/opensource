N = int(input())
A = list(map(int, input().split()))

left_sum = [0] * N
right_sum = [0] * N
current_left_sum = 0
for i in range(N):
    left_sum[i] = current_left_sum
    current_left_sum += A[i]
current_right_sum = 0
for i in range(N - 1, -1, -1):
    right_sum[i] = current_right_sum
    current_right_sum += A[i]
B = [abs(left_sum[i] - right_sum[i])for i in range(N)]
print(" ".join(map(str, B)))
