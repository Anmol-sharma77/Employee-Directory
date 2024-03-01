<script setup>
import { onMounted, ref } from 'vue'
defineProps({
  msg: String,
})
console.log("hello")
const mail = ref('')
const password = ref('')
async function handleSubmit() {
  console.log('Form submitted');
  try{
    const response = await fetch('http://127.0.0.1:5000/login',{
      method:"POST",
      headers:{"Content-Type":"application/json"},
      body:JSON.stringify({mail:mail.value,password:password.value})
    })
    const data = await response.json();
    const token=data.token;
    const user=data.user;
    window.localStorage.setItem( "token" , token );
    window.localStorage.setItem( "user" , JSON.stringify(user) );
    alert(`Welcome back ${user.name}!`);
    location.href="./home";
    }catch (error) {
      alert( "Wrong Credentials" );
       console.error('Error fetching employee data:', error);
    }
}
</script>

<template>
  <div class="login-container">
    <h2>Login Page</h2>
    <form @submit.prevent="handleSubmit" class="login-form">
      <input required type="text" name="mail" placeholder="Email" v-model="mail">
      <input required type="password" name="password" placeholder="Password" v-model="password">
      <button type="submit" id="btn">Login</button>
    </form>
    <a href="/forgot">Forget password</a>
    <p>Don't have an account? <a href="/signup">Sign Up</a></p>  
  </div>
</template>
<style scoped>
body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f7f7f7;
        }

        .login-container {
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            padding: 30px;
            width: 400px;
        }

        .login-container h2 {
            text-align: center;
            margin-bottom: 30px;
            color: #333;
        }

        .login-form input {
            width: 100%;
            padding: 12px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 16px;
        }

        .login-form button {
            width: 100%;
            padding: 12px;
            border: none;
            border-radius: 5px;
            background-color: #4CAF50;
            color: #fff;
            font-size: 16px;
            cursor: pointer;
        }

        .login-form button:hover {
            background-color: #45a049;
        }

        .login-form p {
            text-align: center;
            margin-top: 15px;
            color: black;
        }

        .login-form p a {
            color: #4CAF50;
            color: black;
        }
        p{
          color: black;
        }
</style>
