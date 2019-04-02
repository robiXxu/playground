var r = { a:1, b: {b1:11, b2: 99}};
var s = "b.b2";

var value = s.split('.')
  .reduce((a, b) => {
    return a[b]
  }, r);

console.log(value);