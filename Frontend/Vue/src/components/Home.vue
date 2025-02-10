<script setup>
import { onMounted, ref } from 'vue';
import useStudent from '@/composable/studentApi';

const { studentData, error, getAllStudent } = useStudent();
const isLoading = ref(true); // ✅ Loading state

onMounted(async () => {
  isLoading.value = true;
  await getAllStudent();
  isLoading.value = false;
});
</script>

<template>
  <div>
    <h1>Connect Vue JS with Django</h1>

    <!-- ✅ Show loading while fetching -->
    <div v-if="isLoading">Loading students...</div>

    <!-- ✅ Show error if API fails -->
    <div v-else-if="error" class="text-red-500">
      Oops! Error encountered: {{ error.message }}
    </div>

    <!-- ✅ Show student list -->
    <div v-else>
      <div v-for="({ id, stuname, email }, i) in studentData" :key="id">
        <h2>
          {{ i + 1 }}. {{ stuname }} - {{ email }}
        </h2>
      </div>
    </div>
  </div>
</template>
