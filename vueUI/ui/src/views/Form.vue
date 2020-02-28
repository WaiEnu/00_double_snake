<template>
  <div class="form">
    <Formparts/>
    <Graphparts/>
  </div>
</template>

<script>
// @ is an alias to /src
import Formparts from '@/components/Formparts.vue'
import Graphparts from '@/components/Graphparts.vue'


export default {
  name: 'Form',
  components: {
    Formparts,
    Graphparts
  },
}
</script>