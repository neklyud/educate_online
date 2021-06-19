<template>
    <header>
        <slot name="header">Результат</slot>
    </header>
    <section class="modal-body">
        <slot name="body">
          {{this.$parent.$parent.result}}
        </slot>
    </section>
</template>

<script>
    export default {
        name: "Result",
    }
</script>