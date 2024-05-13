<template>
        <div class="container-fluid">
            <div class="col-12 fs-3 fw-medium mt-3 border-bottom pt-3">Dashboard</div>
            <div class="d-flex">
                <div>
                    <div class="ms-4 d-flex">
                        <div class="col-2 border rounded-3 mt-4 p-3" style="min-height: 150px; min-width: 25vh;">
                            <div class="d-flex justify-content-between">
                                <div>
                                    <div><i class="fa-solid fa-sack-dollar fa-2x"></i></div>
                                    <div class="text-secondary">Revenue</div>
                                </div>
                                <div>
                                    <circle-progress :percent="40" fill-color="#008000" style="width: 55px; height: 0px;"/>
                                    <p class="ms-2 mt-3 small text-success">+38%</p>
                                </div>
                            </div>
                        
                            <div class="fs-3 fw-bold"><i class="fa fa-inr" aria-hidden="true"></i> {{ revenue[0] }}</div>
                            <div class="small text-center text-secondary">Total amount of money generated</div>

                        </div>
                        <div class="col-2 border rounded-3 mt-4 p-3 ms-5" style="min-height: 150px; min-width: 25vh;">
                            <div class="d-flex justify-content-between">
                                <div>
                                    <div><i class="fa fa-paper-plane fa-2x"></i></div>
                                    <div class="text-secondary">Expenses</div>
                                </div>
                                <div>
                                    <circle-progress :percent="-28" fill-color="#cc0000" style="width: 55px; height: 0px;"/>
                                    <p class="ms-2 mt-3 small text-danger">-28%</p>
                                </div>
                            </div>
                        
                            <div class="fs-3 fw-bold"><i class="fa fa-inr" aria-hidden="true"></i> {{ revenue[1] }}</div>
                            <div class="small text-center text-secondary">Total amount of money expended</div>

                        </div>
                        <div class="col-2 border rounded-3 mt-4 p-3 ms-5" style="min-height: 150px; min-width: 25vh;">
                            <div class="d-flex justify-content-between">
                                <div>
                                    <div><i class="fa fa-piggy-bank fa-2x"></i></div>
                                    <div class="text-secondary">Savings</div>
                                </div>
                                <div>
                                    <circle-progress :percent="38" fill-color="#008000" style="width: 55px; height: 0px;"/>
                                    <p class="ms-2 mt-3 small text-success">+38%</p>
                                </div>
                            </div>
                        
                            <div class="fs-3 fw-bold"><i class="fa fa-inr" aria-hidden="true"></i> 1,022</div>
                            <div class="small text-center text-secondary">Total amount of money Saved</div>

                        </div>
                        <div class="col-2 border rounded-3 mt-4 p-3 ms-5" style="min-height: 150px; min-width: 25vh;">
                            <div class="d-flex justify-content-between">
                                <div>
                                    <div><i class="fa   fa-balance-scale fa-2x"></i></div>
                                    <div class="text-secondary">Balance</div>
                                </div>
                                <div>
                                    <circle-progress :percent="18" fill-color='#008000' style="width: 55px; height: 0px;"/>
                                    <p class="ms-2 mt-3 small text-sucsess">18%</p>
                                </div>
                            </div>
                        
                            <div class="fs-3 fw-bold"><i class="fa fa-inr" aria-hidden="true"></i> {{ revenue[0] - revenue[1] }}</div>
                            <div class="small text-center text-secondary">Total Balance Amount</div>

                        </div>

                    </div>
                    <div class="d-flex ms-4 mt-4">
                        <div class="border rounded-3 col-7  p-3">
                            <div class="d-flex justify-content-between  ">
                                <p class="fs-5  fw-medium">Finance Insights</p>
                                <div class="lead">
                                    <div class="btn border btn-light lead">1W</div>
                                    <div class="ms-2 btn border btn-light lead">1M</div>
                                    <div class="ms-2 btn border btn-light lead">3M</div>
                                    <div class="ms-2 btn border btn-light lead">6M</div>
                                    <div class="ms-2 btn border btn-light lead">1Y</div>
                                </div>
                            </div>
                            <div class="mt-3">
                                <div class="btn btn-light border" @click="revenues">Revenue</div>
                                <div class="ms-3 btn btn-light border" @click="getExpenses">Expenses</div>
                            </div>
                            <div class="fs-3 fw-bold mt-3">{{ chartRevenue }}</div>
                            <div class="">
                                <apexchart width="600" height="300" type="area" :options="options" :series="series"></apexchart>
                            </div>
                        </div>
                        <div class="col-4 border ms-5 rounded-3">
                            <div class="d-flex p-3 justify-content-between">
                                <div class="fs-5 fw-medium">Expense Overview</div>
                                <div>
                                    <select class="form-select form-select-sm" aria-label=".form-select-sm example">
                                    <option selected>Filter By Range</option>
                                    <option value="1">This Week</option>
                                    <option value="2">This Month</option>
                                    <option value="3">Today</option>
                                    </select>
                                </div>
                            </div>
                            <div id="chart" class="mt-4 mx-auto ms-3">
                                <apexchart type="donut" width="350" :options="chartOptions" :series="series1"></apexchart>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-3 mt-4 border me-3 rounded-3"> 
                    <div class="fs-5 fw-medium text-center mt-3">Recent Transactions</div>
                    <div class="col-10 border offset-1 mt-3" style="min-height: 60vh;" >
                        <div class="col-12 d-flex" v-for="(transact,index) in transactions" :key="index">
                            <div v-if="transact.type == '1'" class="col-6 bg-light text-success p-2">{{ transact.description }}</div>
                            <div v-else class="col-6 bg-light text-danger p-2">{{ transact.description }}</div>
                            <div v-if="transact.type == '1'" class="col-6 bg-white text-success p-2">{{ transact.amount }}</div>
                            <div v-else class="col-6 bg-white text-danger p-2">{{ transact.amount }}</div>
                        </div>               
                    </div>
                    <div class="d-flex justify-content-center mt-4"><div class="btn btn-light border " @click="this.$router.push('/transaction')">View All</div></div>
                </div>
            </div>      
        </div>
</template>

<script>
import "vue3-circle-progress/dist/circle-progress.css";
import CircleProgress from "vue3-circle-progress";
import VueApexCharts from "vue3-apexcharts";
import axios from 'axios'
export default{
    components: {
        CircleProgress,
        apexchart: VueApexCharts,
    },
    name :'Dashboard',
    mounted(){
        this.getIncomes();
        this.getRevenue();
        this.getDonutExpenses();
        this.getExpenseLabels();
        this.getTransactions();
    },
    data(){
        return{
            transactions: [],
            revenue : [],
            chartRevenue : [],
            userid : '1',
            options: {
                chart: {
                id: 'vuechart-example',
                type: 'area',
                xaxis:{
                    categories: ['January', 'February',]
                }
                },            
            },
            series: [{
            name: 'series1',
            data: []
            }],
            series1: [],
            chartOptions: {
            chart: {
              type: 'donut',
            },
            legend:{
                show: true,
                position: 'bottom',
            },
            plotOptions: {
                pie: {
                    donut: {
                        size: '60%'
                    }
                }
            },
            labels : []
            },
        
        }
    },
    methods:{
        getTransactions(){
            console.log(this.filter)
            const userid = 1
            const filter = 'all'
            axios.post('http://localhost:5000/getTransaction',{userid,filter}).then(res => {
            console.log(res.data)
            this.transactions = res.data
            });
        },
        revenues(){
            this.series[0].data = []
            this.chartRevenue = this.revenue[0]
            this.getIncomes();
        },
        getRevenue(){
            let userid = this.userid;
            axios.post('http://localhost:5000/getRevenue',{userid}).then(res => {
            this.revenue = res.data
            this.chartRevenue = this.revenue[0]
            }
            )
            .catch(error => {
                    console.error('Error:', error);
            });
        },
        getIncomes(){
            let userid = this.userid;
            axios.post('http://localhost:5000/getIncomes',{userid}).then(res =>{
                console.log(res.data)
                console.log(this.series[0].data)

                res.data.forEach(value => {
                    this.series[0].data.push(parseFloat(value[0]));
            });
            })
        },
        getExpenses(){     
            this.chartRevenue = this.revenue[1]       
            let userid = this.userid;
            axios.post('http://localhost:5000/getExpenses',{userid}).then(res =>{

                this.series[0].data = [];
                this.series1 = [];
                res.data.forEach(value => {
                    this.series[0].data.push(parseFloat(value[0]));
                    this.series1.push(parseInt(value[0]));
            });
            })
        },
        getDonutExpenses(){     
            this.series1 = []
            let userid = this.userid;
            axios.post('http://localhost:5000/getExpenses',{userid}).then(res =>{
                res.data.forEach(value => {
                    this.series1.push(parseInt(value[0]));
            });
            })
        },
        getExpenseLabels(){
            this.chartOptions.labels = []
            let userid = this.userid;
            axios.post('http://localhost:5000/getlabels',{userid}).then(res =>{
                res.data.forEach(value => {
                    this.chartOptions.labels.push((value[0]));
            });
            console.log(this.chartOptions.labels)
            })
        }
    }
        
}


</script>