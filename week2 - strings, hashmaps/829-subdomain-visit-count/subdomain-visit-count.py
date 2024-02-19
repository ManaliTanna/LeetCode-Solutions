class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        ans = collections.Counter() #collection where elements are stored as dictionary keys and their counts are stored as dictionary values

        for cpdomain in cpdomains:
            rep, domain = cpdomain.split()
            rep = int(rep)
            fragments = domain.split('.') #store d1,d2,d3 in list

            for i in range(len(fragments)): #discuss.leetcode.com

                ans[".".join(fragments[i::])] += rep #in dictionary store key as each combo and value as count  that we calculated, and sum it so that next time the say key is encountered it'll just increment

       
        return ["{} {}".format(rep, domain) for domain,rep in ans.items()]