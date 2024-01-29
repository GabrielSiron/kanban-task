<script setup lang="ts">
defineProps(['placeholder', 'type', 'color'])

</script>

<template>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" />
    <div :class="'input ' + color">
        <input :type="type" :placeholder="placeholder" />
        <span class="material-symbols-outlined">
        </span>
    </div>
</template>

<style>

.input {
    border: 1px solid black;
    border-radius: 4px;
    display: flex;
    height: 48px;
    min-width: 100px;
}

input {
    border: none;
    width: 80%;
    padding: 10px;
    display: flex;
    font-family: 'Inter', sans-serif;
}

input:focus {
    outline: none;
}

.dark-primary {
    border: 1px solid var(--dark-primary);
}

</style>