<template>
    <button class="btn" @click="back()">Back</button>
    <div class="flex justify-center items-center min-h-screen bg-gradient-to-r from-purple-400 via-pink-500 to-red-500">
        <div class="bg-white p-8 rounded-lg shadow-lg w-96">
            <h1 class="text-3xl font-bold mb-4 text-center text-gray-800">Add Employee</h1>
        <form @submit.prevent="addEmployee" class="space-y-4">
          <div>
            <label for="employeeId" class="block text-sm font-medium text-gray-700">Employee ID</label>
            <input v-model="employeeId" type="text" id="employeeId" name="employeeId" class="mt-1 p-2 block w-full border-2 border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500">
          </div>
          <div>
            <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
            <input v-model="name" type="text" id="name" name="name" class="mt-1 p-2 block w-full border-2 border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500">
          </div>
          <div>
            <label for="department" class="block text-sm font-medium text-gray-700">Department</label>
            <input v-model="department" type="text" id="department" name="department" class="mt-1 p-2 block w-full border-2 border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500">
          </div>
          <div>
            <label for="position" class="block text-sm font-medium text-gray-700">Position</label>
            <input v-model="position" type="text" id="position" name="position" class="mt-1 p-2 block w-full border-2 border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500">
          </div>
          <div>
            <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
            <input v-model="email" type="email" id="email" name="email" class="mt-1 p-2 block w-full border-2 border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500">
          </div>
          <div>
            <label for="phoneNum" class="block text-sm font-medium text-gray-700">Phone Number</label>
            <input v-model="phoneNum" type="tel" id="phoneNum" name="phoneNum" class="mt-1 p-2 block w-full border-2 border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500">
          </div>
          <div>
            <button type="submit" class="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700 transition duration-300 w-full focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">Add Employee</button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        employeeId: '',
        name: '',
        department: '',
        position: '',
        email: '',
        phoneNum: ''
      };
    },
    mounted(){
    const user = JSON.parse(window.localStorage.getItem("user"));
    if (user == null) {
      window.location.href = "/login";
    }
    },
    methods: {
        back(){
            window.location.href='/home'
        },
      addEmployee() {
        console.log({
          employeeId: this.employeeId,
          name: this.name,
          department: this.department,
          position: this.position,
          email: this.email,
          phoneNum: this.phoneNum
        });
        const a=JSON.parse(localStorage.getItem("user"))
        const id=a.userid;
        fetch('http://localhost:5000/addemployee', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({
            employee_id: this.employeeId,
            name: this.name.trim(),
            department: this.department.trim(),
            position: this.position.toUpperCase().trim(),
            email: this.email.trim(),
            phonenum: this.phoneNum.replace(/[-()]/g, ''),
            createdby: id
          })
        }).then(response => response.json())
          .then((result) => {
            alert("New Employee Added!");
            window.location.href='/home'
          })
          .catch((error) => {
            alert("Error Adding New Employee");
            console.log(error);
          });
        this.employeeId = '';
        this.name = '';
        this.department = '';
        this.position = '';
        this.email = '';
        this.phoneNum = '';
      }
    }
  };
  </script>
  
  <style scoped>
  .btn{
  background-color: #28a745;
  color: #fff;
  }
  input[type="text"],
  input[type="email"],
  input[type="tel"] {
    padding: 12px;
    margin-bottom: 16px;
    width: 100%;
    border: none;
    background-color: #f7f7f7;
    color: black;
    border-radius: 8px;
  }
  
  button[type="submit"] {
    background-color: #4F46E5;
    color: white;
    padding: 12px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    width: 100%;
  }
  
  button[type="submit"]:hover {
    background-color: #4338CA;
  }
  </style>
  