process.on('message', (data) => {
  console.log('data from parent', typeof data, data);
  process.send({ received: true })
});