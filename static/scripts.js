document.addEventListener('DOMContentLoaded', () => {
    const chatOutput = document.getElementById('chat-output');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');

    sendBtn.addEventListener('click', () => {
        const userMessage = userInput.value.trim();
        if (userMessage !== '') {
            appendMessage('You', userMessage);
            userInput.value = '';

            fetch('/send', {
                method: 'POST',
                body: JSON.stringify({ message: userMessage }),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(data => {
                appendMessage('Chatbot', data.message);
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    });

    function appendMessage(sender, message) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message');
        messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
        chatOutput.appendChild(messageElement);
        chatOutput.scrollTop = chatOutput.scrollHeight;
    }
});
