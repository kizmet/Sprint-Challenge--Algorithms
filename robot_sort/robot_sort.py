class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l  # The list the robot is tasked with sorting
        self._item = None  # The item the robot is holding
        self._position = 0  # The list position the robot is at
        self._light = "OFF"  # The state of the robot's light
        self._time = 0  # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def insertionSortB(self):
        self.move_right()
        self.swap_item()

        count = 0
        while self.can_move_right() == True and self.can_move_left() == True:
            count += 1
            # print(self._position)
            self.move_left()
            if self.compare_item() == -1:  # less than
                # self.move_left()  # True
                self.swap_item()  # 15
                self.move_right()  # True
                self.swap_item()  # 41
                # self.move_right()  # True
                self.can_move_right()
                self.compare_item()
            elif self.compare_item() == 1:  # greater than
                # self.swap_item()
                # self.move_left()
                # self.swap_item()
                self.move_right()
                self.swap_item()
                self.move_right()
                self.can_move_right()
                self.compare_item()
            elif self.compare_item() == 0:
                self.move_left()
                self.swap_item()
                self.move_right()
                self.move_right()
                self.swap_item()
                self.move_right()
                self.compare_item()
            # key = arr[i]

        print(count)

    def insertionSortA(self):
        # j = i-1
        count = 0
        self.move_right()
        self.swap_item()
        self.move_left()
        while self.can_move_right() == True:
            while self.can_move_left() == True:
                if self.compare_item() == -1:
                    self.swap_item()
                    self.move_right()
                    self.swap_item()
                    print("less than")
                    print("loop 2 is finished")
                    continue
                elif self.compare_item() == 1:
                    self.move_right()
                    self.swap_item()
                    self.move_right()
                    self.swap_item()
                    print("greater than")
                    print("loop 2 is finished")
                    break
                elif self.compare_item() == 0:
                    self.move_right()
                    self.swap_item()
                    self.move_right()
                    self.swap_item()
                    print("equal to")
                    print("loop 2 is finished")
                    break
                self.move_left()
                # continue
                print("moving left")
            print("all the way left")
            if self.compare_item() == -1:
                self.swap_item()
                self.move_right()
                self.swap_item()
                self.move_right()
                # self.move_right()
                print("less than")
                # continue
            self.move_right()
            self.swap_item()
            self.move_right()
            self.swap_item()
            print("going to loop 1")
        print("loop 1 is finished")

    def sort(self):
        """
        overview: bubble sort has an outer and inner loop. the inner loop compares two elements, current index i and i +1. if i is >, they are swapped position. the outer loop loops the inner loop until all the elements are sorted.
  
        psuedocode:  
        until all the cards are sorted low to high: (outer loop)            
            use boolean to track whether a card has been swapped in inner loop
            light start out as "off", turn it "on" and break loop by turning it "off"
            execute inner loop

        since we can't set variable index, move right and left until cards are sorted
        while robot can move right: 
            robot picks up a card
            robot moves right
            robot compares cards
            if robot's card is less than card in front it swaps
                turn light on if there's a swap
            if robot's card is less than or equal to card in front it keeps its card
            go left, put down card and pick up 'none'
            move right
            hits far right, breat this loop

        while robot can move left:
            pick up card
            move left
            if card is greater than, swap
            if card is less than, keep it
            go right, put down card and swap it
            go left



        """
        self.set_light_on()
        while self.light_is_on():
            # keep looping until loop happens and light is turned off bc nothing was swapped
            # print(self)
            t = self._time
            self.set_light_off()
            while self.can_move_right() == True:
                # move right until the end
                self.swap_item()
                self.move_right()
                # if item in front is greater than, swap it, turn light on
                if self.compare_item() == 1:
                    self.swap_item()
                    self.set_light_on()
                self.move_left()
                self.swap_item()
                # swap none
                self.move_right()

            while self.can_move_left() == True:
                # once reached far right, loop cards going left
                self.swap_item()
                self.move_left()
                # if the card in front is less than held card, swap them
                if self.compare_item() == -1:
                    self.swap_item()
                    self.set_light_on()
                # swap none
                self.move_right()
                self.swap_item()
                self.move_left()
            t1 = self._time
            print(t1 - t)

    def __repr__(self):
        return f"index:{self._position} \ncard value:{self._item} \nlight:{self._light} \ntime:{self._time}\n list: {self._list}"


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`
    l2 = [5, 4, 3, 2, 1]
    l3 = [1, 2, 3, 4, 5]
    l = [15, 5, 58, 49, 26]

    # http://www.cs.armstrong.edu/liang/animation/web/BubbleSort.html
    l4 = [
        15,
        5,
        58,
        49,
        26,
        4,
        28,
        8,
        61,
        60,
        65,
        21,
        78,
        14,
        35,
        90,
        54,
        5,
        0,
        87,
        82,
        96,
        43,
        92,
        62,
        97,
        69,
        94,
        99,
        93,
        76,
        47,
        2,
        88,
        51,
        40,
        95,
        6,
        23,
        81,
        30,
        19,
        25,
        91,
        18,
        68,
        71,
        9,
        66,
        1,
        45,
        33,
        3,
        72,
        16,
        85,
        27,
        59,
        64,
        39,
        32,
        24,
        38,
        84,
        44,
        80,
        11,
        73,
        42,
        20,
        10,
        29,
        22,
        98,
        17,
        48,
        52,
        67,
        53,
        74,
        77,
        37,
        63,
        31,
        7,
        75,
        36,
        89,
        70,
        34,
        79,
        83,
        13,
        57,
        86,
        12,
        56,
        50,
        55,
        46,
    ]
    r = SortingRobot(l4)
    r.sort()
