# PJT02_금융

## 느낀점

```python
data.groupby(data['Date'].dt.strftime('%Y-%m'))['Close'].mean().plot()
```
datetime 처리는 항상 어려운 것 같음   
strftime 활용 잘 하기!
>%y : 두 자리 수의 연도    
%Y : 네 자리 수의 연도   
%m : 0을 채운 두 자리 수의 월    
%d : 0을 채운 두 자리 수의 일    
%I : 0을 채운 12시간제의 시간    
%H : 0을 채운 24시간제의 시간    
%M : 0을 채운 두 자리 수의 분    
%S : 0을 채운 두 자리 수의 초 

