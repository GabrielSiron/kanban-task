<script setup lang="ts">
defineProps(['clickFunction', 'color', 'text'])
</script>

<template>
    <button :class="'my-btn ' + color">
        {{ text }}
    </button>
</template>

<style>
.my-btn {
    height: 48px;
    border-radius: 10px;
    background-color: transparent;
    color: black;
    box-shadow: none;
    border: 1px solid black;
    font-family: 'Inter', sans-serif;
    font-size: 16px;
}

.dark-primary + .my-btn {
    background-color: var(--dark-primary);
    color: white;
    border: 1px solid var(--dark-primary);
}

.primary + .my-btn {
    background-color: var(--primary);
    color: white;
    border: 1px solid var(--primary);
}

.light-primary + .my-btn {
    background-color: var(--light-primary);
    color: white;
    border: 1px solid var(--light-primary);
}
</style>