<template>
  <div class="container">
    <h1 class="title">Employee Data</h1>
    <div class="table-container">
      <button class="btn" @click="addData()">Add Employee</button>
      <button class="btn" @click="logout()" style="float: right;">logout</button>
      <div class="custom-table">
        <div class="table-header">
          <div class="header-item" style="width: 15%;">Employee ID</div>
          <div class="header-item" style="width: 15%;">Name</div>
          <div class="header-item" style="width: 15%;">Department</div>
          <div class="header-item" style="width: 15%;">Position</div>
          <div class="header-item" style="width: 15%;">Email</div>
          <div class="header-item" style="width: 15%;">Phone Number</div>
          <div class="header-item" style="width: 10%;">Actions</div>
        </div>
        <div class="table-body">
          <div v-for="(employee, index) in employees" :key="employee.Employee_id" class="table-row">
            <div class="table-cell" style="width: 15%;">
              <input v-model="employee.Employee_id" :disabled="!employee.editable">
            </div>
            <div class="table-cell" style="width: 15%;">
              <input v-model="employee.name" :disabled="!employee.editable">
            </div>
            <div class="table-cell" style="width: 15%;">
              <input v-model="employee.department" :disabled="!employee.editable">
            </div>
            <div class="table-cell" style="width: 15%;">
              <input v-model="employee.position" :disabled="!employee.editable">
            </div>
            <div class="table-cell" style="width: 15%;">
              <input v-model="employee.email" :disabled="!employee.editable">
            </div>
            <div class="table-cell" style="width: 15%;">
              <input v-model="employee.phone_num" :disabled="!employee.editable">
            </div>
            <div class="table-cell" style="width: 10%;">
              <div class="action-buttons"  v-if="employee.id==employee.createdBy||employee.role=='admin'">
                <button v-if="!employee.editable" class="edit" @click="toggleEdit(index)">Edit</button>
                <button v-else class="ok" @click="saveChanges(index)">OK</button>
                <button v-if="!employee.editable" class="del" @click="deleteEmployee(employee)">Delete</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
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
    const user = JSON.parse(window.localStorage.getItem("user"));
    console.log(user);
    if (user == null) {
      window.location.href = "/login";
    }
    this.fetchEmployeeData();
  },
  methods: {
    async fetchEmployeeData() {
      try {
        const user = await JSON.parse(window.localStorage.getItem("user"));
        console.log(user.userid);
        const response = await fetch('http://localhost:5000/data');
        const data = await response.json();
        console.log(data);
        this.employees = data.map(employee => ({ ...employee, editable: false ,role:user.role,id:user.userid}));
      } catch (error) {
        console.error('Error fetching employee data:', error);
      }
    },
    toggleEdit(index) {
      this.employees[index].editable = true;
    },
    cancelEdit(index) {
      this.employees[index].editable = false;
    },
    logout(){
      window.localStorage.removeItem("user");
      window.localStorage.removeItem("token");
      window.location.href='/login'
    },
    saveChanges(index) {
  const updatedEmployee = this.employees[index];
  console.log(updatedEmployee);
  fetch("http://localhost:5000/update", {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(updatedEmployee)
  })
  .then(response => {
    if (response.status!=200) {
      throw new Error('Failed to update employee data');
    }
    this.employees[index].editable = false;
  })
  .catch(error => {
    console.error('Error updating employee data:', error);
  });
},
addData(){
  window.location.href="/addemployee"
},
    deleteEmployee(employee) {
      fetch('http://localhost:5000/delete', {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(employee)
      }).then((response) => {
        if (response.ok) {
        this.employees = this.employees.filter(e => e !== employee);
        }
        else{
          console.log("Error");
        }
      });
    }
  }
};
</script>

<style scoped>
.container {
  width: 1400px;
}
.btn{
  background-color: #28a745;
  color: #fff;
  float: left;
}

.title {
  font-size: 36px;
  margin-bottom: 20px;
  color: white;
  text-align: center;
}
.table-container {
  overflow-x: auto;
}

.custom-table {
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 100%;
}

.table-header {
  display: flex;
  background-color: #f0f0f0;
  border-bottom: 1px solid #ccc;
}

.header-item {
  padding: 15px;
  text-align: center;
  color: black;
  font-size: large;
}
.table-row {
  display: flex;
  border-bottom: 1px solid #ccc;
}

.table-cell {
  padding: 15px;
  text-align: center;
  white-space: nowrap;
}

.action-buttons {
  display: flex;
  justify-content: center;
  align-items: center;
}

.edit,
.del {
  cursor: pointer;
  padding: 5px 10px;
  margin: 0 5px;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.edit {
  background-color: #007bff;
  color: #fff;
}

.del {
  background-color: #dc3545;
  color: #fff;
}

.edit:hover,
.del:hover {
  filter: brightness(0.8);
}
.ok {
  background-color: #28a745;
  color: #fff;
}
.del {
  background-color: #dc3545;
  color: #fff;
}

.ok:hover,
.del:hover {
  filter: brightness(0.8);
}
</style>
