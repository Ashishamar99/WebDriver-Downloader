@echo off
wmic datafile where name="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" get version /value
REM %username% is an environmental variable for the username. 