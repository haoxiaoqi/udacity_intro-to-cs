# example_input = "John is connected to Bryant, Debra, Walter.\
# John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
a = "John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."


#seprate names from content
def sanitize_name(names):
    names = names.replace(".","")
    names = names.replace(" ", "")
    return names.split(',')


def sanitize_sentence(item, sentence):
    user = item[:item.find(sentence)-1].strip(" ")
    user_connections = item[item.find(sentence):].replace(sentence,'')
    return user, user_connections


def create_data_structure(string_input):
    network = {}
    sentences = []
    start = 0
    #find dot
    end = string_input.find('.')
    #loop through all the dots and extract content
    while end != -1:
        sentences.append(string_input[start:end])
        start = end+1
        end = string_input.find('.', start)
    break_connections = "is connected to "
    break_games = "likes to "
    new_connections = None
    new_games = None
    #loop through each sentence extract from while loop
    for sentence in sentences:
        #connections in the element
        if break_connections in sentence:
            user, user_connection = sanitize_sentence(sentence,break_connections)
            new_connections = sanitize_name(user_connection)
        #no new connect, only game
        else:
            user, user_connection = sanitize_sentence(sentence,break_games)
            new_games = sanitize_name(user_connection)
        if user not in network:
            #build up new dictionary for new name
            network[user] = {'connections':[],'games':[]}
        else:
            network[user]['connections'] += new_connections
            network[user]['games'] += new_games
    return network

print create_data_structure(a)

# ----------------------------------------------------------------------------- #
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        #
# ----------------------------------------------------------------------------- #

# -----------------------------------------------------------------------------
# get_connections(network, user):
#   Returns a list of all the connections that user has
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return:
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.

# b = {'Olli': {'connections': ['Mercedes', ' Freda', ' Bryant'], 'games': ['play Call of Arms', ' Dwarves and Swords', ' The Movie: The Game']}}

def get_connections(network, user):
    if user not in network:
        return None
    else:
        return network[user]['connections']


# -----------------------------------------------------------------------------
# get_games_liked(network, user):
#   Returns a list of all the games a user likes
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return:
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.
def get_games_liked(network, user):
    if user not in network:
        return  None
    else:
        return network[user]['games']


# -----------------------------------------------------------------------------
# add_connection(network, user_A, user_B):
#   Adds a connection from user_A to user_B. Make sure to check that both users
#   exist in network.
#
# Arguments:
#   network: the gamer network data structure
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return:
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.
def add_connection(network, user_A, user_B):
    if user_A in network and user_B in network:
        if user_B in network[user_A]['connections']:
            return network
        else:
            network[user_A].append(user_B)
            return network
    else:
        return False

# print add_connection(create_data_structure(a), 'Olli', 'Jennie')
# -----------------------------------------------------------------------------
# add_new_user(network, user, games):
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no
#   connections to begin with.
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return:
#   The updated network with the new user and game preferences added. The new user
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)

def add_new_user(network, user, games):
    while user not in network:
        empty_dic = {user:{'connections': [], 'games': []}}
        network.update(empty_dic)
        network[user]['games'].append(games)
        return network
    return network

# print add_new_user(create_data_structure(a),'hahaha','if')
# -----------------------------------------------------------------------------
# get_secondary_connections(network, user):
#   Finds all the secondary connections (i.e. connections of connections) of a
#   given user.
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return:
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
#
# NOTE:
#   It is OK if a user's list of secondary connections includes the user
#   himself/herself. It is also OK if the list contains a user's primary
#   connection that is a secondary connection as well.
def get_secondary_connections(network, user):
    if user in network:
        primary = network[user]['connections']
        secondary = []
        for primary_connections in primary:
            if primary_connections in network:
                for second_connections in network[primary_connections]['connections']:
                    if second_connections not in secondary:
                        secondary.append(second_connections)
        return secondary
    return None

# print get_secondary_connections(create_data_structure(a),'John')
# -----------------------------------------------------------------------------
# count_common_connections(network, user_A, user_B):
#   Finds the number of people that user_A and user_B have in common.
#
# Arguments:
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return:
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.
def count_common_connections(network, user_A, user_B):
    if user_B in network and user_A in network:
        common_amount = 0
        a_connections = network[user_A]['connections']
        b_connections = network[user_B]['connections']
        for a_connection in a_connections:
            if a_connection in b_connections:
                common_amount =+ 1
        return common_amount
    return False

# print count_common_connections(create_data_structure(a),'John','Debra')

# -----------------------------------------------------------------------------
# find_path_to_friend(network, user_A, user_B):
#   Finds a connections path from user_A to user_B. It has to be an existing
#   path but it DOES NOT have to be the shortest path.
#
# Arguments:
#   network: The network you created with create_data_structure.
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
#
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print find_path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam,
#   who is connected with Zed.
#
# NOTE:
#   You must solve this problem using recursion!
#
# Hints:
# - Be careful how you handle connection loops, for example, A is connected to B.
#   B is connected to C. C is connected to B. Make sure your code terminates in
#   that case.
# - If you are comfortable with default parameters, you might consider using one
#   in this procedure to keep track of nodes already visited in your search. You
#   may safely add default parameters since all calls used in the grading script
#   will only include the arguments network, user_A, and user_B.
def find_path_to_friend(network, user_A, user_B, visited=None):
    path = []
    if user_A in network and user_B in network:
        A_friends = network[user_A]['connections']
        # base case: A and B are friends
        if user_B in A_friends:
            path.append(user_A)
            path.append(user_B)
            return path
        for a_friend in A_friends:
            if visited == None:
                visited = [user_A, user_B]
            if a_friend in visited:
                continue
            else:
                visited.append(a_friend)
            result_path_of_A_friend_to_B = find_path_to_friend(network, a_friend, user_B, visited)
            if result_path_of_A_friend_to_B != []:
                # has connection
                path = [user_A]
                path.append(result_path_of_A_friend_to_B)
                return path
    return path


print find_path_to_friend(create_data_structure(a), 'John', 'Olive')
