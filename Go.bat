@echo off
xtimeq python Main.py %* 2>&1 | tee _go
