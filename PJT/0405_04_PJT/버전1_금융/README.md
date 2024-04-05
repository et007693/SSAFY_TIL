# 프로젝트 내용
Django에서 python 그래프 출력하기

# 프로젝트 목표
Django에서 시각화 및 html로 rendering

# 어려웠던 점
pyplot을 많이 써보지 않아서 plt의 여러 인자들을 사용하는 것이 익숙하지 않았음   

### 과제 1번 
read_csv까지 문제가 없었으나 html에서 렌더링 하는 과정이 어려웠음   
-> {{ data|<strong>safe</strong>}}   
|safe 인자 사용하면 출력이 가능!

---

### 과제 2번
어려운 부분 없었음

---

### 과제 3번
연-월로 묶는 과정이 어려웠음   
범례 설정 과정도 어려웠음 

시도했던 것
1. f-string을 사용해서 'y-m'로 묶기 -> 실패   
2. groupby에 [year, month] 사용 -> year1 - m1, m2, m3... year2 - m1, m2, m3... 같이 나와서 실패   
3. year, month 열을 새로 생성하여 묶기 -> 2번과 같은 이유로 실패   

-> strftime 사용해서 성공(data['Date'].dt.srrftime('%Y-%m'))   

이렇게 했더니 모든 연-월 조합이 x축으로 설정되었음
-> plt.xticks(np.arange(1, total_len, 6))을 사용해서 갯수 설정하여 해결

---

### 과제 4번
한 열에 여러 개의 값이 있을 때 나누는 것이 어려웠음   
plt graph 종류 공부하기   

시도했던 것
1. for문을 사용하여 행의 값을 가져오고 ->   
split으로 값을 나눠서 ->   
값을 각각 세어줌 -> 실패   

-> 아래 코드 사용하여 해결
split(expand = True), stack, reset_index(level=0(index 새로 설정), drop=True(index 삭제))   
