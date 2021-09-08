<template>
    <div>
        <v-row>
            <v-col>
                <ButtonLists :buttons="buttons"/>
            </v-col>
        </v-row>
    </div>
</template>

<script>
import ButtonLists from '~/components/General/ButtonLists.vue'
export default ({
  components: {
    ButtonLists
  },
  data() {
      return {
        buttons: [ 
            {
                name:'Crear Partida',
                route: 'newGame'
            },
            {
                name:'Buscar Partida',
                route: 'findGame'
            },
            {
                name:'Opciones',
                route: 'options'
            },
            {
                name:'Reglas',
                route: 'rules'
            },
            {
                name:'Logout',
                route: '/'
            } 
        ]
        }
      }
  }
)
</script>
