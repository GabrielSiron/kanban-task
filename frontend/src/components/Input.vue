<script setup lang="ts">
import { ref } from 'vue'
const render = ref(0);

defineProps(['placeholder', 'type', 'color'])

var showPassword = false;

const changeShowPasswordStatus = () => {
    showPassword = !showPassword;
    console.log("rodou");
    
    render.value += 1;
}

</script>

<template>
    <div :class="'input ' + color">
        <input :type="showPassword == true? 'text': type" :placeholder="placeholder"/>
        <button v-if="type == 'password'" class="show-pwrd-button" v-on:click="changeShowPasswordStatus" :key="render">
            <img v-if="showPassword == false" src="../assets/icons/visibility.svg" alt="visible">
            <img v-if="showPassword == true" src="../assets/icons/invisibility.svg" alt="invisible">
        </button>
        
    </div>
</template>

<style>

.input {
    border: 1px solid black;
    border-radius: 4px;
    background-color: white;
    display: flex;
    justify-content: space-between;
    height: 48px;
}

input {
    border: none;
    width: 80%;
    padding: 10px;
    display: flex;
    font-family: 'Inter', sans-serif;
    font-size: 16px;
}

input:focus {
    outline: none;
}

.dark-primary {
    border: 1px solid var(--dark-primary);
}

.show-pwrd-button {
    border: none;
    outline: none;
    background-color: transparent !important;
    width: 40px;
}
</style>