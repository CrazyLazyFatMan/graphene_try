get_many_query = """
query getBusiness {
  businesses {
    id
    created
    modified
    name
    employeeNumber
    address
    founder
  }
}
"""

get_one_query = """
query getBusiness {
  business(id: 1) {
    id
    created
    modified
    name
    employeeNumber
    address
    founder
  }

}
"""