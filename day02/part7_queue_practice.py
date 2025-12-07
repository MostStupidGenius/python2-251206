# part7_queue_practice.py
# 프린트 대기열을 Queue 자료구조로 구현하기


if __name__ == "__main__":
    # 함수없이 문서1, 문서2,.. 등을 추가하고
    # 이를 순서대로 출력하는 실습을 해보자.
    printer_queue = []

    # 문서1, 문서2 등을 추가
    printer_queue.append("문서1")
    printer_queue.append("문서2")

    # 추가한 문서를 순차적으로 출력하는 실습
    data = printer_queue.pop(0)
    print(data)

    data = printer_queue.pop(0)
    print(data)
    
