const send = require('gmail-send')({
  user: 'robixxu.notify@gmail.com',
  pass: '',
  to: 'robixxu+gmailSend@live.com',
  subject: 'test',
  text: 'some text'
});

send({},(err, res) => {
  console.log("err", err);
  console.log("res", res);
})