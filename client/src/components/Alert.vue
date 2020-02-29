<template>
  <b-alert variant='success' show>{{ message }}</b-alert>
</template>
<script>
export default {
  props: ['message'],
}
</script>