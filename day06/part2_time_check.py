# part2_time_check.py
# 지금까지 배운 정렬 알고리즘을 모두 가져와서
# 정렬시간을 측정해보려고 한다.

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
from day03.part6_sort_bubble import bubble_sort
from day04.part1_selection_sort import selection_sort
from day04.part2_insertion_sort import insertion_sort
from day05.part1_quick_sort import quick_sort
from day05.part2_merge_sort import merge_sort
from part1_heap_sort import heap_sort

if __name__ == "__main__":
    from time import time
    import random as r
    
    datas = list(range(20000))
    r.shuffle(datas)

    sorts = {
        "quick":quick_sort,
        "merge":merge_sort,
        "heap":heap_sort,
        # "bubble": bubble_sort, 
        "select": selection_sort, 
        "insert": insertion_sort, 
    }

    for sort_name, sort_func in sorts.items():
        start = time()
        sort_func(datas.copy())
        end = time()
        # 끝난시각 - 시작시각
        print(f"{sort_name}: {end-start:.2f}s")