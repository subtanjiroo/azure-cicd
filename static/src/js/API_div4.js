document.addEventListener('DOMContentLoaded', () => {
    const BaseURL="http://localhost:8070";
    // Fetch và render nội dung cho carousel1
    fetch('/get_div_4', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        // Giải mã base64 sang ASCII
        function decodeBase64ToAscii(base64String) {
            // Giải mã base64 thành ASCII
            let binaryString = atob(base64String);
            let asciiString = '';
            for (let i = 0; i < binaryString.length; i++) {
                asciiString += String.fromCharCode(binaryString.charCodeAt(i));
            }
            return asciiString;
        }
        const grid_items = data.projects;
        const HomeData = data;
        const swiperWrapper1 = document.querySelector('#carousel1 .swiper-wrapper'); // Đảm bảo là swiper-wrapper
        const main_title = document.querySelector('.main_title_div4');
        if (main_title) {
            main_title.innerText = HomeData.main_title;
        }

        if (grid_items && swiperWrapper1) {
            grid_items.forEach(item => {
                const img = decodeBase64ToAscii(item.image);
                const cardHTML = `
                    <div class="swiper-slide" data-id="${item.id}"> <!-- Gán data-id để nhận id -->
                        <div class="item_slider">
                            <div class="slider_img">
                                <img src="data:image/png;base64,${img}" alt="img"/>
                            </div>
                            <span>${item.title}</span>
                            <p>${item.small_text}</p>
                        </div>
                    </div>
                `;
                swiperWrapper1.innerHTML += cardHTML;
            });

            // Thêm sự kiện click vào mỗi phần tử
            document.querySelectorAll('#carousel1 .swiper-slide').forEach(slide => {
                slide.addEventListener('click', () => {
                        const itemId = "testing";
                    if (itemId) {
                        window.location.href = `${BaseURL}/details?ID=${itemId}`; // Chuyển hướng tới URL
                    }
                });
            });

            // Khởi tạo Swiper cho carousel1 sau khi phần tử đã được render
            new Swiper('#carousel1', {
                loop: true,
                autoplay: {
                    delay: 3000, // Thời gian chuyển slide (ms)
                    disableOnInteraction: false, // Không dừng autoplay khi tương tác
                },
                slidesPerView: 4,
                spaceBetween: 10,
                breakpoints: {
                    0: { slidesPerView: 1 },
                    600: { slidesPerView: 3 },
                    1000: { slidesPerView: 4 },
                }
            });
        }
    })
    .catch(error => console.error('Error fetching data:', error));

});
