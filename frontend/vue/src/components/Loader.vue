<template>
    <div class="loader"></div>
</template>

<style lang="css">
.loader {
  position:absolute;
  top:50%;
  left:50%;
  width: 50px;
  aspect-ratio: 1;
  border-radius: 50%;
  border: 8px solid;
  border-color: var(--color-border) var(--vt-c-black-soft);
  animation: l1 1s infinite;
}
@keyframes l1 {to{transform: rotate(.5turn)}}
</style>