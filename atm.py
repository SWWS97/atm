# while문을 이용해서 입급, 출급, 영수증 보기, 종료라는 기능이 종료라는 버튼을 누르기 전까지 계속해서 노출되도록 만들어주세요
# 종료를 누르면 서비스를 종료한다는 메시지를 출력하고 현재 잔액을 보여주세요

# 입금한 금액을 받는 변수 : deposit_amount
# 입금한 금액은 balance 변수에 추가되도록 코드를 작성해주세요
# 영수증에 다음 순서로 값이 들어가도록 코드를 만들어주세요 -> ("입금", deposit_amount, balance) 순으로 데이터 넣어주세요
# 단, 영수증에 내역은 변경되지 않아야 하며 입금 또는 출금이 진행될떄마다 이력이 기록됩니다.
# 영수증 변수는 : receipts

receipts = [] # [ ] 대괄호 : list / {key, value} 중괄호 : dict / ( ) : tuple
balance  = 3000 # 현재 잔액을 보여주세요

while True:
    print()             # 출력 내용 한칸 띄우기
    num = input("사용하실 기능을 선택해주세요 (1:입금, 2:출금, 3:영수증 보기, 4:종료)")
    if num == '4':
        break      # 가장 가까운 반복문으로 감
    if num == "1":
        print()
        deposit_amount = int(input("입금할 금액을 입력하세요 : ")) # input() : 내장함수 / int() : 정수형 데이터로 형변환해주는 내장함수()
        balance = balance + deposit_amount # balance += deposit_amount
        receipts.append(("입금", deposit_amount, balance))
        print()
        print(f'입금하신 금액은 {deposit_amount}원이고, 현재 잔액은 {balance}원 입니다')
print()
print(f'서비스를 종료합니다. 현재 잔액은 {balance}원입니다.')