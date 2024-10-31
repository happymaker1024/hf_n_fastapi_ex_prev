# hf_n_fastapi_ex_prev
huggingface and fastapi 실습

# 환경 셋팅
## 가상환경 만들기
```
conda create -n gpu_env_py310 python=3.10
conda activate gpu_env_py310
```

## 설치 라이브러리
```
# huggingface 관련 라이브러리
pip install transformers sentencepiece fsspec==2023.4.0 sacremoses

# fastapi 라이브러리
pip install fastapi "uvicorn[standard]" python-multipart

# 기타
pip install pillow
pip install python-dotenv


# pytorch gpu 버전 설치
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
```

## 가상환경과 jupyter lab 연동
```
pip install ipykernel
python -m ipykernel install --user --name gpu_env_py310 --display-name "gpu_env_py310"
```

# 실습 내용
- exam1.py : FinBERT는 금융 텍스트의 감정을 분석하기 위한 사전 훈련된 NLP 모델
    - 사용 모델 : ProsusAI/finbert 

- exam2.py : 한국어 금융 감성 분석
    - 사용 모델 : snunlp/KR-FinBert-SC

- exam3.py : 문장 요약
    - 사용 모델 : stevhliu/my_awesome_billsum_model (영문), psyche/KoT5-summarization (한글)

- exam4.py : 싱글 파일 업로딩
    
- exam5.py : 다중 파일 업로딩

- exam6.py : 애플리케이션의 생명주기 관리, 비동기 처리

- exam7.py : 한국어 -> 영어 번역, 긍정/부정 분류
    - 사용 모델 : Helsinki-NLP/opus-mt-ko-en, sentiment-analysis
- exam8.py :요약 서비스
    - 사용 모델 : sshleifer/distilbart-cnn-12-6
- exam9.py : 업로딩한 이미지에 설명글 생성하기
    - 사용 모델 : Salesforce/blip-image-captioning-large
- exam10.py : 영어 요약글 한글 번역하기
    - 사용 모델 : sshleifer/distilbart-cnn-12-6
    - 사용 모델 : facebook/nllb-200-distilled-600M
- exam11.py : 한글 영어로 번역, 클라이언트 비동기 처리
    - 사용 모델 : Helsinki-NLP/opus-mt-ko-en
- exam12.py : Annotated(폼 데이터를 통해 전달되는 문자열 받기)
