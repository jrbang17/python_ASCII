# ASCII 이름표 생성기

나만의 텍스트를 멋진 ASCII 아트로 변환해주는 파이썬 패키지입니다.

## 📂 패키지 구조

이 패키지는 다음과 같은 구조로 이루어져 있습니다.

```text
my_package_project/
├── ascii_nametag/          # Source Code
│   ├── __init__.py         # Package Initialization
│   └── core.py             # Core Logic (Class definition)
├── setup.py                # Setup script
├── requirements.txt        # Dependencies
└── README.md               # Documentation
```

## 🚀설치

```bash
pip install .
```

## 💻 사용법

```python
from ascii_nametag import NameTagGenerator

# 인스턴스 생성
tag_maker = NameTagGenerator(font='slant')

# 태그 출력
tag_maker.print_tag("My Package")
```

## 📸 실행 결과

프로그램 실행 결과입니다.

<img width="1574" height="281" alt="Image" src="https://github.com/user-attachments/assets/6f5cda7f-a02a-42e8-8207-6bd70c5bb1a9" />

