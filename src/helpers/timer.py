from datetime import datetime, date
from dateutil.tz import gettz


class Timer:
    
    @staticmethod
    def get_current_time() -> int:
        return int(datetime.now(tz=gettz("Asia/Ho_Chi_Minh")).timestamp())
    
    @staticmethod
    def get_current_format(format: str = "%Y-%m-%d") -> str:
        return datetime.now(tz=gettz("Asia/Ho_Chi_Minh")).strftime(format)
