print ("영걸오빠 짱짱짱!!!")
print ("오늘 비가 와요!!!")
print ("예원이는 바보")
print ("정빈님은 멋쟁이")
import time

colors = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[94m', '\033[95m']
text = "Hello, Python World! 무지개 세상입니다."

print (" world")
for i, char in enumerate(text):
    color = colors[i % len(colors)]
    print(f"{color}{char}", end="", flush=True)
    time.sleep(0.08)
print ("날씨가 무지개같군요!?")
print ("Hello ")
print("\033[0m")  # 색상 초기화
print (" world")
print (" world")
print (" world")
print (" world")
print (" world")
print ("Hello world")

print("호텔에 사쿠라가 휘날립니다")
