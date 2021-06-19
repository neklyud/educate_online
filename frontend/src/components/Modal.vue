<template>
  <div class="modal-backdrop">
    <div class="modal">
      <div v-if="this.$parent.status === 200">
        <Result/>
      </div>
      <div v-else>
        <Error/>
      </div>
      <button type="button" class="btn-close" @click="close">Закрыть</button>
    </div>
  </div>
</template>

<script>
import Error from './Error.vue'
import Result from './Result.vue'

  export default {
    name: 'Modal',
    components: {
      Error,
      Result,
    },
    data () {},
    methods: {
      close() {
        this.$emit('close');
      }
    },
  };
</script>

<style>
  .modal-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .modal {
    position: fixed;
    background-color: #fefefe;
    margin: 15% auto; /* 15% from the top and centered */
    padding: 20px;
    border: 1px solid #888;
    width: 80%; /* Could be more or less, depending on screen size */
  }
</style>
