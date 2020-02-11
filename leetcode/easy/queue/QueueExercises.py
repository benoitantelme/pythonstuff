class RecentCounter:

    def __init__(self):
        self.pings = []

    def ping(self, t: int) -> int:
        self.pings.append(t)

        while len(self.pings) > 0 and self.pings[0] < t - 3000:
            self.pings.pop(0)
        return len(self.pings)


rc = RecentCounter()
rc.pings.append(0)
rc.pings.append(1)
rc.pings.append(100)
rc.pings.append(3001)
print(rc.ping(3002))

