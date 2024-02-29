<template>
    <div class="container">
    <h1 class="title">Oops!</h1>
    <h2 class="subtitle">404 - Page Not Found</h2>
    <img class="image" src="https://aioseo.com/wp-content/uploads/2021/04/how-to-find-and-fix-404-errors-in-wordpress.png.webp" alt="Error Image">
    <a class="home-link" href="/">Go back to Home</a>
  </div>
</template>
<style scoped>
body {
      background-color: #f8f8f8;
      font-family: Arial, sans-serif;
    }

    .container {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }

    .title {
      font-size: 48px;
      color: #fff8f8;
      margin-bottom: 20px;
    }

    .subtitle {
      font-size: 24px;
      color: #ffffff;
      margin-bottom: 40px;
    }

    .image {
      margin-bottom: 20px;
    }

    .home-link {
      color: #58fff4;
      text-decoration: none;
      font-weight: bold;
      border: 2px solid #333;
      padding: 10px 20px;
      border-radius: 5px;
      transition: background-color 0.3s ease;
    }

    .home-link:hover {
      background-color: #333;
      color: #fff;
    }
</style>
