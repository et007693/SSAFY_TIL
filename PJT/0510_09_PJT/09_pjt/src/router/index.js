import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import VideoListComponent from '@/views/VideoListComponent.vue'
import ChannelLikeView from '@/views/ChannelLikeView.vue'
import VideoDetailView from '@/views/VideoDetailView.vue'
import WatchLaterView from '@/views/WatchLaterView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/search',
      name: 'search',
      component: VideoListComponent,
    },
    {
      path: '/detail/:videoid',
      name: 'detail',
      component: VideoDetailView,
    },
    {
      path: '/channels',
      name: 'like-channel',
      component: ChannelLikeView,
    },
    {
      path: '/watchlater',
      name: 'watch-later',
      component: WatchLaterView,
    },
  ]
})

export default router
