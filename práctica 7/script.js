function listen() {
  let inputArea = document.getElementById('input-area')
  let outputArea = document.getElementById('output-area') 
  const d = new Date();
  
  
  var recognition = new webkitSpeechRecognition();
  recognition.lang = "es-MX";
  recognition.start();

  recognition.onresult = function(event) {
    let transcript = event.results[0][0].transcript;
    console.log("Trans:", transcript);
    if (transcript.includes("fecha" || transcript.includes("Fecha"))) {
      outputArea.innerHTML = d.getFullYear(), d.getFullYear();
    } else if (transcript.includes("auto") || transcript.includes("Auto")) {
      window.open("https://www.youtube.com/watch?v=vvp9RRVC4-Y")
    }  else if (transcript.includes("weather")) {
      window.open("https://www.google.com/search?q=weather")
    } else if (transcript.includes("teacher")) {
      outputArea.innerHTML = "What do you want Chief..."
    } else {
      outputArea.innerHTML = "I don't know what you mean."
    }
  }
}
