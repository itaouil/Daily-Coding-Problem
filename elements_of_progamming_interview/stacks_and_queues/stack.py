import bisect


class Stack:
    def __init__(self, things=[]):
        self.things = []
        self.max_cache = []
        for thing in things:
            self.push(thing)

    @property
    def max(self):
        return None if not self.max_cache else self.max_cache[-1]

    def pop(self):
        popped = self.things.pop()
        if popped == self.max:
            self.max_cache.pop()
        return popped

    def push(self, thing):
        if not self.max or thing > self.max: self.max_cache.append(thing)
        self.things.append(thing)


# TODO: add_tests
