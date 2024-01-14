import time
import logging
from telnetlib import Telnet
from basic.Logger import Logger


class TelnetSession():
    
    def __init__(self, host, port, username, password) -> None:
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._logger = Logger("test", logging.DEBUG, "路由器连接")
        self.session = Telnet()
        self._login()
    

    def _login(self):
        try:
            self.session.open(self._host, self._port)
        except:
            self._logger.error("路由器连接失败, ip: %s, port: %d" % (self._host, self._port))
            raise Exception
        
        self.session.read_until(b"login:", timeout=10)
        self.session.write(self._username.encode("ascii") + b"\n")
        self.session.read_until(b"Password: ",timeout=10)
        self.session.write(self._password.encode("ascii") + b"\n")
        
        time.sleep(3)
        
        result = self.session.read_very_eager().decode("ascii")
        if 'Login incorrect' not in result:
            self._logger.info("登录成功, host=%s" % self._host)
            return True
        else:
            print(result)
            self._logger.error("登录失败，用户名或密码错误")
            return False
        
    def exec_cmd(self, cmd, until_str):
        self.session.write(cmd.encode("ascii") + b"\n")
        result = self.session.read_until(until_str.encode("ascii")).decode("ascii")
        self._logger.info(result)
