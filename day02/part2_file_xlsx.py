# part2_file_xlsx.py
# 엑셀 파일을 파이썬을 이용하여 쓰고 읽을 수 있다.
# 이를 위해서 필요한 패키지는 openpyxl이며,
# pip install openpyxl
# 위 명령어로 설치할 수 있다.
import openpyxl as pyxl

def make_xlsx():
    # 엑셀 파일 생성
    # 엑셀 파일은 하나의 workbook으로 취급되며
    # 이 워크북 안에 여러 시트가 들어가는 형식을 취한다.
    wb = pyxl.Workbook()
    # 이러한 워크북에는 기본적으로 활성화된 시트가 하나 반드시 존재한다.
    sheet = wb.active
    # 시트(표)의 셀에 접근할 때에는 두 가지 방식이 있는데
    # 문자+숫자(열, 행) C2
    # 일반적으로 첫 행은 header로서 해당 열에 들어갈 값들을 가리킬 이름을 작성한다.
    sheet["C1"] = "이름"
    sheet["D1"] = "나이"
    # C열에는 이름 값들이 들어갈 것이다.
    names = ["홍길동", "이순신", "김유신"]
    ages = [30, 40, 25]
    
    # 반복문을 활용하여 열에 데이터를 모두 삽입한다.
    for i, name in enumerate(names, 2):
        sheet[f"C{i}"] = name
    for i, age in enumerate(ages, 2):
        sheet[f"D{i}"] = age
    
    sheet.title = "영웅 정보"
    # 엑셀 파일로 저장하기
    wb.save("people.xlsx")

    # 파일명 내보내기
    return "people.xlsx"

# 엑셀 파일 정보 읽어오기
def open_xlsx(file_path, cell:str):
    # 읽어올 때에도 워크북부터 준비한다.
    wb = pyxl.load_workbook(file_path)
    sheet = wb.active

    # 해당 셀을 대괄호[] 방식으로 가져온 뒤
    # .value 속성으로 해당 셀에 저장된 값을 받아올 수 있다.
    result = sheet[cell].value
    return result

if __name__ == "__main__":
    file_path = make_xlsx()

    target = "C4"
    name = open_xlsx(file_path, target)
    print(f"엑셀에서 가져온 값 {target}는 {name}입니다.")
    target = "c3"
    name = open_xlsx(file_path, target)
    print(f"엑셀에서 가져온 값 {target}는 {name}입니다.")

    # 문자열+숫자 방식으로 셀을 지정할 때
    # 대소문자 무관하게 값을 정상적으로 들고 올 수 있다.