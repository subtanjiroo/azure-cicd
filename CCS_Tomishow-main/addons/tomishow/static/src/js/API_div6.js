document.addEventListener('DOMContentLoaded', function () {


    fetch('/get_div_6', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        const grid_items = data.people;
        const swiperWrapper2 = document.querySelector('#carousel2 .swiper-wrapper');
        const main_title = document.querySelector('.main_title_div6');
        if (main_title) {
            main_title.innerText = data.main_title;
        }
        if (grid_items && swiperWrapper2) {
            grid_items.forEach(item => {
                const cardHTML = `
                    <div class="swiper-slide">
                        <div class="Lawer_slider_items">
                            <div class="Lawer_slider_imgs">
                                <img src="https://demo.canhcam.com/the7-law/wp-content/uploads/2016/05/luat-su-truong-thanh-duc-189435-508x508.jpg"/>
                            </div>
                            <div class="Lawer_slider_text">
                                <p class="Lawer_slider_heading">${item.name}</p>
                                <p class="Lawer_slider_subtext">${item.position}</p>
                                <p class="Lawer_slider_texting">${item.text}</p>
                            </div>
                            <div class="Lawer_slider_btn">Xem Chi Tiết</div>
                        </div>
                    </div>
                `;
                swiperWrapper2.innerHTML += cardHTML;
            });
    
            // Khởi tạo Swiper cho carousel2
            new Swiper('#carousel2', {
                loop: true,
                autoplay: {
                    delay: 4000, // Thời gian chuyển slide (ms)
                    disableOnInteraction: false,
                },
                slidesPerView: 3,
                spaceBetween: 10,
                breakpoints: {
                    0: { slidesPerView: 1 },
                    600: { slidesPerView: 2 },
                    1000: { slidesPerView: 3 },
                    1800: { slidesPerView: 4 }
                }
            });
        }
    })
    .catch(error => console.error('Error fetching data:', error));
    
    });
    