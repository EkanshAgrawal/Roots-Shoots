// Your web app's Firebase configuration
var firebaseConfig = {
    apiKey: "AIzaSyDZp2QPsCZKd6eAz-tvHyWaMxGRrbanvWI",
    authDomain: "customer-c5da4.firebaseapp.com",
    projectId: "customer-c5da4",
    storageBucket: "customer-c5da4.appspot.com",
    messagingSenderId: "336630349643",
    appId: "1:336630349643:web:5cad0cc43f9b8235e7b2ce"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  // Reference messages collection
  var messagesRef = firebase.database().ref('messages');
  
  // Listen for form submit
  document.getElementById('contactForm').addEventListener('submit', submitForm);
  
  // Submit form
  function submitForm(e){
    e.preventDefault();
  
    // Get values
    var email = getInputVal('email');
    var select= getInputVal('select')
  
    // Save message
    saveMessage(email,select,);
  
    // Show alert
    document.querySelector('.alert').style.display = 'block';
  
    // Hide alert after 3 seconds
    setTimeout(function(){
      document.querySelector('.alert').style.display = 'none';
    },3000);
  
    // Clear form
    document.getElementById('contactForm').reset();
  }
  
  // Function to get get form values
  function getInputVal(id){
    return document.getElementById(id).value;
  }
  
  // Save message to firebase
  function saveMessage( email,select){
    var newMessageRef = messagesRef.push();
    newMessageRef.set({
      email:email,
      select:select,
    });
  }
