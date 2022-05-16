//'use stric';

var stripe = Stripe('pk_test_51KX5arLvDIT3jWikCrBH1b5jsW12D4fL81PJnH1RjCVqKTScj3bC28uI5qmdqj5EtccIEO6z7qBzXMq5kpXzJITJ0030qYHEGq');

var elem = document.getElementById('submit');
client_secret = elem.getAttribute('data-secret');

// Set up Stripe.js and Elements to use in checkout form
var elements = stripe.elements();
var style = {
base: {
  
  color: "#000",
  lineHeight: '2.4',
  fontSize: '16px'
}
};


var card = elements.create("card", { style: style,hidePostalCode:true });
card.mount("#card-element");

card.on('change', function(event) {
var displayError = document.getElementById('card-errors')
if (event.error) {
  displayError.textContent = event.error.message;
  $('#card-errors').addClass('alert alert-info');
} else {
  displayError.textContent = '';
  $('#card-errors').removeClass('alert alert-info');
}
});

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
ev.preventDefault();


var custName = document.getElementById("name").value;
var custCountry = document.getElementById("country").value;
var custState = document.getElementById("state").value;
var custCity = document.getElementById("city").value;
var custDistrict = document.getElementById("district").value;
var custStreet = document.getElementById("street").value;
var CustNumber = document.getElementById("number").value;
var cep = document.getElementById("cep").value;
var custPhone = document.getElementById("phone").value;


  $.ajax({
    type: "POST",
    url: 'http://127.0.0.1:8000/orders/add/',
    data: {
      order_key: client_secret, 
      csrfmiddlewaretoken: CSRF_TOKEN,
      action: "post",
    },
    success: function (json) {
      console.log(json.success)

      stripe.confirmCardPayment(client_secret, {
        payment_method: {
          card: card,
          billing_details: {
            address:{
                line1:custDistrict,
                line2:custStreet,
                city:custCity,
                state:custState,
                country:custCountry,
                postal_code:cep,
            },
            name: custName,
            phone:custPhone 
          },
        }
      }).then(function(result) {
        if (result.error) {
          console.log('payment error')
          console.log(result.error.message);
        } else {
          if (result.paymentIntent.status === 'succeeded') {
            console.log('payment processed')
            // There's a risk of the customer closing the window before callback
            // execution. Set up a webhook or plugin to listen for the
            // payment_intent.succeeded event that handles any business critical
            // post-payment actions.
            window.location.replace("http://127.0.0.1:8000/payment/orderplaced/");
          }
        }
      });

    },
    error: function (xhr, errmsg, err) {},
  });
});