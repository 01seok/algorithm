def solution(bandage, health, attacks):


    heal_time, sec_heal,bonus_heal = bandage[0], bandage[1], bandage[2] # 붕대 감기 성능
    cur_health = health # 현재 체력 최대 체력으로 초기화
    cur_attack_time = 0 # 공격 시간 0으로 초기화

    for attack_time, damage in attacks:

        time_gap = attack_time - cur_attack_time - 1

        heal_amount = sec_heal * time_gap
        bonus_heal_cnt = time_gap // heal_time
        heal_amount += bonus_heal_cnt * bonus_heal

        cur_health += heal_amount
        if cur_health > health:
            cur_health = health


        cur_health -= damage

        if cur_health <= 0:
            return -1

        cur_attack_time = attack_time

    return cur_health