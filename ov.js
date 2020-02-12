const ov = (...fn) => (...args) => fn.map(f => f.apply(null, args));

const sincos = ov(Math.sin, Math.cos);

const result = sincos(30);

console.log(result);


