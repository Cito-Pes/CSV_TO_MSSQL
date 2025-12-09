"""
CDR 파일 처리 프로그램 - cx_Freeze 빌드 스크립트
Python 3.13.6 + PySide6
"""

import sys
from cx_Freeze import setup, Executable

# 빌드 옵션
build_exe_options = {
    "packages": [
        "os",
        "sys",
        "csv",
        "re",
        "sqlite3",
        "datetime",
        "pathlib",
        "requests",
        "pyodbc",
        "openpyxl",
        "PySide6.QtCore",
        "PySide6.QtGui",
        "PySide6.QtWidgets",
        "zipfile",      # PySide6/shiboken6 필수
        "xml",          # PySide6 필수
        "urllib",       # requests 필수
        "PySide6",      # 전체 PySide6 패키지
        "shiboken6",    # PySide6 바인딩
    ],
    "includes": [
        "openpyxl.styles",
        "openpyxl.cell",
        "openpyxl.worksheet",
        "openpyxl.workbook",
    ],
    "excludes": [
    "tkinter",      # Tkinter만 제외
    "unittest",     # 테스트 프레임워크만 제외
    "email",
    "html",
    "http",
    "pydoc",
    "doctest",
    ],
    "include_files": [
        # 아이콘 파일 포함 (존재하는 경우만)
    ],
    "zip_include_packages": ["encodings", "PySide6"],
    "optimize": 2,
}

# 아이콘 파일이 존재하면 포함
import os
if os.path.exists("images/icon.ico"):
    build_exe_options["include_files"].append(("images/icon.ico", "images/icon.ico"))
if os.path.exists("images/app_icon.png"):
    build_exe_options["include_files"].append(("images/app_icon.png", "images/app_icon.png"))

# 실행파일 기본 정보
base = None
if sys.platform == "win32":
    base = "gui"  # 콘솔 창 숨기기 (cx_Freeze 7.x 이상)

# 아이콘 파일 설정
icon_file = None
if os.path.exists("images/app_icon.ico"):
    icon_file = "images/app_icon.ico"
elif os.path.exists("images/icon.ico"):
    icon_file = "images/icon.ico"

# 실행파일 설정
executable = Executable(
    script="Make_CDR_v5.py",  # 메인 파이썬 파일명
    base=base,
    icon=icon_file,  # 실행파일 아이콘 (ICO 파일만 가능)
    target_name="Make_CDR_v5.exe",  # 생성될 실행파일 이름
)

# Setup 설정
setup(
    name="Make_CDR",
    version="2.0",
    description="CDR 파일 처리 및 미통화 리스트 생성 프로그램",
    author="CDR Team",
    options={"build_exe": build_exe_options},
    executables=[executable],
)