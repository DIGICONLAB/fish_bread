from exception import gassExeption,  moneyExption
import sys

class Red_bean():

  number = 0
  balnce = 0
  money = 1000
  count = 0
  gass = 0

  def __init__(self, gass, ingredients, price):
    self.gass = int(gass)
    self.ingredients = ingredients
    self.price = int(price)

  #붕어빵 만들기
  def make_fish_bread(self, num = 0):
    if Red_bean.count == 0:
      if self.gass <= 0:
        raise gassExeption()

      Red_bean.number = int(self.gass) // 10
      Red_bean.money -= self.gass * 10  

      for i in range(1,Red_bean.number+1):
          print(f"{self.ingredients} 재료가 {i}개 부어졌습니다.")
          self.gass -= 10
      Red_bean.gass = self.gass

    else:
      for i in range(1,num+1):
          print(f"{self.ingredients} 재료가 {i}개 부어졌습니다.")
          Red_bean.gass -= 10
    
      Red_bean.number += num
      
    print(f"\n현재 판매 가능한 붕어빵: {Red_bean.number}개")
    Red_bean.count += 1 
  
  #붕어빵판매
  def sale_fish_bread(self, buy):
    if Red_bean.number < buy:
      print("오늘은 붕어빵이 부족합니다. 조금 적게 주문해 주세요!\n")
    else:
      currnet_fish_bread = Red_bean.number - buy
      
      print(f"판매된 붕어빵: {buy}개  | 남은 붕어빵 수: {currnet_fish_bread}  \n남은 가스연료: {Red_bean.gass}")  
      Red_bean.balnce += self.price * buy
      print(f"현재 판매 수익: {str(Red_bean.balnce)}원\n현재 자본금: {Red_bean.money}")
      print("=========================================\n")
      Red_bean.number =  currnet_fish_bread

  #붕어빵 다시 만들기 질문
  def question_remake(self):
    print(f"현재 가스량: {Red_bean.gass}, 현재 자본금: {Red_bean.money}")
    
    answer = input("계속해서 붕어빵을 만드시겠습니까? (y/n)\n")
    while answer != 'y': 
      if answer == 'n':
        break
      else:
        print("y/n 정확하게 입력해 주세요")
        answer = input("계속해서 붕어빵을 만드시겠습니까? (y/n)\n")

    if answer == 'y':
      if Red_bean.gass <=0 :
        print("\n가스가 다 소진되었습니다.\n붕어빵을 만들기 위해 가스를 구매해야 합니다.")
        charge_gass = int(input("얼마나 구매 하시겠습니까?\n"))
          
        if charge_gass * 10 > Red_bean.money:
          raise moneyExption()
        else:
          Red_bean.gass += charge_gass
          Red_bean.money -= charge_gass * 10
          print(f"\n{charge_gass * 10}원 구매하셨습니다.\n남은 자본금: {Red_bean.money}원\n현재 가스량: {Red_bean.gass}")

          Red_bean.remake_fish_bread(self) 
      else:
        Red_bean.remake_fish_bread(self)     
    elif answer =='n':
      sys.exit()    
         
  #붕어빵 다시만들기
  def remake_fish_bread(self):
    num = int(input("\n몇 개 만드시겠습니까?\n"))
    if num * 10 > Red_bean.gass:
      raise gassExeption()
    else:  
      print("\n== 반죽 붓기 ======================================\n")
      Red_bean.make_fish_bread(self, num) 