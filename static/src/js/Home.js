// <!-- link config -->

document.addEventListener('DOMContentLoaded', function () {
    // Khai báo biến URL
    const baseURL = 'http://127.0.0.1:8070';

    // Gắn sự kiện click cho phần tử có class 'navLogo'
    document.querySelector('.navLogo').addEventListener('click', function () {
        window.location.href = `${baseURL}/home`;
        
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


//glow up menu effect
document.addEventListener('DOMContentLoaded', function() {
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

        if (targetElement) {
            smoothScrollTo(targetElement, 1000, 40); // Gọi hàm cuộn mượt
        }
    }
});



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



// scroll animation
function smoothScrollTo(element, duration, offset) {
    const targetPosition = element.getBoundingClientRect().top + window.scrollY - offset; // Vị trí đích
    const startPosition = window.scrollY; // Vị trí bắt đầu
    const distance = targetPosition - startPosition; // Khoảng cách cần cuộn
    let startTime = null;

    function animation(currentTime) {
        if (!startTime) startTime = currentTime; // Thời điểm bắt đầu
        const timeElapsed = currentTime - startTime; // Thời gian đã trôi qua
        const progress = Math.min(timeElapsed / duration, 1); // Tiến độ (tối đa 1)
        const ease = easeInOutCubic(progress); // Áp dụng easing (có thể thay đổi hàm easing)

        window.scrollTo(0, startPosition + distance * ease); // Cuộn tới vị trí hiện tại

        if (timeElapsed < duration) {
            requestAnimationFrame(animation); // Tiếp tục nếu chưa đạt thời gian tối đa
        }
    }

    function easeInOutCubic(t) {
        return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
    }

    requestAnimationFrame(animation); // Bắt đầu animation
}

// Thêm sự kiện click vào menu item
document.querySelectorAll('.menu-item').forEach(function (item) {
    item.addEventListener('click', function (event) {
        event.preventDefault(); // Ngăn hành vi mặc định
        const targetId = this.getAttribute('id').replace('menuItems', 'section');
        const targetElement = document.querySelector(`#${targetId}`);
        if (targetElement) {
            smoothScrollTo(targetElement, 800, 40); // Gọi hàm cuộn mượt
        }
    });
});
