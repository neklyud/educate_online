<template>
      <header class="modal-header">
        <slot name="header">
          Произошла ошибка
        </slot>
      </header>
      <section class="modal-body">
        <slot name="body">
          <ul>
            <li v-for="item in this.$parent.$parent.detail"  :key="item.detail">
              Поле: {{item["loc"][1]}}
              Текст ошибки: {{item["msg"]}}
            </li>
          </ul>
          Код ошибки: {{this.$parent.$parent.status}}
        </slot>
       </section>
</template>

<script>
    export default {
        name: 'Error',
    }
</script>