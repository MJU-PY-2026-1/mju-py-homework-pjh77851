# 파일이름 :
# 작 성 자 : 박준형

"""#1 성과 입력
planets_destroyed = int(input("💥파괴한 소행성 개수: "))
humans_captured = int(input("👤생포한 지구인 수: "))

#2 기본 수당 및 공제 계산
base_pay = 500
gross_pay = base_pay + (planets_destroyed*2000) + (humans_captured*500)
total_deductions = 300 + 1200 + 400 # 산소비+ 리스비 + 보험료
net_pay = gross_pay - total_deductions

#3 등급 판정
if net_pay >= 5000:
    rank = "S"  #은하계 금수저
elif net_pay >=3000:
    rank = "A"  #은하계 은수저
elif net_pay >=0:
    rank = "B"  #평범한 약탈자
else:
    rank = "F"  #산소 도둑

#4 값에 따른 보상,형벌
match rank:
    case"S":
        company_action = "회장님 전용 스카이라운지 이용권 지급"
    case"A":
        company_action = "우주선 무료세차 및 산소 리필 쿠폰 증정"
    case"B":
        company_action = "인사팀 면담 면제(생존 확인됨)"
    case"F":
        company_action = "즉시 연료탱크 청소및 산소 공급 50% 제한"
    case _:
        company_action = "보안팀 출동: 정체 불명의 생명체 발견"

print(f' 실수령액: {net_pay}크레딧')
print(f' 최종등급: [{rank}]')
print(f' 회사조치: {company_action}")"""




import time
# (전역 변수 설정) - 프로그램 전체에서 유지되는 사원 데이터
employee = '없음'
employee_net_pay = 0
employee_action = '데이터 없음'
total_years_served = 0

def input_performance():
    print('💥[실적입력] 이번 달 당신이 저지른 악행을 보고하십시오.')
    planets = int(input('파괴한 소행성 개수: '))    
    humans = int(input('생포한 지구인 수: '))

    base_pay = 500
    gross_pay = base_pay + (planets*2000) + (humans*500)
    deductions = 300 + 1200 + 400 #산소비 + 리스비 + 보험료
    net_pay = gross_pay - deductions
    return net_pay

def evaluate_rank(net_pay):
    global employee_rank, employee_net_pay, employee_action
    employee_net_pay = net_pay

    #등급판정
    if net_pay >= 5000:
        employee_rank = 'S' # 은하계 금수저
    elif net_pay >= 3000:
        employee_rank = 'A' # 은하계 은수저
    elif net_pay >= 0:
        employee_rank = 'B' # 평범한 약탈자
    else:
        employee_rank = 'F' # 산소 도둑
    #회사 조치
    match employee_rank:
        case'S':
            employee_action = '회장님 전용 스카이라운지 이용권 지급'
        case'A':
            employee_action = '우주선 무료세차 및 산소 리필 쿠폰증정'
        case'B':
            employee_action = '인사팀 면담 면제(생존 확인됨)'
        case'F':
            employee_action = '즉시 연료탱크 청소 및 산고 공급 50% 제한'
        case _:
            employee_action = '보안팀 출동: 정체 불명의 생명체 발견'
    print('등급 심사가 완료되었습니다. 명세서 조회 메뉴에서 확인하세요.')

def display_salary_statement():
    print('\n' + '='*45)
    print('🛸우주 정복 주식회사 월간급여 명세서🛸')
    print('='*45)
    print(f'💰실수령액: {employee_net_pay}크레딧')
    print(f'🎖️최종등급: {employee_rank}')
    print(f'📢회사조치: {employee_action}')
    print('='*45)

def analyze_career():
    global total_years_saved
    total_years_saved += 1
    print('[은하계 인사 분석 시스템]')
    print(f'-> 당신은 본사에서 현재 [{total_years_saved}년째] 착취당하는 중입니다.')

    if employee_rank == 'F':
        print('⚠️경고: 현재 산소 부족상태로 다음 달 생존 확률이 42%입니다.')
    elif employee_rank == 'S':
        print('🎉분석: 임원진들이 당신의 우주선을 호시탐탐 노리고 있습니다.')
    else:
        print('👀 분석: 가늘고 길게 살아남는 중입니다. 노예로서 백점 만점!')
print('🛸 [우주 정복 주식회사] 인트라넷 시스템 가동🛸')

while True:
    print('\n' + '='*40)
    print(' 1. 실적 입력(노동)')
    print(' 2. 명세서 조회(확인)')
    print(' 3. 은하계 분석(미래)')
    print(' 4. 프로그램 종료(퇴사)')
    print('='*40)

    menu = input('원하시는 번호를 입력하세요: ')

    if menu == '1':
        pay_result = input_performance()
        evaluate_rank(pay_result)
    elif menu == '2':
        display_salary_statement()
    elif menu == '3':
        analyze_career()
    elif menu == '4':
        print('🚨[경고] 퇴사는 계약서 제 404조에 의거해 불가능합니다........')
        print("🤖AI 보안관:'농담입니다 휴먼. 탈출을 축하합니다.'")
        print('시스템을 종료합니다. 후다닥💨')
        break
    else:
        print('잘못된 입력입니다. 광선총 맞기 전에 똑바로 입력하십시오.')
        time.sleep(1)


import time
blacklist = []
def load_blacklist():
    print('\n💾 [인사팀 서버] 살생부를 본사 메인 서버에 동기화(저장)합니다...')
    try:
        with open('blacklist.txt','r',encoding = 'utf-8') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 3:
                    blacklist.append([data[0], data[1], int(data[2])])
        print("✅ 반역자 명단을 성공적으로 확보했습니다. 사냥을 시작하죠!")
    except FileNotFoundError:
        print("⚠️ [보안 경고] 누군가 살생부 기록을 해킹해 삭제했습니다! 빈 문서로 새로 시작합니다.")

def add_traitor():
    print('\n☠️ [살생부 등록] 회사를 배신한 자의 정보를 입력하십시오.')
    name = input('반역자 이름: ')
    reason = input('배신 죄목 (예: 산소 횡령, 광선총 탈취): ')
    try:
        bounty = int(input('현상금 (크레딧):'))
    except ValueError:
        print('⚠️ [인사팀 경고] 이봐요! 현상금은 크레딧(숫자)으로만 걸 수 있습니다!')
        print('👉 기본 현상금(100 크레딧)으로 강제 등록됩니다.')
        bounty = 100
    blacklist.append([name, reason, bounty])
    print(f"\n🚨 [{name}] 요원이 1급 수배자 명단에 올랐습니다! (현상금: {bounty}크레딧)")

def display_wanted_poster():
    print('\n' + '🔥'*20)
    print(' ☠️ 우주 정복 주식회사 1급 현상수배 전단 ☠️')
    print('🔥'*20)

    if not blacklist:
        print("현재 수배된 반역자가 없습니다. 평화로운(착취하기 좋은) 은하계네요!")
        print('='*40)
        return

    printprint(f"{'악당 이름':<10} | {'배신 죄목':<15} | {'현상금(크레딧)':<10}")
    print('-'*45)

    for traitor in blacklist:
        for i,item in enumerate(traitor):
            if i < len(traitor) - 1:
                print(f"{str(item):<12}", end=" | ")
            else:
                print(f"{str(item):<10}")
    print('-'*45)

def save_blacklist():
    print('\n💾 [인사팀 서버] 살생부를 본사 메인 서버에 동기화(저장)합니다...')
    try:
        with open('blacklist.txt','w',encoding='utf-8') as file:
            for traitor in blacklist:
                file.write(f"{traitor[0]},{traitor[1]},{traitor[2]}\n")
        print("✅ 살생부 백업 완료! (이제 우주 끝까지 도망쳐도 소용없습니다.)")
    except Exception as e:
        print(f"⚠️ 저장 중 알 수 없는 시스템 오류가 발생했습니다: {e}")
print('🛸 [우주 정복 주식회사] 인사팀 비밀 인트라넷 접속 🛸')
load_blacklist() 

while True:
    print('\n' + '='*40)
    print(' 1. 새로운 반역자 등록 (살생부 추가)')
    print(' 2. 현상수배 전단지 확인 (명단 조회)')
    print(' 3. 살생부 서버 수동 백업 (파일 저장)')
    print(' 4. 시스템 로그아웃 (종료)')
    print('='*40)

    menu = input('원하시는 업무 번호를 입력하세요: ')

    if menu == '1':
        add_traitor()
    elif menu == '2':
        display_wanted_poster()
    elif menu == '3':
        save_blacklist()
    elif menu == '4':
        print('\n🚨 [보안 시스템] 로그아웃 절차를 진행합니다.')
        save_blacklist() # 종료 전 안전하게 자동 저장
        print("🤖 AI 보안관: '오늘도 훌륭한 숙청이었습니다. 보안 유지하십시오.'")
        print('시스템을 완전히 종료합니다. 삐빅- 💨')
        break
    else:
        print('\n접근 권한이 없거나 잘못된 입력입니다. 광선총 맞기 전에 다시 누르십시오.')
        time.sleep(1)
