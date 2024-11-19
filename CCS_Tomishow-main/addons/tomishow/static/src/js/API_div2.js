fetch('/get_div_2', {
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
    console.log(HomeData);

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
    const main_text = document.querySelector('.main_text');
    if (main_text) {
        main_text.innerText = HomeData.main_text;
    }
    const main_title = document.querySelector('.main_title');
    if (main_title) {
        main_title.innerText = HomeData.main_title;
    }
    const flipBoardData = HomeData.flip_board
    const contentBox = document.getElementById('content2-box');
    
    // Kiểm tra nếu có dữ liệu flip_board
    if (flipBoardData && contentBox) {
        // Lặp qua các phần tử flip_board và render vào div
        flipBoardData.forEach(flip => {
            const cardHTML = `
                <div class="content2_card">
                    <div class="card-inner">
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
            // Thêm phần tử vào div chứa thẻ bài
            contentBox.innerHTML += cardHTML;
        });
    } else {
        console.error('Dữ liệu flip_board không hợp lệ hoặc không có');
    }
})
.catch(error => {
    console.error('Error fetching data:', error);
});
