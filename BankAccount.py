# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    #초기화 메서드
    def __init__(self, id, name, balance):
        #self.id = id
        #self.name = name 
        #self.balance = balance 
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    #입금 메서드
    def deposit(self, amount):
        self.__balance += amount 
    #결과 메서드
    def withdraw(self, amount):
        self.__balance -= amount
    #결과를 문자열로 리턴 toString())메서드
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.withdraw(3000)
print(account1)

#클래스 외부(인스턴스)
#print(account1.__balance)