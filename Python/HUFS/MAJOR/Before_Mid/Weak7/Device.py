from abc import ABC, abstractmethod

#추상 클래스 Device
class Device(ABC):
    def __init__(self, name):
        self.name = name
        self.__status = False

    @property #getter
    def status(self):
        return self.__status
    
    @abstractmethod
    def turn_on(self):
        self.__status = True
        
    @abstractmethod
    def turn_off(self):
        self.__status = False
    
# 상속 클래스 Light
class Light(Device):
    def __init__(self, name, brightness):
        super().__init__(name)
        self.__brightness = brightness

    def turn_on(self):
        super().turn_on()
        return print(f"[{self.name}] 조명이 켜졌습니다 (밝기 {self.__brightness})")
    
    def turn_off(self):
        super().turn_off()
        return print(f"[{self.name}] 조명이 꺼졌습니다")
    
    @property   # getter
    def brightness(self):
        return self.__brightness
    
    @brightness.setter
    def brightness(self, brightness):
        v = int(brightness)
        if (v <= 0):
            raise ValueError("Brightness must be larger than 0.")
        self.__brightness = v
        print(f"[{self.name}] 밝기 설정 : {self.__brightness}")        
    
    def __str__(self):
        status_str = "ON" if self.status else "OFF"
        return f"Light('{self.name}', status={status_str})"

# ====== 실행 ======

devices = [Light("거실등", brightness=70),
          Light("침실등", brightness=30)]

print("=== 초기 상태 ===")
for d in devices:
    print(d, "| status =", d.status)

print("/n=== 일괄 점등 ===")
for d in devices:
    d.turn_on()

print("\n=== 밝기 변경 ===")
devices[0].brightness = 90

print("\n=== 일괄 소등 ===")
for d in devices:
    d.turn_off()

print("\n=== 최종 상태 ===")
for d in devices:
    print(d, "| status =", d.status)