import random
def loop(prisoner_num):
    count = 1
    current_value = boxes[prisoner_num - 1]
    
    while current_value != prisoner_num:
        current_value = boxes[current_value - 1]
        count += 1
    return count
l=10000
wr=0.0
for xi in range(l):
    s = list(random.sample(range(1,101),100)) #[17, 15, 26, 81, 97, 48, 64, 67, 74, 98, 87, 36, 31, 45, 82, 94, 39, 65, 33, 75, 4, 56, 54, 22, 72, 70, 59, 38, 14, 7, 73, 3, 28, 58, 79, 57, 62, 20, 2, 37, 46, 84, 40, 27, 76, 21, 89, 60, 32, 93, 41, 83, 66, 47, 34, 44, 90, 88, 16, 1, 85, 23, 6, 42, 5, 78, 18, 19, 61, 11, 55, 68, 80, 51, 49, 35, 10, 9, 25, 30, 77, 69, 92, 100, 95, 99, 29, 12, 53, 96, 63, 71, 91, 86, 50, 43, 13, 52, 8, 24]
    boxes = s 

    s_count = 0
    for p in range(1, 101):
        if loop(p) <= 50:
            s_count += 1
    if s_count == 100:
        wr+=1.0

prs=wr/l

print(f"persentasi {prs: .1%}")

