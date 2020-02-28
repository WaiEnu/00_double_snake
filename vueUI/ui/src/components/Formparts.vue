<template>
  <div class="formparts">
    <div class="formset">
      <form id="generate">
        <div class="fieldset">
          <label class="field_input" for="length">塩基長：<input name="length" id="length" type="number" step="100" min="100" max="10000" v-model.number="length"></label>
          <label class="field_input" for="locate">変異導入箇所：<input name="locate" id="locate" type="range" value="1" step="1" min="1" v-bind:max="length">{{ length }}</label>
          <label class="field_input" for="iteration">配列本数：<input name="iteration" id="number" type="number" value="1000" step="1" min="1" max="10000"></label>
          <label class="field_input" for="base">導入変異：<select name="base" id="base">
            <option value="1">A挿入</option>
            <option value="2">G挿入</option>
            <option value="3">C挿入</option>
            <option value="4">T挿入</option>
            <option value="5">削除</option>
          </select></label>
        </div>
        <div class="field_btn"><input type="submit" value="送信"></div>
      </form>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { mapActions } from 'vuex'
export default {
  name: 'Formparts',
  data: function(){
    return {
      length: this.$store.state.length,
    }
  },
  computed: {
    ...mapGetters(['getLength'])
  },
  methods: {
    ...mapActions(['setLength'])
  }
}
</script>
