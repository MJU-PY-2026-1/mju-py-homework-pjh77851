# 파일이름 :
# 작 성 자 : 박준형

#1 성과 입력
planents_destroyed = int(input("💥파괴한 소행성 개수: "))
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
