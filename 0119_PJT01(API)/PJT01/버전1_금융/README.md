# PJT 01

### 이번 pjt 를 통해 배운 내용

API 사용
API -> json -> 데이터 처리 방법 습득
API 형식 적용 방법

## 1. 데이터 추출 - key 값 출력하기

  ### 과제 : json에서 key값만 출력

  API의 데이터 형식이 어떤 것인지 몰라서 받아온 값에서 data를 뽑는 것이 어려웠음
  <br>
  -> dictonary 형태

## 2. 데이터 추출 - 전체 정기예금 상품 리스트

  ### 과제 : 정기예금 상품 정보 출력

  각 key들의 value 값이 무엇인지 몰라서 처리에 어려움을 겪음 
  <br>
  -> API페이지에 나와 있는 내용 확인하기

## 3. 데이터 가공 - 전체 정기예금 옵션 리스트

  ### 과제 : 데이터 재구조화

  dictionary를 list에 추가 하는 방식이 어려웠음 - 빈 dict를 만들고 일일히 key-value 를 지정하였는데, 아래 두가지 방식으로 풀기
  ```python
  ### 1
  dict_name = {
    'key' : value, 
    'key2' : value2
    }
  
  ### 2
  list_name.append({
    'key' : value, 
    'key2' : value2
  })
  ``` 

## 4. 데이터 가공 - 새로운 값을 만들어 변환하기

  ### 과제 : 다른 key에서 value 값을 가져와 list를 만들고, value로 지정

  새로운 dict를 만들 때 value가 list이려면 어떻게 처리해야하는지 어려웠음
  <br>
  툭히 value에 넣어야 하는 값들이 다른 key에 있어서 난이도가 더 높았음
  
  -> dict 선언시 value를 []로 설정, 이후 

  ```python
  dict['key'].append(value)
  ```
  를 사용하여 value list에 값 추가
....



# 후기

API 사용법 알았으니 공모전에서 활용해야겠음
<br>
json 값을 dataframe으로 어떻게 만들지 공부하기
