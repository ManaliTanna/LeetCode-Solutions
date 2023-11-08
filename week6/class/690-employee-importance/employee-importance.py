"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        #hashmap to retrieve employee info
        emap = {e.id: e for e in employees}

        def dfs(eid):
            #retrieve employee by id
            employee = emap[eid]
            # recursively - find current and importance of subordinates - sum it up
            return (employee.importance + 
            sum(dfs(eid) for eid in employee.subordinates))

        # call dfs on the id given to us
        return dfs(id)
                