################################################
# CNU 버거 키오스크
# - 일자: 2023년 05월 02일
# - 작성자: 차시현
# - 내용: console 프로그램(햄버거 판매 키오스크)
################################################

# 조건
# - 결제 X
# - 화면 -> console창
# - 사용자 최대 주문: 버거1개, 사이드 1개, 음료1개 고정

#################
# 1.메뉴와 가격표 #
#################
burger_name = {1: "몬스터 와퍼", 2: "빅맥", 3: "싸이버거"}
side_name = {1: "감자튀김", 2: "치즈스틱", 3: "치킨너겟"}
drink_name = {1: "사이다", 2: "콜라", 3: "환타"}

burger_price = {1: 7000, 2: 5000, 3: 4000}
side_price = {1: 2000, 2: 1500, 3: 2000}
drink_price = {1: 1500, 2: 1500, 3: 1000}

##################
# 2.주문 내역 저장 #
##################
menu_save = {}   # 고객 주문 내역 기록
price_save = {}  # 고객 주문 금액 기록

##################
# 3.메인 메뉴 선택 #
##################
print("■" * 50)
print("■■ == CNU 버거(ver 1.1) ==")
print("■■ CNU 버거에 방문해주셔서 감사합니다.")
print("■" * 50)
print("■ 메뉴")
print("□ 1.햄버거 세트")
print("□ 2.햄버거 단품")
print("□ 3.사이드 단품")
print("□ 4.음료 단품")
print("■" * 50)

# 사용자로부터 메뉴 주문 받기
while True:
    menu_num = int(input(">> 번호: "))

    if menu_num >= 1 and menu_num <= 4:
        break
    else:
        print("경고: 1~4 사이의 값만 입력해주세요.")

##################
# 4.세부 메뉴 선택 #
##################

if menu_num == 1:  # 세트
    pass
elif menu_num == 2:  # 햄버거
    print("■" * 50)
    # 1.햄버거 메뉴 출력
    for key, value in burger_name.items():
        print(f"□ {key}.{value}")
    # 2.사용자가 햄버거 메뉴 선택
    while True:
        menu_num = int(input(">> 번호: "))

        if menu_num >= 1 and menu_num <= 3:
            break
        else:
            print("경고: 1~4 사이의 값만 입력해주세요.")
    # 3.사용자가 선택한 메뉴 저장
    menu_save["burger"] = burger_name[menu_num]
    price_save["burger"] = burger_price[menu_num]
elif menu_num == 3:  # 사이드
    pass
elif menu_num == 4:  # 음료
    pass

print(menu_save)
print(price_save)