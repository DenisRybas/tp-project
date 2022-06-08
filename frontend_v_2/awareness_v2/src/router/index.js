import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/Login.vue'
import RegisterView from '../views/Register.vue'
import FaqView from '../views/Faq.vue'
import ContactsView from '../views/Contacts.vue'
import AboutView from '../views/About.vue'
import MyDiaryView from '../views/MyDiary.vue'
import SettingsView from '../views/Settings.vue'
import DiaryOfTemplatesView from "@/views/DiaryOfTemplates.vue";
import HabitTrackerView from "@/views/HabitTracker.vue";
import DiaryOfEmotionsView from "@/views/DiaryOfEmotions.vue";
import DiaryOfSituationsView from "@/views/DiaryOfSituations.vue";
import TechnicalSupportUserView from "@/views/TechnicalSupportUser.vue";
import MyAppealsView from "@/views/MyAppeals.vue";
import ViewingDiaryTemplatesView from "@/views/ViewingDiaryTemplates.vue";
import ViewingDiaryEmotionsView from "@/views/ViewingDiaryEmotions.vue";
import ViewingDiarySituationsView from "@/views/ViewingDiarySituations.vue";
import ViewingDiaryTemplatesIdView from "@/views/ViewingDiaryTemplatesId.vue";
import ViewingDiaryEmotionsIdView from "@/views/ViewingDiaryEmotionsId.vue";
import ViewingDiarySituationsIdView from "@/views/ViewingDiarySituationsId.vue";
import MyAppealsIdView from "@/views/MyAppealsId.vue";
import ViewingHabitTrackerIdView from "@/views/ViewingHabitTrackerId.vue";
import ViewingHabitTrackerView from "@/views/ViewingHabitTracker.vue";

const routes = [
    {
        path: '/',
        name: 'home',
        meta: {layout: 'main'},
        component: HomeView
    },
    {
        path: '/login',
        name: 'login',
        meta: {layout: 'main'},
        component: LoginView
    },
    {
        path: '/registration',
        name: 'registration',
        meta: {layout: 'main'},
        component: RegisterView
    },
    {
        path: '/faq',
        name: 'faq',
        meta: {layout: 'main'},
        component: FaqView
    },
    {
        path: '/contacts',
        name: 'contacts',
        meta: {layout: 'main'},
        component: ContactsView
    },
    {
        path: '/about',
        name: 'about',
        meta: {layout: 'main'},
        component: AboutView
    },
    {
        path: '/diary',
        name: 'diary',
        meta: {layout: 'main'},
        component: MyDiaryView
    },
    {
        path: '/settings',
        name: 'settings',
        meta: {layout: 'main'},
        component: SettingsView
    },
    {
        path: '/diary_of_templates',
        name: 'diary_of_templates',
        meta: {layout: 'main'},
        component: DiaryOfTemplatesView
    },
    {
        path: '/diary_of_emotions',
        name: 'diary_of_emotions',
        meta: {layout: 'main'},
        component: DiaryOfEmotionsView
    },
    {
        path: '/habit_tracker',
        name: 'habit_tracker',
        meta: {layout: 'main'},
        component: HabitTrackerView
    },
    {
        path: '/diary_of_situations',
        name: 'diary_of_situations',
        meta: {layout: 'main'},
        component: DiaryOfSituationsView
    },
    {
        path: '/technical_support_user',
        name: 'technical_support_user',
        meta: {layout: 'main'},
        component: TechnicalSupportUserView
    },
    {
        path: '/my_appeals',
        name: 'my_appeals',
        meta: {layout: 'main'},
        component: MyAppealsView
    },
    {
        path: '/viewing_diary_situations',
        name: 'viewing_diary_situations',
        meta: {layout: 'main'},
        component: ViewingDiarySituationsView
    },
    {
        path: '/viewing_diary_emotions',
        name: 'viewing_diary_emotions',
        meta: {layout: 'main'},
        component: ViewingDiaryEmotionsView
    },
    {
        path: '/viewing_diary_templates',
        name: 'viewing_diary_templates',
        meta: {layout: 'main'},
        component: ViewingDiaryTemplatesView
    },
    {
        path: '/viewing_diary_templates/:id',
        name: 'viewing_diary_templates_id',
        meta: {layout: 'main'},
        component: ViewingDiaryTemplatesIdView,
        props: (route) => {
            const id = Number.parseInt(route.params.id);
            return {id};
        },
    },
    {
        path: '/viewing_diary_emotions/:id',
        name: 'viewing_diary_emotions_id',
        meta: {layout: 'main'},
        component: ViewingDiaryEmotionsIdView,
        props: (route) => {
            const id = Number.parseInt(route.params.id);
            return {id}
        },
    },
    {
        path: '/viewing_diary_situations/:id',
        name: 'viewing_diary_situations_id',
        meta: {layout: 'main'},
        component: ViewingDiarySituationsIdView,
        props: (route) => {
            const id = Number.parseInt(route.params.id);
            return {id}
        },
    },
    {
        path: '/my_appeals/:id',
        name: 'my_appeals_id',
        meta: {layout: 'main'},
        component: MyAppealsIdView,
        props: (route) => {
            const id = Number.parseInt(route.params.id);
            return {id}
        },
    },
    {
        path: '/viewing_habit_tracker',
        name: 'viewing_habit_tracker',
        meta: {layout: 'main'},
        component: ViewingHabitTrackerView
    },
    {
        path: '/viewing_habit_tracker/:id',
        name: 'viewing_habit_tracker_id',
        meta: {layout: 'main'},
        component: ViewingHabitTrackerIdView,
        props: (route) => {
            const id = Number.parseInt(route.params.id);
            return {id}
        },
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

router.beforeEach((to, from, next) => {
    const loggedIn = localStorage.getItem('x-access-token')

    // to.matched will give us an array of the records that match that to route
    // some method allows us to iterate over taht collection of routes
    if (to.matched.some(record => record.meta.requiresAuth) && !loggedIn) {
        // redirect to home page
        next('/')
    }
    next()
})

export default router
