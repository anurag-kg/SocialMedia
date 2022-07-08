$(".elements li a").each(function (i) {
  $(this).hover(function () {
    $(".socialWrapper").toggleClass("elementsActive" + (i + 1));
  });
});

$(".elements li a").each(function (i) {
  $(this).hover(function () {
    $("body").toggleClass("elementsActive" + (i + 1));
  });
});