## bluechatbot-emotionClassifier
emotion classifier using koBERT  
ㅤ　　  　  

### 학습 데이터  
- [Aihub 감성대화 말뭉치](https://aihub.or.kr/aidata/7978)  
ㅤ　　  　  

### 사용 모델
- pretrained koBERT  
ㅤ　　  　  

### 파일 설명
- dataloader/emotion.py : 감성대화 데이터를 임베딩 및 정제하여 데이터로더에 적재하는 코드.
- model/kobert.py : **koBERT 모델**과 입력 문장 1개를 정제하는 **kobert_input**함수가 정의되어 있는 코드.
- model/configuration.py : 모델에서 사용하는 사전 파라미터들을 정의해둔 코드.
- train/train-kobert-for-classification.ipynb : Colab 환경에서 모델을 학습시키는 코드. 학습 진행상황과 모델을 지속적으로 체크포인트로 저장하여 끊어서 학습을 진행할 수 있음.
- execute/kobert_execute.ipynb : Colab 환경에서 학습된 모델을 불러온 뒤 한 문장씩 테스트할 수 있는 코드.  
　  

### 실행 전 세팅
**디렉토리 구조 도식도**  
　  root_path ㅡ conversationModel	ㅡ	dataloader  
　  　 　　　 ㄴ **dataset** 　　　　　 ㄴ	model  
 　 　　 　　　　　　　　 　　　　 ㄴ train  
 　 　　　 　　　　　　　 　　　　 ㄴ execute  
 　 　　　　 　　　　　　 　　　　 ㄴ checkpoint  
　                               
- train 코드의 `필요 패키지 설치` 부분 경로를 자신의 디렉토리 경로로 수정
- `Path 추가` 부분에서 root_path와 code_path를 자신의 디렉토리 경로로 수정.
- root_path 아래에 **dataset** 디렉토리를 만들어 그 안에 학습 데이터를 다운로드. 또는 data_path를 학습 데이터가 위치한 경로로 수정.
