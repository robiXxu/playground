const data = {
  property1: {
    property11: {
      u : "m",
      v : 50
    },
    property12: {
      property121: {
        test1: "test",
        test2: "test2"
      },
      test: "test",
      property122: {
        property1221: {
          u : "m",
          v : 30
        },
        property1222: "testing",
        property1223: {
          property12231: {
            u : "m",
            v : 20
          }
        }
      }
    },
  }
};


const isUndefined = (object) => typeof(object) !== "undefined";
const arePropsAvailable = (object) => Object.keys(object).length === 2 && !isUndefined(object.u) && !isUndefined(object.v);
const isObject = (object) => constructor === Object;

const findAndReplace = (object, callback) => {
  if( isObject(object) && arePropsAvailable(object) ) {
    return callback(object);
  } else if( isObject(object) ) {
    return Object.keys(object).map((k) => findAndReplace(object[k], callback));
  } else {
    return object;
  }
}

const x = findAndReplace(data,(object) => {
  return {
    u : "m",
    v : object.v * 2 + 10
  }
});


// const mutateObjectProperty = (conv, obj) =>
//   obj.constructor === Object && Object.keys(obj).forEach(key => {
    
//     if( !isUndefined(obj[key]['u']) && !isUndefined(obj[key]['v']) ) {
//       obj[key]['u'] = conv.u;
//       obj[key]['v'] *= conv.v;
//     } else if( ){

//     }
//   })
    
// mutateObjectProperty({
//   u : 'ft',
//   v : 22
// }, data)