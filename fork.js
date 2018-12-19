const { fork } = require('child_process');

const forked = fork('forkChild.js');

forked.on('message', (data) => {
  console.log('child has responded with ', typeof data, data);
});

const toSend = () => {
  return 1+1;
}

forked.send({
  func: toSend,
  someProp: false
});