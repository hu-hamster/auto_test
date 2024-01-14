import logging
from utils.Logger import Logger

class BaseTestCase():
    
    def __init__(self, session, desc, parallel) -> None:
        self._session = session
        self._desc = desc
        self._parallel = parallel
        self._logger = Logger("", logging.DEBUG, self._desc)
        
        
    def run(self):
        self._session.exec_cmd()