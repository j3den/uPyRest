class DisplaySingleService():
    _instance_of = None
    def __new__(cls,*args,**kwargs):
        print(cls._instance_of)
        if not cls._instance_of:
            cls._instance_of = super(DisplaySingleService,cls).__new__(cls,*args,**kwargs)
            return cls._instance_of