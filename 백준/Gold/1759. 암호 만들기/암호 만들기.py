import sys

def find_password(cur_len, start_idx, cur_password):
    
    # L개 카드 다 뽑았으면 이 조합이 가능한 조합인지 확인
    if cur_len == L:
        vowel_cnt = 0   #모음 개수
        con_cnt = 0 # 자음 개수
        
        for char in cur_password:
            if char in vowels:
                vowel_cnt += 1
            else:
                con_cnt += 1
        
        if vowel_cnt >= 1 and con_cnt >= 2:
            print("".join(cur_password))
        return
    
    # L개 카드 다 못뽑았으면 카드 뽑으러
    for i in range(start_idx, C):
        cur_password.append(chars[i])
        # 한 장 뽑았으니 카드 길이 + 1, 오름차순해야하니 현재 뽑은 카드보다 한 칸 더가서 뽑기
        find_password(cur_len+1, i+1, cur_password)
        # 다음 조합 만들기위해 방금 뽑았던 카드 다시 돌려놓기 (백트래킹, 위에 함수가 길이 L될 때까지 재귀로 돌거니까)
        cur_password.pop()

L, C = map(int, sys.stdin.readline().split())
chars = sorted(sys.stdin.readline().split())
vowels = "aeiou"

find_password(0,0,[])