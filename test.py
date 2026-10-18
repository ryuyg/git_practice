print ("영걸오빠 짱짱짱!!!")
print ("오늘 비가 와요!!!")
import time

colors = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[94m', '\033[95m']
text = "Hello, Python World! 무지개 세상입니다."

for i, char in enumerate(text):
    color = colors[i % len(colors)]
    print(f"{color}{char}", end="", flush=True)
    time.sleep(0.08)
print("\033[0m")  # 색상 초기화

print ("Hello world")

print("호텔에 사쿠라가 휘날립니다")
