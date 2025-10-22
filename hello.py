import psutil
import time

print('hello world')

time.sleep(1) 

cpu_percent = psutil.cpu_percent(interval=None) 
print(f'CPU Usage: {cpu_percent}%')

mem = psutil.virtual_memory()
gb_conversion = 1024**3 # Bytes 轉 GB 

print(f'Total Memory: {mem.total / gb_conversion:.2f} GB')
print(f'Used Memory: {mem.used / gb_conversion:.2f} GB')
print(f'Memory Usage: {mem.percent}%')

disk = psutil.disk_usage('/') 

print(f'Total Disk Space: {disk.total / gb_conversion:.2f} GB')
print(f'Used Disk Space: {disk.used / gb_conversion:.2f} GB')
print(f'Disk Usage: {disk.percent}%')
