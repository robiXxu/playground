const dostuff = (cb) => {
  console.log('here??');
  //some async stuff...
  setTimeout(() => {
    console.log('here 2')
    console.log(typeof cb);
    if(cb) cb(null);
  },3000);
};

const x = (cb) => {
  dostuff(cb(true));
}

x(d => { console.log(d) });