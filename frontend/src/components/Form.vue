<template>
  <form v-on:submit.prevent="onSubmit">
  <p>
    <input id="number1" name="number1" v-model="RequestData.number1">
  +
    <input id="number1" name="number1" v-model="RequestData.number2">
  </p>
  <input type="submit" value="Результат">
  </form>
</template>


<script>
import axios from "axios"

  export default {
    data() {
      return {
        RequestData: {
          number1: 0,
          number2: 0
        },
      }
    },
    methods: {
      onSubmit() {
        try {
          let response = axios.post("/api/calc",  this.RequestData).then(
            (response) => {
              this.$parent.setResult(response)
            }, (error) => {
              this.$parent.showModal(error.response)
              this.result = response
            }
          )
          return response;
        } catch(e) {
            this.console.log(e)
        }
      }
    }
  }
</script>