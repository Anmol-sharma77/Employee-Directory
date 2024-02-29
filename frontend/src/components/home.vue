<template>
    <div>
      <h1>Employee Data</h1>
      <table class="table">
        <thead>
          <tr>
            <th>Employee ID</th>
            <th>Name</th>
            <th>Department</th>
            <th>Position</th>
            <th>Email</th>
            <th>Phone Number</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="employee in employees" :key="employee.Employee_id">
            <td>{{ employee.Employee_id }}</td>
            <td>{{ employee.name }}</td>
            <td>{{ employee.department }}</td>
            <td>{{ employee.position }}</td>
            <td>{{ employee.email }}</td>
            <td>{{ employee.phone_num }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        employees: []
      };
    },
    mounted() {
      this.fetchEmployeeData();
    },
    methods: {
      async fetchEmployeeData() {
        try {
          const response = await fetch('http://localhost:5000/data');
          const data = await response.json();
          this.employees = data;
        } catch (error) {
          console.error('Error fetching employee data:', error);
        }
      }
    }
  };
  </script>
  
  <style>
  .table {
    width: 100%;
    border-collapse: collapse;
  }
  
  .table th,
  .table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }
  
  
  </style>
  