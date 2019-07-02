<template>
    <div class="medicamentos_crear">
        <h1 v-if="medicamento.id!=null">Editar entrada</h1>
        <h1 v-else>Creación de Medicamento</h1>
        <form action="">
            <label for="">Código</label>
            <input type="text" v-model="medicamento.codigo"> <br> <br>

            <label for="">Nombre</label>
            <input type="text" v-model="medicamento.nombre"> <br> <br>

            <label for="">Fecha de vencimiento</label>
           <input type="date" v-model="medicamento.fecha_ven"> <br> <br>

            <label for="">Descripción</label>
            <textarea name="" id="" v-model="medicamento.descripcion"> </textarea>
            <button v-if="medicamento.id!=null" @click.prevent="guardarMedicamento"  type="button" name="button">Editar Medicamento</button>
            <button v-else  @click.prevent="guardarMedicamento"  type="button" name="button">Crear Medicamento</button>
        </form>
    </div>
</template>

<script>

    import axios from 'axios'

    export default {
        name:"medicamentos_crear",

        mounted(){
          var id = this.$route.params.id

            if (id!=null){
                axios.get('http://127.0.0.1:8000/api/medicamentos/'+id)
              .then((respuesta) => (
                  this.medicamento=respuesta.data
              ))
            }
        },
        data(){
           return {
               medicamento:{id:null, codigo:"", nombre:"", fecha_ven:"", descripcion:""}
           }
        },
        methods:{
            guardarMedicamento(){
                var datos={
                    codigo: this.medicamento.codigo,
                    nombre: this.medicamento.nombre,
                    fecha_ven: this.medicamento.fecha_ven,
                    descripcion: this.medicamento.descripcion
                }

                var router = this.$router

                if (this.medicamento.id!=null){
                    axios.put('http://127.0.0.1:8000/api/medicamentos/'+this.medicamento.id+'/', datos)
                        .then((respuesta) => {
                        if(respuesta.statusText == "OK"){
                            router.push('/medicamentos')
                        } else {
                            alert('Error al editar el medicamento')
                        }

                    })
                } else {
                    axios.post('http://127.0.0.1:8000/api/medicamentos/', datos)
                    .then((respuesta) => {
                        if(respuesta.statusText == "Created"){
                            router.push('/medicamentos')
                        } else {
                            alert('Error al crear el medicamento.')
                        }
                    })
                }
            }
        }
    }

</script>

<style scoped>

</style>