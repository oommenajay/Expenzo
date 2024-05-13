<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-7 bg-light" style="max-height: 90vh;">
        <div class="position-absolute" style="top: 70%; left: 5%;">
          <p class="display-2 text-primary">Expenzo.</p>
          <p class="lead text-secondary btn btn-light border p-3">AI powered budget manager</p>
        </div>
        <img src="../assets/auth-v2-login-illustration-light-C3P37pvv.png" class="img-fluid" style="height: 100vh;" alt="">
      </div>
      <div class="col-5 d-flex justify-content-center p-5" style="height: 100vh;">
        <div class="col-9 p-5 rounded-4 shadow-sm">
          <p class="fs-4 mb-0">Welcome to Expenzo.</p>
          <p v-if="signup" class="light text-muted mt-">Create New Account</p>
          <p v-else class="light text-muted mt-">Please sign into your account and start the adventure</p>
          <form action="">
            <div class="form-group mt-5" v-if="signup">
              <label for="exampleFormControlInput1">Username</label>
              <input type="email" v-model="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
            </div>
            <div class="form-group mt-3">
              <label for="exampleFormControlInput1">Email address</label>
              <input type="email" v-model="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
            </div>
            <div class="form-group mt-3">
              <label for="exampleFormControlInput1" class="sr-only">Password</label>
              <input type="password" v-model="password" class="form-control" id="exampleFormControlInput1" placeholder="password">
            </div>
          </form>
          <div class="col-12 mt-5 btn btn-primary rounded-5" @click="submit">{{ loginText }}</div>
          <p class="light text-muted mt-5 text-center" v-if="signup">Already have an account <span class="text-primary btn" @click="login">Login</span></p>
          <p class="light text-muted mt-5 text-center" v-else>New on our platform? <span class="text-primary btn" @click="signUp"> Create an account</span></p>
        </div>
      </div>
    </div>
  </div>    
</template>

<script>
import axios from 'axios'
export default{
    name : 'Login',
    data(){
        return{
          email: '',
          password: '',
          signup: false,
          loginText: 'Login'
        }
    },
    mounted(){
      console.log(this.$router);
    },
    methods:{
      login(){
        this.signup = false;
        this.loginText = 'Login'
      },
      signUp(){
        this.signup= true;
        this.loginText = 'Signup';
      },
      submit(){
        if(this.signup){
          console.log("hello")
        }
        else{
          console.log(this.email, this.password)
          axios.post('http://localhost:5000/login', {
          email: this.email,
          password: this.password
          })
          .then(response => {
              console.log(response.data);
              this.$router.push('/dashboard');
          })
          .catch(error => {
              console.error('Error:', error);
          });
      }
        
      }
    }
}
</script>