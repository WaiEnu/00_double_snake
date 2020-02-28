<template>
  <div class="resultview">
    <div class="vue">
      <ul class="tabs">
        <li class="nav-item global origin">
          origin
        </li>
        <li class="nav-item global mutate">
          mutate
        </li>
      </ul>
      <div class="contents">
        <div id="table_origin">
          ## table_o ##
        </div>
        <div id="read_origin">
          ## read_o ##
        </div>
      </div>
      <div class="contents">
        <div id="table_mutate">
          ## table_m ##
        </div>
        <div id="read_mutate">
          ## read_m ##
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Resultview',
}
</script>
