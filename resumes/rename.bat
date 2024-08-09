@echo off
setlocal enabledelayedexpansion

REM Initialize counter
set count=1

REM Loop through each file in the current directory
for %%f in (*) do (
    REM Check if the filename starts with a digit
    if "%%~nf" neq "" if "%%~nf" lss "a" (
        REM Format the counter to ensure it has leading zeros
        set filename=%%~nf
        set ext=%%~xf
        if !count! LSS 10 (
            set newname=0!count!%%~xf
        ) else (
            set newname=!count!%%~xf
        )
        REM Rename the file
        ren "%%f" "!newname!"
        REM Increment the counter
        set /a count+=1
    )
)

echo Files have been renamed successfully.
