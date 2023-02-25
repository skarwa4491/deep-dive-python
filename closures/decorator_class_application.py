def info(self):
    from datetime import datetime , timezone
    result = list()
    result.append('time :\'{}'.format(datetime.now(timezone.utc)))
    result.append('id : {}'.format(hex(id(self))))
    result.append('class : {}'.format(self.__class__.__name__))
    for k,v in vars(self).items():
        result.append('{}:{}'.format(k,v))
    return result

def debug(cls):
    cls.debug = info
    return cls

@debug
class AutoMobile:
    
    def __init__(self , name , model , make_year , top_speed) -> None:
        self.name = name
        self.model = model
        self.make_year = make_year
        self.top_speed = top_speed
        self._speed = 0
    
    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self , speed):
        if speed > self.top_speed:
            raise ValueError('Speed cannot be greater than top speed')
        else:
            self._speed = speed


a = AutoMobile('Ford' , 'Model - A' , '1973' , 45)
print(a.debug())
a.speed = 40
print(a.speed)
print(a.debug())

