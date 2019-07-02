<template>
    <div class="medicamentos">
        <h1>Listado de medicamentos</h1>
        <router-link :to="{name:'medicamentos-crear'}">Crear Medicamento</router-link>
        <table border="1">
            <tr>
                <td>Código</td>
                <td>Nombre</td>
                <td>Fecha</td>
                <td>Descripción</td>
                <td>Acción</td>
            </tr>
            <tr v-for="medicamento in medicamentos">
                <td>{{medicamento.codigo}}</td>
                <td>{{medicamento.nombre}}</td>
                <td>{{medicamento.fecha_ven}}</td>
                <td>{{medicamento.descripcion}}</td>
                <td>
                    <router-link :to="{name:'medicamentos-editar', params:{id:medicamento.id}}">Editar</router-link> |
                    <a @click.prevent="eliminarMedicamento(medicamento.id)" href="#">Eliminar</a>

                </td>

            </tr>
        </table>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        mounted(){
            this.cargarMedicamentos()
        },
        data(){
           return {
               medicamentos:[]
           }
        },
        methods:{
            cargarMedicamentos(){
                axios.get('http://127.0.0.1:8000/api/medicamentos/')
                .then((respuesta) => (
                    this.medicamentos = respuesta.data

                ))
            },

            eliminarMedicamento(id){

                var op = window.confirm("Desea eliminar el medicamento?")

                if(op){
                    axios.delete('http://127.0.0.1:8000/api/medicamentos/'+id+'/')
                    .then(() => {
                        this.cargarMedicamentos()
                    })
                    alert("Registro eliminado correctamente")
                }
            }
        }
    }
</script>

<style scoped>

</style>