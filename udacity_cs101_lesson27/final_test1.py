from final_test import create_data_structure

b = {'Olli': {'connections': ['Mercedes', ' Freda', ' Bryant'], 'games': ['play Call of Arms', ' Dwarves and Swords', ' The Movie: The Game']}}
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
def get_connections(network, user):
    if user not in network:
        return None
    else:
        return network[user]['connections']

print get_connections(create_data_structure(a), 'Olli')


def get_games_liked(network, user):
    if user not in network:
        return  None
    else:
        return network[user]['games']

print get_games_liked(create_data_structure(a), 'Olli')




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

print add_connection(create_data_structure(a), 'Olli', 'Jennie')

# -----------------------------------------------------------------------------
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

