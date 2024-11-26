document.addEventListener('DOMContentLoaded', () => {
    async function fetchAndRenderData() {
        try {
            const response = await fetch('/get_div_2', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            function decodeBase64ToAscii(base64String) {
                // Giải mã base64 thành ASCII
                let binaryString = atob(base64String);
                let asciiString = '';
                for (let i = 0; i < binaryString.length; i++) {
                    asciiString += String.fromCharCode(binaryString.charCodeAt(i));
                }
                return asciiString;
            }
            if (response.ok) {
                const data = await response.json();
                const HomeData = data;
                

                const title_1 = document.querySelector('.title_1');
                if (title_1) {
                    title_1.innerText = HomeData.title_1;
                }
                const title_2 = document.querySelector('.title_2');
                if (title_2) {
                    title_2.innerText = HomeData.title_2;
                }
                const title_3 = document.querySelector('.title_3');
                if (title_3) {
                    title_3.innerText = HomeData.title_3;
                }
                const title_4 = document.querySelector('.title_4');
                if (title_4) {
                    title_4.innerText = HomeData.title_4;
                }
                const text_1 = document.querySelector('.text_1');
                if (text_1) {
                    text_1.innerText = HomeData.text_1;
                }
                const text_2 = document.querySelector('.text_2');
                if (text_2) {
                    text_2.innerText = HomeData.text_2;
                }
                const text_3 = document.querySelector('.text_3');
                if (text_3) {
                    text_3.innerText = HomeData.text_3;
                }
                const text_4 = document.querySelector('.text_4');
                if (text_4) {
                    text_4.innerText = HomeData.text_4;
                }
                const main_text = document.querySelector('.main_text_div2');
                if (main_text) {
                    main_text.innerText = HomeData.main_text;
                }
                const main_title = document.querySelector('.main_title_div2');
                if (main_title) {
                    main_title.innerText = HomeData.main_title;
                }

                const flipBoardData = HomeData.flip_board;
                const contentBox = document.getElementById('content2_box2');
                if (flipBoardData && contentBox) {
                    flipBoardData.forEach(flip => {
                        const cardHTML = `
                            <div class="content2_card">
                                <div class="card-inner" style="background:linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.8)),url(data:image/png;base64,${decodeBase64ToAscii(flip.background_image)});background-size: cover;background-position: center top;background-repeat: no-repeat;">
                                    <!-- Front of the Card -->
                                    <div class="card-front">
                                        <p>${flip.text_not_flipped}</p>
                                    </div>
                                    <!-- Back of the Card -->
                                    <div class="card-back">
                                        <h2>Hiệu Lực Hợp Đồng</h2>
                                        <p>${flip.text_flipped}</p>
                                    </div>
                                </div>
                            </div>
                        `;
                        contentBox.innerHTML += cardHTML;
                    });
                } else {
                    console.error('Dữ liệu flip_board không hợp lệ hoặc không có');
                }
            } else {
                const text = await response.text();
                throw new Error('Received non-JSON response: ' + text);
            }
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }

    // Gọi hàm
    fetchAndRenderData();
});