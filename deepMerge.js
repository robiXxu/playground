const o1 = {
  testing: {
    id: 1,
    code: {
      id: 1
    },
    cod2w: {
      v: [
        {}, 
        {v: 33, n: 11},
      ]
    }
  }
}

const o2 = {
  testing: {
    code: {
      cc: 'hehe',
      ccc: {d: 2},
      id: 2
    },
    cod2w: {
      n: { v: 3 },
      v: [
        {
          v: 3,
        },
        {
          v: 2
        }
      ]
    }
  }
}

// not great
const deepMerge = (dest, source) =>
  Object
    .entries(source)
    .reduce((acc, [key, val]) =>
      acc = {
        ...acc,
        [key]: typeof val === 'object'
          ? deepMerge(dest[key] || {}, source[key])
          : Array.isArray(val)
            ? deepMerge(dest[key] || [], source[key])
            : val,
      },
      dest,
    )


const ret = deepMerge(o1, o2) 
console.log(JSON.stringify(ret, null, 2))
