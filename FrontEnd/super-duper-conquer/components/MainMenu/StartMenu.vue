<template>
    <div>
        <v-row>
            <v-col>
                <Panel/>
            </v-col>
            <v-col>
                <Panel/>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <Panel/>
            </v-col>
            <v-col >
                <Panel/>
            </v-col>
        </v-row>
    </div>
</template>

<script>
import Panel from '~/components/General/Panel.vue'
export default ({
  components: {
    Panel
  }
})
</script>
