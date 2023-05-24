<template>
  <div>
    <h1>Перенаправление...</h1>
  </div>
</template>

<script>
export default {
  name: "redirect",
  mounted() {
    const slug = this.$route.params.slug;
    this.$http.get(/${slug})
        .then(response => {
          window.location.href = response.data.url
        })
        .catch(error => {
          console.error(error)
        })
  }

}
</script>

<style scoped>

</style>