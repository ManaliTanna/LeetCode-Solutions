class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        my_set = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            idx_of_plus = email.find('+')
            if(idx_of_plus!=-1):
                local_name = local_name[0:idx_of_plus]
            local_name = local_name.replace('.','')
            my_set.add(local_name+'@'+domain_name)
        return len(my_set)
