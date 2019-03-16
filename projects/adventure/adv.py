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


def dft(current, prev_room_id=None):
    print('GRAPH LEN', len(graph))
    print('RMGRAPH LEN', len(roomGraph))
    if len(graph) < len(roomGraph):
        # set current room
        cur_room_id = current
        print(f'CURRENT ROOM: {player.currentRoom.id}')
        print('PREVROOM', prev_room_id)
        # print(f'GRAPH2: {graph}')
        # room_exits returns an array of directions
        # i.e. ['n', 's', 'e', 'w']
        room_exits = None
        exits_dict = {}
        if cur_room_id not in graph:
            room_exits = player.currentRoom.getExits()
            print(f'exits: {room_exits}')

            # adds exits from room_exits to exits_dict and sets value to '?'
            for exit in room_exits:
                exits_dict[exit] = '?'
            # adds room with its exits to graph
            graph[cur_room_id] = exits_dict
            print(f'GRAPH: {graph}')
        else:
            exits_dict = graph[cur_room_id]

        print(f'exits_dict: {exits_dict}')

        if prev_room_id is not None:
            inv_dir = traversalPath[-1]
            print('TRAVPATH', traversalPath)
            graph[cur_room_id][inverse[inv_dir]] = prev_room_id
            print('CUR ROOM ID', cur_room_id)
            print('INV', inverse[inv_dir])
            print('PREV', prev_room_id)
            graph[prev_room_id][inv_dir] = cur_room_id

        if '?' in graph[cur_room_id].values():
            # dictionary of directions not yet traveled
            print(exits_dict)
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
                dft(player.currentRoom.id, cur_room_id)
        else:
            # backtrack will be the path list from bfs
            backtrack = bfs(cur_room_id)
            if backtrack:
                cur = backtrack[0]
                # back_dirs = []
                while len(backtrack) > 1:
                    print('backtrack:', backtrack)
                    for direction in graph[backtrack[0]]:
                        print('DIRECTION', direction)
                        if graph[backtrack[0]][direction] == backtrack[1]:
                            # if direction in graph[player.currentRoom.id]
                            # print(f'DIRECTION: {direction}')
                            print(f'CURRENT RM: {player.currentRoom.id}')
                            traversalPath.append(direction)
                            player.travel(direction)
                            print(f'TRAVELED TO: {player.currentRoom.id}')
                            cur = backtrack.pop(0)
                            print('cur', cur)
                            print('POPPEDbacktrack:', backtrack)
                            break

                # print(f'GRAPH3: {graph}')
                dft(player.currentRoom.id, cur)


def bfs(start):
    q = [[start]]
    visited = set()
    print(f'START: {start}')
    while len(q) > 0:
        # path = []
        path = q.pop(0)
        # print(f'BACK PATH: {path}')
        cur = path[-1]
        if cur not in visited:
            visited.add(cur)
            if '?' in graph[cur].values():
                print('running')
                return path
            for direction in graph[cur].values():
                new_path = list(path)
                new_path.append(direction)
                q.append(new_path)


dft(player.currentRoom.id)
# print(f'GRAPH: {graph}')
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
