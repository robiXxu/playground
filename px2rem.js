const fontBaseSize = 16;

const px2Rem = (min, max, step = 1) => {
  const range = [];
  for (let i = min; (max - i) * step >= 0; i += step) {
    range.push(i.toFixed(2));
  }
  return range.reduce((obj, v) => {
    obj[`${v}px`] = `${v / fontBaseSize}rem`;
    return obj;
  }, {});
};

console.log(px2Rem(10, 14, 2));

console.log(px2Rem(-1, 1, 0.05));