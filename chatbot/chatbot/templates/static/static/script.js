```javascript
const chatWindow = document.getElementById("chatWindow");
const userInput = document.getElementById("userInput");
const sendBtn = document.getElementById("sendBtn");


function addMessage(message, sender){

    const div = document.createElement("div");

    div.className = sender + "-message";

    div.innerHTML = message;

    chatWindow.appendChild(div);

    chatWindow.scrollTop = chatWindow.scrollHeight;

}


function typingAnimation(){

    const div = document.createElement("div");

    div.className = "typing";

    div.id = "typing";

    div.innerHTML = "🤖 Typing...";

    chatWindow.appendChild(div);

    chatWindow.scrollTop = chatWindow.scrollHeight;

}


function removeTyping(){

    const typing = document.getElementById("typing");

    if(typing){

        typing.remove();

    }

}


async function sendMessage(){

    const message = userInput.value.trim();

    if(message==="") return;

    addMessage(message,"user");

    userInput.value="";

    typingAnimation();

    try{

        const response = await fetch("/chat",{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({

                message:message

            })

        });

        const data = await response.json();

        removeTyping();

        addMessage(data.reply,"bot");

    }

    catch(error){

        removeTyping();

        addMessage(
            "Server Error. Please try again.",
            "bot"
        );

    }

}


sendBtn.addEventListener("click",sendMessage);


userInput.addEventListener("keypress",function(e){

    if(e.key==="Enter"){

        sendMessage();

    }

});
```
