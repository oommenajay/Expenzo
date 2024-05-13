<template>
    <div class="row">
        <div class="bg-light border-bottom d-flex align-items-center justify-content-between"> 
            <p class="lead mt-3">Maintain your Budgets</p>
            <div class="btn btn-success btn- rounded-5 " @click="createBudget"><i class="fa fa-plus" aria-hidden="true"></i><span class="px-2">Add New</span></div>
        </div>
        <div v-if="modal" class="col-6 border border-success shadow offset-2 bg-light rounded-3" style="height: 50vh; z-index: 1; position:absolute; top: 150px;">
            <div class="mt-3 btn btn-sm" @click="closeModal"><i class="fa fa-close fa-2x"></i></div>
            <div class="d-flex justify-content-center">
                <p class="p-1 text-primary rounded-2 fw-bold"> Create A New Budget !</p>
            </div>
            <div class="col-8 border border-primary offset-2 rounded bg-white p-5 mt-5 ">
                <select class="form-select form-select-lg mb-3" aria-label=".form-select-lg example" v-model="category_id" >
                    <option value="" disabled selected>Select Category</option>
                    <option v-for="(value,index) in category" :key="index" :value="value.id" >{{value.category_name}}</option>
                </select>
                <div class="input-group">
                    <input type="text" class="form-control" placeholder="Enter Monthly Budget" v-model="budget"> 
                </div>
            </div>
            <div class="col-4 btn btn-success px-4 rounded-4 offset-4 mt-5" @click="setBudget"><span class="fw-medium">Submit</span></div>
        </div>
        <div>
            <div class="d-flex m-4" style="gap: 30px;">
                <div class="col-2 rounded border border-primary bg-light p-3 d-flex align-items-center justify-content-around">
                    <i class="fa fa-ticket fa-3x text-primary" aria-hidden="true"></i>
                    <div>
                        <p>Overall Budgeted</p>
                        <p class="text-end lead fw-bold">{{ totalAmount }}</p>
                    </div>
                </div>
                <div class="col-2 rounded border border-primary bg-light p-3 d-flex align-items-center justify-content-around">
                    <i class="fa fa-paper-plane fa-3x text-primary" aria-hidden="true"></i>
                    <div>
                        <p>Total Expended</p>
                        <p class="text-end lead">15,000</p>
                    </div>
                </div>
                
            </div>
            
            <div class="container mt-3 text-center">
                <div class="lead text-success"> Your Monthly Budgets </div>                
            </div>
            <div class="d-flex p-5 justify-content-center col-10 flex-wrap offset-1" style="gap: 25px;">
                <div class="col-3 border border-success rounded-3 bg-light p-3 d-flex justify-content-around " v-for="(budget,index) in myBudgets" :key="index">
                    <div class="">
                        <i class="fa fa-ticket fa-2x text-primary" aria-hidden="true"></i>
                    </div>
                    <div>
                        <p class="fw-medium">{{ budget.category_name }}</p>
                        <p class="text-end fw-bold fs-3">{{ budget.amount }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
export default{
    name: 'Budget',
    data(){
        return{
            category_id: '',
            budget: '',
            modal: false,
            category: [],
            myBudgets: []
        }
    },
    mounted(){
        this.getCategory();
        this.getBudgets();
    },
    computed:{
    totalAmount() {
      return this.myBudgets.reduce((total, item) => total + parseFloat(item.amount), 0);
    }
    },
    methods:{
        getBudgets(){
            const userid  = 1;
            axios.post('http://localhost:5000/getBudgets',{userid}).then(response => {
                    this.myBudgets = response.data
                    console.log(this.myBudgets)
                })
        },
        setBudget(){
            if(this.budget == ''){
                alert("budget cannot be empty");
            }
            if(this.isNumeric(this.budget)){
                const params ={
                    budget : this.budget,
                    category : this.category_id
                }
                axios.post('http://localhost:5000/createBudget',{params}).then(response => {
                    this.closeModal();
                    this.getBudgets();
                })
                .catch(error => {
                    console.error('Error:', error);
                });
                    console.log(params)
            }
            else {
                alert("Please enter a valid amount")
            }
        },
        isNumeric(input) {
        var regex = /^[0-9]+$/;
            return regex.test(input);
        },
        getCategory(){
            axios.post('http://localhost:5000/getCategory').then(response => {
              console.log(response.data);
              this.category = response.data;
              console.log(this.category)
          })
          .catch(error => {
              console.error('Error:', error);
          });
        },
        createBudget(){
            this.modal = !this.modal
        },
        closeModal(){
            this.modal= false;
            this.budget='';
            this.category_id='';
        }
    }
}
</script>
