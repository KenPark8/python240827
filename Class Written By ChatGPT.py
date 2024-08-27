# Person 클래스 정의
class Person:
    """
    Person 클래스는 사람의 기본 정보를 담고 있는 클래스입니다.
    각 사람은 고유의 ID와 이름을 가지고 있습니다.
    """

    def __init__(self, person_id, name):
        """
        생성자 메서드로, Person 객체를 초기화합니다.
        :param person_id: 사람의 고유 ID를 나타내는 정수형 값
        :param name: 사람의 이름을 나타내는 문자열 값
        """
        self.person_id = person_id  # 사람의 고유 ID를 저장하는 속성
        self.name = name  # 사람의 이름을 저장하는 속성

    def printInfo(self):
        """
        사람의 ID와 이름을 출력하는 메서드입니다.
        """
        print(f"ID: {self.person_id}, Name: {self.name}")  # ID와 이름을 출력


# Manager 클래스 정의 (Person을 상속)
class Manager(Person):
    """
    Manager 클래스는 Person 클래스를 상속받아 매니저의 추가 정보를 담고 있는 클래스입니다.
    매니저는 기본적인 사람의 정보 외에 직책(title) 정보를 추가로 가집니다.
    """

    def __init__(self, person_id, name, title):
        """
        생성자 메서드로, Manager 객체를 초기화합니다.
        :param person_id: 매니저의 고유 ID를 나타내는 정수형 값
        :param name: 매니저의 이름을 나타내는 문자열 값
        :param title: 매니저의 직책을 나타내는 문자열 값
        """
        super().__init__(person_id, name)  # 상위 클래스(Person)의 생성자를 호출하여 person_id와 name을 초기화
        self.title = title  # 매니저의 직책을 저장하는 속성

    def printInfo(self):
        """
        매니저의 ID, 이름, 직책을 출력하는 메서드입니다.
        """
        super().printInfo()  # 상위 클래스의 printInfo 메서드를 호출하여 ID와 이름을 출력
        print(f"Title: {self.title}")  # 직책을 추가로 출력


# Employee 클래스 정의 (Person을 상속)
class Employee(Person):
    """
    Employee 클래스는 Person 클래스를 상속받아 직원의 추가 정보를 담고 있는 클래스입니다.
    직원은 기본적인 사람의 정보 외에 기술(skill) 정보를 추가로 가집니다.
    """

    def __init__(self, person_id, name, skill):
        """
        생성자 메서드로, Employee 객체를 초기화합니다.
        :param person_id: 직원의 고유 ID를 나타내는 정수형 값
        :param name: 직원의 이름을 나타내는 문자열 값
        :param skill: 직원이 가진 기술을 나타내는 문자열 값
        """
        super().__init__(person_id, name)  # 상위 클래스(Person)의 생성자를 호출하여 person_id와 name을 초기화
        self.skill = skill  # 직원의 기술을 저장하는 속성

    def printInfo(self):
        """
        직원의 ID, 이름, 기술을 출력하는 메서드입니다.
        """
        super().printInfo()  # 상위 클래스의 printInfo 메서드를 호출하여 ID와 이름을 출력
        print(f"Skill: {self.skill}")  # 기술을 추가로 출력


# 테스트 코드
if __name__ == "__main__":
    """
    다음은 Person, Manager, Employee 클래스를 테스트하는 코드입니다.
    각각의 객체를 생성하고, printInfo() 메서드를 호출하여 객체의 정보를 출력합니다.
    """

    # Person 객체 테스트
    person1 = Person(1, "Alice")
    person1.printInfo()  # ID와 이름을 출력
    print("---")

    person2 = Person(2, "Bob")
    person2.printInfo()  # ID와 이름을 출력
    print("---")

    # Manager 객체 테스트
    manager1 = Manager(3, "Charlie", "Project Manager")
    manager1.printInfo()  # ID, 이름, 직책을 출력
    print("---")

    manager2 = Manager(4, "David", "Sales Manager")
    manager2.printInfo()  # ID, 이름, 직책을 출력
    print("---")

    # Employee 객체 테스트
    employee1 = Employee(5, "Eve", "Python Developer")
    employee1.printInfo()  # ID, 이름, 기술을 출력
    print("---")

    employee2 = Employee(6, "Frank", "Data Scientist")
    employee2.printInfo()  # ID, 이름, 기술을 출력
    print("---")

    # 추가 테스트 케이스
    manager3 = Manager(7, "Grace", "HR Manager")
    manager3.printInfo()  # ID, 이름, 직책을 출력
    print("---")

    employee3 = Employee(8, "Hank", "Java Developer")
    employee3.printInfo()  # ID, 이름, 기술을 출력
    print("---")

    person3 = Person(9, "Ivy")
    person3.printInfo()  # ID와 이름을 출력
    print("---")

    employee4 = Employee(10, "Jack", "Front-End Developer")
    employee4.printInfo()  # ID, 이름, 기술을 출력
    print("---")


