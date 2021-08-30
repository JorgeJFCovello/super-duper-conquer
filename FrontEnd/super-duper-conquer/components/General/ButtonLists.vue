<template>
    <div>
        <v-row v-for="button in buttons" :key="button.name">
            <v-col py-2 my-2 align="center">
                <v-btn elevation="1" dark :to="button.route" color="#283593">
                    {{ button.name }}
                </v-btn>
            </v-col>
        </v-row>
    </div>
</template>


<script>
export default ({

    props: {
        buttons: {
            type: Array,
            require: true
        }
    },
    methods: {
       getButtonName(aButton){
           return aButton.name
       } 
    }
})
</script>