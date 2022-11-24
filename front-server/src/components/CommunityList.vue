<template>
    <div>
      <div>
          <div>
              <div style="background-color: #7B93B3" class="comment-list-item-name">
                  <div class="w1">번호</div>
                  <div class="w2">제목</div>
                  <div class="w3">작성자</div>
                  <div class="w4">작성시간</div>
              </div>
              <div class="table-area">
                  <div class="article-list" v-if="articles">
                  <CommunityListItem
                  v-for="article in articles"
                  :key="article.id"
                  :article="article"
                  />
              </div>
              
          </div>
      </div>
  
      </div>
      
      
    </div>
  </template>
  
  <script>
  import CommunityListItem from '@/components/CommunityListItem'
  
  export default {
      name: 'CommunityList',
      components: {
          CommunityListItem
      },
      computed: {
          articles() {
              return this.$store.state.articles
          }
      },
  
  }
  </script>
  
  <style>
  .article-list {
      text-align: start;
  }
  .table-area {
      height: 1000px;
      width: 1000px;
      background-color: #C2D7F3;
  }
  .comment-list-item-name {
    display: flex;
    flex-direction: row;
    align-items: center;
    border: 0.5px solid whitesmoke;
    padding: 1em;
  }
  .w1 {
    width: 10%;
    text-align: start;
  }
  .w2 {
    width: 40%;
    text-align: start;
  }
  .w3 {
    width: 20%;
    text-align: start;
  }
  .w4 {
    width: 30%;
    text-align: start;
  }
  
  </style>