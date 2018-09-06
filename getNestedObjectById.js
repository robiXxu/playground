const root = {    
   "objects":[
       {
           "id" : "id_1",
           "type" : "Unit",
           "name" : "name_1",
           "isPlayer" : true,
           "isPlayable" : true,
           "designation" : "Grenadier",
           "health" : 1,
            "children" : [
                {
                    "id" : "id_16",
                    "type" : "Group",
                    "name" : "Group 1",
                    "isPlayable" : true,
                    "designation" : "Grenadier",
                   "health" : 1,
                   "children":[
                       {
                           "id" : "id_17",
                           "type" : "Unit",
                           "name" : "Antonio Banderas",
                           "isPlayable" : true,
                           "designation" : "Sniper",
                           "health" : 1
                       }
                   ]
                }
            ]
       },
       {
           "id" : "id_1_1",
           "type" : "Unit",
           "name" : "name_1_1",
           "isPlayable" : true,
           "designation" : "Grenadier",
           "health" : 1
       },
       {
           "id" : "id_1_2",
           "type" : "Unit",
           "name" : "name_1_2",
           "isPlayable" : true,
           "designation" : "Grenadier",
           "health" : 1

       }
   ]
};

const id = 'id_17';

// not efficient at all
const getNestedObjectById = ( array, id ) =>
   array.reduce((object, item) => {
         return Object.keys(object).length > 0 ?
           object :
           (item.id === id ?
             item :
             (typeof item.children !== "undefined" ?
                 getNestedObjectById( item.children, id ) :
                 object));
     },{});

console.log(obj);