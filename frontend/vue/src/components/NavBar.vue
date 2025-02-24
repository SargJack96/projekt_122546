<script setup lang="tsx">
</script>

<template>
    <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
    </nav>
</template>

<style lang="css" scoped>
nav {
    justify-content: flex-start;
    display: flex;
    flex-direction: column;
    height: 100%;
    width: 100%;
    font-size: 12px;
    text-align: center;
    margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
  cursor: default;
  background-color: var(--color-hover);
}

nav a.router-link-exact-active:hover {
  /* background-color: transparent; */
}

nav a {
    border-radius: 6px;
    font-size: 1.5rem;
    display: inline-block;
    padding: 1rem;
    margin-top: 1rem;
    /* margin: 0.5rem; */
}

nav a:first-of-type {
  border: 0;
}
</style>