from __future__ import print_function
from game import sd_peers, sd_spots, sd_domain_num, init_domains, \
    restrict_domain, SD_DIM, SD_SIZE
import random, copy

class AI:
    def __init__(self):
        self.conflict = False

    def solve(self, problem):
        domains = init_domains()
        restrict_domain(domains, problem) 
        stack = []
        while True:
            if self.propagate(domains) == False:
                if self.dom_size(domains) == True:
                    return domains
                orig_domains = copy.deepcopy(domains)
                spot, num = self.search(domains)
                stack.append((spot, num, orig_domains))
            else:
                if len(stack) == 0:
                    return None
                domains = self.backtrack(stack, domains)
                self.conflict = False

    def propagate(self, domains):
        tmp_dom = None
        while True:
            tmp_dom = copy.deepcopy(domains)
            for spot in domains:
                if len(domains[spot]) == 1:
                    self.remove_peers(domains, spot, domains[spot][0])
                if self.conflict == True:  
                    return True
                else:
                    continue
            if tmp_dom == domains:
                return False

    # Search/Decision algo 
    # Picks the spot with the smallest domain and chooses a number as assigment from its domain
    def search(self, domains):
        spot = self.smallest_dom(domains)
        num = domains[spot][0]
        domains[spot] = [num]
        return spot, num 

    # Removes the decision made from search alg, and removes the number that caused the conflict
    def backtrack(self, stack, domains):
        spot, num, orig_dom = stack.pop()
        domains = orig_dom
        domains[spot].remove(num)
        return domains

    # Function to find the size of the domains
    # If size of at least one spot in the domain has multiple elements, returns false
    # If size of a spot in the domain has zero elements, returns -1
    # If size of each spot in the domain has 1 element, returns True. 
    def dom_size(self, domains):
        for spot in domains:
            if len(domains[spot]) > 1:
                return False
            elif len(domains[spot]) == 1:
                continue
        return True
    
    # Function to remove num from domains of peers of spot
    def remove_peers(self, domains, spot, num):
        for peer in sd_peers[spot]:
            if num in domains[peer]:
                domains[peer].remove(num)
                if len(domains[peer]) == 0:
                    self.conflict = True

    # Returns the spot with the smallest domain 
    def smallest_dom(self, domains):
        min_spot = None
        min_num = float('inf')
        for spot in domains:
            if len(domains[spot]) > 1:
                if len(domains[spot]) < min_num:
                    min_spot = spot
                    min_num = len(domains[spot])
        return min_spot













    #### The following templates are only useful for the EC part #####

    # EC: parses "problem" into a SAT problem
    # of input form to the program 'picoSAT';
    # returns a string usable as input to picoSAT
    # (do not write to file)
    def sat_encode(self, problem):
        text = ""

        # TODO: write CNF specifications to 'text'

        return text

    # EC: takes as input the dictionary mapping 
    # from variables to T/F assignments solved for by picoSAT;
    # returns a domain dictionary of the same form 
    # as returned by solve()
    def sat_decode(self, assignments):
        # TODO: decode 'assignments' into domains
        
        # TODO: delete this ->
        domains = {}
        for spot in sd_spots:
            domains[spot] = [1]
        return domains
        # <- TODO: delete this
