document.addEventListener('DOMContentLoaded', () => {
    async function fetchAndRenderData() {
        const loadingOverlay = document.querySelector('.loading-overlay');
        
        try {
            // Hiển thị overlay khi bắt đầu render
            if (loadingOverlay) {
                loadingOverlay.classList.remove('hidden');
            }
            function decodeBase64ToAscii(base64String) {
                // Giải mã base64 thành ASCII
                let binaryString = atob(base64String);
                let asciiString = '';
                for (let i = 0; i < binaryString.length; i++) {
                    asciiString += String.fromCharCode(binaryString.charCodeAt(i));
                }
                return asciiString;
            }
            const response = await fetch('/get_header', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            const HomeData = await response.json();
            // Render data từ API
            const bannerDiv = document.querySelector('.banner');
            if (bannerDiv) {
                bannerDiv.style.background = `linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.8)), url(data:image/png;base64,${decodeBase64ToAscii(HomeData.back_ground)})`;
            }
            const logoBanner = document.querySelector('.logo_banner');
            if (logoBanner) {
                logoBanner.src = `data:image/png;base64,${decodeBase64ToAscii(HomeData.logo)}`;
            }
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

            // Ẩn overlay và kích hoạt animation sau khi render xong
            if (loadingOverlay) {
                loadingOverlay.classList.add('hidden');
            }

            const banner = document.querySelector('.banner');
            if (banner) {
                banner.classList.add('show-animation');
            }
        } catch (error) {
            console.error('Error fetching data:', error);

            // Ẩn overlay trong trường hợp lỗi
            if (loadingOverlay) {
                loadingOverlay.classList.add('hidden');
            }
        }
    }

    // Gọi hàm để lấy và render dữ liệu
    fetchAndRenderData();
});
