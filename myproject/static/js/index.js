/*$('#click_advance1').click(function() {
    $('#display_advance1').toggle('1000');
    $("i", this).toggleClass("fa fa-chevron-up fa fa-chevron-down ");
});

$('#click_advance2').click(function() {
    $('#display_advance2').toggle('1000');
    $("i", this).toggleClass("fa fa-chevron-up fa fa-chevron-down ");
});

$('#click_advance3').click(function() {
    $('#display_advance3').toggle('1000');
    $("i", this).toggleClass("fa fa-chevron-up fa fa-chevron-down ");
});

$('#click_advance4').click(function() {
    $('#display_advance4').toggle('1000');
    $("i", this).toggleClass("fa fa-chevron-up fa fa-chevron-down ");
});

$('#click_advance5').click(function() {
    $('#display_advance5').toggle('1000');
    $("i", this).toggleClass("fa fa-chevron-up fa fa-chevron-down ");
});

$('#click_advance6').click(function() {
    $('#display_advance6').toggle('1000');
    $("i", this).toggleClass("fa fa-chevron-up fa fa-chevron-down ");
});



*/














//(document).foundation();
function background() {
  var leftSide = document.getElementById('left-side');
  var pattern = Trianglify({
    height: leftSide.clientHeight,
    width: leftSide.clientWidth,
    cell_size: 250,
    x_colors: ['#3B5168', '#364b60', '#3F5870', '#445E79', '#496481', '#4D6B89', '#527191']
  });

  /*lighten($main-color, 12%, 10%, 7%, 5%)
  ['#435c77','#3f5771','#3a5067','#364b60']*/

  /*https://vis4.net/blog/posts/avoid-equidistant-hsv-colors/
  lighten($main-color, 20%) lighten($main-color, 5%)

  ['#3B5168', '#364b60', '#3F5870', '#445E79', '#496481', '#4D6B89', '#527191']*/
  console.log("errouu");
  leftSide.setAttribute('style', 'background-image: url\(' + pattern.png() + '\)');
}

background();
$('.do-toggle').click(function() {
  $(this).closest('.toggle-title').next().slideToggle();
  if ($(this).find('i').hasClass('fa-chevron-up')) {
    $(this).find('i').removeClass('fa-chevron-up').addClass('fa-chevron-down');
  } else {
    $(this).find('i').removeClass('fa-chevron-down').addClass('fa-chevron-up');
    if ($(this).closest('#left-side').length > 0) {
      setTimeout(background, 500);
    }
  }
});

//Chirs Coyer Resizing
var resizeTimer;

$(window).on('resize', function(e) {

  clearTimeout(resizeTimer);
  resizeTimer = setTimeout(background, 250);

});


