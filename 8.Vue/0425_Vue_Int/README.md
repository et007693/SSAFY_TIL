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