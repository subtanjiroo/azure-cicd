document.addEventListener('DOMContentLoaded', () => {
    fetch('/get_div_7', {
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
        const main_title = document.querySelector('.main_title_div7');
        if (main_title) {
            main_title.innerText = HomeData.main_title;
        }
        const title = document.querySelector('.title_div7');
        if (title) {
            title.innerText = HomeData.title;
        }
        const grid_items = HomeData.process;
        const menu_items = HomeData.rule;
        const contentBox = document.getElementById('content7_grid');
        let counting = 0;
        
        

        // Lặp qua process và render vào contentBox
        grid_items.forEach((item, index) => {
            counting++;
            const cardHTML = `
                <div class="content7_grid_number">${counting}</div>
                <div class="content7_grid_items">${item.text}</div>
            `;
            contentBox.innerHTML += cardHTML;
        });


        // Vòng lặp để render nội dung vào các circle_text
        menu_items.forEach((item, index) => {
            // Tạo class selector tương ứng: circle_text1, circle_text2, ...
            const circleTextSelector = `.circle_text${index + 1}`;
            const circleTextElement = document.querySelector(circleTextSelector);

            if (circleTextElement) {
                // Render nội dung vào phần tử
                const cardHTML = `
                    <i class="fa-solid fa-graduation-cap center_circle_logo"></i>
                    <p class="center_circle_text">${item.title}</p>
                    <p class="center_circle_subtext">${item.text}</p>
                `;
                circleTextElement.innerHTML = cardHTML;
            }
        });




    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
});
