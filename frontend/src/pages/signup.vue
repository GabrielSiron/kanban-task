<script setup lang="ts">
import Input from '../components/Input.vue';

</script>
<template>
    
    <div class="page">
        <div class="image-container">
            <h2>Divide your tasks to conquer your results.</h2>
            <h4>The solution you need.</h4>
        </div>
        <div class="form-container">
            <h1>Welcome</h1>
            <h4>Good to see you again</h4>
            <Input class="text-input" placeholder="name" type="text" color="dark-primary"/>
            <Input class="text-input" placeholder="email" type="text" color="dark-primary"/>
            <Input class="text-input" placeholder="password" type="password" color="dark-primary"/>
        </div>
    </div>
</template>

<style>

h2, h1 {
    padding: 90px 40px 0;
}

h4 {
    padding-top: 20px;
}

h2, h4, h1 {
    text-align: center;
}

h2, .image-container h4 {
    color: white;
}

h1, .form-container h4 {
    color: #1b1f45;
    padding-bottom: 20px;
}

.title, .slogan {
    display: block;
    width: 100%;
}

.page {
    width: 100vw;
    height: 100vh;
    background-color: white;
    display: grid;
    grid-template-columns: 1fr 1fr;
}

.text-input {
    margin-bottom: 10px;
    width: 40%;
}
.image-container {
    position: relative;
    justify-content: center;
    text-align: center;
    background-image: url(../assets/images/img-side.png);
    background-position-x: center;
    background-position-y: center;
    background-size: cover;
    background-repeat: no-repeat;
}

.image-container .fill {
    position: absolute;
    top: 0;
    left: 0;
    background-color: #1b1f458f !important;
    width: 100%;
    height: 100%;
}

.form-container {
    display: flex;
    flex-direction: column;
    align-items: center;
}

@media screen and (max-width: 30em){
    .page {
        display: flex;
    }

    .page .image-container {
        position: absolute;
        top: 0;
        left: 0;
        width: 100vw;
        background-position-y: top;
        height: 100vh;
    }

    .page .form-container {
        width: 100%;
        background: rgb(255,255,255);
        background: linear-gradient(0deg, rgba(255,255,255,0.8) 50%, rgba(255,255,255,0) 100%); 
        z-index: 10;
    }
    
    .image-container h2, .image-container h4 {
        display: none;
    }
}
</style>