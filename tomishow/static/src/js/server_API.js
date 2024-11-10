/** @odoo-module **/

export async function sendMessage(messageState, env) {
    const messageInput = document.getElementById('message_input');
    const chatInput = document.getElementById('CHAT_INPUT');

    // Lấy giá trị tin nhắn từ messageState
    const message = messageState.message;
    if (message) {
        try {
            const response = await env.services.rpc('/chat/send', { message: message });

            // Tạo div chứa tin nhắn của người dùng
            const client_message = document.createElement('div');
            client_message.className = 'client_message';
            client_message.textContent = message;

            // Sử dụng CSS để hiển thị văn bản có ký tự xuống dòng
            client_message.style.whiteSpace = 'pre-line';

            const messagesContainer = document.getElementById('messages');
            messagesContainer.appendChild(client_message);

            // Tạo div chứa tin nhắn từ server
            const server_message = document.createElement('div');
            server_message.className = 'server_message';
            server_message.textContent = response.status;
            server_message.style.whiteSpace = 'pre-line';

            messagesContainer.appendChild(server_message);
            messagesContainer.scrollTo(0, messagesContainer.scrollHeight);

            // Reset tin nhắn sau khi gửi
            messageState.message = '';
            messageInput.style.height = '30px'; // Đặt lại chiều cao ban đầu cho textarea
            chatInput.style.height = '4em'; // Đặt lại chiều cao ban đầu cho phần chat input

        } catch (error) {
            console.error("Error sending message:", error);
        }
    }
}