$('.chat-bubble').click(function(){
	console.log("Bubbling")
	$('.chat-box').toggleClass('hide');
	$('.chat-bubble').toggleClass('chat-bubble-hover');
})

function scrolldown(l) {
    var div = $(".inner-container");
    div.scrollTop(div.prop('scrollHeight'));
}

const voice = document.querySelector(".voice");
const voice2text = document.querySelector(".voice2text");

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recorder = new SpeechRecognition();

function addHumanText(text) {
  const chatContainer = document.createElement("div");
  chatContainer.classList.add("chat-container");
  const chatBox = document.createElement("p");
  chatBox.classList.add("voice2text");
  const chatText = document.createTextNode(text);
  chatBox.appendChild(chatText);
  chatContainer.appendChild(chatBox);
  return chatContainer;
}

function addBotText(text) {
  const chatContainer1 = document.createElement("div");
  chatContainer1.classList.add("chat-container");
  chatContainer1.classList.add("darker");
  const chatBox1 = document.createElement("p");
  chatBox1.classList.add("voice2text");
  const chatText1 = document.createTextNode(text);
  chatBox1.appendChild(chatText1);
  chatContainer1.appendChild(chatBox1);
  return chatContainer1;
}

function botVoice(message) {
    const speech = new SpeechSynthesisUtterance();
    speech.text = "Sorry, I did not understand that.";

    if (message.includes('how are you')) {
      speech.text = "I am fine, thanks. How are you?";
    }
    if (message.includes('hello')) {
      speech.text = "Hi!! Welcome to our Website. How can I help you today?";
    }
    if (message.includes('good')) {
      speech.text = "That's Nice";
    }
    if (message.includes('fine')) {
      speech.text = "Nice to hear that. How can I assist you today?";
    }
    if (message.includes('weather')) {
      speech.text = "Of course. Where are you currently?";
    }
    if (message.includes('are you a bot')) {
      speech.text = "Yes, I am a bot and a good one. Let me prove it by helping you. How can I assist you?";
    }
    if (message.includes('bye')) {
      speech.text = "Good Bye. Hope to see you soon.";
      setTimeout(() => {  	$('.chat-box').toggleClass('hide'); $('.chat-bubble').toggleClass('chat-bubble-hover'); }, 3000);
    }

    if (message.includes('one') || message.includes('1') || message.includes('what is the difference between bright, medium and low light plants') || message.includes('bright, medium and low light plants') ||(message.includes('bright light plant') && message.includes('what'))  || (message.includes('medium light plant') && message.includes('what'))  || (message.includes('low light plant') && message.includes('what'))) {
      speech.text = "Bright light plants will do well in direct or strong sunlight for the most part of a day. Medium light plants should stay out of the direct sunlight. They should be placed in a bright room and will enjoy partial or filtered sunlight. Low light plants prefer to stay in the shade or to be displayed under fluorescent light."
    }
    if (message.includes('two') || message.includes('2') || message.includes('which indoor plants are the easiest to care for') || message.includes('easiest') || message.includes('indoor plants')) {
      speech.text = "Pothos, Aglaonema, Sansevieria, Dracaena Lisa, Spider, Corn, Iron, ZZ plants, Bird’s Nest fern, Cacti, Succulents.";
    }
    if (message.includes('three') || message.includes('3') || message.includes('which plants are hardy and can take some level of neglect') || message.includes('hardy') || message.includes('neglect')) {
      speech.text = "Iron plant is the toughest. Sansevieria, ZZ, Aglaonema, Dracaena Lisa, Dracaena Art, Yucca, Jade plants, Ponytail Palm, Succulents and Cacti can deal well with some degree of neglect.";
    }
    if (message.includes('four') || message.includes('4') || message.includes('we only have the fluorescent light in our office') || (message.includes('fluorescent light plant') && message.includes('choose'))) {
      speech.text = "Dracaena Lisa, Corn plant, Sansevieria, Iron plant, ZZ plant, Aglaonema. These plants will survive in very well lit with the fluorescent light space. The light must be on for at least 8-10 hours a day.";
    }
    if (message.includes('five') || message.includes('5') || message.includes("I don't have much light in my home. Which plants should I try") || (message.includes('low light plant') && message.includes('choose'))) {
      speech.text = "Iron, Aglaonema, Dracaena Lisa, Sansevieria plants.";
    }
    if (message.includes('six') || message.includes('6') || message.includes('I have a lot of sun in my space. Which plants should I choose') || (message.includes('bright light plant') && message.includes('choose')) || (message.includes('sun') && message.includes('choose'))) {
      speech.text = "Ponytail and Bella palm, Bird of Paradise, Yucca, Jade plant, Majesty palm.";
    }
    if (message.includes('seven') || message.includes('7') || message.includes('do you offer any care tips for plants') || message.includes('care tips')) {
      speech.text = "With a plant of your choice, you will receive printed basic care tips to help you to understand your plant better and get a general understanding of its care. You can always reach out to our customer service at helpdesk@greenway.com if you have any questions or concerns.";
    }
    if (message.includes('eight') || message.includes('8') || message.includes('what fertilizer do you recommend for indoor plants') || message.includes('fertilizer')) {
      speech.text = "Most plants need to be fertilized during Spring time - March, April and May. The fertilizer we use can be applied anything time. Its unique formula will help your plants grow and thrive with this. It contains oilseed extract, a renewable source of plant nutrition which contains amino acids known to improve overall plant health. No GMOs. Pathogen free - heavy metals free. Gentle on plants - no root burn issues.";
    }
    if (message.includes('nine') || message.includes('9') || message.includes('how can I tell if a plant is struggling') || message.includes('struggling')) {
      speech.text = "Here are some general signs of a problem:\n- yellowing or dropping leaves;\n- leaf spots appear brown with a yellow halo;\n- brown or yellow spots or brown edges on leaves;\n- leaves are curling in;\n- droopiness or wilting;\n- white spots or web are showing on a plant;\n- loss of leaf color;\n- weak growth.";
    }
    if (message.includes('ten') || message.includes('10') || message.includes('can I have a plant replaced using an existing planter') || (message.includes('replace') && message.includes('planter'))) {
      speech.text = "If you have purchased a plant potted in one of our Lechuza self-watering planters, you can replace your plant using an existing planter. The same type or any other type of a plant that is available for this planter shape and color.";
    }
    if (message.includes('eleven') || message.includes('11') || message.includes('can I replace a plant I bought in nursery pot') || message.includes('replace')) {
      speech.text = "If your plant dies within first 3 days, we will replace it free of charge. After 3 days period, we don't offer any replacement discounts.";
    }
    if (message.includes('twelve') || message.includes('12') || message.includes('what if my plants/planters arrived damaged') || message.includes('damage')) {
      speech.text = "If your plant(s) or planter(s) arrive damaged, we will replace it free of charge. Notify us within 24 hours via email helpdesk@greenway.com and we will send a replacement asap. Please include pictures and order number.";
    }
    if (message.includes('thirteen') || message.includes('13') || message.includes('suggestions') || message.includes('feedback')) {
      speech.text = "We will be happy to hear from you. Please write to us on greenway@gmail.com";
    }

	$(function() {
		scrolldown();
	});
    speech.volume = 1;
    speech.rate = 1;
    speech.pitch = 1;
    window.speechSynthesis.speak(speech);
    var element = document.getElementById("container");
    element.appendChild(addBotText(speech.text));
}

recorder.onstart = () => {
  console.log('Voice activated');
};

recorder.onresult = (event) => {
  const resultIndex = event.resultIndex;
  const transcript = event.results[resultIndex][0].transcript;
  var element = document.getElementById("container");
  element.appendChild(addHumanText(transcript));
  botVoice(transcript);
};

voice.addEventListener('click', () =>{
  recorder.start();
});