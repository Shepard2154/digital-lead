import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import colors from 'vuetify/es5/util/colors';

Vue.use(Vuetify);


export default new Vuetify({
    primary: colors.blue.base,
    secondary: colors.cyan.base,
    accent: colors.grey.base,
    error: colors.pink.base,
    warning: colors.brown.base,
    info: colors.yellow.base,
    success: colors.green.base
})
