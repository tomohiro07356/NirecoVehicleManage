import time

class HeavyTask():
    
    wait_time:int = 10
    status:bool = False

    def __init__(self, wait_time:int=10) -> None:
        self.wait_time = wait_time
        print(f'background task initialized. set wait time {self.wait_time} s')
    
    def __call__(self) -> None:
        try:
            self.status = True
            print(f'sleep start.')
            time.sleep(self.wait_time)
        except Exception as e:
            print(e)
        finally:
            self.status = False
        print('sleep finished.')
    
    def get_status(self) -> bool:
        return self.status
