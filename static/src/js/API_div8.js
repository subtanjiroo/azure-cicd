document.addEventListener('DOMContentLoaded', () => {
    fetch('/get_div_8', {
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
        // Giải mã base64 sang ASCII
        function decodeBase64ToAscii(base64String) {
            // Giải mã base64 thành ASCII
            let binaryString = atob(base64String);
            let asciiString = '';
            for (let i = 0; i < binaryString.length; i++) {
                asciiString += String.fromCharCode(binaryString.charCodeAt(i));
            }
            console.log(asciiString);
            return asciiString;
        };
        const HomeData = data;
        console.log(HomeData);

        const connection = document.querySelector('.content8_text2');
        const connection_items = HomeData.connections;
        connection_items.forEach(item => {
            const img = decodeBase64ToAscii(item.icon);
            const cardHTML = `
                <div class="icon_items">
                    <div><img class="logo_items" src="data:image/png;base64,${img}" alt="img"/></div>
                    <div class="content8_text2_subtext">${item.title}</div>
                    <div class="content8_text2_info">${item.text}</div>
                </div>
            `;
            connection.innerHTML += cardHTML;
        });

    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
});
