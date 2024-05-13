<template>
    <div class="container-fluid">
        <div class="col-12 fs-3 fw-medium mt-3 border-bottom pt-3">Transactions</div>
        <div class="container mt-4 ">
            <div class="row">
                <div class="col-6 ">
                    <div class="col-4">
                        <select class="form-select" aria-label="Default select example " @change="getTransactions" v-model="filter">
                            <option value="all" selected>All Transactions</option>
                            <option value="1">Income</option>
                            <option value="0">Expense</option>
                        </select>
                    </div>
                </div>
                <div class="col-6">
                    <div class="d-flex justify-content-end">
                        <div class="light p-2 me-2">Available Balance <i class="ms-2 fa   fa-balance-scale"></i> </div>
                        <div class="border col-3 rounded-3 p-2 text-center text-success fw-medium"><i class="fa fa-inr" aria-hidden="true"></i>10,255</div>
                        <div class="btn btn-primary ms-5" @click="createTransact">Add New Transaction</div>
                    </div>
                </div>
            </div>
            <div v-if="modal" class="col-8 border border-success shadow bg-light" style="height: 80vh; z-index: 1; position:absolute; top: 150px;">
                <div class="btn btn-sm" @click="closeModal"><i class="fa fa-close fa-2x"></i></div>
                <div class="d-flex justify-content-center">
                    <p class="text-primary col-12 fw-bold border-bottom text-center"> Create A New Transaction !</p>
                </div>
                <div class="p-3 col-6 offset-3 border rounded-3 border-primary">
                    <div>
                        <p class="fs-5 text-muted">Date</p>
                        <datepicker v-model="picked" />
                    </div>
                    <div class="mt-3">
                        <p class="fs-5 text-muted">Amount</p>
                        <input v-model="amount" type="number" class="form-control" id="amountInput" placeholder="Enter amount">
                    </div>
                    <div class="">
                        <p class="fs-5 text-muted mt-3">Type</p>
                        <select class="form-select" id="typeSelect" v-model="type">
                            <option selected>Select type</option>
                            <option value="income">Income</option>
                            <option value="expense">Expense</option>
                        </select>
                    </div>
                    <div class="mt-3">
                        <p class="fs-5 text-muted">Description</p>
                        <textarea class="form-control" id="descriptionTextarea" rows="3" placeholder="Enter description" v-model="description"></textarea>
                    </div>
                    <div class="mt-3">
                        <label for="formFile" class="form-label">Or Select Receipt</label>
                        <input class="form-control" type="file" id="formFile" @input="uploadFile">
                    </div>
                </div>
                <div class="btn btn-primary col-6 offset-3 mt-3 rounded-4" @click="addTransact"> Add Transaction </div>          
            </div>
            <div class="col-10 rounded-3 bg-light border mt-4 p-3 offset-1">
                <div class="col-12 border" style="height:60vh; overflow-y: scroll;">
                    <table class="table table-striped" >
                <thead>
                    <tr>
                        <th class="fw-medium">#</th>
                        <th class="fw-medium">Amount</th>
                        <th class="fw-medium">Description</th>
                        <th class="fw-medium">Type</th>
                        <th class="fw-medium">Date</th>
                        <th class="fw-medium">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(transaction, index) in transactions" :key="index">
                    <td v-if="transaction.type == '1'" class="text-success">{{ index + 1 }}</td>
                    <td v-else class="text-danger">{{ index +1 }}</td>
                    <td v-if="transaction.type == '1'" class="text-success">{{ transaction.amount }}</td>
                    <td v-else class="text-danger">{{ transaction.amount }}</td>

                    <td v-if="transaction.type == '1'" class="text-success">{{ transaction.description }}</td>
                    <td v-else class="text-danger">{{ transaction.description }}</td>

                    <td v-if="transaction.type == '1'" class="text-success"> Income </td>
                    <td v-else class="text-danger"> Expense </td>

                    <td v-if="transaction.type == '1'" class="text-success">{{ formattedDate(transaction.date) }}</td>
                    <td v-else class="text-danger">{{ formattedDate(transaction.date)}}</td>

                    <td>
                        <div class="btn btn-light ms-2"><i class="fa fa-trash"></i></div>
                    </td>
                    </tr>
                </tbody>
                </table>
                </div>
               
            </div>
            
        </div>
    </div>
</template>

<script>
import Datepicker from 'vue3-datepicker'
import axios from 'axios'
export default{
    name:'Transaction',
    components: {
      Datepicker
    },
    data() {
    return {
        picked: new Date(),
        amount: '',
        description:'',
        type:'',
        modal: false,
        transactions: [],
        filter : 'all',
        file : null
    };
  },
  mounted(){
    this.getTransactions()
  },
  methods:{
    uploadFile(event){
        console.log('hello');
        this.file = event.target.files[0];
        const formData = new FormData();
        formData.append('file', this.file);

        axios.post('http://localhost:5000/uploads', formData, {
            headers: {
            'Content-Type': 'multipart/form-data'
            }
        })
        .then(response => {
            console.log(response.data);
            this.type = 'expense';
            this.amount = response.data['Total bill amount'];
            this.description = response.data['Store name']
            // this.picked = response.data['Date']
        })
        .catch(error => {
            console.error('Error uploading file', error);
        });
    },
    formattedDate(dates) {
      let date = new Date(dates);
      let day = date.getDate();
      let month = date.toLocaleString('default', { month: 'short' });
      let year = date.getFullYear();

      return `${day} ${month} ${year}`;
    },
    getTransactions(){
        console.log(this.filter)
       const userid = 1
       const filter = this.filter
       axios.post('http://localhost:5000/getTransaction',{userid,filter}).then(res => {
        console.log(res.data)
        this.transactions = res.data
       });
    },
    formatDate(date) {
        let day = date.getDate();
        let month = date.getMonth() + 1;
        let year = date.getFullYear();

        if (day < 10) {
            day = '0' + day;
        }
        if (month < 10) {
            month = '0' + month;
        }

        return year + '-' + month + '-' + day;
    },
    addTransact(){
        let picked_date = this.formatDate(this.picked)
        if(this.picked === ""){
            alert("pick a date")
            return
        }
        if(this.amount === ""){
            alert("Enter amount")
            return
        }
        if(this.type === ""){
            alert("pick a transaction type")
            return
        }
        if(this.description === ""){
            alert("Enter description")
            return
        }
        
        const params = {
            userid : 1,
            date : picked_date,
            amount : this.amount,
            type : this.type,
            description : this.description
        }
        axios.post('http://localhost:5000/createTransaction',params).then(response =>{
            this.picked = '';
            this.type = '';
            this.amount = '';
            this.description = '';
            this.getTransactions();
        })
        .catch(error => {
                    console.error('Error:', error);
        });
        
        },
    createTransact(){
        this.modal = !this.modal
    },
    closeModal(){
        this.modal = false;
        this.picked = new Date();
        this.type = '';
        this.amount = '';
        this.description = '';
    }
  }
}
</script>