function openNav() {
    document.getElementById("myNav").classList.toggle("menu_width");
    document
        .querySelector(".custom_menu-btn")
        .classList.toggle("menu_btn-style");
}

$(".owl-carousel").owlCarousel({
    loop: true,
    margin: 20,
    nav: true,
    navText: [],
    autoplay: true,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 2
        },
        1000: {
            items: 3
        }
    }
});

$(document).ready(function(){
    $('a[href^="#"]').on('click', function (e) {
        e.preventDefault();
        var target = this.hash;
        var $target = $(target);
        $('html, body').stop().animate({
            'scrollTop': $target.offset().top
        }, 900, 'swing', function () {
            window.location.hash = target;
        });
    });
});

document.getElementById('callbackForm').addEventListener('submit', function(event) {
    alert('Заявка была успешно отправлена!');
});

document.addEventListener('DOMContentLoaded', function() {
    var rentCarButton = document.getElementById('rentCarButton');

    if (rentCarButton) {
        rentCarButton.addEventListener('click', function(event) {
            event.preventDefault();
            alert('Машина была успешно арендована, поздравляем! Наши менеджеры свяжутся с вами в ближайшее время.');
            event.target.closest('form').submit();
        });
    }
});

document.addEventListener('DOMContentLoaded', function() {
    var messageElement = document.getElementById('serverMessage');
    if (messageElement) {
        var message = messageElement.getAttribute('data-message');
        if (message) {
            alert(message);
        }
    }
});



