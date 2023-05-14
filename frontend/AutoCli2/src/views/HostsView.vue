<script setup lang="ts">
    // Application component import:
    import ObjectListComponent from '../components/ObjectListComponent.vue'
</script>

<template>
    <Suspense>
        <template #default>
            <ObjectListComponent />
        </template>
        <template #fallback>
            <div>Loading...</div>
        </template>
    </Suspense>
</template>

<style scoped>
</style>
