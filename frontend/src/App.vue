<template>
  <Modal v-show="isModalVisible" @close="closeModal">
  </Modal>
    <div id="IndexPage">
        <h1>Калькулятор</h1>
        <h2>Тестовое задание Educate online.</h2>
        <hr>
        <Form />
    </div>
</template>

<script>
import Form from './components/Form.vue'
import Modal from './components/Modal.vue'

export default {
  name: 'App',
  components: {
    Form,
    Modal,
  },
  data () {
    return {
      isModalVisible: false,
      detail: [],
      status: 200,
      statusText: "",
      result: '',
    }      
  },
  methods: {
    closeModal() {
      this.isModalVisible = false
    },
    setErrorData(data) {
      this.isModalVisible = true
      this.detail = data["data"]["detail"]
      this.status = data["status"]
      this.statusText = data["statusText"]
    },
    setResult(data) {
      this.isModalVisible = true
      this.status = data["status"]
      this.result = data.data["result"]
    },
    showModal(data) {
      if (data["status"] >= 400 && data["status"] < 500) {
        this.setErrorData(data)
      }
      console.log(data)
      if (data["status"] === 200) {
        console.log("Status is 200")
        this.setResult(data)
      }
    },
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
