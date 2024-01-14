

class Ftp():
    
    def __init__(self, session, host, username, password) -> None:
        self._session = session
        self._host = host
        self._username = username
        self._password = password
        self._login()
        
    def _login(self):
        self._session.exec_cmd("ftp %s" %self._host)
        self._session.exec_cmd(self._username)
        self._session.exec_cmd(self._password)
        
    def put(self, filename):
        pass
        
    def quit(self):
        self._session.exec_cmd("quit")