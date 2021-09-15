"""Terminal Railyard Game

Runs a railyard game in the terminal. Yard object for managing
the game board and Track object for managing individual lines in 
the Yard. Lines are linked lists representing trains in a railyard.

File:
    railyard.py

Name:
    Christian P. Byrne

Course:
    CSC120 | Summer 2021


"""

from list_node import ListNode 


class Yard:
    """Yard class manages group of Track subclass instances.
    
    List of Track objects from yard file are managed through
    this class. Run game by instancing and calling new_round
    method until program exits.

    Args:
        file_lines (list) : List of lines from the yard file.
    """

    def __init__(self, file_lines):
        self._tracks = [Track(line) for line in file_lines]
        self._retired = False
        self._print()
        self._print_counts()

    def _move(self, number, from_, to):
        """Executes a move.
        
        Updates Track instances for affected lanes and prints
        a log to stdout.
        
        Args:
            number (int) : Number of cars to move. 0 for just loco.
            from_ (int) : Track number to move cars from.
            to (int) : Track number to move cars to.
        
        
        """
        self._tracks[int(to) - 1].push(
            self
            ._tracks[int(from_) - 1]
            .shift(int(number)+1)
        )

        print(
            f"\nThe locomotive on track {from_} moved",
            f"{number} cars to track {to}.\n"
        )
    
    def _departures(self):
        """Get departure status of recent round.
        
        Triggers departure-check methods on each track, 
        and returns status of checks. 

        Returns:
            False if no departures occurred. Else, an array containing each
                departure -- each departure element is a tuple of the shape
                (lane number, (number of departed cars, destination)).
        """
        # Track's status method returns False if no departure
        lane_status = [track.status() for track in self._tracks]
        withdraws = any(lane_status)
        return ([
                (lane, status) 
                for lane, status 
                in enumerate(lane_status) 
                if status
        ]) if withdraws else False

    def _get_move(self):
        """Gets move from stdin and returns formmated array of commands.
        Quits program if command is 'quit'.

        Returns:
            list : [number: int, from: int, to: int].
        """
        print("What is your next command?")
        move = input().lower().replace("move", "")
        if move.strip() == "quit":
            quit("\nQuitting!")
        return ([
            parsed_int 
            for parsed_int 
            in move.strip().split() 
            if parsed_int
        ])

    def _validate_stdin(self, stdin):
        """Check for the given error conditions.
        
        Args:
            stdin (list) : [number of cars, from track #, to track #].

        Returns:
            False if the move is valid. A string representing the error
                message if invalid.
        """
        if len(stdin) != 3:
            return (
                "ERROR: The only valid command formats are (where each"
                + " X represents an integer):\nmove X X X\nquit\n"
            )
        for arg, param in zip(stdin, ["count", "from-track", "to-track"]):
            if not arg.isnumeric() and arg[0] != "-":
                return (
                    f"ERROR: Could not convert the '{param}'"
                    + f" value to an integer: '{arg}'"
                )
            if (
                arg[0] == "-" 
                or int(arg) > len(self._tracks) and param != "count" 
                or int(arg) < 1 and param != "count"
            ):
                return "ERROR: The to-track or from-track number is invalid."
        return False

    def _composition(self):
        """Provides the composition of the yard.
        
        Returns:
            tuple : (numbers of locomotives, number of unique destinations)
        """
        loco_count = sum(
            [track.has_locomotive() for track in self._tracks]
        )

        # Merged destination-dicts to count unique destination.
        destinations = [track.destinations() for track in self._tracks]
        merged = {}
        for destination in destinations:
            merged.update(destination)
        loco_offset = 1 if loco_count > 0 else 0
        return loco_count, len(merged.keys()) - loco_offset

    def _vacant(self):
        """Returns True if no locomotive in yard, else False.
        Constitutes the game-over check."""
        if not sum(
                [track.has_locomotive() for track in self._tracks]
            ):
            print("The last locomotive has departed!\n")
            return True
        return False

    def _print_counts(self):
        """Print number of locomotives and unique destinations in yard."""
        print(
            f"Locomotive count:  {self._composition()[0]}\n"
            + f"Destination count: {self._composition()[1]}\n"
        )

    def _print(self):
        """Print current state of yard."""
        for index, line in enumerate(
            [track.print() for track in self._tracks]
            ):
            print(
                f"{index + 1}: {line}"
            )

    def new_round(self):
        """Public main method for starting a new round of game. 
        Can call infinitelyand wait for quit() to be called by 
        one of the other methods.
        """
        stdin = self._get_move()
        occupied = lambda lane : self._tracks[
            int(stdin[lane]) - 1
            ].has_locomotive()
        
        direction = lambda axis : self._tracks[
            int(stdin[axis]) - 1]
        
        # Error Checking.
        if self._validate_stdin(stdin):
            print(self._validate_stdin(stdin))
        elif not occupied(1): 
            print(
                f"ERROR: Cannot move from track {stdin[1]}",
                "because it doesn't have a locomotive."
            ) 
        elif occupied(2):
            print(
                f"ERROR: Cannot move to track {stdin[2]}",
                "because it already has a locomotive." 
            )
        elif direction(1).count() < int(stdin[0]) + 1:
            print(
                f"ERROR: Cannot move {stdin[0]} cars from track",
                f"{stdin[1]} because it doesn't have that many cars."
            )
        elif direction(2).vacancies() < int(stdin[0]) + 1:
            print(
                f"ERROR: Cannot move {stdin[0]} cars to track",
                f"{stdin[2]} because it doesn't have enough space."
            )
        else:
            self._move(*stdin)

        self._print()
        withdraws = self._departures()
        if withdraws:
            # If departures occurred, print log for each one, then print yard.
            for train in withdraws:
                print(
                    f"*** ALERT***  The train on track {train[0] + 1},",
                    f"which had {train[1][0] - 1} cars, departs",
                    f"for destination {train[1][1]}.\n"
                    )
            self._retired = self._vacant()
            self._print()
        self._print_counts()
        if self._retired:
            quit()


class Track:
    """Single track on railyard.

    Extended by Yard class. Stores cars on track in linked lists.

    Args:
        line (str) : Single populated line from yard file.

    Attributes:
        string (str) : Cars and locomotive in string format.
        length (int) : Number of spaces on line not including padding.
    """

    def __init__(self, line):
        self.length = len(
            line.strip("\n")
            .strip()
            ) - 2

        self.string = self._format(line)
        self._trains = self._map(self.string)
    
    def _map(self, string):
        """Construct linked list object from track string."""
        head = ListNode(string[0]) if string else None
        cur = head
        for car in string[1:]:
            nxt = ListNode(car)
            cur.next = nxt
            cur = nxt
        if len(string) > 1:
            nxt.next = None
        return head

    def status(self):
        """Get status of the track to check for departure.

        Returns:
            False if no locomotive, no cars, or multiple cars
                going to different destinations. Else if a
                departure is warranted, returns a tuple 
                (number of trains leaving, destination).


        """
        characters = self.to_str()
        if (
            "T" not in characters 
            or len(characters.replace("T", "")) < 1
        ):
            return False
        characters = characters.replace("T", "")
        ret = any(
            letter != characters[0] for letter in characters
            )

        if not ret:
            ret = (
                self.count(), 
                characters[0]
            )
            self._trains = None
            return ret
        return not ret

    def _format(self, string):
        """Format track string correctly and reverse."""
        for character in [" ", "\n", "-"]:
            string = string.replace(character, "")
        return (
            "".join(
                reversed(
                    list(
                        string
                    )
                )
            )
        )

    def has_locomotive(self):
        """ Rerturn 1 if locomotive on track else 0."""
        return 1 if "T" in self.to_str() else 0

    def destinations(self):
        """Return dictionary of all unique destination characters."""
        ret = {}
        for destination in self.to_str():
            ret[destination] = destination
        return ret

    def vacancies(self):
        """Returns: 
            int: Empty spaces relative to original yard file.
        """
        return self.length - len(self.to_str())

    def count(self):
        """Gives number of cars in the track

        Returns:
            int : Length of track.
        """
        ret = 0
        cur = self._trains
        while cur is not None:
            ret += 1
            cur = cur.next
        return ret

    def to_str(self):
        """Get track characters as concatenated string.

        Returns:
            str : All val properties of track list concatenated.
        """
        cur = self._trains
        ret = ""
        while cur is not None:
            ret += cur.val
            cur = cur.next
        return ret

    def print(self):
        """Gives formatted track for displaying.

        Returns:
            str : Track cars and empty spaces formatted.
        """
        return (
            f"-{self.vacancies() * '-'}{self._format(self.to_str())}-"
        )

    def shift(self, number):
        """Move cars off track.
        
        Remove vehicales from track and return their values as concatenated
        string. Track must have a locomotive.

        Args:
            number (int) : Number of cars to shift. Must have greater than
                or equal to number already on track.

        Returns:
            str : Concatenated val properties of shifted cars.


        """
        ret = ""
        cur = self._trains
        for _ in range(number):
            ret += cur.val
            cur = cur.next
        self._trains = cur
        return ret

    def push(self, incoming):
        """Move cars onto track.
        
        Move car nodes onto track. Track must not have a locomotive
        already present. Void.

        Args:
            incoming (str) : Concatenated val properties of shifted cars.
                Assumes cars are single digit values.


        """
        linked = self._map(incoming)
        if not self._trains:
            self._trains = linked
            return

        cur = linked
        while cur.next is not None:
            cur = cur.next
        cur.next = self._trains
        self._trains = linked


def get_yard_file():
    """Gets yard file from user at stdin. Custom error handling
    for FileNotFoundError.
    
    Returns:
        list : Lines in file.
    """
    print("Please give the yard file:")
    try:
        yard_file = open(
            input(),
            "r"
        ).readlines()
    except FileNotFoundError:
        quit("ERROR: The yard filename doesn't exist")
    return yard_file


def main():
    x = Yard(get_yard_file())
    while True:
        x.new_round()


if __name__ == "__main__":
    main()