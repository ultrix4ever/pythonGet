n = int(input())
lessons = []
for _ in range(n):
    m = int(input())
    lesson = {input() for _ in range(m)}
    lessons.append(lesson)
common = set.intersection(*lessons)
for student in sorted(common):
    print(student)
    
            
        