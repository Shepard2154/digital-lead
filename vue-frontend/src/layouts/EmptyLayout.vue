<template>
    <v-row>
        <v-img
            max-height="150"
            max-width="250"
            src="../assets/grazh.svg"
            style="position: absolute; top: 40px; left:40px"
        ></v-img>
        <v-col cols="5" style="display: flex; align-items: center; justify-content: center;">
            <router-view/>
        </v-col>

        <v-col cols="7" id="empty-layout">
        </v-col>
    </v-row>
</template>

<style scoped>
    #empty-layout{
        position: absolute;
        width: 100%;
        height: 100%;

        right: 0;

        background-image: url('../assets/login_back.png');
    }
</style>