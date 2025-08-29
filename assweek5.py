# Parent 
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"{self.brand} {self.model}"

# Child  
class Smartphone(Device):
    def __init__(self, brand, model, storage, camera):
        super().__init__(brand, model)   
        self.storage = storage
        self.camera = camera
    
    def take_photo(self):
        return f"{self.brand} {self.model} takes a {self.camera}MP photo!"
    
    def upgrade_storage(self, extra_gb):
        self.storage += extra_gb
        return f"Storage upgraded! Total: {self.storage}GB"


class Tablet(Device):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size
    
    def info(self):   
        return f"{self.brand} {self.model} with {self.screen_size}-inch display"


phone = Smartphone("Samsung", "Galaxy S23", 128, 108)
tablet = Tablet("Apple", "iPad Pro", 12.9)


print(phone.info())
print(phone.take_photo())
print(phone.upgrade_storage(64))
print(tablet.info())   
