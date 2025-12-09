"""
빌드 자동화 스크립트
실행: python build.py
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

def check_virtual_env():
    """가상환경 활성화 확인"""
    print("=" * 60)
    print("가상환경 확인 중...")
    print("=" * 60)
    
    # 가상환경 체크
    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )
    
    if in_venv:
        print(f"✓ 가상환경 활성화됨: {sys.prefix}")
    else:
        print("⚠ 가상환경이 활성화되지 않았습니다.")
        print("\n가상환경을 활성화해주세요:")
        print("  Windows: .venv\\Scripts\\activate")
        print("  Linux/Mac: source .venv/bin/activate")
        return False
    
    print(f"✓ Python 버전: {sys.version}")
    print()
    return True

def check_requirements():
    """필수 패키지 확인 (현재 실행 중인 Python 환경)"""
    print("=" * 60)
    print("필수 패키지 확인 중...")
    print("=" * 60)
    
    required_packages = {
        "cx_Freeze": "cx_Freeze",
        "PySide6": "PySide6", 
        "pyodbc": "pyodbc",
        "openpyxl": "openpyxl",
        "requests": "requests",
    }
    
    missing_packages = []
    
    for display_name, import_name in required_packages.items():
        try:
            module = __import__(import_name)
            version = getattr(module, '__version__', 'unknown')
            print(f"✓ {display_name} {version}")
        except ImportError:
            print(f"✗ {display_name} 미설치")
            missing_packages.append(display_name)
    
    if missing_packages:
        print("\n" + "=" * 60)
        print("❌ 다음 패키지가 설치되지 않았습니다:")
        print("=" * 60)
        for pkg in missing_packages:
            print(f"  {pkg}")
        print("\n설치 방법:")
        print("  pip install -r requirements.txt")
        print("\n또는 개별 설치:")
        for pkg in missing_packages:
            print(f"  pip install {pkg}")
        return False
    
    print("\n✓ 모든 필수 패키지가 설치되어 있습니다.\n")
    return True

def check_files():
    """필수 파일 확인"""
    print("=" * 60)
    print("필수 파일 확인 중...")
    print("=" * 60)
    
    required_files = [
        # "cdr_processor.py",
        # "setup.py",
        "Make_CDR_v5.py","cx_Freeze_Setup.py"
    ]
    
    optional_files = [
        "images/icon.ico",
        "images/app_icon.png",
    ]
    
    missing_files = []
    missing_optional = []
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file} 존재")
        else:
            print(f"✗ {file} 없음")
            missing_files.append(file)
    
    for file in optional_files:
        if os.path.exists(file):
            print(f"✓ {file} 존재")
        else:
            print(f"⚠ {file} 없음 (선택사항)")
            missing_optional.append(file)
    
    if missing_files:
        print("\n" + "=" * 60)
        print("❌ 다음 필수 파일이 없습니다:")
        print("=" * 60)
        for file in missing_files:
            print(f"  {file}")
        return False
    
    if missing_optional:
        print("\n⚠ 선택사항 파일이 없습니다:")
        for file in missing_optional:
            print(f"  {file}")
        print("아이콘 없이 빌드가 진행됩니다.")
    
    print("\n✓ 모든 필수 파일이 존재합니다.\n")
    return True

def clean_build():
    """이전 빌드 정리"""
    print("=" * 60)
    print("이전 빌드 파일 정리 중...")
    print("=" * 60)
    
    dirs_to_remove = ["build", "dist"]
    
    for dir_name in dirs_to_remove:
        if os.path.exists(dir_name):
            try:
                shutil.rmtree(dir_name)
                print(f"✓ {dir_name} 폴더 삭제됨")
            except Exception as e:
                print(f"⚠ {dir_name} 폴더 삭제 실패: {e}")
    
    print()

def build_exe():
    """실행파일 빌드"""
    print("=" * 60)
    print("실행파일 빌드 시작...")
    print("=" * 60)
    print()
    
    try:
        # cx_Freeze 빌드 실행
        result = subprocess.run(
            # [sys.executable, "setup.py", "build"],
            [sys.executable, "cx_Freeze_Setup.py", "build"],
            capture_output=False,  # 실시간 출력 표시
            text=True,
            check=True
        )
        
        print()
        print("=" * 60)
        print("✓ 빌드 성공!")
        print("=" * 60)
        return True
            
    except subprocess.CalledProcessError as e:
        print()
        print("=" * 60)
        print("❌ 빌드 실패")
        print("=" * 60)
        print(f"\n오류 코드: {e.returncode}")
        if e.stderr:
            print(f"오류 메시지:\n{e.stderr}")
        return False
    except Exception as e:
        print()
        print("=" * 60)
        print("❌ 빌드 중 예외 발생")
        print("=" * 60)
        print(f"\n오류: {e}")
        return False

def create_readme():
    """README 파일 생성"""
    readme_content = """
# CDR 파일 처리 프로그램 v2.0

## 프로그램 설명
CDR CSV 파일을 처리하여 미통화 리스트를 생성하고 엑셀 파일로 저장하는 프로그램입니다.

## 사용 방법

1. **프로그램 실행**
   - CDR_Processor.exe 파일을 실행합니다.
   
2. **자동 설정**
   - 프로그램이 자동으로 데이터베이스 설정 파일(Config_DB.db)을 다운로드합니다.
   - 데이터베이스 연결 정보가 자동으로 로드됩니다.

3. **파일 선택**
   - "파일 선택" 버튼을 클릭하여 CDR CSV 파일을 선택합니다.
   - 파일명 형식: CDR-25120900.csv

4. **처리 시작**
   - "처리 시작" 버튼을 클릭합니다.
   - 진행 상태를 로그 창에서 확인할 수 있습니다.

5. **결과 확인**
   - 처리가 완료되면 엑셀 파일이 생성됩니다.
   - 파일명 형식: 20251208_미통화리스트.xlsx

## 시스템 요구사항

- Windows 10 이상
- SQL Server 2008 R2 이상
- 인터넷 연결 (초기 설정 파일 다운로드용)

## 생성되는 파일/폴더

- `./DB/Config_DB.db` - 데이터베이스 설정 파일
- `YYYYMMDD_미통화리스트.xlsx` - 처리 결과 엑셀 파일

## 문제 해결

### "Config_DB.db 파일을 다운로드할 수 없습니다"
- 인터넷 연결을 확인하세요.
- 방화벽 설정을 확인하세요.

### "DB 연결 실패"
- SQL Server가 실행 중인지 확인하세요.
- 네트워크 연결을 확인하세요.
- Config_DB.db의 설정 정보가 올바른지 확인하세요.

### "CSV 파일 읽기 실패"
- 파일명이 CDR-YYMMDD00.csv 형식인지 확인하세요.
- 파일이 손상되지 않았는지 확인하세요.

## 버전 정보
- Version: 2.0
- 개발 환경: Python 3.13.6 + PySide6

## 연락처
문의사항이 있으시면 관리자에게 연락하세요.
"""
    
    build_dir = Path("build")
    if build_dir.exists():
        # build 폴더에서 exe가 있는 폴더 찾기
        exe_dirs = [d for d in build_dir.iterdir() if d.is_dir()]
        if exe_dirs:
            readme_path = exe_dirs[0] / "README.txt"
            try:
                with open(readme_path, "w", encoding="utf-8") as f:
                    f.write(readme_content)
                print(f"✓ README 파일 생성: {readme_path}")
            except Exception as e:
                print(f"⚠ README 생성 실패: {e}")

def show_build_info():
    """빌드 결과 정보 표시"""
    print("\n" + "=" * 60)
    print("빌드 완료 정보")
    print("=" * 60)
    
    build_dir = Path("build")
    if not build_dir.exists():
        print("❌ build 폴더를 찾을 수 없습니다.")
        return
    
    exe_dirs = [d for d in build_dir.iterdir() if d.is_dir()]
    if not exe_dirs:
        print("❌ 빌드된 실행파일 폴더를 찾을 수 없습니다.")
        return
    
    exe_path = exe_dirs[0]
    exe_file = exe_path / "CDR_Processor.exe"
    
    print(f"\n📁 빌드 폴더: {exe_path}")
    
    if exe_file.exists():
        file_size = exe_file.stat().st_size / (1024 * 1024)  # MB
        print(f"✓ 실행파일: {exe_file}")
        print(f"  크기: {file_size:.2f} MB")
    else:
        print("⚠ CDR_Processor.exe를 찾을 수 없습니다.")
    
    # 포함된 파일 확인
    print(f"\n📦 포함된 파일:")
    if (exe_path / "images").exists():
        print(f"  ✓ images/ 폴더")
    if (exe_path / "lib").exists():
        print(f"  ✓ lib/ 폴더")
    if (exe_path / "README.txt").exists():
        print(f"  ✓ README.txt")
    
    # 전체 크기 계산
    total_size = sum(
        f.stat().st_size 
        for f in exe_path.rglob('*') 
        if f.is_file()
    ) / (1024 * 1024)
    
    print(f"\n📊 전체 크기: {total_size:.2f} MB")
    
    print("\n" + "=" * 60)
    print("📦 배포 방법")
    print("=" * 60)
    print(f"1. 다음 폴더 전체를 압축하세요:")
    print(f"   {exe_path}")
    print(f"\n2. 압축 파일을 사용자에게 전달")
    print(f"\n3. 사용자는 압축 해제 후 CDR_Processor.exe 실행")
    
    print("\n" + "=" * 60)

def main():
    """메인 빌드 프로세스"""
    print("\n")
    print("*" * 60)
    print("*" + " " * 58 + "*")
    print("*" + "  CDR 파일 처리 프로그램 - 빌드 스크립트".center(58) + "*")
    print("*" + " " * 58 + "*")
    print("*" * 60)
    print("\n")
    
    # 0. 가상환경 확인
    if not check_virtual_env():
        print("\n❌ 빌드를 중단합니다.")
        input("\nPress Enter to exit...")
        return
    
    # 1. 필수 패키지 확인
    if not check_requirements():
        print("\n❌ 빌드를 중단합니다.")
        input("\nPress Enter to exit...")
        return
    
    # 2. 필수 파일 확인
    if not check_files():
        print("\n❌ 빌드를 중단합니다.")
        input("\nPress Enter to exit...")
        return
    
    # 3. 이전 빌드 정리
    clean_build()
    
    # 4. 실행파일 빌드
    if not build_exe():
        print("\n❌ 빌드를 중단합니다.")
        input("\nPress Enter to exit...")
        return
    
    # 5. README 생성
    create_readme()
    
    # 6. 빌드 정보 표시
    show_build_info()
    
    print("\n" + "=" * 60)
    print("✓ 모든 작업이 완료되었습니다!")
    print("=" * 60)
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n사용자에 의해 중단되었습니다.")
        input("\nPress Enter to exit...")
    except Exception as e:
        print(f"\n❌ 예상치 못한 오류 발생: {e}")
        import traceback
        traceback.print_exc()
        input("\nPress Enter to exit...")