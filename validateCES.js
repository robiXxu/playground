
//astea presupun ca is pe global scope sau vin de undeva.. 
const endPoints2Users = {
  '/deployment/14/revision/save': ['A700048'],
  '/v2/ticker/': [
    'A700033',
    'A700048',
  ],
  '/product/14/deployment/16/revision/getAll': ['A700052'],
  '/deployment/15/revision/delete': ['A700541']
};

const validateCES = (req)  => {
  const claim = { ivu: 'A700033' }; // bbvaNet.getClaim(req);
  const targetEndpoint = "/v2/ticker/"; //req.url

  if ( !Object.keys(endPoints2Users).includes(targetEndpoint) ) return false; //daca nu exista endpoint-ul respectiv no point in checking further.
  return endPoints2Users[targetEndpoint].filter(ivu => ivu === claim.ivu).length > 0;
};

const x = validateCES();
x //?