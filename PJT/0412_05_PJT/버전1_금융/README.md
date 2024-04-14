# 프로젝트 내용
키워드 검색량 분석을 위한 데이터 수집

# 프로젝트 목표
크롤링 및 데이터 시각화 하여 rendering

## A(base.html)
다른 템플릿 경로로 이동할 수 있는 링크 출력
### 어려웠던 점
없음

## B(keyword.html)
검색하고자 하는 키워드를 추가 및 삭제할 수 있도록 구성
생성하기 및 삭제하기 버튼을 통해 keyword 테이블에 데이터를 저장 및 삭제하도록 구성
### 어려웠던 점
없음

## C(crawling.html)
keyword 테이블에 저장된 키워드들을 활용하여 크롬 검색 결과 페이지 크롤링을 수행   
페이지의 정보 중 검색 결과 개수 를 추출하여 Trend 테이블에 저장   
저장 시 이미 저장되어 있는 키워드라면, 새로 생성하지 않고 검색 결과 개수만 변경   
### 어려웠던 점
1. keyword DB에 저장되어 있는 keyword만 크롤링을 어떻게 할 것인가?   
Trend.object.all()을 했을 경우 Keyword에 없는 값들도 출력이 되었음   
-> context를 선언하고 크롤링을 수행하고 값을 추가하는 방식으로 변경

2. 이미 저장되어 있는 키워드일 때 변경을 어떻게 수행할 것인지?   
시도한 것 : get_or_create method를 사용했으나 실패   
-> create 부분에서 값이 입력되지 않아 오류 발생   
-> try, except를 사용하여 해결

## D(crawling_histogram.html)
전체 기간 검색 결과를 이용하여 막대 그래프를 출력
### 어려웠던 점
1. rendering과정에서 오류 발생   
figure 이미지를 rendering 하는 과정에서 제대로 출력되지 않는 오류가 발생   
-> endcode, decode 하는 부분 변경(replace 뒷부분 삭제)   

2. keyword 별로 색이 다른 그래프가 생성됨   
for문을 활용하여 plt.bar를 그렸을 때 keyword별로 다른 색이 나옴   
-> 값을 저장하고 plt.bar를 한 번에 수행   

## E(crawling_advanced.html)
검색 결과 페이지 중 '지난 1년'을 기준으로 필터링하여 크롤링을 수행
### 어려웠던 점
1. 검색 기간 '지난 1년'을 어떻게 설정할 것인가?   
시도한 것 : selenium을 사용하여 도구 -> 지난 1년 클릭 (url 변경이 효과적임)
```python
if year == True:
    url = f'https://www.google.com/search?q={keyword}&tbs=qdr:y'
else:
    url = f'https://www.google.com/search?q={keyword}'
```
위와 같이 url을 변경하여 year == True가 입력되었을 때만 url 변경하여 크롤링 실행