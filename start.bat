@echo off
chcp 65001 >nul
title SpikeFit - 排球专项体能与健身计划
echo --------------------------------------------------
echo 正在启动 SpikeFit 排球体能与健身规划器...
echo --------------------------------------------------
cd /d "%~dp0"
python server.py
pause
