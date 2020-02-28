<template>
  <div class="mainview">
    <h1>{{ msg }}</h1>
    <img alt="Vue logo" src="../assets/logo.png">
    <p>
      For a guide and recipes on how to configure / customize this project,<br>
      check out the
      <a href="https://cli.vuejs.org" target="_blank" rel="noopener">vue-cli documentation</a>.
    </p>
  </div>
</template>

<script>
export default {
  name: 'Mainview',
  props: {
    msg: String
  }
}
</script>
