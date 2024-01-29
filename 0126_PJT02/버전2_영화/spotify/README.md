# PJT 02

## 어려웠던 내용

1. API 설명 페이지가 깔끔하지 않아 찾기 힘들었음

2. 기존 API 실습과 데이터 받는 방식이 달라서 낯설었음
    
    - headers 추가 : 이게 어떤것인지 몰라 파악하는 데 시간이 걸렸음, 기존엔 api key를 직접 입력 했다면, getHeaders라는 module을 만들어 api key 입력하고 access token을 발급 받아 데이터를 요청하는 듯
    - q : query 입력 방식이 낯설었음, 'artist : name genre : name' 이런 식으로 따로 입력하지 않고 띄어쓰기를 기준으로 구분하는 방식
    - problem_a : 예시를 보면 차트 순으로 값이 나오는 것 같은데 이렇게 하려면 어떻게 해야 되는지 모르겠음

## 새로 안 내용

1. 이름과 값을 받았을 때 값을 기준으로 정렬하고 이름을 출력하는 방법(sorted에 key 사용)

```python
music_list = [music[0] for music in sorted(music_list, key = lambda x : x[1], reverse=True)]
```