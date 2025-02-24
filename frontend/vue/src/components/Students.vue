<script lang="tsx" setup>
import router from '@/router'
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import Loader from './Loader.vue'

const route = useRoute()

const loading = ref(false)
const students = ref(null)
const error = ref(null)
watch(() => route, fetchData, { immediate: true })
async function fetchData() {
    loading.value = true
    error.value = null
    try {
        students.value = await fetch("http://localhost:5000/students").then(res => res.json());
    } catch (err) {
        error.value = err.toString()
    } finally {
        loading.value = false
    }
}
const goToStudent = (student: any) => {
    router.push({name: 'student', params: {id: student.student_index}});
}
</script>

<template>
    <Loader v-if="loading" />
    <ul>
        <li v-for="student in students" :key="student.student_index" @click="goToStudent(student)">
            <span>{{ student.FirstName }}</span>
            <span>{{ student.LastName }}</span>
            <span>{{ student.MajorName }}</span>
            <span>{{ student.student_index }}</span>
            <span>{{ student.GroupName }}</span>
        </li>
    </ul>
</template>

<style lang="css">
    ul {
        list-style-type: none;
        width: 100%;
        height: 100%;
        padding: 0;
        overflow-y: scroll;
    }
    li {
        display: flex;
        justify-content: center;
        width: 100%;
        padding: 1rem;
        border-bottom: 1px solid var(--color-border);
    }
    li span {
        width: 20%;
        text-align: center;
    }
    li:nth-child(odd) {
        background-color: var(--color-bg-light);
    }
    li:nth-child(even) {
        background-color: var(--color-bg-dark);
    }
    li:hover {
        background-color: var(--color-hover);
        cursor: pointer;
    }
</style>