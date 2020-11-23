<template>
    <v-autocomplete
        v-model="select"
        :loading="loading"
        :items="items"
        :search-input.sync="search"
        cache-items
        class="mx-4"
        persistent-hint
        hide-no-data
        :label="label"
    ></v-autocomplete>
</template>

<script>
export default {
    props: {
        states: Array,
        label: String
    },

    data() {
        return {
                loading: false,
                items: [],
                search: null,
                select: null
        }
    },

    watch: {
    search (val) {
        val && val !== this.select && this.querySelections(val)
        },
    },

    methods: {
        querySelections (v) {
        this.loading = true
        setTimeout(() => {
            this.items = this.states.filter(e => {
            return (e || '').toLowerCase().indexOf((v || '').toLowerCase()) > -1
            })
            this.loading = false
        }, 500)
        },
    }
}
</script>