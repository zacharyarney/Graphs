# from room import Room
from player import Player
from world import World
from rooms_graph import roomGraph

import random

# Load world
world = World()
world.loadGraph(roomGraph)
world.printRooms()
# initializes player in starting room
player = Player("Name", world.startingRoom)


# FILL THIS IN
traversalPath = []
graph = {}
inverse = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}


def dft(prev_room_id=None):
    # set current room
    cur_room_id = player.currentRoom.id
    print(f'CURRENT ROOM: {player.currentRoom.id}')
    # room_exits returns an array of directions
    # i.e. ['n', 's', 'e', 'w']
    room_exits = None
    exits_dict = {}
    if cur_room_id not in graph:
        room_exits = player.currentRoom.getExits()

        # adds exits from room_exits to exits_dict and sets value to '?'
        for exit in room_exits:
            exits_dict[exit] = '?'
        # adds room with its exits to graph
        graph[cur_room_id] = exits_dict
    else:
        room_exits = graph[cur_room_id]

    print(f'EXITS: {room_exits}')

    if prev_room_id is not None:
        inv_dir = traversalPath[-1]
        graph[cur_room_id][inverse[inv_dir]] = prev_room_id
        graph[prev_room_id][inv_dir] = cur_room_id

    if '?' in graph[cur_room_id].values():
        # dictionary of directions not yet traveled
        filtered_exits = {k: v for k, v in exits_dict.items() if v == '?'}
        print(f'FILTERED EXITS: {filtered_exits}')

        if len(filtered_exits) is not 0:
            # pick a random direction from filtered exits
            travel_dir = random.choice(list(filtered_exits.keys()))
            # append direction to traversal path
            traversalPath.append(travel_dir)
            # move in that direction
            player.travel(travel_dir)
            # Recurse
            dft(cur_room_id)
    else:
        return


def bfs(start):
    q = [start]
    visited = set()
    print(f'START: {start}')
    while len(q) > 0:
        path = []
        path.append(q.pop(0))
        cur = path[-1]
        if cur not in visited:
            visited.add(cur)
            if '?' in graph[cur].values():
                return path
            for direction in graph[cur].values():
                new_path = list(path)
                new_path.append(direction)
                q.append(new_path)


dft()
print(f'GRAPH: {graph}')
print(f'PATH: {traversalPath}')


# TRAVERSAL TEST
visited_rooms = set()
player.currentRoom = world.startingRoom
visited_rooms.add(player.currentRoom)
print(f'VISITED: {visited_rooms}')
for move in traversalPath:
    player.travel(move)
    visited_rooms.add(player.currentRoom)

if len(visited_rooms) == len(roomGraph):
    print(
        f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(roomGraph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.currentRoom.printRoomDescription(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     else:
#         print("I did not understand that command.")
