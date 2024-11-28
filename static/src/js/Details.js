// <!-- javascript cua Owl carousel -->

$(document).ready(function() {
    $("#carousel3").owlCarousel({
        items: 1,         
        loop: true,       
        autoplay: true,   
        mouseDrag: true,  
        touchDrag: true,  
        nav: false,       
        dots: false,
        responsive: {
            0:{
                items: 1
            },
            850:{
                items: 2
            },
            1200: {
                items: 1
            },
        },
    });
});


{/* <!-- link config --> */}

document.addEventListener('DOMContentLoaded', function () {
    // Khai báo biến URL
    const baseURL = 'http://localhost:8069';

    // Gắn sự kiện click cho phần tử có class 'navLogo'
    document.querySelector('.navLogo').addEventListener('click', function () {
        window.location.href = `${baseURL}/home`;
    });
});

{/* <!-- API information --> */}

document.addEventListener('DOMContentLoaded', function () {
    const urlParams = new URLSearchParams(window.location.search);
    const itemId = urlParams.get('ProjectID');

    if (itemId) {
        console.log('ID đã nhận:', itemId);
    }
});


// <!-- javascript menu side -->

function toggleMenu() {
    const sideMenu = document.getElementById("sideMenu");
    const overlay = document.getElementById("dark_overlay");
    const navigation_bar = document.getElementById("nav_bar");
    sideMenu.classList.toggle("open");
    overlay.classList.toggle("display");
    navigation_bar.classList.toggle("hide");
    if (navigation_bar.classList.contains("hide")) {
        navigation_bar.classList.remove("fixed");
    } else {
        navigation_bar.classList.add("fixed");
    }
};

document.addEventListener('DOMContentLoaded', function() {
    // Lắng nghe sự kiện click vào các item trong menu
    var navItems = document.querySelectorAll('.menu-item');

    navItems.forEach(function(item) {
        item.addEventListener('click', function(event) {
            // Ngăn chặn hành vi mặc định (di chuyển đến phần tử)
            event.preventDefault();

            // Lấy ID của item và phần tử tương ứng
            var targetId = 'section' + item.id.replace('menuItems', '');
            console.log('Target ID:', targetId); // Debugging

            // Kiểm tra phần tử có tồn tại không
            var targetElement = document.querySelector('#' + targetId);
            if (!targetElement) {
                console.log('Không tìm thấy phần tử với ID:', targetId); // Debugging nếu không tìm thấy phần tử
                return;
            }

            // Cuộn mượt đến phần tử tương ứng
            targetElement.scrollIntoView({
                behavior: 'smooth',
                block: 'start' // Đảm bảo phần tử xuất hiện ở đầu màn hình
            });
        });
    });
});







// <!--navigationbar menu effect -->

document.addEventListener('DOMContentLoaded', function() {
    const wrapwrap = document.getElementById('wrapwrap');
    const navigation_bar = document.getElementById('nav_bar');
    if (navigation_bar) {
        wrapwrap.addEventListener('scroll', function() {
            
            if (wrapwrap.scrollTop > 50) {
                navigation_bar.classList.add('fixed');
            } else {
                navigation_bar.classList.remove('fixed');
            }
        });
    } else {
        console.error('Element with ID "wrapwrap" or "nav_bar" not found.');
    }
});


document.addEventListener('DOMContentLoaded', function () {
        const menuItems = document.querySelectorAll('.menu-item');

        menuItems.forEach(item => {
            item.addEventListener('click', function () {
                const itemId = this.id;
                window.location.href = `http://localhost:8069/home?itemId=${itemId}`;
            });
        });
    });

