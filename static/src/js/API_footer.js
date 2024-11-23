document.addEventListener('DOMContentLoaded', function () {
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
