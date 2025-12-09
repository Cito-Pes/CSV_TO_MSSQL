# CDR 파일 처리 프로그램 - 빌드 가이드

## 📋 목차
1. [준비사항](#준비사항)
2. [프로젝트 구조](#프로젝트-구조)
3. [빌드 방법](#빌드-방법)
4. [배포 방법](#배포-방법)
5. [문제 해결](#문제-해결)

---

## 준비사항

### 1. Python 환경
- Python 3.13.6 설치 필요
- 가상환경(.venv) 활성화

### 2. 필수 패키지 설치

```bash
# 가상환경 활성화
.venv\Scripts\activate

# 패키지 일괄 설치
pip install -r requirements.txt
```

또는 개별 설치:
```bash
pip install cx_Freeze PySide6 pyodbc openpyxl requests
```

### 3. 필수 파일 확인

프로젝트 루트에 다음 파일들이 있어야 합니다:

```
프로젝트 폴더/
├── cdr_processor.py      # 메인 프로그램
├── setup.py              # cx_Freeze 설정
├── build.py              # 빌드 자동화 스크립트
├── requirements.txt      # 패키지 목록
├── images/
│   ├── icon.ico         # 프로그램 파비콘
│   └── app_icon.png     # 실행파일 아이콘
└── .venv/               # 가상환경
```

---

## 프로젝트 구조

```
CDR_Processor/
│
├── cdr_processor.py          # 메인 프로그램 파일
├── setup.py                  # cx_Freeze 빌드 설정
├── build.py                  # 자동 빌드 스크립트
├── requirements.txt          # 필수 패키지 목록
│
├── images/                   # 이미지 리소스
│   ├── icon.ico             # 윈도우 아이콘 (프로그램)
│   └── app_icon.png         # 실행파일 아이콘
│
├── .venv/                   # 가상환경 (자동생성)
│
├── build/                   # 빌드 결과물 (자동생성)
│   └── exe.win-amd64-3.13/
│       ├── CDR_Processor.exe
│       ├── lib/
│       ├── images/
│       └── README.txt
│
└── DB/                      # 데이터베이스 폴더 (자동생성)
    └── Config_DB.db         # 설정 DB (자동다운로드)
```

---

## 빌드 방법

### 방법 1: 자동 빌드 스크립트 사용 (권장)

가장 간단하고 안전한 방법입니다.

```bash
# 가상환경 활성화
.venv\Scripts\activate

# 빌드 스크립트 실행
python build.py
```

빌드 스크립트가 자동으로 수행하는 작업:
1. ✓ 필수 패키지 확인
2. ✓ 필수 파일 확인
3. ✓ 이전 빌드 폴더 정리
4. ✓ 실행파일 빌드
5. ✓ README 파일 생성
6. ✓ 빌드 결과 요약

### 방법 2: 수동 빌드

```bash
# 가상환경 활성화
.venv\Scripts\activate

# 이전 빌드 정리 (선택사항)
rmdir /s /q build
rmdir /s /q dist

# cx_Freeze 빌드 실행
python setup.py build
```

### 빌드 결과 확인

빌드가 성공하면 다음 폴더가 생성됩니다:

```
build/exe.win-amd64-3.13/
├── CDR_Processor.exe        # 실행파일
├── python313.dll            # Python 런타임
├── lib/                     # 라이브러리 폴더
│   ├── library.zip          # Python 라이브러리
│   └── PySide6/             # Qt 라이브러리
├── images/                  # 이미지 리소스
│   ├── icon.ico
│   └── app_icon.png
└── README.txt               # 사용 설명서
```

---

## 배포 방법

### 1. 배포 파일 준비

```bash
# build/exe.win-amd64-3.13/ 폴더 전체를 압축
# 압축 파일명 예: CDR_Processor_v2.0.zip
```

### 2. 배포 패키지 구성

압축 파일에 포함되어야 할 항목:
- ✓ CDR_Processor.exe
- ✓ python313.dll
- ✓ lib/ 폴더 전체
- ✓ images/ 폴더 전체
- ✓ README.txt

### 3. 사용자 설치 가이드

사용자에게 전달할 설치 방법:

1. **압축 해제**
   - CDR_Processor_v2.0.zip 파일을 원하는 위치에 압축 해제

2. **실행**
   - CDR_Processor.exe 더블클릭

3. **초기 설정**
   - 프로그램이 자동으로 Config_DB.db 다운로드
   - 데이터베이스 연결 정보 자동 로드

4. **사용**
   - CDR CSV 파일 선택
   - 처리 시작 버튼 클릭

### 4. 시스템 요구사항

사용자 PC에 필요한 사항:
- Windows 10 이상 (64bit)
- 인터넷 연결 (초기 설정 시)
- SQL Server 연결 가능
- 약 200MB 디스크 공간

**주의**: Python 설치 불필요! (실행파일에 포함됨)

---

## 문제 해결

### 빌드 오류

#### 1. "ModuleNotFoundError: No module named 'cx_Freeze'"
```bash
pip install cx_Freeze
```

#### 2. "파일을 찾을 수 없습니다: images/icon.ico"
```bash
# images 폴더 생성
mkdir images

# 아이콘 파일 복사
# icon.ico와 app_icon.png를 images 폴더에 넣어주세요
```

#### 3. "ImportError: DLL load failed"
```bash
# Visual C++ 재배포 패키지 설치 필요
# https://aka.ms/vs/17/release/vc_redist.x64.exe
```

#### 4. 빌드는 성공했지만 실행파일이 실행되지 않음
```bash
# 바이러스 백신 확인
# 실행파일이 격리되었는지 확인

# 의존성 확인
python setup.py build --includes=PySide6,pyodbc,openpyxl,requests
```

### 실행 오류

#### 1. "Config_DB.db 파일을 다운로드할 수 없습니다"
- 인터넷 연결 확인
- 방화벽 설정 확인
- 구글 드라이브 링크 유효성 확인

#### 2. "DB 연결 실패"
- SQL Server 실행 여부 확인
- 네트워크 연결 확인
- Config_DB.db의 설정 정보 확인

#### 3. 실행파일 크기가 너무 큼 (>100MB)
- 정상입니다. PySide6와 Python 런타임이 포함되어 있습니다.
- 일반적으로 150~200MB 정도입니다.

---

## 개발자 참고사항

### setup.py 주요 옵션

```python
build_exe_options = {
    "packages": [...],        # 포함할 패키지
    "includes": [...],        # 명시적으로 포함할 모듈
    "excludes": [...],        # 제외할 패키지 (크기 최적화)
    "include_files": [...],   # 포함할 파일/폴더
    "optimize": 2,            # 최적화 레벨 (0~2)
}
```

### 크기 최적화

불필요한 패키지 제외하여 크기 줄이기:
```python
"excludes": [
    "tkinter",      # Tkinter GUI (미사용)
    "unittest",     # 테스트 프레임워크
    "email",        # 이메일 라이브러리
    ...
]
```

### 아이콘 변경

1. **프로그램 아이콘** (윈도우 제목 표시줄)
   - `images/icon.ico` 파일 교체
   - 크기: 16x16, 32x32, 48x48 (멀티 사이즈 ICO)

2. **실행파일 아이콘** (exe 파일 아이콘)
   - `images/app_icon.png` 파일 교체
   - 권장 크기: 256x256 PNG

### 버전 관리

setup.py에서 버전 변경:
```python
setup(
    name="CDR_Processor",
    version="2.0",  # 여기를 변경
    ...
)
```

---

## 체크리스트

빌드 전 확인사항:

- [ ] Python 3.13.6 설치 확인
- [ ] 가상환경 활성화
- [ ] requirements.txt의 모든 패키지 설치
- [ ] cdr_processor.py 파일 존재
- [ ] images/icon.ico 파일 존재
- [ ] images/app_icon.png 파일 존재
- [ ] setup.py 파일 존재
- [ ] build.py 파일 존재

빌드 후 확인사항:

- [ ] build/ 폴더 생성 확인
- [ ] CDR_Processor.exe 실행 테스트
- [ ] DB 설정 자동 다운로드 확인
- [ ] CSV 파일 처리 테스트
- [ ] 엑셀 파일 생성 확인

배포 전 확인사항:

- [ ] 다른 PC에서 실행 테스트
- [ ] Python 미설치 환경에서 테스트
- [ ] README.txt 포함 확인
- [ ] 압축 파일 크기 확인 (150~200MB)
- [ ] 사용자 매뉴얼 작성 완료

---

## 추가 자료

- [cx_Freeze 공식 문서](https://cx-freeze.readthedocs.io/)
- [PySide6 공식 문서](https://doc.qt.io/qtforpython/)
- [PyODBC 문서](https://github.com/mkleehammer/pyodbc/wiki)

---

## 연락처

빌드 관련 문의: [관리자 이메일]

---

**마지막 업데이트**: 2024-12-09
**버전**: 2
