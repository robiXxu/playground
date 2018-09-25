const endPoints2Users = {
  '/deployment/{deploymentPlanId}/revision/{configurationRevisionId}/rollback': ['A700048'],
  '/deployment/{deploymentPlanId}/revision/{configurationRevisionId}/update': [
    'A700033',
    'A700048',
  ],
  '/deployment/{deploymentPlanId}/revision/{configurationRevisionId}': ['A700052'],
  '/deployment/{deploymentPlanId}/revision/{configurationRevisionId}/service/{serviceId}': ['A700541']
};

const clean = s => s.length > 0
const endPoints2UsersKeys = Object.keys(endPoints2Users).map(k => k.split('/').filter(clean));
const partTypes = {
  "{deploymentPlanId}": "number",
  "{configurationRevisionId}": "number",
  "{serviceId}": "number"
};

;

// const validateCES = (req)  => {
  const claim = { ivu: 'A700033' }; // bbvaNet.getClaim(req);
  const targetEndpoint = "/deployment/45/revision/26/rollback"; //req.url
  const target = targetEndpoint.split('/').filter(clean).map(s => {
    const val = parseInt(s);
    return isNaN(s) ? s : val;
  });

  const x = endPoints2UsersKeys.map((array) => {
    const targetCopy = JSON.parse(JSON.stringify(target));
    return array.reduce((path, current) => {
      // const item = path[0];
      // if(current.includes('{') && partTypes[current] === typeof(item)){
      //   path.splice(0,1);
      // } else if(current === item){
      //   path.splice(0,1);
      // }
      // return path;
    },targetCopy);
  });
  x

//   return Object.keys(endPoints2Users).includes(targetEndpoint) ? 
//     endPoints2Users[targetEndpoint].filter(ivu => ivu === claim.ivu).length > 0 : 
//     false;
// };