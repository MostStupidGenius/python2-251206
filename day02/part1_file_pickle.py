# part1_file_pickle.py
# 피클링(pickling)
# 피클링이란, 파이썬에서 다루는 값, 변수, 함수, 클래스 등
# 대부분의 객체를 바이너리 파일로 직렬화하여 저장할 수 있는 기술을 말한다.
# 사용처: 일반적으로 AI를 학습한 데이터를 다른 개발자에게나 다른 환경에서
# 옮겨 사용하고자 할 때 많이 쓰인다.
# 혹은 json, xml, csv, xlsx 등 텍스트로 나타낼 수 없는 데이터 객체를
# 보관, 전달, 공유하고자 할 때 사용된다.
# 이러한 피클 패키지는 파이썬에 기본 내장되어 있어서 별다른 설치가 필요없다.

# 피클링을 하려면 기능을 가져와야(import) 한다.
import pickle as pkl # as ~~는 아래에서 해당 기능을 사용할 때
# 짧게 호출하기 위한 별명 같은 것이다.

data = {
    "name": "홍길동",
    "age": 30
}

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"my name is {self.name}\nage is {self.age}")

if __name__ == "__main__":
    # pickling
    # 함수를 정의한 뒤 해당 함수를 pickling하여 내보내자
    
    # with open()을 이용하여 확장자는 자유롭게 설정한 뒤
    # 'wb'모드로 피클링 파일을 내보낼 수 있다.
    with open("my_data.pkl", "wb") as file:
        # .dump를 이용하여 파일을 내보낸다.
        pkl.dump(data, file)

    hong = Person("홍길동", 30)

    # 클래스를 기반으로 만들어진 객체를 내보내보자.
    with open("hong_person.pkl", "wb") as file:
        pkl.dump(hong, file)