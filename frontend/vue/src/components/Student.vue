<script setup lang="tsx">
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import Loader from './Loader.vue'

const route = useRoute()
const student = ref(null)
const payments = ref(null)
const total = ref(null)

const loadingStudent = ref(true)
const loadingPayments = ref(true)
const loadingTotal = ref(true)

const error = ref(null)
async function fetchStudentData(id) {
//   error.value = post.value = null
    loadingStudent.value = true
    loadingTotal.value = true
    loadingPayments.value = true
  try {
    // replace `getPost` with your data fetching util / API wrapper
    student.value = await fetch("http://localhost:5000/students/" + id).then(res => res.json())
    loadingStudent.value = false
    total.value = await fetch("http://localhost:5000/totals/" + id).then(res => res.json())
    loadingTotal.value = false
    let tmpPayments = await fetch("http://localhost:5000/payments/" + id).then(res => res.json())
    payments.value = tmpPayments.map((payment) => {
        return { id: tmpPayments.indexOf(payment), ...payment
            
        }
    })
    loadingPayments.value = false
  } catch (err) {
    error.value = err.toString()
  } finally {
    loadingStudent.value = false
    loadingTotal.value = false
    loadingPayments.value = false
  }
}

watch(() => route.params.id, fetchStudentData, { immediate: true })
</script>

<template>
    <Loader v-if="loadingStudent" />
    <main>
        <h1>{{ student[0].FirstName || "" }} {{ student[0].LastName || "" }}</h1>
        <div v-if="student[0]">
            <div id="column_names">
                <span>Kierunek</span>
                <span>Indeks</span>
                <span>Grupa</span>
            </div>
            <ul>
                <li v-for="s in student" :key="s.student_index">
                    <span>{{ s.MajorName }}</span>
                    <span>{{ s.student_index }}</span>
                    <span>{{ s.GroupName }}</span>
                </li>
            </ul>
        </div>
        <span id="total">
            <Loader v-if="loadingTotal" />
            {{ total[0].amount_due > 0 ? `Do zapłacenia` : `Nadpłata` }}: {{ Math.abs(total[0].amount_due) + "zł" || "" }}
        </span>
        <Loader v-if="loadingPayments" />
        <div id="column_names_money">
            <span>Kwota (PLN)</span>
            <span>Data płatności</span>
        </div>
        <ul>
        <li v-for="payment in payments" :key="payment.id">
            <span>{{ payment.Amount }}</span>
            <span>{{ payment.PaymentDate }}</span>
        </li>
    </ul>
    </main>
</template>

<style lang="css" scoped>
  h1 {
    text-align: center;
    margin-top: 1rem;
    margin-bottom: 0.5rem;
  }
  #column_names, #column_names_money {
    display: flex;
    justify-content: center;
    width: 100%;
    padding: 1rem;
    border-bottom: 1px solid var(--color-border);
    background-color: var(--vt-c-black-soft);
    
  }
  #column_names span {
    width: 33%;
    font-weight: 700;
    text-align: center;
  }
  #column_names_money span {
    width: 50%;
    font-weight: 700;
    text-align: center;
  }
  ul, li {
    width: 100%;
    }
    li {
        display: flex;
        justify-content: center;
        width: 100%;
        padding: 1rem;
        border-bottom: 1px solid var(--color-border);
    }
    li span {
        width: 100%;
        text-align: center;
    }
    #total {
        margin-top: 5rem;
        display: flex;
        justify-content: center;
        width: 100%;
        padding: 1rem;
        border-bottom: 1px solid var(--color-border);
    }
  #column_names ul li span {
    width: 33%;
    font-weight: 700;
    text-align: center;
  }
</style>