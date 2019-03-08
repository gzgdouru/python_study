'''
实现状态对象或者状态机
'''


class Connection:
    '''普通方案，好多个判断语句，效率低下~~'''

    def __init__(self):
        self.state = "CLOSED"

    def read(self):
        if self.state != "OPEN":
            raise RuntimeError("Not open")
        print("reading")

    def write(self):
        if self.state != "OPEN":
            raise RuntimeError("Not open")
        print("writing")

    def open(self):
        if self.state == "OPEN":
            raise RuntimeError("Already open")
        self.state = "OPEN"

    def close(self):
        if self.state == "CLOSED":
            raise RuntimeError("Already closed")
        self.state = "CLOASED"


class ConnectionState:
    @staticmethod
    def read(conn):
        raise NotImplementedError()

    @staticmethod
    def write(conn, data):
        raise NotImplementedError()

    @staticmethod
    def open(conn):
        raise NotImplementedError()

    @staticmethod
    def close(conn):
        raise NotImplementedError()


class OpenConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print('reading')

    @staticmethod
    def write(conn, data):
        print('writing')

    @staticmethod
    def open(conn):
        raise RuntimeError('Already open')

    @staticmethod
    def close(conn):
        conn.new_state(ClosedConnectionState)


class ClosedConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        raise RuntimeError('Not open')

    @staticmethod
    def write(conn, data):
        raise RuntimeError('Not open')

    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)

    @staticmethod
    def close(conn):
        raise RuntimeError('Already closed')


class Connection1:
    """新方案——对每个状态定义一个类"""

    def __init__(self):
        self.new_state(ClosedConnectionState)

    def new_state(self, newstate):
        self._state = newstate

    def read(self):
        return self._state.read(self)

    def write(self, data):
        return self._state.write(self, data)

    def open(self):
        return self._state.open(self)

    def close(self):
        return self._state.close(self)


if __name__ == "__main__":
    c = Connection1()
    print(c._state)

    c.open()
    print(c._state)
    c.read()
    c.write("hello")

    c.close()
    print(c._state)
