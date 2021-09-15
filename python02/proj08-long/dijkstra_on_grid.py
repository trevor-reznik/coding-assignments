""" Dijkstra on Grid


Dijkstra's Algorithm: 
    An algorithm for finding the shortest paths between nodes 
    in a graph, which may represent, for example, road networks. 
    Dijkstra's algorithm uses a data structure for storing and 
    querying partial solutions sorted by distance from the start. 
    While the original algorithm uses a min-priority queue and runs 
    in time Θ((|V|+|E|)log|V|)} (where is the number of edges), it 
    can also be implemented in Θ(|V|2).

Spec Requirements:
    - Each node in the map bmust be represted by a DijkstraNode obj.
    - Use the DijkstraNode obj to keep track of all info about each node.
      Don't use other data stuctures.
    - Assume that all inputs are valid.
    - p always < 100. Characters expanded to three spaces in output.
    - Empty spaces = three whitespaces.
    - Single-digits have a leading space.
    - Double-digits have a trailing space.
    - No edges between diagonally-adjacent nodes.
    - All edges are length 1.
    - When you have two nodes on the todo list which have the same distance,
      sort the todo list and take the first one in the sorted array.
    - Animation Command:
        - Unreached spaces are still hash symbols but padded by whitespace.
        - Spaces with unfinalized p's have a ? proceeding.
        - Print todo list after map.
    - Todo list:
        - Sorted list of paths to points that you've found.
        - List<tuple: [p: int, x: int, y: int]>
        - Sorted insert or sort after each insertion.

Author:
    Christian P. Byrne

File:
    dijkstra_on_grid.py

Course:
    CSC 120 | Summer 21

"""


from dijkstra_node import DijkstraNode


class GridMap:
    """
    """

    def __init__(self, lines):
        self.lines = lines
        self.nodes = [
            [DijkstraNode() if char == "#" else " " for char in line]
            for line in lines
        ]

    def insert_start_pos(self, start):
        """Initialize the todo list with the starting position
        which will have a distance of 0.

        Args:
            start (tuple) : (int, int)


        """
        self.todo = [
            (0, start[0], start[1])
        ]
        self.nodes[start[1]][start[0]].update_dist(0)

    def print_todo(self):
        """Print the current todo list padded by two linebreaks."""
        self.prioritize()
        print(
            "\n",
            f"TODO list: {self.todo}",
            "\n",
            sep=""
        )

    def prioritize(self):
        """Sort the current todo list with respect to shortest
        distance."""
        self.todo.sort()

    def resolve_position(self, pos, distance):
        """Test all four lateral directions from a position on the grid.

        Four each of the four possible steps (up, down, left, right), 
        test if the relative position is valid, then check if there is a 
        node at the position. If there is a node and it is not done,
        update its distance if the current distance is less than its existing
        distance property.

        Args:
            pos (tuple) : (x, y) coordinate on the grid.
            distance (int) : Distance of the tested position plus 1.


        """
        x, y = pos
        slopes = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        for slope in slopes:
            test_pos = (x - slope[0], y - slope[1])
            test_x, test_y = test_pos
            if self.path_open(test_pos):
                node = self.nodes[test_y][test_x]
                if node != " ":
                    if (
                        not node.is_reached()
                        or not node.is_done()
                        and distance < node.get_dist()
                    ):
                        node.update_dist(distance)
                        self.todo.append(
                            (distance, test_x, test_y)
                        )

    def traverse_one(self):
        """Resolve the position at the first position in the todo list/queue.

        Sort the queue, test the position in all four directions, update the
        nodes where appropriate, set the tested node to done and pop it from
        the queue, then return Boolean indicating whether todo list is empty.

        Returns:
            bool: False if no more nodes to test, otherwise True.


        """
        if not self.todo:
            return False

        priority = sorted(self.todo)[0]
        node_start = self.nodes[priority[2]][priority[1]]
        self.resolve_position(
            (priority[1], priority[2]),
            priority[0] + 1
        )
        node_start.set_done()
        self.todo.pop(0)
        if not self.todo:
            return False
        return True

    def print(self):
        """Print the current map.

        Map is formatted such that each coordinate is
        2 characters in width, right-alligned, followed by a whitespace if
        the node is done or a question mark if not. Empty nodes are three
        whitespaces


        """
        for row in self.nodes:
            line_display = []
            for cell in row:
                if cell == " ":
                    val = "   "
                elif not cell.is_reached():
                    val = " # "
                else:
                    suffix = " " if cell.is_done() else "?"
                    val = f"{cell.get_dist():>2}{suffix}"
                line_display.append(val)
            print("".join(line_display))

    def pos_exists(self, pos):
        """Validate indices in grid.

        Avoid IndexError by validating both coordinates.

        Returns:
            True if coordinates are valid indices, otherwise False.


        """
        if (
            pos[1] < len(self.lines)
            and pos[0] < len(self.lines[pos[1]])
        ):
            return True
        return False

    def vacant(self, pos):
        """Check if coordinate in grid is occupied by node or vacant.

        Returns:
            True if vacant (no node here), otherwise False.


        """
        if self.lines[pos[1]][pos[0]] == "#":
            return False
        return True

    def path_open(self, pos):
        """Check if coordinate is both valid indices and housing a node
        as opposed to a whitespace.

        Args:
            pos (tuple) : (x, y) coordinates in grid to test.

        Returns:
            True if valid indices and node at pos, otherwise False.


        """
        if (
            pos[0] >= 0
            and pos[1] >= 0
            and self.pos_exists(pos)
            and not self.vacant(pos)
        ):
            return True
        return False


def get_stdin():
    """Read three commands at stdin and map to a dictionary.

    Returns:
        dict : {map: str, start: str, operation: str}


    """
    return format_stdin({
        "map": open(
            input("Please give the grid file:\n"),
            "r"
        ),
        "start": input("Where to start?\n"),
        "operation": input("What type of operation?\n")
    })


def format_stdin(stdin):
    """Apply formatting operations for each command type.
    Turn map into 2D array after stripping newline char.
    Turn start command into integer tuple.

    Args:
        stdin (dict) : {map: str, start: str, operation: str}

    Returns:
        dict: {
            start: (int, int), 
            map: str[][], 
            operation: str
        }


    """
    stdin["start"] = (
        int(stdin["start"].split()[0]),
        int(stdin["start"].split()[1])
    )
    stdin["map"] = [
        list(line.strip("\n")) for line in stdin["map"].readlines()
    ]
    stdin["operation"] = stdin["operation"].strip().lower()

    return stdin


def animate_grid(grid):
    """Solve the grid, replacing each hash sing with the shortest
    distance to reach from the start position.

    On each check of each node, print the current TODO list and the 
    current grid, indicating with question marks the completion status
    of each node.

    """
    unfinished = True
    print("CURRENT GRID:")
    grid.print()
    grid.print_todo()
    grid.prioritize()
    while unfinished:
        grid.prioritize()
        unfinished = grid.traverse_one()
        if unfinished:
            print("CURRENT GRID:")
        if not unfinished:
            print(
                "-------- All reachable spaces filled. ",
                "This is the final map --------"
            )
        grid.print()
        if unfinished:
            grid.print_todo()
        grid.prioritize()


def fill_grid(grid):
    """Solve the grid, replacing each hash sing with the shortest
    distance to reach from the start position."""
    unfinished = True
    while unfinished:
        grid.prioritize()
        unfinished = grid.traverse_one()
        if not unfinished:
            grid.print()


def main():
    stdin = get_stdin()
    grid = GridMap(
        stdin["map"],
    )

    if stdin["operation"] == "fill":
        grid.insert_start_pos(stdin["start"])
        fill_grid(grid)

    elif stdin["operation"] == "animate":
        print(
            f"Searching from {stdin['start']} outward." 
        )
        print()
        print("STARTING GRID:")
        grid.print()
        grid.insert_start_pos(stdin["start"])
        print()
        animate_grid(grid)


if __name__ == "__main__":
    main()
