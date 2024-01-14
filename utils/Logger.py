import os
import datetime
import logging

project_path = os.path.dirname(os.path.dirname(__file__))

class Logger():
    
    """ args:
    name: 测试任务名称（每个测试任务单独给出）
    level: 日志等级
    desc: 此次测试的描述：如测试单板
    """
    def __init__(self, name, level, desc) -> None:
        self._name = name
        self._level = level
        self._desc = desc
        self.logger = self._init_log_conf()
        
    def _init_log_conf(self):
        logger = logging.getLogger(self._name)
        logger.setLevel(self._level)
        
        formatter = logging.Formatter("%(asctime)s-%(levelname)s-%(name)s: %(message)s")
        
        path = os.path.join(project_path, "logs", self._desc)
        print(project_path)
        self._creater_dir(path)
        filename = str(datetime.date.today()) + self._desc + ".log"
        path = os.path.join(path, filename)
        
        fileHandler = logging.FileHandler(path, encoding="utf-8") 
        fileHandler.setLevel(self._level)
        fileHandler.setFormatter(formatter)
        
        logger.addHandler(fileHandler)
        return logger
    
    def _creater_dir(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
            
    def debug(self, msg):
        return self.logger.debug(msg)
 
    def info(self, msg):
        return self.logger.info(msg)

    def warning(self,msg):
        return self.logger.warning(msg)
    
    def error(self, msg):
        return self.logger.error(msg)
    
    def critical(self, msg):
        return self.logger.critical(msg)