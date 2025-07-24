const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");

function addMessage(message, sender) {
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("message", sender);
  messageDiv.textContent = message;
  chatBox.appendChild(messageDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function sendMessage() {
  const input = userInput.value.trim();
  if (input === "") return;

  addMessage("You: " + input, "user");
  userInput.value = "";

  fetch("http://localhost:5000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question: input })
  })
  .then(res => res.json())
  .then(data => {
    addMessage("Bot: " + data.answer, "bot");
  })
  .catch(err => {
    console.error(err);
    addMessage("Bot: Sorry, there was an error.", "bot");
  });
}
