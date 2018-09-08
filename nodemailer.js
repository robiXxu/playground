var nodemailer = require('nodemailer');
var sgTransport = require('nodemailer-sendgrid-transport');

var options = {
  auth: {
    api_user: 'robixxutest1',
    api_key: 'test123123'
  }
}

var client = nodemailer.createTransport(sgTransport(options));

var email = {
  from: 'zkfw@nezzart.com',
  to: 'robixxu@yahoo.com',
  subject: 'Hello',
  text: 'Hello world',
  html: '<b>Hello world</b>'
};

client.sendMail(email, function(err, info){
    if (err ){
      console.log(err);
    }
    else {
      console.log('Message sent: ' + JSON.stringify(info, null, 2));
    }
});