import {createStore} from 'vuex'
import axios from "axios";

export default createStore({
    state: {
        user: null
    },
    getters: {
        loggedIn(state) {
            // return the truthiness or the falseness of the value
            return !!state.user
        }
    },
    mutations: {
        SET_USER_DATA(state, userData) {
            state.user = userData
            console.log(userData)
            // localStorage expects a string, not a object
            localStorage.setItem('user', JSON.stringify(userData))
            // We need to set the headers of our instance axios with that token from the user data
            // ---- We are just adding the token into the header ----- //
            // ---- So that when we make API calls, we have that token that the server can verify !!! ----
            axios.defaults.headers.common['x-access-token'] = `${
                userData.token
            }`
        },
        CLEAR_USER_DATA() {
            // state.user = userData
            localStorage.removeItem('user')
            // axios.defaults.headers.common['Authorization'] = null
            // .reload is a more scalable solution as our application grows
            // il reloads the current page, it forces a refresh of our page
            location.reload()
        }
    },
    actions: {
        register({commit}, credentials) {
            return axios
                .post('//localhost:8000/register', credentials)
                .then(({data}) => {
                    commit('SET_USER_DATA', data)
                })
        },
        login({commit}, credentials) {
            return axios
                .post('http://127.0.0.1:8000/login', credentials)
                .then(({data}) => {
                    console.log('hello')
                    commit('SET_USER_DATA', data)
                })
        }
    },
    modules: {}
})
