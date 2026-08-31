@echo off
REM Restart the local Jekyll preview server for pikaia.github.io.
REM
REM Stops whatever is holding 127.0.0.1:4000, then serves with the
REM local-only _config_dev.yml layered on top of _config.yml (adds the
REM "LOCAL --" title, shows future-dated posts, keeps the inline Watch
REM button, and shows the homepage pipeline badges). Production builds
REM from _config.yml alone and is unaffected.
REM
REM Run from anywhere - it cd's to the repo root itself.
REM Leave this window open; Ctrl-C stops the server.

setlocal
cd /d "%~dp0.."

echo Stopping any server on 127.0.0.1:4000 ...
for /f "tokens=5" %%P in ('netstat -ano ^| findstr "127.0.0.1:4000" ^| findstr "LISTENING"') do (
  echo   killing PID %%P
  taskkill /F /PID %%P >nul 2>&1
)
timeout /t 1 /nobreak >nul

echo Starting: jekyll serve --config _config.yml,_config_dev.yml
echo   ( http://127.0.0.1:4000 )
echo.
jekyll serve --config _config.yml,_config_dev.yml
