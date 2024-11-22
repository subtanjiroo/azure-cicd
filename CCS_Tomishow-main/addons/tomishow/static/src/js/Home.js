// <!-- link config -->

document.addEventListener('DOMContentLoaded', function () {
    // Khai báo biến URL
    const baseURL = 'http://127.0.0.1:8070';

    // Gắn sự kiện click cho phần tử có class 'navLogo'
    document.querySelector('.navLogo').addEventListener('click', function () {
        window.location.href = `${baseURL}/home`;
        
    });

    const SlidersItems = document.querySelectorAll('.item_slider');
    SlidersItems.forEach(item => {
        item.addEventListener('click', function () {

            //id project here

            const itemId = "testing";
            
            window.location.href = `${baseURL}/details?ProjectId=${itemId}`;
        });
    });
    
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
    var navItems = document.querySelectorAll('.menu-item');
    navItems.forEach(function(item) {
        item.addEventListener('click', function(event) {
            // Ngăn chặn hành vi mặc định (di chuyển đến phần tử)
            event.preventDefault();

            // Lấy ID của item và phần tử tương ứng
            var targetId = 'section' + item.id.replace('menuItems', '');
            // Kiểm tra phần tử có tồn tại không
            var targetElement = document.querySelector('#' + targetId);

            // Cuộn mượt đến phần tử tương ứng
            targetElement.scrollIntoView({
                behavior: 'smooth',
                block: 'start' // Đảm bảo phần tử xuất hiện ở đầu màn hình
            });
        });
    });

    // Chọn tất cả các phần tử có id như #section1, #section2, #section3, ...
    const sections = document.querySelectorAll('[id^="section"]'); // Chọn tất cả các phần tử có id bắt đầu bằng 'section'

    // Khởi tạo một đối tượng để theo dõi trạng thái đã xuất hiện của từng section
    const visibilityMap = {};

    const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        const sectionId = entry.target.id;

        const menuItem = document.querySelector(`#menuItems${sectionId.replace('section', '')}`);
        if (entry.isIntersecting) {
            
            // Gỡ bỏ class 'watching' khỏi tất cả các menu item khác
            const allMenuItems = document.querySelectorAll('.menu-item');
            allMenuItems.forEach(item => {
                if (item !== menuItem) {
                    item.classList.remove('watching');
            }});


            // Khi phần tử xuất hiện trong viewport
            if (!visibilityMap[sectionId]) {
                menuItem.classList.add('watching');
                visibilityMap[sectionId] = true; // Đánh dấu phần tử đã xuất hiện
            }
            } else {
            // Khi phần tử không còn xuất hiện trong viewport
            if (visibilityMap[sectionId]) {
                menuItem.classList.remove('watching');
                visibilityMap[sectionId] = false; // Đánh dấu phần tử không còn xuất hiện trong viewport
            }
        }
    });
    }, { threshold: 0.2 }); // Ngưỡng xuất hiện trong viewport

    // Áp dụng observer cho tất cả các section
    sections.forEach(section => {
    observer.observe(section);
    });

});


// <!--navigationbar menu effect -->

document.addEventListener('DOMContentLoaded', function() {
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
});

document.addEventListener('DOMContentLoaded', function () {
    const urlParams = new URLSearchParams(window.location.search);
    const itemId = urlParams.get('itemId');

    if (itemId) {
        var targetId = 'section' + itemId.replace('menuItems', '');
        var targetElement = document.querySelector('#' + targetId);
        console.log(targetId)
        console.log(targetElement)
        targetElement.scrollIntoView({
                behavior: 'smooth',
                block: 'start' // Đảm bảo phần tử xuất hiện ở đầu màn hình
            });
    }
});


// <!-- javascript cua Owl carousel -->
// $(document).ready(function() {
//     // Cấu hình cho carousel thứ nhất


//     // Cấu hình cho carousel thứ hai

//     $("#carousel3").owlCarousel({
//         items: 1,         
//         loop: true,       
//         autoplay: true,   
//         mouseDrag: true,  
//         touchDrag: true,  
//         nav: false,       
//         dots: false,
//         responsive: {
//             0:{
//                 items: 1
//             },
//             850:{
//                 items: 2
//             },
//             1200: {
//                 items: 1
//             },
//         },
//     });
// });


// infor circle effect
function showText(index) {
    // Ẩn tất cả các text
    const texts = document.querySelectorAll('.center_circle div');
    texts.forEach(text => {
        text.classList.remove('active');
    });

    // Hiển thị text tương ứng
    const selectedText = document.querySelector(`.circle_text${index}`);
    if (selectedText) {
        selectedText.classList.add('active');
    }
}

// Hiển thị mặc định text1
document.addEventListener('DOMContentLoaded', () => {
    showText(1);
});

// fade in 
document.addEventListener("DOMContentLoaded", function () {
    const fadeElements = document.querySelectorAll('.fade-in');

    const observerOptions = {
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // Chỉ trigger một lần
            }
        });
    }, observerOptions);

    fadeElements.forEach(el => {
        observer.observe(el);
    });
});


