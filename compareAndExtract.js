const json1 = { "id": "617fbe0be301c360f6f91a19", "name": "New York", "buildingTypeId": "5eb3da170bccd80a238a2cfd", "scheduleId": "5eb3da1b0bccd80a238a2d02", "geoLocation": { "address1": "Mack Road", "altitude": { "u": "m", "v": 0 }, "city": "Georgetown", "iso3166CountryA2": "US", "formattedAddress": "Mack Road, Georgetown, 13072", "latitude": { "u": "deg", "v": 42.806872 }, "longitude": { "u": "deg", "v": -75.759087 }, "postcode": "13072", "province": "New York" }, "meta": { "createdAt": "2021-11-01T10:14:35.731Z", "lastUpdatedAt": "2021-11-01T10:14:35.731Z", "lastUpdatedBy": { "organisationId": "fbd1d788-c221-447d-bfa1-d92d96e4c2fc", "userId": "fbd1d788-c221-447d-bfa1-d92d96e4c2fc" }, "modelDataRevision": 1, "owner": { "organisationId": "fbd1d788-c221-447d-bfa1-d92d96e4c2fc", "userId": "fbd1d788-c221-447d-bfa1-d92d96e4c2fc" }, "storageLocationHint": { "iso3166CountryA2": "US", "iso3166Subdivision": "US-VA", "m49Region": "019", "m49SubRegion": "021" }, "volatileAccessType": "own", "resourceVisibility": "private" }, "weatherId": "334535303532354332384631" }

const json2 = { "id": "617fbe0be301c360f6f91a19", "name": "New York", "buildingTypeId": "asdfdssfdsafdffff", "scheduleId": "5eb3da1b0bccd80a238a2d02", "geoLocation": { "address1": "Mack Road", "altitude": { "u": "m", "v": 0 }, "city": "Georgetown", "iso3166CountryA2": "US", "formattedAddress": "Mack Road, Georgetown, 13072", "latitude": { "u": "deg", "v": 42.806872 }, "longitude": { "u": "deg", "v": -74.759087 }, "postcode": "13072", "province": "New York" }, "meta": { "createdAt": "2021-11-01T10:14:35.731Z", "lastUpdatedAt": "2021-11-01T10:14:35.731Z", "lastUpdatedBy": { "organisationId": "fbd1d782-c221-447d-bfa1-d92d96e4c2fc", "userId": "fbd1d788-c221-447d-bfa1-d92d96e4c2fc" }, "modelDataRevision": 1, "owner": { "organisationId": "fbd1d788-c221-447d-bfa1-d92d96e4c2fc", "userId": "fbd1d788-c221-447d-bfa1-d92d96e4c2fc" }, "storageLocationHint": { "iso3166CountryA2": "US", "iso3166Subdivision": "US-VA", "m49Region": "019", "m49SubRegion": "021" }, "volatileAccessType": "own", "resourceVisibility": "private" }, "weatherId": "3345353035323asdffsdf" }



const compareAndExtract = (original, updated) => 
  Object
    .entries(original)
    .reduce(
      (acc, [key, v]) => acc = {
        ...acc,
        [key]: typeof v === 'object'
          ? compareAndExtract(original[key], updated[key])
          : v === updated[key]
            ? null
            : updated[key],
      },
      {}
    )


const compareAndExtract1 = (original, updated) => 
  Object
    .entries(original)
    .reduce(
      (acc, [key, v]) => {
        acc = {
          ...acc,
          [key]: typeof v === 'object'
            ? compareAndExtract1(original[key], updated[key])
            : v === updated[key]
              ? null
              : updated[key],
        }
        if(
          acc[key] === null || 
          typeof acc[key] === 'object' && 
            Object.keys(acc[key]).length === 0
        ) delete acc[key]
        return acc
      },
      {}
    )







console.log(compareAndExtract1(json1,json2))
