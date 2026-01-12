def solution(phone_book):
    
    # 모든 전화번호 딕셔너리에 넣기
    # key : phone number, value : 1
    hash = {}
    
    # 전화번호부 순회하면서 있는 것들 1로 체크해두기
    for phone_num in phone_book:
        hash[phone_num] = 1
    
    for phone_num in phone_book:
        
        # 이번 번호가 있는지 체크하기 위해 사용할 임시 문자열
        temp_num = ""
        
        for num in phone_num:
            temp_num += num
            
            # hash에 있는지 확인하되 자기 자신은 제외
            if temp_num in hash and temp_num != phone_num:
                return False
    
    return True
