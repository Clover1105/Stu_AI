"""
- flush()立即将缓冲区内容写入硬盘
- 正常情况下文件关闭时自动刷新
- 用于实时写入监控日志等场景
"""

# 演示flush立即写入
import time

f = open("log.txt", "w", encoding="utf-8")

f.write("第一条日志")
f.flush()  # 立即写入硬盘
print("第一条已写入，检查log.txt文件")

time.sleep(2)

f.write("\n第二条日志")
f.flush()  # 再次立即写入
print("第二条已写入")

f.close()
print("文件已关闭")