#!/usr/bin/env python3
import psutil

stats = psutil.virtual_memory()
mem = stats.percent


def size(bytes):
    suffix = 'B'
    if bytes > 1024:
        bytes /= 1024
        suffix = 'K'
    if bytes > 1024:
        bytes /= 1024
        suffix = 'M'
    if bytes > 1024:
        bytes /= 1024
        suffix = 'G'
    return "%8.2f%s" % (bytes, suffix)


color = '#cc575d' if mem > 75 else '#d19a66' if mem > 50 else '#68b382'

print("Mem: <span color='%s'>%3.d%%</span>|font=monospace" % (color, mem))
print("---")
print("Total:     %s|font=monospace" % size(stats.total))
print("Available: %s|font=monospace" % size(stats.available))
print("Used:      %s|font=monospace" % size(stats.used))
print("Buffers:   %s|font=monospace" % size(stats.buffers))
print("Cached:    %s|font=monospace" % size(stats.cached))
print("Shared:    %s|font=monospace" % size(stats.shared))
print("---")
print("System monitor|iconName=utilities-system-monitor-symbolic" +
      " bash=gnome-system-monitor terminal=false")
