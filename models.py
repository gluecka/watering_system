import json

class ConfigClass:
    # define the path of configfile directly in init line as parameter
    def __init__(self, config_path='config.json'):
        # open and put the config data in a self.... parameter
        with open(config_path, 'r') as f:
            self.config = json.load(f)

        # for loop with each key - value pair to deploy that for further operations
        for key, value in self.config.items():
            setattr(self, key, value)



class SensorValueTrasformator(ConfigClass):
    
    def __init__(self, imput_value):
        # inherit the parameters of parents class
        super().__init__()

        self.imput_value = imput_value
    

    def percent_calculation(self) -> float:
        
        if self.imput_value >= self.low_wather:
            return 0
        elif self.imput_value <= self.high_wather:
            return 100
        else:
            gradient = -100 / (self.low_wather - self.high_wather)
            y_distance = 100 - (gradient * self.high_wather)
            soil_condition = round(gradient * self.imput_value + y_distance, 2)
            return soil_condition