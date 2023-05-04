# kiosk에 필요한 기능들(함수)

# 1.세부 메뉴 출력
def print_sub_menu(sub_name, sub_price):
    for key, value in sub_name.items():
        print(f"□ {key}.{value}({sub_price[key]}원)")


# 2.사용자 메뉴 선택
def choice_menu_num(max_num):
    while True:
        menu_num = int(input(">> 번호: "))

        if menu_num >= 1 and menu_num <= max_num:
            break
        else:
            print(f"경고: 1~{max_num} 사이의 값만 입력해주세요.")
    return menu_num
