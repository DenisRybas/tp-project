import { createRouter, createWebHistory } from 'vue-router'
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
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
