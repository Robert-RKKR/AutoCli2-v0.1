<script setup lang="ts">
  import { ref } from 'vue'
  const count = ref(0)

  var socket = new WebSocket("ws://127.0.0.1:8000/ws/notification/");

  socket.onmessage = function(event) {
    var collect = event.data;
    var collect_json = JSON.parse(collect)
    console.log(collect_json)
  }
</script>

<template>
  <main>
    <h1>AutoCli2</h1>
    <p>
      Welcome on AutoCli2 page.
    </p>
    <p>{{ count }}</p>
    <button @click="count--">-</button>
    <button @click="count++">+</button>
  </main>
</template>

<style scoped>
</style>
