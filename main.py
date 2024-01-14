from basic.TelnetSession import TelnetSession


if __name__ == "__main__":
    session = TelnetSession("192.168.2.100", 23, "test", "test")
    session.exec_cmd("cat /usr/local/redis-6.2.7/redis.conf", "]$")
    