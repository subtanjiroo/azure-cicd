document.addEventListener('DOMContentLoaded', () => {
    fetch('/get_div_3', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        // Kiểm tra xem phản hồi có phải là JSON không
        if (response.ok) {
            return response.json();  // Chỉ chuyển thành JSON nếu phản hồi hợp lệ
        } else {
            // Nếu không phải JSON, kiểm tra nội dung trả về
            return response.text().then(text => {
                throw new Error('Received non-JSON response: ' + text);
            });
        }
    })
    .then(data => {
        const HomeData = data;
        const main_title = document.querySelector('.main_title_div3');
        if (main_title) {
            main_title.innerText = HomeData.main_title;
        }
        const text_div3 = document.querySelector('.text_div3');
        if (text_div3) {
            text_div3.innerText = HomeData.text_div3;
        }
        const grid_items = HomeData.icon_and_text;
        const contentBox = document.getElementById('content3_box2_grid');

        if (grid_items && contentBox) {
            // Lặp qua các phần tử flip_board và render vào div
            grid_items.forEach(items => {
                const cardHTML = `
                    <div class="content3_box2_grid_item">
                        <div class="content3_logo"><i class="fa-solid fa-graduation-cap"></i></div>
                        <div class="content3_box2_text">${items.text}</div>
                    </div>
                `;
                // Thêm phần tử vào div chứa thẻ bài
                contentBox.innerHTML += cardHTML;
            });
        }



    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
});