document.addEventListener('DOMContentLoaded', () => {

    // Fetch và render nội dung cho carousel1
    fetch('/get_div_4', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        const grid_items = data.projects;
        const HomeData = data;
        const swiperWrapper1 = document.querySelector('#carousel1 .swiper-wrapper'); // Đảm bảo là swiper-wrapper
        const main_title = document.querySelector('.main_title_div4');
        if (main_title) {
            main_title.innerText = HomeData.main_title;
        }

        if (grid_items && swiperWrapper1) {
            grid_items.forEach(item => {
                const cardHTML = `
                    <div class="swiper-slide">
                        <div class="item_slider">
                            <div class="slider_img">
                                <img src="https://demo.canhcam.com/the7-law/wp-content/uploads/2018/01/bg-law-section-06-440x440.jpg" alt="img"/>
                            </div>
                            <span>${item.title}</span>
                            <p>${item.small_text}</p>
                        </div>
                    </div>
                `;
                swiperWrapper1.innerHTML += cardHTML;
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
