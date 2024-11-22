document.addEventListener('DOMContentLoaded', () => {
    async function fetchAndRenderData() {
        try {
            const response = await fetch('/get_banner', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            const HomeData = await response.json();
            console.log(HomeData)
            // Render data from API
            const logo_left_text = document.querySelector('.logo_left_text_banner');
            if (logo_left_text) {
                logo_left_text.innerText = HomeData.logo_left_text;
            }
            const logo_right_text = document.querySelector('.logo_right_text_banner');
            if (logo_right_text) {
                logo_right_text.innerText = HomeData.logo_right_text;
            }
            const big_title = document.querySelector('.big_title_banner');
            if (big_title) {
                big_title.innerText = HomeData.big_title;
            }
            const small_title = document.querySelector('.small_title_banner');
            if (small_title) {
                small_title.innerText = HomeData.small_title;
            }
            const phone_number = document.querySelector('.phone_number_banner');
            if (phone_number) {
                phone_number.innerText = HomeData.phone_number;
            }
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }

    // Gọi hàm để lấy và render dữ liệu
    fetchAndRenderData();
});
