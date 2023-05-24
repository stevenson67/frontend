<template>
  <div>
    <h1>Сокращение ссылок</h1>
    <input v-model="url" type="text" placeholder="Введите ссылку">
    <button @click="shortenLink">Сократить</button>
    <div v-if="shortenedLink">
      <p>Ваша сокращенная ссылка:</p>
      <a :href="shortenedLink" target="_blank">{{ shortenedLink }}</a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'heroIndex',
  data() {
    return {
      url: '',
      shortenedLink: ''
    }
  },
  methods: {
    shortenLink() {
      this.$http.post('/shorten', { url: this.url })
          .then(response => {
            this.shortenedLink = response.data.short_url
          })
          .catch(error => {
            console.error(error)
          })
    }
  }
}
</script>
