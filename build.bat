@echo off
setlocal enabledelayedexpansion

echo === HEAVE v1.0.0 Builder ===

REM Set Rust environment
set RUSTUP_HOME=%USERPROFILE%\.rustup
set CARGO_HOME=%USERPROFILE%\.cargo
set Path=%USERPROFILE%\.cargo\bin;%Path%

echo.
echo Verifying Rust installation...
cargo --version
if errorlevel 1 (
    echo ERROR: Cargo not found!
    exit /b 1
)

echo Verifying npm...
npm --version
if errorlevel 1 (
    echo ERROR: npm not found!
    exit /b 1
)

echo.
echo Starting HEAVE build...
npm run build

if errorlevel 1 (
    echo ERROR: Build failed!
    exit /b 1
)

echo.
echo Build completed successfully!
