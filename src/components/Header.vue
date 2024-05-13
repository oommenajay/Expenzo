<template>
    <div class="row bg-secondary" style="height: 8vh;">
        <div class="col-12 badge badge-primary text-end d-flex justify-content-end align-items-center" style="gap: 30px;">
            <p class="fw-bold fs-5 pt-3">Welcome! Ajay</p>
            <div class="btn border px-4 rounded-4" @click="this.$router.push('/')">Logout</div>
        </div>
    </div>
</template>
<script>
export default{
    name:'Header',
data(){
    return{

    }
}
}
</script>