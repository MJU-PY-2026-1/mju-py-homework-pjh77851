[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/MiVO5zfB)
# 🐍 [2026-01] 나만의 파이썬 소프트웨어 개발 프로젝트

## 1. 시나리오 제목
*우주 정복 주식회사 요원의 급여를 관리하는 시스템
<br>


## 2. 시나리오 (5~10줄)
* (이곳에 한 학기 동안 개발할 프로그램의 전체 시나리오를 개괄적으로 요약합니다.)
* 우주 정복 주식회사 요원의 급여를 관리하는 시스템입니다.
* 당신은 은하계에서 가장 악명 높은 **우주 정복 주식회사** 에 갓 입사한 신입 침공 요원입니다. 면접 당시 "지구라는 행성은 기후도 적당하고 생명체들도 연약해서 정복하기 딱 좋다"는 인사 담당자의 말에 속사 50광년을 날아왔죠. 하지만 현실은 냉혹했습니다. 출근 첫날 받은 개인용 우주선은 할부금이 빽빽하게 적힌 리스 차량이였고, 선배 요원들은 "지구의 중력은 생각보다 끈질기니 관절염을 조심하라"는 조언만 남긴채 퇴근해버렸습니다. 이 회사의 급여 체계는 철저한 **성과 중심적 약탈제** 입니다. 기본급은 우주 편의점 알바보다 적지만, 행성을 파괴하거나 희귀한 지구인을 생포해 오면 어마어마한 수당이 붙습니다. 하지만 조심해야 합니다. 회사는 당신이 마시는 산소 한 모금, 우주선에 채우는 연료 한 방울까지 전부 월급에서 공제하는 지독한 블랙 기업이니까요. 심지어 우주 미아가 될 경우를 대비한 보험료까지 강제로 징수합니다. 오늘은 당신의 첫 월급날입니다. 과연 당신은 지구를 탈탈 털어 우주 부자가 되었을까요, 아니면 산소값도 못내서 우주선 연료 탱크나 닦는 신세로 전락했을까요? 자, 이제 당신의 파괴적인 성과를 입력할 시간입니다!
<br>


## 3. 예상 기능 및 메뉴 (최소 5개)
(예시)
1. 신규 급여 명세서 생성
2. 이달의 침공 실적 조회(평균 급여, 파괴행성 수, 지구인 생포)
3. 공제 항목(산소 할부금, 연료비, 우주미아 보험)
4. 요원 등급 판정
5. 시스템 로그아웃

<br>

# 🚀 [버전별 개발 일지 & AI 협업 기록]

## 🟦 [1차 과제: V1.0] 시나리오 기획
    
### **🤖 AI 파트너십 과정**
(예시)
 1. **내용 1 : 길드 매니저 컨셉 도출**
    * **프롬프트 요약:** ""파이썬으로 RPG 게임 같은 프로그램을 만들고 싶어. 내가 어떤 역할을 맡아서 이 프로그램을 관리하면 1학년 학생들이 재미있게 코딩할 수 있을까? 멋진 컨셉 하나만 추천해줘.""
    * **적용 내용:** AI가 제안한 여러 아이디어 중 **'우주 정복 회사 급여 명세서'**라는 컨셉이 가장 마음에 들어 채택함. 단순히 급여 명세서가 아니라 우주 정복 회사라는 스토리를 넣어 생체 포획 수 행성 파괴등 성과와 여러 조건등에 따라 급여가 바뀌니 재미있음 .
      
 2. **내용 2 : 로드맵 도출**
    * **프롬프트 요약:** "1차 과제 필수 요건(변수 5개, 자료형 3개 이상)을 충족하기 위한 캐릭터 초기 스탯 데이터 구조 모델링 논의"
    * **적용 내용:** 요원 식별 코드, 정복 행성 수 생체 포획 개수등 변수 여러게 사용, 데이터 특성에 맞춰 문자형(`char` - 요원의 고유 ID), 정수형(`int` - 행성파괴 개수, 생체수치), (`float` - 임무 성공 확률, 특별 성과 배율)으로 자료형을 명확히 분리하여 입력 데이터의 구조적 완성도를 높임. 
    
### **📁 증빙 자료:**
  * [1차_AI협업캡처.pdf 첨부 완료] (첨부 후 링크)
[파이썬 과제(AI협업)1.pdf](https://github.com/user-attachments/files/26480948/AI.1.pdf)

<br>

## 🟩 [2차 과제: V1.0] 입출력 + 리스트 + 조건문 - 향후 작성 예정
### **✨2차 과제 내용:**
(예시)
  * 이번 과제는 용사 등록 및 정밀 진단 시스템 구현으로, 사용자로부터 데이터를 입력받아 리스트에 저장하고, 가중치 연산을 통해 결과값을 도출하는 시스템을 구축하는 것입니다. 특히 `if-elif` 조건문과 `and/or` 논리 연산자를 활용하여 상황에 맞는 등급과 특별 칭호를 부여하는 지능형 로직을 완성해야 합니다.
  * input()으로 용사의 이름, 체력, 마력, 공격력을 입력받아 리스트에 저장.
  * 가중치 공식을 적용하여 종합 전투력 산출: (체력 * 0.7) + (마력 * 0.5) + (공격력 * 1.8).
  * if-elif-else를 사용하여 S등급부터 F등급까지 5단계 등급 판정 로직 추가.
  * and 연산자를 활용하여 '전설의 대마법사' 등 특별 칭호 부여 기능 구현.
    
### **🤖 AI 파트너십 과정**
(예시) 
1. **내용 1: 길드 매니저 컨셉 및 로직 도출**
    * **프롬프트 요약:** "내가 길드 매니저가 되어 용사를 관리하는 프로그램을 만들 거야. 1학년 수준에서 리스트와 조건문을 활용해 등급을 매기는 재미있는 로직을 짜줘."
    * **적용 내용:** AI가 제안한 '가중치 전투력 산출' 방식과 'S등급이면서 마력이 높으면 대마법사 칭호 부여'라는 복합 조건 아이디어를 실제 코드에 반영함.

2. **내용 2: 효율적인 리스트 활용법 자문**
    * **프롬프트 요약:** "파이썬 기초 문법 단계(리스트 → 조건문 → 반복문 → 함수/딕셔너리)에 맞춰, '용사 길드 관리자' 컨셉의 프로그램이 어떻게 발전할 수 있을지 4단계 기능 확장 로드맵을 제안해줘."
    * **적용 내용:** 단순 입출력을 넘어, **'기초 정보 입력 및 리스트 저장(1차) → 전투 등급 판독기 구현(2차) → 무한 메뉴 시스템 구축(3차) → 딕셔너리를 활용한 다중 캐릭터 관리(4차)'**로 이어지는 논리적인 확장 로드맵을 확립함.
#1.성과 입력
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
print(f' 회사조치: {company_action}")
### **🛠️ Troubleshooting & 기술 회고:**
(예시) 
1. **문제 1: 숫자를 입력했는데 계산이 안 되는 현상 (TypeError)**
    * **원인:** `input()`으로 받은 데이터는 기본적으로 '글자'라서 숫자와 곱셈 연산이 불가능했음.
    * **해결:** `int()'를 함수를 사용하여 입력값을 숫자로 바꾸는 '형변환' 마법을 부려 해결함.
2. **문제 2: 조건문 뒤에 자꾸 생기는 빨간 줄 (SyntaxError)**
    * **원인:** `if`와 `elif` 'match' 'case'조건식 끝에 마법의 기호인 `:`(콜론)을 자꾸 빠뜨려서 발생함.
    * **해결:** 파이썬의 모든 조건문과 반복문 끝에는 항상 땡땡(`:`)이 들어가야 한다는 규칙을 학습하고 수정함.
     
### **📁 증빙 자료:**
  * [2차_AI협업캡처.pdf 첨부 완료] [파이썬 과제(AI협업) 2차.pdf](https://github.com/user-attachments/files/27014584/AI.2.pdf)

  * [2차과제_실행결과.jpg] [파이썬 결과 2차과제.pdf](https://github.com/user-attachments/files/27014598/2.pdf)

<br>

## 🟨 [3차 과제: V3.0] 무한 루프와 메뉴 시스템 (반복문) - 향후 작성 예정
### **✨3차 과제 업데이트 내용:**
  * 내용.
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
### **🤖 AI 파트너십 과정**
 1. **내용 1** while True가 들어간 재미있는 컨셉 추가
    * **프롬프트 요약:**  ... while True를 집어 넣어서 퇴사 전까지는 절대로 벗어날 수 없는 블랙기업의 굴레라는 컨셉을 추가함
    * **적용 내용:** .... 1.실적입력(노동) 2.명세서 조회(확인) 3.은하계 분석(미래) 4.프로그램 종료(퇴사)로 이어지는 무한반복
    
### **🛠️ Troubleshooting & 기술 회고:**
  1. **문제 1:** ...def 함수를 만들때 자꾸 :와 ()를 뺴먹어서 실행이 안됨
     * **원인:** ... :와()를 빼먹음
     * **해결:** .. :와 () 잘 적음
     
### **📁 증빙 자료:**
  * [3차_AI협업캡처.pdf 첨부 완료] (첨부 후 링크) [파이썬 과제(AI협업) 3차.pdf](https://github.com/user-attachments/files/28175324/AI.3.pdf)

  * [3차과제_실행결과.jpg] [파이썬 결과 3차과제.pdf](https://github.com/user-attachments/files/28175400/3.pdf)

<br>

### 🟥 [4차 과제: V4.0] 모듈화 및 데이터 확장 (배열과 함수) - 🌟최종 완성 -- 향후 작성 예정
### **✨4차 과제 업데이트 내용:**
  * 내용.
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
            
### **🤖 AI 파트너십 과정**
 1. **내용 1**
    * **프롬프트 요약:**  ... '우주 정복 주식회사'라는 악당 컨셉의 기존 파이썬 프로그램에 4가지 필수 프로그래밍 과제 요건(이중 리스트, 이중 순회, 파일 입출력, 예외 처리)을 가장 잘 어울리는 재미있는 스토리와 함께 통합해 달라는 요청입니다.
    * **적용 내용:** .... 이중 리스트 (2D List) 활용: blacklist = [[이름, 죄목, 현상금], [이름, 죄목, 현상금], ...] 형태로 여러 배신자들의 데이터를 하나의 전역 변수에 누적하여 저장하도록 구현했습니다. 이중 순회 (Nested Loops) 출력: 바깥쪽 for문으로 각 반역자의 리스트를 꺼내고, 안쪽 for문(enumerate 활용)으로 내부 항목을 꺼내어 깔끔한 표 형태의 '현상수배 전단지'를 출력하게 만들었습니다. 파일 입출력 (File I/O): with open() 구문을 사용하여 프로그램 시작 시 blacklist.txt에서 데이터를 불러오고, 3번 메뉴나 종료(4번) 선택 시 최신 살생부 데이터를 텍스트 파일로 저장(백업)하도록 구성했습니다. 예외 처리 (try-except) 2종 적용: FileNotFoundError: 처음 실행하거나 파일이 지워졌을 때 시스템이 뻗지 않고, "누군가 살생부를 해킹해 지웠다"며 빈 문서로 시작하도록 자연스럽게 처리했습니다. ValueError: 현상금 입력 칸에 문자를 입력할 경우, 에러 대신 경고 메시지와 함께 기본 현상금(100 크레딧)으로 강제 세팅되도록 방어 코드를 작성했습니다.
    
### **🛠️ Troubleshooting & 기술 회고:**
  1. **문제 1:** ... 파일 입출력에서 오류가 발생함
     * **원인:** ... '' 작은 따옴표를 빼먹음 'blacklist.txt','w',encoding='utf-8'
     * **해결:** .. '' 작은 따옴표를 추가함
     
### **📁 증빙 자료:**
  * [4차_AI협업캡처.pdf 첨부 완료] (첨부 후 링크)
  * [4차과제_실행결과.jpg]
<br>
