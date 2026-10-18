import time

colors = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[94m', '\033[95m']
text = "Hello, Python World! 무지개 세상입니다."

for i, char in enumerate(text):
    color = colors[i % len(colors)]
    print(f"{color}{char}", end="", flush=True)
    time.sleep(0.08)
print("\033[0m")  # 색상 초기화

print ("Hello world")