<template>
  <div class="container">
      <v-client-table
          :data="tableData"
          :columns="columns"
          :options="options">
      </v-client-table>
  </div>
</template>

<script>

export default {
    data() {
        return {
            columns: ['id', 'title', 'description', 'professor', 'time'],
            tableData: [],
            options: {
                headings: {
                    id: 'ID',
                    title: 'Course Title',
                    description: 'Description',
                    professor: 'Professor Name',
                    time: 'Period'
                },
                sortable: ['id', 'title', 'description', 'professor', 'time'],
                filterable: ['id', 'title', 'description', 'professor', 'time']
            }
        }
    },
    mounted() {
        this.axios.get('http://127.0.0.1:8000/api/courses/').then(res => {
            this.tableData = res.data
        })
    }

}
</script>

<style>
#app {
  width: 95%;
  margin-top: 50px;
}

.VuePagination {
  text-align: center;
}

.vue-title {
  text-align: center;
  margin-bottom: 10px;
}

.vue-pagination-ad {
  text-align: center;
}

.glyphicon.glyphicon-eye-open {
  width: 16px;
  display: block;
  margin: 0 auto;
}

th:nth-child(3) {
  text-align: center;
}

.VueTables__child-row-toggler {
  width: 16px;
  height: 16px;
  line-height: 16px;
  display: block;
  margin: auto;
  text-align: center;
}

.VueTables__child-row-toggler--closed::before {
  content: "+";
}

.VueTables__child-row-toggler--open::before {
  content: "-";
}

</style>
