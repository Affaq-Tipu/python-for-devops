import psutil
def check_cpu_threshold():
    cpu_threshold = int(input("enter threshold"))
    current_cpu = psutil.cpu_percent(interval=1)
    current_cpu_memory = psutil.swap_memory()
    current_disk = psutil.disk_usage('/')
    print("current cpu: ",current_cpu)
    print("cuuuent memory: ",current_cpu_memory)
    print("current disk: ",current_disk)
    if current_cpu > cpu_threshold:
        print("send email")
    else:
        print("safe side")
check_cpu_threshold()