import random
import time
def coinRoll(mind,coin,hapDamage):#코인 돌리기
    gunHap = 0
    for i in range(coin): 
        random_num = random.randint(1,100)
        if random_num <= 50 + mind: # 기본확률50% + 정신력 ㅇ
            gunHap += hapDamage
            print("O",end='')
        else:
            print("0",end='')
    return gunHap
print("""
 _      _             _                         _        
| |    (_)           | |                       (_)       
| |     _  _ __ ___  | |__   _   _  _ __   ___  _  _ __  
| |    | || '_ ` _ \ | '_ \ | | | || '_ \ / __|| || '_ \ 
| |____| || | | | | || |_) || |_| || | | |\__ \| || | | |
\_____/|_||_| |_| |_||_.__/  \__,_||_| |_||___/|_||_| |_|
                                                                               
""")
while True:
    print("""
        1.게임시작
        2.게임설명
        3.나가기""")
    start = int(input())
    if start == 1:
        break
    elif start == 2:
        print("""ㅖ 림버스랑 비슷합니다 일단 적이 먼저 데미지를 보여줍니다.
            자신이 가진 스킬중 그거에 대항할 만한 것을 선택하여 합을 진행합니다.
            이기면 합 횟수만큼 정신력 증가합니다. 지면 적 정신력이 증가합니다.
              0이게 뒷면이고 O이게 앞면입니다.""")
    elif start == 3:
        exit()
#Player
PlayerHp = 50
mind = 0 # 정신력
#enemy
EnemyHp = 50
EnemyMind = 0
#PlayerSkill
while True:
    if PlayerHp < 1:
        print("패배")
        exit()
    elif EnemyHp < 1:
        print("승리")
        exit()
    hapCnt = 0
    print("""
          Player현재 체력:%d
          현재 정신력:%d
          enemy 체력:%d
          현재 정신력:%d
          """%(PlayerHp,mind,EnemyHp,EnemyMind))
    first = True
    EnemyRandom = random.randint(1,2)
    if EnemyRandom == 1:
        EnemyHapDamage = 3 
        EnemyCoin = 2
        BaseEnemyDamage = 5
    else:
        EnemyHapDamage = 2
        EnemyCoin = 4
        BaseEnemyDamage = 5
    if PlayerHp < 1:
        break
    EnemyDamage = BaseEnemyDamage + coinRoll(EnemyMind,EnemyCoin,EnemyHapDamage)
    print(" EnemyDamage:%d"%EnemyDamage)
    print("""
          1 스킬 합공격력:5 코인:2 기본뎀:5
          2 스킬 합공격력:3 코인:4 기본뎀:4
          3 스킬 합공격력:-3 코인:3 기본뎀:15
          """)
    a = int(input())
    if a == 1:#최대 11
        hapDamage = 3 
        coin = 2
        BaseDamage = 5
    elif a == 2:
        hapDamage = 3
        coin = 4
        BaseDamage = 4
    elif a == 3:
        hapDamage = -3
        coin = 3
        BaseDamage = 15
    while True:
        if not first:#처음 보여준 값과 동일한 값을 유지하기 위해?
            EnemyDamage = BaseEnemyDamage + coinRoll(EnemyMind,EnemyCoin,EnemyHapDamage)
            print(" EnemyDamage:%d"%EnemyDamage)
        if coin < 1 :
            PlayerHp -= EnemyDamage
            print("아프다! 남은체력:%d"%PlayerHp)
            EnemyMind += hapCnt
            break
        elif EnemyCoin < 1:
            EnemyHp -= Damage
            print("꼴좋다 남은적 체력:%d"%EnemyHp)
            mind += hapCnt
            time.sleep(1)
            break
        Damage = BaseDamage + coinRoll(mind,coin,hapDamage)
        #초기화를 안해서 코인을 돌릴때 마다 값이 중첩되는 문제 해결
        print("나의 코인값 Damage:%d"%Damage)
        if EnemyDamage > Damage:
            print("Player패배")
            coin -= 1
            hapCnt+=1
            first = False
            
        elif EnemyDamage < Damage:
            print("enemy패배")
            EnemyCoin -= 1
            hapCnt+=1
            first = False
            
        elif EnemyDamage == Damage:
            print("다시")
            hapCnt+=1
            first = False
        
        time.sleep(2)
        print("------------------------")
