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