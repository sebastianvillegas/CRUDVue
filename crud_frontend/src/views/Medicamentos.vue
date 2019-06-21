<template>
    <div class="medicamentos">
        <h1>Listado de medicamentos</h1>
        <table border="1">
            <tr>
                <td>Código</td>
                <td>Nombre</td>
                <td>Fecha</td>
                <td>Descripción</td>
            </tr>
            <tr v-for="medicamento in medicamentos">
                <td>{{medicamento.codigo}}</td>
                <td>{{medicamento.nombre}}</td>
                <td>{{medicamento.fecha_ven}}</td>
                <td>{{medicamento.descripcion}}</td>
            </tr>
        </table>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        mounted(){
            axios.get('http://127.0.0.1:8000/api/medicamentos/')
                .then((respuesta) => (
                    this.medicamentos=respuesta.data
                ))
        },
        data(){
           return {
               medicamentos:[]
           }
        }
    }
</script>

<style scoped>

</style>