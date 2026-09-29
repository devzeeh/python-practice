from datetime import datetime

now = datetime.now()
print(now)                          # 2026-09-26 14:32:10.123456
print(now.strftime("%Y-%m-%d"))     # 2026-09-26
print(now.strftime("%B %d, %Y"))    # September 26, 2026