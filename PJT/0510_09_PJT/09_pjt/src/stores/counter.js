import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {

  const videos = ref(
    [
      {
        "kind": "youtube#searchResult",
        "etag": "6CCc0DqH3pWFaE8F7ikSf-y8dJg",
        "id": {
          "kind": "youtube#video",
          "videoId": "2-Rvl-PQMZk"
        },
        "snippet": {
          "publishedAt": "2023-07-14T07:29:03Z",
          "channelId": "UCkinYTS9IHqOEwR1Sze2JTw",
          "title": "&#39;적폐청산&#39;, &#39;정치 사법화&#39;…민주주의 위기 초래? 신기욱 미국 스탠퍼드대학교 교수 출연 / SBS / 편상욱의뉴스브리핑",
          "description": "[편상욱의 뉴스브리핑] 인터뷰를 인용보도할 때는 프로그램명 'SBS 〈편상욱의 뉴스브리핑〉'을 정확히 밝혀주시기 바랍니다. 저작권 ...",
          "thumbnails": {
            "default": {
              "url": "https://i.ytimg.com/vi/2-Rvl-PQMZk/default.jpg",
              "width": 120,
              "height": 90
            },
            "medium": {
              "url": "https://i.ytimg.com/vi/2-Rvl-PQMZk/mqdefault.jpg",
              "width": 320,
              "height": 180
            },
            "high": {
              "url": "https://i.ytimg.com/vi/2-Rvl-PQMZk/hqdefault.jpg",
              "width": 480,
              "height": 360
            }
          },
          "channelTitle": "SBS 뉴스",
          "liveBroadcastContent": "none",
          "publishTime": "2023-07-14T07:29:03Z"
        }
      },
      {
        "kind": "youtube#searchResult",
        "etag": "vdTs1nis4T54u4gbj7ei7sfRjX4",
        "id": {
          "kind": "youtube#video",
          "videoId": "nnGive6J_tI"
        },
        "snippet": {
          "publishedAt": "2022-07-15T10:50:31Z",
          "channelId": "UC5Oq6jxwXcIHMAnKvOluWcg",
          "title": "에스프레소 머신 한 대를 15년째 쓰고 있는 사장님이 알려주는 관리 노하우 (로스팅마스터스 신기욱 대표 2부)",
          "description": "카페마감 #카페운영 #언스페셜티 티 제작: 김종민, 안치훈 출연한 사람: 신기욱 대표 \"카페 실무 메뉴얼\" 저자 로스팅 마스터스 대표 ...",
          "thumbnails": {
            "default": {
              "url": "https://i.ytimg.com/vi/nnGive6J_tI/default.jpg",
              "width": 120,
              "height": 90
            },
            "medium": {
              "url": "https://i.ytimg.com/vi/nnGive6J_tI/mqdefault.jpg",
              "width": 320,
              "height": 180
            },
            "high": {
              "url": "https://i.ytimg.com/vi/nnGive6J_tI/hqdefault.jpg",
              "width": 480,
              "height": 360
            }
          },
          "channelTitle": "안스타",
          "liveBroadcastContent": "none",
          "publishTime": "2022-07-15T10:50:31Z"
        }
      },
      {
        "kind": "youtube#searchResult",
        "etag": "J06vWAsSfH3BHipXuwAj7YFHWHw",
        "id": {
          "kind": "youtube#video",
          "videoId": "WzCxjI1wSVk"
        },
        "snippet": {
          "publishedAt": "2022-08-14T08:00:16Z",
          "channelId": "UC5Oq6jxwXcIHMAnKvOluWcg",
          "title": "에스프레소 머신, 카페 설비 &quot;이렇게&quot; 관리하시면 불필요한 지출을 줄일 수 있습니다. (로스팅마스터스 신기욱 대표 3부)",
          "description": "매달 검증된 브랜드의 스페셜티 커피를 특별한 이벤트와 함께 소개합니다. https://unspecialty.com - 성장하고 싶은 바리스타들을 위한 ...",
          "thumbnails": {
            "default": {
              "url": "https://i.ytimg.com/vi/WzCxjI1wSVk/default.jpg",
              "width": 120,
              "height": 90
            },
            "medium": {
              "url": "https://i.ytimg.com/vi/WzCxjI1wSVk/mqdefault.jpg",
              "width": 320,
              "height": 180
            },
            "high": {
              "url": "https://i.ytimg.com/vi/WzCxjI1wSVk/hqdefault.jpg",
              "width": 480,
              "height": 360
            }
          },
          "channelTitle": "안스타",
          "liveBroadcastContent": "none",
          "publishTime": "2022-08-14T08:00:16Z"
        }
      },
      {
        "kind": "youtube#searchResult",
        "etag": "aqxzoMMyxpQ1gnLXZMSn7vBckl0",
        "id": {
          "kind": "youtube#video",
          "videoId": "Pb36UGlAOHQ"
        },
        "snippet": {
          "publishedAt": "2022-07-09T10:00:21Z",
          "channelId": "UC5Oq6jxwXcIHMAnKvOluWcg",
          "title": "에스프레소 머신과 그라인더 청소부터 하수구 관리까지 한편으로 끝내기 (로스팅마스터스 신기욱 대표 1부)",
          "description": "에스프레소머신청소 #그라인더청소 #카페마감 제작: 김종민, 안치훈 출연한 사람: 신기욱 대표 \"카페 실무 메뉴얼\" 저자 로스팅 ...",
          "thumbnails": {
            "default": {
              "url": "https://i.ytimg.com/vi/Pb36UGlAOHQ/default.jpg",
              "width": 120,
              "height": 90
            },
            "medium": {
              "url": "https://i.ytimg.com/vi/Pb36UGlAOHQ/mqdefault.jpg",
              "width": 320,
              "height": 180
            },
            "high": {
              "url": "https://i.ytimg.com/vi/Pb36UGlAOHQ/hqdefault.jpg",
              "width": 480,
              "height": 360
            }
          },
          "channelTitle": "안스타",
          "liveBroadcastContent": "none",
          "publishTime": "2022-07-09T10:00:21Z"
        }
      },
      {
        "kind": "youtube#searchResult",
        "etag": "VFDXqcA8XSd9FX9vEAtPxle6syM",
        "id": {
          "kind": "youtube#video",
          "videoId": "0bZgbFVpQjs"
        },
        "snippet": {
          "publishedAt": "2023-03-28T11:45:45Z",
          "channelId": "UCEAURqzD092U6h1yDfNsPlw",
          "title": "[커피의 신기욱] 홈카페, 회사카페에서 편하게 즐길 수 있는 미디엄 로스팅 드립커피 내리는 방법",
          "description": "커피 #핸드드립커피 #인생커피 #매뉴얼.",
          "thumbnails": {
            "default": {
              "url": "https://i.ytimg.com/vi/0bZgbFVpQjs/default.jpg",
              "width": 120,
              "height": 90
            },
            "medium": {
              "url": "https://i.ytimg.com/vi/0bZgbFVpQjs/mqdefault.jpg",
              "width": 320,
              "height": 180
            },
            "high": {
              "url": "https://i.ytimg.com/vi/0bZgbFVpQjs/hqdefault.jpg",
              "width": 480,
              "height": 360
            }
          },
          "channelTitle": "커피의 신 기욱",
          "liveBroadcastContent": "none",
          "publishTime": "2023-03-28T11:45:45Z"
        }
      },
    ]
  )

  const GetVideo = function (videoid) {
    const video = videos.value.find(video => video.id.videoId === videoid)
    return video
  }

  const watchLater = ref([])

  const toggleWatchLater = function(videoid, video) {
    const idx = watchLater.value.findIndex(item => item.videoID === videoid)
    if (idx !== -1) {
      watchLater.value.splice(idx, 1)
    } else {
      watchLater.value.push({ 'videoID': videoid, 'detail': video })
    }
  }
  

  const isLatervideo = function (videoid) {
    const video = watchLater.value.find(video => video.videoID === videoid)
    return video
  }
  // const LikeChannel = ref([

  // ])

    return { videos, GetVideo, watchLater, toggleWatchLater, isLatervideo }
}, { persist: true })
