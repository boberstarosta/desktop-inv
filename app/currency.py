
class Currency(int):
    def __new__(cls, *args):
        if len(args) == 0:  # Currency() => 0
            return int.__new__(cls, 0)
        elif len(args) == 1:
            a = args[0]
            if isinstance(a, str):  # Currency("1.23") => 123
                return cls.parse(a)
            elif isinstance(a, float):  # Currency(1.23) => 123
                return cls.parse("{:.2f}".format(a))
            else:  # Currency(123) => 123
                return int.__new__(cls, int(a))
        else:
            raise ValueError("Too many arguments: {}".format(len(args)))

    @classmethod
    def parse(cls, str_):
        """Returns int from a given string."""
        if not str_:  # Empty string => Currency(0)
            return cls(0)

        words = str_.replace(",", ".").split(".")
        if len(words) == 1:  # Currency("12") == Currency("12.00")
            return cls(100 * int(words[0]))
        elif len(words) == 2:
            zl, gr = words
            if len(gr) < 2:
                gr += "0"
            elif len(gr) > 2:
                gr = gr[:2]
            zl_int = int(zl)
            gr_int = int(gr)
            if gr_int < 0:
                raise ValueError("gr < 0 in {}".format(str_))
            value = 100*zl_int
            value += gr_int if zl_int > 0 else -gr_int
            return cls(value)
        else:
            raise ValueError("Can't parse string {}".format(str_))

    def to_str(self):
        zl = int(self) // 100
        gr = int(self) % 100
        if self < 0:
            if gr:
                zl += 1
                gr = 100 - gr
        sign = "-" if self < 0 else ""
        return sign + str(abs(zl)) + "." + str(gr).zfill(2)

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.to_str())

    def __str__(self):
        return self.to_str()

    def __add__(self, other):
        return self.__class__(int(self) + int(other))

    def __sub__(self, other):
        return self.__class__(int(self) - int(other))

    def __mul__(self, other):
        return self.__class__(int(self) * int(other))

    def __floordiv__(self, other):
        return self.__class__(int(self) // int(other))

    def __neg__(self):
        return self.__class__(-int(self))

    def __matmul__(self, other): raise NotImplementedError
    def __truediv__(self, other): raise NotImplementedError
    def __divmod__(self, other): raise NotImplementedError
    def __pow__(self, other, *args): raise NotImplementedError
    def __lshift__(self, other): raise NotImplementedError
    def __rshift__(self, other): raise NotImplementedError
    def __and__(self, other): raise NotImplementedError
    def __xor__(self, other): raise NotImplementedError
    def __or__(self, other): raise NotImplementedError
    def __pos__(self): raise NotImplementedError
    def __abs__(self): raise NotImplementedError
    def __invert__(self): raise NotImplementedError

