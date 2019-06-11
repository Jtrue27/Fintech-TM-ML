<template>
  <div id="app" class="fillcontain">
    <transition mode="out-in">
      <router-view></router-view>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'app',
}
</script>
<style lang="scss" scoped>
  @import '~@/common/scss/base';
</style>