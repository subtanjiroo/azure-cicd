fetch('/get_div_1', {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    }
})
.then(response => response.json())
.then(data => {
    const HomeData = data;
    // <!-- render data from api -->
    const main_title = document.querySelector('.main_title');
    if (main_title) {
        main_title.innerText = HomeData.main_title;
    }
    const main_text = document.querySelector('.main_text');
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
})
.catch(error => {
    console.error('Error fetching data:', error);
});