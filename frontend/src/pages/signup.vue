<script setup lang="ts">
import Input from '../components/Input.vue';
import Button from '../components/Button.vue';

var form = {name: '', email: '', password: '', repeat_password: ''}
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
            <Input 
                v-model="form.name"
                @input="
                ($event) => {
                    form.name = $event.target.value
                }" 
                placeholder="name" 
                type="text" 
                color="dark-primary"/>
            <Input 
                v-model="form.email"
                @input="
                ($event) => {
                    form.email = $event.target.value
                }"
                placeholder="email" 
                type="text" 
                color="dark-primary"/>
            <Input 
                v-model="form.password"
                @input="
                ($event) => {
                    form.password = $event.target.value
                }"
                placeholder="password" 
                type="password" 
                color="dark-primary"/>
            <Input 
                v-model="form.repeat_password"
                @input="
                ($event) => {
                    form.repeat_password = $event.target.value
                }"
                placeholder="repeat password" 
                type="password" 
                color="dark-primary"/>
            <Button color="dark-primary" text="Create an account"></Button>
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

.input, .my-btn {
    margin-bottom: 20px !important;
    width: 60% !important;
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

    .input, .my-btn {
        margin-bottom: 20px !important;
        width: 80% !important;
    }
}
</style>