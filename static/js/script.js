// smooth-scrolling
function scrollTopBtn() {
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
}
$(document).ready(function () {
  var swiper = new Swiper(".swiper", {
    effect: "coverflow",
    grabCursor: false,
    centeredSlides: true,
    slidesPerView: "auto",
    coverflowEffect: {
      rotate: 15,
      stretch: 0,
      depth: 150,
      modifier: 2,
      slideShadows: true,
    },
    autoplay: {
      delay: 2500,
      disableOnInteraction: false,
    },
    loop: true,
    pagination: {
      el: ".swiper-pagination",
    },
  });

  // text-box-slider
  $(".owl-carousel").owlCarousel({
    items: 1,
    loop: true,
    autoplay: true,
    autoplaySpeed: 1000,
    autoplayTimeout: 10000,
    dots: false,
    touchDrag: false,
    mouseDrag: false,
    smartSpeed: 500,
    animateIn: "slideInRight",
    animateOut: "fadeOut",
  });

  // sticky-header
  window.onscroll = function () {
    headerFunction();
  };

  var body = document.body;
  var sticky = body.offsetTop;

  function headerFunction() {
    if (window.pageYOffset > 150) {
      body.classList.add("sticky");
    } else {
      body.classList.remove("sticky");
    }
  }
  //   mobile-menu
  function MobileMenu() {
    let menuIcon = document.querySelector(".hamburger");
    let body = document.querySelector("body");
    let overlay = document.querySelector(".overlay");
    menuIcon.addEventListener("click", function () {
      body.classList.toggle("active");
    });
    overlay.addEventListener("click", function () {
      body.classList.remove("active");
    });
    $(".mobile-menu ul li").click(() => {
      body.classList.remove("active");
    });
  }
  MobileMenu();

  //   activating-main-header-elements
  $("header .menu li").click(function () {
    $("header .menu li.active").removeClass("active");
    $(this).addClass("active");
  });

  //   activating-elements-mobile-menu
  $(".mobile-menu ul li").click(function () {
    $("header .mobile-menu li.active").removeClass("active");
    $(this).addClass("active");
  });

  // latest-things-slider
  $(".latest").slick({
    lazyLoad: "ondemand",
    dots: true,
    arrows: true,
    prevArrow:
      '<button class="slide-arrow prev-arrow"><i class="fas fa-chevron-left"></i></button>',
    nextArrow:
      '<button class="slide-arrow next-arrow"><i class="fas fa-chevron-right"></i></button>',
    infinite: true,
    speed: 500,
    slidesToShow: 3,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 4000,
    pauseOnHover: true,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1,
          infinite: true,
        },
      },
      {
        breakpoint: 769,
        settings: {
          arrows: false,
          slidesToShow: 2,
          slidesToScroll: 1,
        },
      },
      {
        breakpoint: 481,
        settings: {
          arrows: false,
          slidesToShow: 1,
          slidesToScroll: 1,
        },
      },
    ],
  });
});
AOS.init();

$(document).on("submit", "form.ajax", function (e) {
  e.preventDefault();
  var $this = $(this);

  document.onkeydown = function (evt) {
    return false;
  };

  var url = $this.attr("action");
  var method = $this.attr("method");
  var isReload = $this.hasClass("reload");
  var isRedirect = $this.hasClass("redirect");
  var noLoader = $this.hasClass("no-loader");
  var noPopup = $this.hasClass("no-popup");

  if (!noLoader) {
    Swal.showLoading();
  }

  jQuery.ajax({
    type: method,
    url: url,
    dataType: "json",
    data: new FormData(this),
    cache: false,
    contentType: false,
    processData: false,
    success: function (data) {
      console.log("success");
      if (!noLoader) {
        Swal.hideLoading();
      }

      var message = data["message"];
      var status = data["status"];
      var title = data["title"];
      var redirect = data["redirect"];
      var redirect_url = data["redirect_url"];
      var stable = data["stable"];

      if (status == "success") {
        if (title) {
          title = title;
        } else {
          title = "Success";
        }

        function doAfter() {
          if (stable != "yes") {
            console.log(isRedirect );
            console.log(redirect);
            if (isRedirect && redirect === "yes") {
              window.location.href = redirect_url;
              console.log(window.location.href);
            }
            if (isReload) {
              window.location.reload();
            }
          }
        }

        if (noPopup) {
          doAfter();
        } else {
          Swal.fire({
            icon: status,
            title: title,
            html: message,
          }).then((result) => {
            console.log(result.isConfirmed);
            if (result.isConfirmed) {
              doAfter();
            }
          });
        }
        document.onkeydown = function (evt) {
          return true;
        };
      } else {
        if (title) {
          title = title;
        } else {
          title = "An Error Occurred";
        }

        Swal.fire(title, message, "error");

        if (stable != "true") {
          window.setTimeout(function () {}, 2000);
        }
        document.onkeydown = function (evt) {
          return true;
        };
      }
    },
    error: function (data) {
      console.log("err");
      Swal.hideLoading();

      var title = "An error occurred";
      var message = "An error occurred. Please try again later.";
      document.onkeydown = function (evt) {
        return true;
      };
      Swal.fire(title, message, "error");
    },
  });
});


