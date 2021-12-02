from intro import intro
from red_bean import Red_bean
from exception import gassExeption,exhaustExption,moneyExption


######## 인트로 ################
intro = intro()

#### 붕어빵 만들기 ################
while True:
  try:
    #red_bean = Red_bean(gass, 재료, price)
    red_bean = Red_bean(intro[0], intro[1], intro[2])
    
    if red_bean.number <= 0:
      print("\n== 반죽 붓기 ======================================\n")
      red_bean.make_fish_bread() 
    
    #주문하기
    print("\n== 장사 시작! ==================================\n")
    #fish_bread = input("\n어서오세요~! 어떤 붕어빵을 원하세요?(팥,크림)\n")
    numberOf_fish_bread = input("어서오세요~! 몇 개 구매하실 건가요?\n")

    #붕어빵 판매
    print("=== 판매 상황 ======================================\n") 
    red_bean.sale_fish_bread(int(numberOf_fish_bread))
    
    #붕어빵 계속 만들기
    red_bean.question_remake()
    
  except moneyExption:
    print("돈이 부족하여 가스를 구매할 수 없습니다.")
    break  
  except gassExeption:
    print("가스가 부족하여 붕어빵을 만들 수 없습니다.")
    break
  except exhaustExption:
    print("자본금이 모두 소진되어 제작을 진행 할 수 없습니다.")
    break
    
  
   
    
    # #계속 구매하기
    # answer = input("계속 구매하시겠습니까? y / n\n")
    # while answer != 'y':
    #   if answer =='n':
    #     break
    #   else:
    #     print("y 또는 n을 정확히 입력해 주세요!\n")
    #     answer = input("계속 구매하시겠습니까? y / n\n")
    
    # #종료하기    
    # if answer == 'n':
    #   print("\n== 장사 종료! ==================================\n")
    #   print("구매해 주셔서 감사합니다!\n")
    #   print("=========================================\n")
    #   break      
   

