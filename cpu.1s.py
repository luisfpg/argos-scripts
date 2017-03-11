#!/usr/bin/env python3
import psutil

cpus = psutil.cpu_percent(interval=1, percpu=True)
total = 0
for cpu in cpus:
    total += cpu
avg = total / len(cpus)


def show(cpu):
    color = '#cc575d' if cpu > 75 else '#d19a66' if cpu > 50 else '#68b382'
    return "<span color='%s'>%3d%%</span>" % (color, cpu)


print("CPU: %s|font=monospace" % show(avg))
print("---")
for i, cpu in enumerate(cpus):
    print("CPU %d: %s|font=monospace" % (i, show(cpu)))
print("---")
print("System monitor|iconName=utilities-system-monitor-symbolic" +
      " bash=gnome-system-monitor terminal=false")
