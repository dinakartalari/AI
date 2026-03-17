async function sendMessage() {
    const input = document.getElementById("message");
    const chatBox = document.getElementById("chat-box");

    const userText = input.value;
    chatBox.innerHTML += `<p><b>You:</b> ${userText}</p>`;

    input.value = "";

    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userText })
    });

    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    let aiMessage = "";
    chatBox.innerHTML += `<p><b>AI:</b> <span id="ai-response"></span></p>`;
    const aiSpan = document.getElementById("ai-response");

    while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        const chunk = decoder.decode(value);
        aiMessage += chunk;
        aiSpan.innerHTML = aiMessage;
    }
}