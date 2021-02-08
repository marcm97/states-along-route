class StatesAlongRoute:
    def __init__(self,api_key,start,end):
        self.api_key = api_key
        self.start = start
        self.end = end
        self.states = {}

    """
    returns a list of lat,longs for each turn
    """
    def get_route(mode ="driving"):
        pass


    """
    takes in a lat and long, and returns current state
    """
    def current_state(lat,long):
        pass



    """
    binary search to figure out how much of the route was coveredd in each state
    """
    def binary_search():
        pass

    """
    if a sub route is >100 miles, breakup the subroute into 100 mile chunks
    """
    def breakup_subroute():
        pass


    """
    returns a list of states that were passed through
    using polylines
    """
    def get_states_m1():
        pass

    """
    returns a list of states that were passed through
    using reverse geocodes
    """
    def get_states_m2():
        pass


    """
    returns a dictionary of the distances travelled in each state
    """
    def get_distances():
        pass

    """
    returns a dictionary of duration spent in each state
    """
    def get_durations():
        pass

    """
    shows a visual map of the route and the % of time spent in each state
    """
    def create_map():
        pass
