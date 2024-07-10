# Vue

```html
<!-- vue import -->
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<!-- lodash import -->
<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>

<button v-on:click="func">+</button>

const { createApp, ref } = Vue

const app = createApp({
  setup() {
    const var1 = ref()
    const var2 = ref()
    ...
  
  const func = function() {
    statement
  }

<!-- prompt - 알림창 -->
  const func2 = function () {
    let inputValue = prompt('Enter new name:', user.value.name)
  }

  return {
    var1,
    var2,
    func
  }
  }
app.mount('#id')
})
```

# Basic Syntax1
```html
# v-html
<!-- tag를 포함한 html은 text로 인식하기 때문에 v-html 사용-->
<div v-html='rawhtml'></div>
const rawhtml = ref('<span style='color:red'>test</span>')

# v-bind -> :
<!-- html tag 내에서 {{}} 사용 불가 하므로 v-bind 사용 -->
<!-- 두 개가 같음 -->
<div v-bind:id='dynamicId'></div>
<div :id='dynamicId'></div>
const dynamicId = ref('my-id')

<!-- 동적 할당 -->
const key = ref('style')
const value = ref('red')
<button :[key]='value'></button>

<!-- class 정의 -->
const isboolean = ref(false)
const color = ref('red')
<div :class='{ active : isboolean, 'font-color':color }'></div>

<!-- class 정의 - object -->
const classObj = ref({
  active: false,
  'font-family': bold,
})
<div :class='classObj'></div>

<!-- style 정의 -->
const classObj = ref({
  active: false,
  'font-family': bold,
})
<div :style='classObj'></div>

<!-- v-on (event) -->
const count = ref(0)
<button @click='count++'>+</button>
<button @click='warning('경고입니다', $evnet)'>+</button>

<!-- form input -->
# v-bind v-on
const inputvalue = ref('')
const oninput = function(event) {
  inputvalue.value = event.currentTarget.value
}
<input :value='inputvalue' @input='oninput'>

# v-model
<!-- v-model = ''에 들어갈 값은 input에 맞는 값 -->
const inputvalue = ref('')
<input v-model='inputvalue'>
```

# Basic Syntax2
```html
<!-- computed -->
# 의존하는 데이터가 변경될 때 실행, html에서 name을 사용해서 값 return
const name = computed(() => {
  return statement
})

<!-- watch -->
watch(message, (newValue, oldValue) => {
  massageLength.value = newValue.length
})

<!-- if -->
<p v-if='boolean'>statement</p>
<p v-else='boolean'>statement2</p>

<!-- v-for -->
<div v-for='item in items' :key='item.pk'>
  {{ item.text }}
</div>
<div v-for='(item, key, index) in items' :key='item.pk'>
  {{ item.text }}
</div>

```

# Single File Component
```html
<!-- vite 프로젝트 생성 -->
$ npm create vue@latest

$ cd vue-project
$ npm install
$ npm run dev

<!-- import components -->
import { ref } from 'vue'
import name from '@/components/name.vue'
