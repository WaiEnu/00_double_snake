<template>
  <div class="top">
    <Mainview msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Mainview from '@/components/Mainview.vue'

export default {
  name: 'Top',
  components: {
    Mainview
  }
}
</script>