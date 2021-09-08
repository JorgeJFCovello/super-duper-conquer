<template>
  <div >
      <v-row>
        <v-text-field label="Username!" title="username" v-model="username" @keyup.enter="enterInSystem(username)"/>
      </v-row>
      <v-row>
        <v-btn block @click="enterInSystem(username)">
            log in!
        </v-btn>
      </v-row>
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
            this.$router.push('/mainMenu');
            return value;
        }
    }
}
</script>

