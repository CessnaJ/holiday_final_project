<template>
  <div>
    <div>
        <!-- <h2>게시글 리스트</h2> -->
        <div class="board-table" >
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
.board-table {
    height: 1000px;
    width: 800px;
    background-color: #99ccff;
}

</style>