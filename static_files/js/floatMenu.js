window.onload = function(){
  $(function() {

      function moveFloatMenu() {
          var menuOffset
          var w = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
          //set offset using windowWidth rules
          if(w>991){
            menuOffset = 10 + $(this).scrollTop() + "px";
          } else {
            menuOffset = 10 + "px";
          }
          // var isMouseOver = false;
          // $('#floatMenu').mouseEnter(function(){isMouseOver = true;});
          // $('#floatMenu').mouseover(function(){isMouseOver = true;});
          // $('#floatMenu').mouseout(function(){isMouseOver = false;});
          // if (isMouseOver == false){
          //   $('#floatMenu').animate({
          //       top: menuOffset
          //   }, {
          //       duration: 50,
          //       queue: false
          //   });
          // }
      }

      // menuYloc = $('#floatMenu').offset();
      $(window).scroll(moveFloatMenu);
      $(window).resize(moveFloatMenu);

      //get the window dimensions
      // var w = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
      // console.log(w);
      //if width is less than one of the breakpoints, don't call this function.

      moveFloatMenu();
  });
}
