# 선택 메서드
```javascript
//  요소 한 개 선택
document.querySelector()

//  요소 여러 개 선택
document.querySelectorAll()
```

# DOM 조작
```javascript
# 클래스 속성 조작 메서드
//  classList - 클래스 목록을 DOMTokenList(유사 배열) 형태로 변환

// 지정한 클래스 값을 추가
element.classList.add()

// 지정한 클래스 값을 제거
element.classList.remove()

// 클래스가 존재한다면 제거 + false, 존재하지 않으면 클래스 추가 + true
element.classList.toggle()
```

```javascript
# 일반 속성 조작 메서드
// 해당 요소에 지정된 값을 반환
element.getAttribute()

// 지정된 요소의 값을 설정, 이미 있다면 값을 갱신
element.setAttribute(name, value)

// 요소에 지정된 이름을 가진 속성 제거
element.removeAttribute()
```

```javascript
# HTML 콘텐츠 조작
element.textContent
```

```javascript
# DOM 요소 조작 메서드
// 작성한 tagName의 HTML요소를 생성하여 반환
document.createElement(tagName)

// 한 Node를 특정 Node의 자식 NodeList 중 마지막 자식으로 삽입 후 추가된 객체를 반환
Node.appendChild()

// DOM에서 자식 Node를 제거, 제거된 객체를 반환
NOde.removeChild()
```

```javascript
# style 조작
pTag.style.color = 'crimson'
pTag.style.fontSize = '2rem'
pTag.style.border = '1px solid black'
```

# 함수
```javascript
# 선언식
function name() {
}

# 표현식
const name = function() {
}
## 화살표 함수
const name = param => statement

# 객체 구조
const user = {
  name: 'alice',
  'key with space' : true,
  greeting() {
    return 'hello'
  }
}
```

# 배열
```javascript
# method
push / pop
unshift / shift

# Array Helper Method
// filter, find, some, every
# foreach
const numbers = [1,2,3]
// 1
numbers.forEach(function (num)){}
// 2
const name = function(num) {}
number.forEach(name)

# map
// 1
const arr2 = arr.map(function (param)) {}
// 화살표 함수
const arr2 = arr.map((param) => {})
```

```javascript
# n번째 요소 선택
const list1 = document.querySelector('li:nth-child(1)')
const contact = document.querySelector('h2:nth-of-type(3)')
```