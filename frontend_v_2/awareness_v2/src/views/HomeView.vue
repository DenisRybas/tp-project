<template>
       <div class="benefits__wrap">
                <h2 class="benefits__title">
                    Choose of the options:
                </h2>
         <div class="benefits__cards">
                      <div class="benefits__card">
                        <div class="benefits__card-pic">
                            <img src="img/svg/Vector.png" alt="" class="benefits__card-thumb">
                        </div>
                        <h3 class="benefits__card-title">
                           Diary by template
                        </h3>
                        <p class="benefits__card-desc">
                            Here is a brief description of the diary
                        </p>
                       <a class="link1">
                         <router-link class="a" to="/diary_of_templates"> Get started</router-link>
                       </a>
                    </div>
                    <div class="benefits__card">
                        <div class="benefits__card-pic">
                            <img src="img/svg/Subtract.png" alt="" class="benefits__card-thumb">
                        </div>
                        <h3 class="benefits__card-title">
                            Diary of emotions
                        </h3>
                        <p class="benefits__card-desc">
                            Here is a brief description of the diary
                        </p>
                        <router-link class="a" to="/diary_of_emotions"> Get started</router-link>
                    </div>
                    <div class="benefits__card">
                        <div class="benefits__card-pic">
                            <img src="img/svg/OpenBook.png" alt="" class="benefits__card-thumb">
                        </div>
                        <h3 class="benefits__card-title">
                               Diary of situations
                        </h3>
                        <p class="benefits__card-desc">
                            Here is a brief description of the diary
                        </p>
                        <router-link class="a" to="/diary_of_situations"> Get started</router-link>
                    </div>

                     <div class="benefits__card">
                        <div class="benefits__card-pic">
                            <img src="img/svg/Outline.png" alt="" class="benefits__card-thumb">
                        </div>
                        <h3 class="benefits__card-title">
                               Habit tracker
                        </h3>
                        <p class="benefits__card-desc">
                            Here is a brief description of the habit tracker
                        </p>
                         <router-link class="a" to="/habit_tracker"> Get started</router-link>
                    </div>
                </div>
            </div>
</template>
<script>

export default {
  name: 'HomeView',
}
</script>
