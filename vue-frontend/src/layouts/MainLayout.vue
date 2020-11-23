<template>
    <div id="main-layout">
        <Navbar @click="isOpen = !isOpen"/>
            <router-view class="mb-8"/>
        <Footer />
    </div>
</template>

<script>
    import Navbar from '../components/Navbar'
    import Footer from '../components/Footer'

    export default {
        name: 'main-layout',
        data: () => ({
          isOpen: true
        }),
        components: {
            Navbar,
            Footer
        }
    }
</script>
