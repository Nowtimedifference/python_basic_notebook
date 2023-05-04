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

from kiosk_fnc import print_sub_menu, choice_menu_num

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
menu_num = choice_menu_num(4)

##################
# 4.세부 메뉴 선택 #
##################

if menu_num == 1:  # 세트
    print_sub_menu(burger_name, burger_price)
    menu_num = choice_menu_num(3)
    menu_save["burger"] = burger_name[menu_num]
    price_save["burger"] = burger_price[menu_num]

    print_sub_menu(side_name, side_price)
    menu_num = choice_menu_num(3)
    menu_save["side"] = side_name[menu_num]
    price_save["side"] = side_price[menu_num]

    print_sub_menu(drink_name, drink_price)
    menu_num = choice_menu_num(3)
    menu_save["drink"] = drink_name[menu_num]
    price_save["drink"] = drink_price[menu_num]
elif menu_num == 2:  # 햄버거
    print("■" * 50)
    # 1.햄버거 메뉴 출력
    print_sub_menu(burger_name, burger_price)
    # 2.사용자가 햄버거 메뉴 선택
    menu_num = choice_menu_num(3)
    # 3.사용자가 선택한 메뉴 저장
    menu_save["burger"] = burger_name[menu_num]
    price_save["burger"] = burger_price[menu_num]
elif menu_num == 3:  # 사이드
    print_sub_menu(side_name, side_price)
    menu_num = choice_menu_num(3)
    menu_save["side"] = side_name[menu_num]
    price_save["side"] = side_price[menu_num]
elif menu_num == 4:  # 음료
    print_sub_menu(drink_name, drink_price)
    menu_num = choice_menu_num(3)
    menu_save["drink"] = drink_name[menu_num]
    price_save["drink"] = drink_price[menu_num]

# print(menu_save)
# print(price_save)

#########################
# 5.주문 메뉴 출력 및 계산 #
#########################
# Total 주문 금액 계산
total_price = 0  # 총 주문금액
for price in price_save.values():
    total_price += price

print("■" * 50)
print("■■ 고객님이 주문하신 메뉴는")
for i, menu in enumerate(menu_save.values()):
    print(f" {i+1}.{menu}")
print(f"으로 총 주문 금액은 {total_price}원 입니다.")
print("■" * 50)
print("■■ 이용해주셔서 감사합니다. 또 방문해주세요.")
print("■" * 50)