# part1_file_unpickle.py

import pickle as pkl


if __name__ == "__main__":
    # 피클링된 파일을 읽어올 때에는 바이너리 읽기 모드로 읽어온다.
    with open("my_data.pkl", "rb") as file:
        # .load(file)
        data = pkl.load(file)
    
    # 가져온 기능을 실행해보자.
    print(data["name"]) # 홍길동

    with open("hong_person.pkl", "rb") as f:
        hong = pkl.load(f)
    # hong = Person("홍길동", 30)
    # hong으로 들고 온 객체는 기반이 되는 클래스를 import를 해야
    # 사용이 가능하다.
    from part1_file_pickle import Person
    hong.introduce()
