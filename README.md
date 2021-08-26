## bluechatbot-emotionClassifier
emotion classifier using koBERT  
　  
### 파일 설명
- dataloader/emotion.py : 감성대화 데이터를 임베딩 및 정제하여 데이터로더에 적재하는 코드.
- model/kobert.py : **koBERT 모델**과 입력 문장 1개를 정제하는 **kobert_input**함수가 정의되어 있는 코드.
- model/configuration.py : 모델에서 사용하는 사전 파라미터들을 정의해둔 코드.
- train/train-kobert-for-classification.ipynb : Colab 환경에서 모델을 학습시키는 코드. 학습 진행상황과 모델을 지속적으로 체크포인트로 저장/로드하여 끊어서 학습을 진행할 수 있음.
- execute/kobert_execute.ipynb : Colab 환경에서 학습된 모델을 불러온 뒤 한 문장씩 테스트할 수 있는 코드.  
　  

### 실행 전 세팅
root_path ㅡ conversationModel	ㅡ	dataloader  
　 　　　 ㄴ **dataset** 　　　　　 ㄴ	model  
　　 　　　　　　　　 　　　　 ㄴ train  
　　　 　　　　　　　 　　　　 ㄴ execute  
　　　　 　　　　　　 　　　　 ㄴ **checkpoint**  
                               
- `Path 추가` 부분에서 root_path를 자신의 파일 경로로 수정. 현재 세팅된 하위 구조는 위와 같음.
- 직전 상위 폴더에 **dataset** 폴더를 만들어 그 안에 학습 데이터를 위치시키거나, data_path를 학습 데이터가 현재 위치한 경로로 수정.
- 폴더 안에 **checkpoint** 라는 이름의 폴더를 추가. 혹은 checkpoint_path와 save_ckpt_path를 체크포인트를 저장할 다른 경로로 수정.
