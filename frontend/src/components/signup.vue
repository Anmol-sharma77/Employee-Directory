<script setup>
import { ref } from 'vue'

const username = ref('');
const email = ref('');
const password = ref('');

function handleSubmit() {
  console.log('Form submitted');
  console.log('Username:', username.value);
  console.log('Email:', email.value);
  console.log('Password:', password.value);
  try{
      fetch('http://localhost:5000/signup',{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({username:username.value,password:password.value,email:email.value})
      }).then(function(response){
        if(response.status==200)
        window.location.href="/home"
        else alert("Wrong Username or Password");
      })
  }catch(err)
  {
    console.log(err);
    alert("Invalid credentials");
  }
}
</script>

<template>
  <div class="signup-container">
    <h2>Signup Page</h2>
    <form @submit.prevent="handleSubmit" class="signup-form">
      <input type="text" name="username" placeholder="User Name" v-model="username" required>
      <input type="email" name="mail" placeholder="Email" v-model="email" required>
      <input type="password" name="password" placeholder="Password" v-model="password" required>
      <button type="submit" id="btn">Sign Up</button>
    </form>
    <p>Already have an account? <a href="/login">Log In</a></p>
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
        .signup-container {
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            padding: 30px;
            width: 400px;
        }

        .signup-container h2 {
            text-align: center;
            margin-bottom: 30px;
            color: #333;
        }

        .signup-form input {
            width: 100%;
            padding: 12px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 16px;
        }

        .signup-form button {
            width: 100%;
            padding: 12px;
            border: none;
            border-radius: 5px;
            background-color: #4CAF50;
            color: #fff;
            font-size: 16px;
            cursor: pointer;
        }

        .signup-form button:hover {
            background-color: #45a049;
        }

        .signup-form p {
            text-align: center;
            margin-top: 15px;
        }

        .signup-form p a {
            color: #4CAF50;
        }
        p{
            color: black;
        }
</style>
