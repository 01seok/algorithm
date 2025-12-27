import sys

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0 , -1, 1]



N = int(input())

# 교실 격자 초기화
classroom = [[0] * N for _ in range(N)]

# 학생들이 좋아하는 학생들을 저장할 딕셔너리
students = {}

# 순서대로 자리 배치하기 위해 입력 순서 기록할 리스트
order = []

# 학생 정보 입력
for _ in range(N * N):
    line = list(map(int, input().split()))
    student_id = line[0]
    likes = line[1:]
    students[student_id] = likes
    order.append(student_id)
    
# 학생 배치 시작
for student in order:
    
    # 해당 학생의 최적의 자리와 좋아하는 학생 수, 주변 빈칸 수 초기화
    best_seat = None
    max_like = -1
    max_empty = -1
    
    # 교실 모든 칸 순회
    for r in range(N):
        for c in range(N):
            if classroom[r][c] != 0:
                continue
            
            # 현재 자리에서 인접 4방향 탐색
            cur_like = 0
            cur_empty = 0
            
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                
                if 0 <= nr < N and 0 <= nc < N:
                    
                    # 인접 칸에 좋아하는 학생과 빈 칸 인지 확인
                    if classroom[nr][nc] in students[student]:
                        cur_like += 1
                        
                    if classroom[nr][nc] == 0:
                        cur_empty += 1
                        
            # 규칙 적용 및 비교
            # 1번 규칙 : 좋아하는 학생 수 더 많으면 갱신
            if cur_like > max_like:
                max_like = cur_like
                max_empty = cur_empty
                best_seat = (r,c)
                
            # 2번 규칙 : 좋아하는 학생 수 같으면, 빈칸 더 많은 경우 갱신
            elif cur_like == max_like and cur_empty > max_empty:
                max_empty = cur_empty
                best_seat = (r,c)
                
        
    if best_seat:
        classroom[best_seat[0]][best_seat[1]] = student
            
# 만족도 계산
total_point = 0

for r in range(N):
    for c in range(N):
        student = classroom[r][c]
        like_cnt = 0
        
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if classroom[nr][nc] in students[student]:
                    like_cnt += 1
        
        if like_cnt > 0:
            total_point += 10 ** (like_cnt - 1)
        
print(total_point)