<template>
    <div>
         <div class="d-flex flex-column flex-shrink-0 p-3 border min-vh-100 pull-left" style="width: 280px;">
            <div class="text-center fs-2 fw-medium text-muted">Expenzo</div>
             <div class="mt-5 text-center">
                <div class="border rounded-4 bg-light d-flex justify-content-between align-items-center px-3">
                    <span><i class="fa fa-home "></i></span>
                    <span @click="this.$router.push('/')" class="btn">Home</span>
                </div>
                <div class="border rounded-4 bg-light d-flex justify-content-between align-items-center px-3 mt-3">
                    <span><i class="fa fa-dashboard "></i></span>
                    <span @click="this.$router.push('/dashboard')" class="btn">Dashboard</span>
                </div>
                <div class="border rounded-4 bg-light d-flex justify-content-between align-items-center px-3 mt-3">
                    <span><i class="fa fa-ticket "></i></span>
                    <span @click="this.$router.push('/transaction')" class="btn">Transaction</span>
                </div>
                <div class="border rounded-4 bg-light d-flex justify-content-between align-items-center px-3 mt-3">
                    <span><i class="fa fa-dollar "></i></span>
                    <span @click="this.$router.push('/budget')" class="btn">Budgets</span>
                </div>

             </div>               
                
        </div>
    </div>
</template>

<script>
import { RouterLink} from 'vue-router'
export default{
 name : 'Sidebar'
}
</script>