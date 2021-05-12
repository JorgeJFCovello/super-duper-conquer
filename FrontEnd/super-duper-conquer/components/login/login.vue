<template>
  <div >
    <v-card raised class="center_class" width="50%" height="50%"  title="welcome">
      <v-text-field label="Username!" title="username" v-model="username" @enter="enterInSystem(username)"/>
      <v-btn mx-2 @click="enterInSystem(username)">
          log in!
      </v-btn>
    </v-card>
  </div>
</template>

<script>

export default {
    data() {
        return { 
            username: null
        }
    },
    methods: {

        enterInSystem(value) {
            return value;
        }
    }
}
</script>


<style scoped>
.center_class {
  margin: 20%;
  border: 3px solid green;
  padding: 10px;
}
</style>