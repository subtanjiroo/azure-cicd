document.addEventListener('DOMContentLoaded', () => {
    async function fetchAndRenderData() {
        try {
            const response = await fetch('/get_div_5', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            
            if (response.ok) {
                const data = await response.json();
                const HomeData = data;
                console.log(HomeData);
                function decodeBase64ToAscii(base64String) {
                    // Giải mã base64 thành ASCII
                    let binaryString = atob(base64String);
                    let asciiString = '';
                    for (let i = 0; i < binaryString.length; i++) {
                        asciiString += String.fromCharCode(binaryString.charCodeAt(i));
                    }
                    return asciiString;
                }
                const img = decodeBase64ToAscii(HomeData.image);

                const imgs_div5 = document.querySelector('.content5_img');
                if (imgs_div5) {
                    imgs_div5.innerHTML = `<img loading="lazy" src="data:image/png;base64,${img}"/>`;
                }
                const quote_div5 = document.querySelector('.quote_div5');
                if (quote_div5) {
                    quote_div5.innerText = HomeData.quote;
                }
                const author_div5 = document.querySelector('.author_div5');
                if (author_div5) {
                    author_div5.innerText = HomeData.author;
                }
                const title_div5 = document.querySelector('.title_div5');
                if (title_div5) {
                    title_div5.innerText = HomeData.title;
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