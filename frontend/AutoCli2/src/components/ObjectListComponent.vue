<script setup lang="ts">
    // Axios import:
    import axios from 'axios'
    // API key import:
    import { apiKey, applicationName } from '../settings';
    // VUE import:
    import { ref, watch } from 'vue'



    import objectDescription from '../objects/hosts.json'


    // Collect host data:
    const config = {
        headers: {
            'Authorization': `Token ${apiKey.value}`}}

    const pageNumber = ref(1)
    const collectedData = ref(null)
    const collectedLinks = ref(null)
    const collectedPages = ref(null)
    const collectedOptions = ref(objectDescription.GET)
    const collectedColumns = ref(Object.keys(collectedOptions.value).length)



    
    const collectObjects = async () => {
        const response = await axios.get(`http://${applicationName}/api-inventory/full-host/?page_number=${pageNumber.value}&page_size=10`, config)
        collectedData.value = response.data.page_results
        collectedLinks.value = response.data.page_links
        collectedPages.value = response.data.page_count
    }

    watch(pageNumber, async () => {
        console.log(pageNumber.value)
        const res = await axios.get(`http://${applicationName}/api-inventory/full-host/?page_number=${pageNumber.value}&page_size=10`, config)
        collectedData.value = res.data.page_results
    })

    const deleteObject = async (pk=0) => {
        const response = await axios.delete(`http://${applicationName}/api-inventory/host/${pk}/`, config)
        console.log(response)
        collectObjects()
    }

    // Run main functions:
    collectObjects()

</script>

<template>
    <div id="objects">

        <div class="objects_section objects_search">
            <input type="text">
            <button>Search</button>
            <button>View</button>
            <span class='icon'>backspace</span>
            <span class='icon'>edit_square</span>
            <span class='icon'>file_copy</span>
        </div>

        <article class="objects_section objects_list">
            <div class='table'>
                <div class='row table_head'>
                    <div class='cell head_cell' v-for="option in collectedOptions">{{ option.label }}</div>
                </div>
                <div class='row body_row' v-for="host in collectedData" :key="host.pk">
                    <div class="cell" v-for="(option, key) in collectedOptions" :key="key">
                        <!-- <span v-if="option.type === 'datetime'">{{ Date(host[key]) }}</span> -->
                        <span v-if="option.type === 'datetime'">{{ new Date(host[key]).toLocaleString('en-US', { year: 'numeric', month: 'numeric', day: 'numeric', hour: 'numeric', minute: 'numeric', hour12: false }) }}</span>
                        <span v-else-if="option.type === 'sub_object'">
                            <span v-if="host[key]">{{ host[key][option.sub_object] }}</span>
                            <span v-else>Empty</span>
                        </span>
                        <span v-else-if="option.type === 'choice'">
                            <span v-for="choice in option.choices">
                                <span v-if="host[key] === choice.value">{{ choice.display_name }}</span>
                            </span>
                        </span>
                        <span v-else>{{ host[key] }}</span>
                    </div>
                </div>
            </div>
        </article>

        <div class="objects_section objects_navigation">
            <button v-if="pageNumber > 1" @click="pageNumber--">Previous</button>
            <button v-else disabled>Previous</button>
            <button v-if="pageNumber < collectedPages" @click="pageNumber++">Next</button>
            <button v-else disabled>Next</button>
        </div>

    </div>

</template>

<style scoped>
    #objects {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .objects_section {
        background: #fff;
        background-clip: border-box;
        box-shadow: var(--box_shadow);
        border: 0.5px solid rgba(26,54,126,.125);
    }

    .objects_search,
    .objects_navigation {
        height: 50px;
    }

    .objects_list {
        margin: 20px 0px;
        padding: 0px;
    }

    .table {
        height: calc(100vh - 260px);
        overflow-y: auto;
        width: 100%;
    }
    .table_head {
        top: 0px;
        position: sticky;
    }

    .head_cell {
        background: var(--color_third);
    }

    .body_row:nth-child(2) {
        margin-top: 20px;
    }

    .row {
        display: grid;
        grid-template-columns: repeat(v-bind('collectedColumns'), 1fr);
        justify-items: stretch;
        align-items: center;
    }

    .cell {
        height: 100%;
        min-width: 150px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 20px;
        word-wrap: break-word;
        border-right: 1px solid rgba(26,54,126,.256);
        border-bottom: 1px solid rgba(26,54,126,.256);
    }

    .objects_navigation {
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        align-items: center;
    }

    .objects_navigation button {
        border: none;
        cursor: pointer;
        background: #ffffff;
    }
</style>