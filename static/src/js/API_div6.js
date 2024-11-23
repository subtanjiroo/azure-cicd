document.addEventListener('DOMContentLoaded', function () {


    fetch('/get_div_6', {
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
        const grid_items = data.people;
        const swiperWrapper2 = document.querySelector('#carousel2 .swiper-wrapper');
        const main_title = document.querySelector('.main_title_div6');
        if (main_title) {
            main_title.innerText = data.main_title;
        }
        if (grid_items && swiperWrapper2) {

            grid_items.forEach(item => {
                const img = decodeBase64ToAscii(item.image);
                const cardHTML = `
                    <div class="swiper-slide">
                        <div class="Lawer_slider_items">
                            <div class="Lawer_slider_imgs">
                                <img src="data:image/png;base64,${img}" alt="img"/>
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
    