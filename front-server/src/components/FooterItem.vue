<template>
    <div class="footersize bgcolor align fontwhite">
        <div class="fontwhite">
            <p>대전 3반 여러분</p>
            <p>한학기 동안 즐거웠습니다.</p>
            <p>열심히 달렸으니 다들 푹 쉬시고,</p>
            <p>잡페어때 다시 뵙겠습니다.</p>
            <p></p>
            

        </div>

        <div>
            <p>김성중 Github: eon8748@gmail.com</p>
            <p>황다솔 Github: pinetree-1017@naver.com</p>
        
        </div>

    </div>
</template>



<script>


export default {
  name: 'FooterItem',
  components: {
    
  },
  computed: {


  }
}
</script>



<style>

.article-list {
  text-align: start;
}


.bgcolor {
    background-color: #262626;;
}


.footersize {
    height: 300px;
}


.fontwhite {
    font: white
}

.align {
    display: flex;
    justify-content: space-evenly;
    align-items: center;
}

</style>
