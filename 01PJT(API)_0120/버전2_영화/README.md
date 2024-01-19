# PJT 01

### 이번 pjt 를 통해 배운 내용

API 사용
API -> json -> 데이터 처리 방법 습득
API 형식 적용 방법

## 1-a. 제공되는 도서 데이터의 주요 내용 수집

  ### 과제 : API를 json으로 입력 받아 데이터 재구조화

## 1-b. 제공되는 도서 데이터의 주요내용 수정

  ### 과제 : id 값만 존재하는 경우 상세 데이터에서 제목을 가져와 값 변경
  
  ! roop를 돌면서 일일히 값을 비교했는데 데이터가 많아지면 시간이 매우 오래 걸릴것으로 예상
  
  NTD : 알고리즘 공부하면서 비슷한 유형 있을 때 어떻게 처리하는지 공부하고 습득하기

## 1-c. 다중 데이터 분석 및 수정

  ### 과제 : 값이 여러개인 API를 입력 받았을 때 원하는 값만으로 재구조화

## 1-d. 알고리즘을 사용한 데이터 출력

  ### 과제 : 값이 높은 순대로 책 제목 출력

  - 처리방식 : 값이 max인 index를 받아 다른 list에 적용해서 가격이 가장 높은 책 제목 출력

  ! max인 값이 두 개일 때 위의 방식대로 처리하면 문제 발생

  NTD1 : 알고리즘 공부하면서 비슷한 유형 있을 때 어떻게 처리하는지 공부하고 습득하기
  <br>
  NTD2 : glob을 사용하여 폴더 안의 '*.json'을 불러오는 방식으로도 처리 가능 했음 **glob 공부하기**

## 1-e. 알고리즘을 사용한 데이터 출력

  ### 과제 : 값을 이용한 filtering

  - 처리방식 : enmerate 사용(index 처리를 위해), loop문을 돌면서 값을 확인하고 찾는 값과 일치하면 index를 사용하여 출력하였음

## 1-f1

  ### 과제 : filtering, 평점이 가장 높은 책 제목 출력

  ! 1-d와 같은 방식을 사용해서 같은 문제 발생

## 1-f2

  ### 과제 : filtering, 가격이 높은 순대로 책 제목 정렬

  NTD : 가격이 높은 순으로 책 제목 정렬하는 방식을 몰라서 chatgpt 사용했음, 유용한 코드 두 개 발견 했는데 앞으로 사용하기 위해서 공부하기
  <br>
  zip과 sort에 lambda를 사용하는 방식
  
  ```python
  book_names = ["BookA", "BookB", "BookC"]
  prices = [30, 20, 25]

  #### 1
  # 책 이름과 가격을 묶은 리스트를 생성
  book_price_pairs = list(zip(book_names, prices))

  # 가격을 기준으로 정렬
  sorted_book_price_pairs = sorted(book_price_pairs, key=lambda x: x[1])

  # 정렬된 결과를 출력
  for book_name, price in sorted_book_price_pairs:
      print(f"{book_name}: ${price}")

  #### 2
  # 인덱스를 기준으로 정렬된 순열의 인덱스 리스트를 얻음
  sorted_indices = sorted(range(len(prices)), key=lambda k: prices[k])

  # 정렬된 인덱스에 따라 책 이름을 출력
  for index in sorted_indices:
      print(f"{book_names[index]}: ${prices[index]}")
  ``` 

## 2-a : 제공되는 아티스트 데이터의 주요내용 수집

  ### 과제 : 1-a와 유사, 데이터 재구성

## 2-b : 제공되는 아티스트 데이터의 주요내용 수집

  ### 과제 : 1-b와 유사, id를 기준으로 값을 찾아 제목으로 변경

## 2-c : 다중 데이터 분석 및 수정

  ### 과제 : 1-c와 유사, 값이 여러개일 때 데이터 재구조화, 및 id값을 name으로 변경(2-b 코드 사용)
  
## 2-d : 알고리즘을 사용한 데이터 출력

  ### 과제 : 1-d와 유사, json이 여러개의 파일일 때 처리

## 2-e : 알고리즘을 사용한 데이터 출력

  ### 과제 : 1-e와 유사, filtering, 문자열 처리(:을 기준으로 다음 값)

## 2-f1

  ### 과제 : 2-e와 유사, filtering

## 2-f2

  ### 과제 : 장르가 특정 값을 포함할 때 이름 출력
  

## 후기

알고리즘 문제 풀면서 발생 했던 문제들인데 기억이 안 났음
<br>
-> 보고 끝나는게 아니라 공부해서 내 것으로 만들기
<br>
glob 공부하기

