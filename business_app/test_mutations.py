create_mutation = """
    mutation createBusiness {  
      createBusiness(inputData: {
      name: "JK Furman und Young",
      employeeNumber: 200,
      address: "Berlin",
      founder: "Otto Furman"
  }) {
        ok
        business{
          id
          name
          employeeNumber
          founder
        }
      }
    }
"""

update_mutation = """
    mutation updateBusiness {
      updateBusiness(instanceId:1, inputData: {
        name: "Updated_name", 
        employeeNumber: 200, 
        address: "Berlin", 
        founder: "Otto Furman"
        }) {
        ok
        business {
          id
          name
          employeeNumber
          address
          founder
        }
      }
    }
"""

delete_mutation = """
    mutation deleteBusiness {
      deleteBusiness(instanceIds: [1]) {
        ok
      }
    }
"""