const SparkPost = require('sparkpost');
const API_KEY = '3a5dfb97448d6e7f0257676eec2689dbc93b2808';
const client = new SparkPost(API_KEY, { debug: true});

client.transmissions.send({
  content: {
    from: 'chothajest@wemel.top',
    subject: 'Hello, World!',
    html:'<html><body><p>Testing SparkPost - the world\'s most awesomest email service!</p></body></html>'
  },
  recipients: [
    {address: 'robixxu+testmail@live.com'}
  ]
})
.then(data => {
  console.log('Woohoo! You just sent your first mailing!');
  console.log(data);
})
.catch(err => {
  console.log('Whoops! Something went wrong');
  console.log(err);
});