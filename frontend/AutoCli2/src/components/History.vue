<!-- <script setup lang="ts">
  import devices from "./assets/devices.json"
  import { ref, watch } from 'vue'

  const count = ref(0)
  const status = ref(false)
  const search = ref("")
  const displayObjects = ref(devices)

  watch(search, () => {
    displayObjects.value = devices.filter(device => device.name.toLowerCase().includes(search.value.toLowerCase()))
  })

  fetch("http://127.0.0.1:8000/api-inventory/host/", {
    headers: {
      "Authorization": "Token " + "28befc9a9922fa6644c7fd70d5ee5fcd51246823"
    }
  }).then( resp => {
    if(!resp.ok) {
      return {}
    } else {
      return resp.json();
    }
  }).then( rest_object => {
    devices = ref(rest_object.page_results)
  });

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
    <button @click="status = true">Open</button>
    <button @click="status = false">Close</button>
    <div v-if="status">Window</div>
    <input v-model.trim="search" type="text" placeholder="Search...">
    <div class="box">
      <div v-for="device in displayObjects" :key="device.pk" class="box_item">
        <h3>{{ device.name }}</h3>
        <span>
          <p>Hostname:</p>
          <p>{{ device.hostname }}</p>
        </span>
        <span>
          <p>Description:</p>
          <p>{{ device.description }}</p>
        </span>
        <span>
          <p>Site:</p>
          <p>{{ device.site }}</p>
        </span>
        <span>
          <p>Platform:</p>
          <p>{{ device.platform }}</p>
        </span>
        <span>
          <p>Credential:</p>
          <p>{{ device.credential }}</p>
        </span>
      </div>
    </div>
  </main>
</template>

<style scoped>
  .box {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr; 
  }
  .box_item {
    background-color: #eee;
    padding: 10px;
    margin: 10px;
    display: flex;
    flex-direction: column;
  }
  .box_item > span {
    display: flex;
    flex-direction: row;
  }
  .box_item > span p {
    padding: 2px;
  }
</style> -->
