# part3_sort_time.py
# 정렬 시간 측정
# time 라이브러리를 활용하여 현재 시간을 추출한 뒤
# 정렬이 끝난 시점의 시간값에서 정렬 전의 시간값과의 차를 구하여 정렬 시간을 측정한다.

# 이러한 시간 측정의 start_time과 end_time의 차를 구하는 부분을
# 데코레이터 함수에 구현한 뒤, 정렬 함수를 전달하는 방식으로
# 정렬 시간을 측정해보자.

# 정렬 함수 가져오기
from part1_selection_sort import selection_sort
from part2_insertion_sort import insertion_sort
# day03에 있는 .py파일은 모듈을 추가한 뒤 해당 파일을 가져와야 한다.
import sys # 시스템에 경로 등록을 위해서 가져오기
import os # 경로를 추출하는 기능을 사용하기 위해서 가져오기
# 현재 파일의 경로를 추출
file_path = __file__
# 상위 폴더의 경로를 추출(day04 폴더)
folder_path = os.path.dirname(file_path)
# 최상위 폴더(root) -> workspace 폴더 경로 추출
root_folder_path = os.path.dirname(folder_path)

# 시스템에 경로 등록
sys.path.append(root_folder_path)

# 시스템에 경로 등록을 하면, 해당 폴더 아래에 있는 폴더를
# from으로 가져올 수 있다.
from day03.part6_sort_bubble import bubble_sort

# 시간 측정을 위한 time 라이브러리 가져오기
import time

def sort(func, datas, show=False):
    start = time.time()
    result = func(datas, show)
    end = time.time()
    # 함수명을 문자열로 가져오는 매직 메서드
    func_name = func.__name__
    print(f"{func_name}_duration: {end-start:.2f}")
    return result


if __name__ == "__main__":
    import random as r
    datas = list(range(3000))
    r.shuffle(datas)

    # 같은 리스트로 여러 정렬 알고리즘에 사용을 하면
    # 정렬된 리스트로 또 정렬을 해버리기 때문에 .copy()를 이용하여
    # 정렬시간만 측정할 것이다.
    sorts = [bubble_sort, selection_sort, insertion_sort]
    for e in sorts:
        sort(e, datas.copy())




# ※ 외부에서 선언된 함수는 데코레이터@를 사용하기 번거롭기 때문에
# 위에서는 함수 직접 전달방식으로 구현되었다.
# 아래에서는 bubble_sort에 대해서만 직접 정의한 뒤
# 데코레이터@를 붙이는 방식으로 진행되었다.

# 데코레이터 함수
# 데코레이터 함수는 다른 함수를 전달받는 매개변수를 정의하여
# 내부 함수에서 해당 함수를 실행하고 그 앞뒤로 추가적으로 실행할 내용을 작성할 수 있다.
# 이것이 전달받은 원본함수를 '꾸미는 것(decorate)' 같다고 하여 데코레이터라고 부른다.

# 데코레이터 함수 만들기
def get_duration(func): 
    def wrapper(*args): # *을 하나 붙인 매개변수는 특정되지 않은 매개변수명을
        # 받아서 처리할 수 있음을 가리킨다. -> tuple로 처리된다.
        start = time.time()
        result = func(args[0], args[1])
        end = time.time()
        # 동작이 끝난 시점에서 시작한 시점의 시간값을 빼면
        # 걸린 시간이 나온다.
        print(f"{end-start:.2f}초")
        return result
    return wrapper

@get_duration
def bubble_sort(datas:list, show:bool):
    # 1. 전달된 데이터를 반복문(for)으로 반복한다.
    for i in range(len(datas)):
        # 외부 반복은 path를 관장하며, 전체 데이터를 훑는 목적으로 사용된다.
        # 내부 반복은 실제로 인접한 요소끼리 비교하여 교환하는 동작을 취한다.
        for j, e in enumerate(datas): # 인덱스가 필요하기 때문에
            # enumerate()를 사용한다.
            # 만약에 i+1이 len(datas)보다 작다면
            if j+1 < len(datas):
                # 마지막 요소가 아니므로 비교를 시행한다.
                if datas[j] > datas[j+1]:
                    # 맞바꾼다.(swap)
                    datas[j], datas[j+1] = datas[j+1], datas[j]
                else:
                    # 정상적인 순서이므로 행동없이 지나간다.
                    continue
    return datas

if __name__ == "__main__":
    bubble_sort(datas.copy(), False)