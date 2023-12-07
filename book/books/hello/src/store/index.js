import {createStore} from "vuex";
import {increment} from './mutation-types'

const store = createStore({
    state() {
        return {}
    },
    mutations: {

        [increment](state, payload) {
            state.count += payload.n;
        },
    },
});

export default store;
