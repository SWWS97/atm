# while문을 이용해서 입급, 출급, 영수증 보기, 종료라는 기능이 종료라는 버튼을 누르기 전까지 계속해서 노출되도록 만들어주세요
# 종료를 누르면 서비스를 종료한다는 메시지를 출력하고 현재 잔액을 보여주세요

# 출금 요청한 금액을 받는 변수 : withdraw_amount
# 출금을 요청한 금액을 balance 변수에서 뺀 결과가 들어가도록 코드를 작성해주세요
# 영수증에 다음 순서로 값이 들어가도록 코드를 만들어주세요 -> ("출금", withdarw_amount, balance) 순으로 데이터 넣어주세요
# 가지고 있는 금액보다 출금을 원하는 금액이 클때 가지고 있는 금액만 출금되도록 코드를 작성해주세요
# 단, 영수증에 내역은 변경되지 않아야 하며 입금 또는 출금이 진행될떄마다 이력이 기록됩니다.
# 영수증 변수는 : receipts

# 입력 검증 및 에러 처리 추가
# 잘못된 입력 값(숫자가 아닌값, 음수 값 등)을 처리하도록 기능을 추가해주세요
# 유효하지 않은 메뉴 선택 시 경고 메시지 또는 사용방법 재안내를 해주세요

receipts = [] # [ ] 대괄호 : list / {key, value} 중괄호 : dict / ( ) : tuple
balance  = 3000 # 현재 잔액을 보여주세요

while True:
    print()             # 출력 내용 한칸 띄우기
    num = input("사용하실 기능을 선택해주세요 (1:입금, 2:출금, 3:영수증 보기, 4:종료)")
    if num == '4':
        break      # 가장 가까운 반복문으로 감
    if num == "1":
        print()
        deposit_amount = input("입금할 금액을 입력하세요 : ") # input() : 내장함수 / int() : 정수형 데이터로 형변환해주는 내장함수()
        if deposit_amount.isdigit() and int(deposit_amount) > 0: #1000 -> True, 천원 -> False
            balance = balance + int(deposit_amount) # balance += deposit_amount
            receipts.append(("입금", deposit_amount, balance))
            print()
            print(f'입금하신 금액은 {deposit_amount}원이고, 현재 잔액은 {balance}원 입니다')
        else:
            print("입금한 금액을 숫자 형태의 음수가 아닌값을 입력해주세요")
    if num == "2":
        print()
        withdraw_amount = int(input('출금할 금액을 입력하세요 : '))
        withdraw_amount = min(balance, withdraw_amount)
        balance -= withdraw_amount
        receipts.append(('출금', withdraw_amount, balance))
        print()
        print(f'출금하신 금액은 {withdraw_amount}원이고, 현재 잔액은 {balance}원 입니다')
    if num == "3":
        #영수증에 값이 있을때, 값이 없을때
        if receipts:  # 프로그램이 시작되자마자 3번을 눌렀을 경우 이 조건은 참인가요 거짓인가요?
            print('===영수증===')
            for i in receipts:#[("입금", deposit_amount, balance),('출금', withdraw_amount, balance)]
                print(f'{i[0]}: {i[1]}원 | 잔액: {i[2]}원')
        else:
            print('영수증 내역이 없습니다.')                           

print()
print(f'서비스를 종료합니다. 현재 잔액은 {balance}원입니다.')