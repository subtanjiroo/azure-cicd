document.addEventListener('DOMContentLoaded', function () {
    // Khai báo biến URL
    const baseURL = 'http://127.0.0.1:8070';

    // Gắn sự kiện click cho phần tử có class 'navLogo'
    document.querySelector('.navLogo').addEventListener('click', function () {
        window.location.href = `${baseURL}/home`;
    });


{/* <!-- API information --> */}


    const urlParams = new URLSearchParams(window.location.search);
    const itemId = urlParams.get('ProjectID');

    if (itemId) {
        console.log('ID đã nhận:', itemId);
    }










// <!--navigationbar menu effect -->

    const wrapwrap = document.documentElement;
    const navigation_bar = document.getElementById('nav_bar');
    if (navigation_bar) {
        window.addEventListener('scroll', function() {
            if (wrapwrap.scrollTop > 50) {
                navigation_bar.classList.add('fixed');
            } else {
                navigation_bar.classList.remove('fixed');
            }
        });
    } else {
        console.error('Element with ID "wrapwrap" or "nav_bar" not found.');
    }





        const menuItems = document.querySelectorAll('.menu-item');

        menuItems.forEach(item => {
            item.addEventListener('click', function () {
                const itemId = this.id;
                window.location.href = `${baseURL}/home?itemId=${itemId}`;
            });
        });




        // Cấu hình Swiper
        const swiper = new Swiper('#carousel3', {
            loop: true, // Cho phép vòng lặp không giới hạn
            spaceBetween: 10, // Khoảng cách giữa các item
            slidesPerView: 1, // Mặc định chỉ hiển thị 1 item
    
            // Cấu hình responsive breakpoints
            breakpoints: {
                1500: {
                    slidesPerView: 1, 
                },
                1200: {
                    slidesPerView: 1, 
                },
                850: {
                    slidesPerView: 2, 
                },
                600: {
                    slidesPerView: 1,
                },
            },
    
            // Loại bỏ pagination và navigation (dots và arrows)
            pagination: false,
            navigation: false
        });
});

