

class Simplest:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class Rotate:
    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third


    def get_first(self):
        return self.first


    def get_second(self):
        return self.second


    def get_third(self):
        return self.third


    def rotate(self):
        temp = self.third
        temp2 = self.second
        self.third = self.first
        self.second = temp
        self.first = temp2


class Band:
    def __init__(self, new_singer):
        self.singer = new_singer
        self.drummer = None
        self.guitar = []

    
    def get_singer(self):
        return self.singer

    
    def set_singer(self, new_singer):
        self.singer = new_singer

    
    def get_drummer(self):
        return self.drummer

    
    def set_drummer(self, new_drummer):
        self.drummer = new_drummer


    def add_guitar_player(self, new_guitar):
        self.guitar.append(new_guitar)

    
    def fire_all_guitar_players(self):
        self.guitar = []


    def get_guitar_players(self):
        ret = self.guitar[:]
        return ret


    def play_music(self):
        print("Do be do be do") if self.singer == "Frank Sinatra" else \
            print("bargle nawdle zouss") if self.singer == "Kurt Cobain" else \
                print("La la la")
        if self.drummer:
            print("Bang bang bang!")
        for _ in self.guitar:
            print("Strum!")


class Color:
    def __bound_rgb__(self, n):
        return 255 if n > 255 else 0 if n < 0 else n
    
    
    def __init__(self, r, g, b):
        self._r = self.__bound_rgb__(r)    
        self._g = self.__bound_rgb__(g)    
        self._b = self.__bound_rgb__(b)    


    def __str__(self):
        return f"rgb({self._r},{self._g},{self._b})"
    
    def html_hex_color(self):
        return f"#{self._r:02X}{self._g:02X}{self._b:02X}"


    def get_rgb(self):
        return (self._r, self._g, self._b)

    
    def set_standard_color(self, name):
        codes = {
            "red" : (255, 0, 0),
            "yellow" : (255, 255, 0),
            "white" : (255, 255, 255),
            "black" : (0, 0, 0)
        }
        if name.lower() in codes.keys():
            self._r, self._g, self._b = \
                codes[name.lower()][0], codes[name.lower()][1], \
                    codes[name.lower()][2]
    

    def remove_red(self):
        self._r = 0
