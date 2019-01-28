<template>
<div> logout page </div>
</template>

<script>
import * as types from '@/store/mutation-types'
export default {
  mounted() {
    // `this` works in mounted mode.
    let redirect = decodeURIComponent(this.$route.query.redirect ||
      '/')
    this.$store.commit(types.LOGOUT, {
      redirect: redirect
    })
  }
}
</script>
