class Extent:
    '''
    Used to store minX, minY of bbox for queries, and to check their extent is not too large
    '''
    
    def calculate_area(self):
        '''
        TODO: what about edge case with wraparound?
        '''
        return (self.max_x - self.min_x) * (self.max_y - self.min_y)

    def exceeds_area(self,size_limit:float):
        print(f"Area was determined to be {self.calculate_area()}")
        return size_limit < self.calculate_area()

    @staticmethod
    def parse(extent_string:str):
        split_string = extent_string.split(",")
        if len(split_string) != 4:
            raise ValueError("Invalid extent string")
        
        return Extent(float(split_string[0]),float(split_string[1]),float(split_string[2]),float(split_string[3]))

    def __init__(self,min_x:float,min_y:float,max_x:float,max_y:float):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y
        