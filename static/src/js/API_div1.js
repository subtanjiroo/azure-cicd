document.addEventListener('DOMContentLoaded', () => {
    async function fetchAndRenderData() {
        try {
            const response = await fetch('/get_div_1', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            const HomeData = await response.json();
            console.log(HomeData);
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


            // Render data from API
            // const card_logo_left = document.querySelector('.card_logo_left');
            // if (card_logo_left && HomeData.left_icon) {
            //     let asciiString = decodeBase64ToAscii(HomeData.left_icon); // Giải mã base64 sang ASCII
            //     card_logo_left.src = `data:image/png;base64,${asciiString}`; // Gán vào thẻ <img>

            // }

            const card_logo_mid = document.querySelector('.card_logo_mid');
            if (card_logo_mid && HomeData.mid_icon) {
                let asciiString = decodeBase64ToAscii(HomeData.mid_icon);
                card_logo_mid.src = `data:image/png;base64,${asciiString}`;
            }

            const card_logo_right = document.querySelector('.card_logo_right');
            if (card_logo_right && HomeData.right_icon) {
                let asciiString = decodeBase64ToAscii(HomeData.right_icon);
                card_logo_right.src = `data:image/png;base64,${asciiString}`;
            }

            const main_title = document.querySelector('.main_title_div1');
            if (main_title) {
                main_title.innerText = HomeData.main_title;
            }
            const main_text = document.querySelector('.main_text_div1');
            if (main_text) {
                main_text.innerText = HomeData.main_text;
            }
            const left_title = document.querySelector('.left_title');
            if (left_title) {
                left_title.innerText = HomeData.left_title;
            }
            const left_text = document.querySelector('.left_text');
            if (left_text) {
                left_text.innerText = HomeData.left_text;
            }
            const mid_title = document.querySelector('.mid_title');
            if (mid_title) {
                mid_title.innerText = HomeData.mid_title;
            }
            const mid_text = document.querySelector('.mid_text');
            if (mid_text) {
                mid_text.innerText = HomeData.mid_text;
            }
            const right_title = document.querySelector('.right_title');
            if (right_title) {
                right_title.innerText = HomeData.right_title;
            }
            const right_text = document.querySelector('.right_text');
            if (right_text) {
                right_text.innerText = HomeData.right_text;
            }
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }

    // Gọi hàm để lấy và render dữ liệu
    fetchAndRenderData();
});
