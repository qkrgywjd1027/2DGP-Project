***
# 2DGP-Project
+ 2018182046 박효정 게임공학과 
***

## 1. 게임의 소개
+ 제목: 똥 피하기(Avoid The Poop)
```
단순하게 날아오는 장애물을 피하는 게임입니다.
장애물을 맞으면 게임이 종료되고 최대한 많은시간을 버티는것이 게임 점수로 연결되며 그 기록이 랭킹에 저장되어 순위로 기록됩니다.
결국 높은 랭킹 순위에 드는 것이 목적입니다.
게임 플레이 도중 가끔 내려오는 특정 아이템에 의해 스코어를 올리는데 도움을 받을 수 있습니다.
게임은 방향키를 이용하여 장애물을 피할 수 있습니다.              
```    
[메인게임 화면구성 예시]    
<img width="574" alt="playex" src="https://user-images.githubusercontent.com/63097748/95647230-c2285880-0b08-11eb-83a1-6b6cb84658e4.PNG"> 
    
***
## 2. GameState (Scene)의 수 및 각각의 이름
+ GameState의 수는 총 6개
```
1.start state 
2.title state 
3.main state 
4.pause state 
5.result state 
6.score state
```
***
## 3. 각 GameState 별 다음 항목
+ start state: 게임 최초 실행, 한번만 학교 로고를 보여준다.
```
  -화면에 표시할 객체: 학교 타이틀 이미지   
  -처리할 키/마우스: 없음  
  -다른 state로 이동 조건 및 방법 : 정해진 시간 대기 후 자동으로 title state로 넘어간다.    
```
+ title state: 내 게임의 메인 이미지를 보여준다.  
```
  -화면에 표시할 객체: 메인게임 이미지, 폰트  
  -처리할 키/마우스: space bar , s  
  -다른 state로 이동 조건 및 방법 : space bar 눌렀을 때 main state로 이동 , s키 누르면 score state로 넘어간다.  
```
+ main state: 게임을 플레이하는 주 화면   
```
  -화면에 표시할 객체: 플레이어, 장애물, 아이템, 배경화면, 사운드 , 점수  
  -처리할 키/마우스: 방향키, esc  
  -다른 State로 이동 조건 및 방법: Esc키를 누르면 Pause state로 이동, 장애물에 맞으면 게임이 종료되어 result state로 넘어간다   
```  
+ Pause state: 사운드를 조정하거나 게임 재시작, title state로 돌아가기 기능이있다.  
```  
  -화면에 표시할 객체: pause state 화면이미지, 폰트  
  -처리할 키/마우스: s (사운드 끄기/켜기) , space bar , esc   
  -다른 state 이동 조건 및 방법: space bar를 누르면 게임을 재시작하는 main state로 넘어가고 esc를 누르면 title  state로 돌아간다.  
```  
+ result state: 게임 결과 창 , 최종 스코어 점수를 보여준다.  
``` 
  -화면에 표시할 객체: 결과창 화면이미지, 플레이어 이미지, 폰트  
  -처리할 키/마우스: esc ,
  -다른 State로 이동 조건 및 방법: esc를 누르면 title  state로 돌아가고 s를 누르면 score state로 넘어간다.  
``` 
+ score state: 게임 랭킹 창 , 랭킹 순위 기록을 보여준다.  
``` 
  -화면에 표시할 객체: 랭킹 창 화면이미지, 플레이어 이미지, 폰트  
  -처리할 키/마우스: esc  
  -다른 State로 이동 조건 및 방법: esc를 누르면 title  state로 돌아간다.  
```
***
## 4. 게임 실행 흐름 

![20201010_162313709](https://user-images.githubusercontent.com/63097748/95648828-22bd9280-0b15-11eb-976e-cea669c40c3f.jpg)     

***
## 5. 게임 개발 범위    
|항목|내용 |
|:---:|:---:|
|캐릭터컨트롤|2방향(좌우)키보드로 움직여 장애물 피함|
|맵|스테이지1개 - 초원|
|게임기능|무적아이템에 맞으면 5초간 무적|   
||코인아이템에 맞으면 모든 장애물이 코인으로 변하면서 맞는만큼 스코어 증가 |
||스코어는 살아있는 시간에 비례해서 증가|   
||장애물에 맞으면 게임오버|    
||게임오버 시 스코어 랭킹등록 |    
|사운드|배경음악, 장애물 맞는 효과음 , 게임오버효과음,   무적&코인아이템 맞는 효과음 , 코인아이템맞으면 모든 장애물이 코인으로 바뀌는 효과음 , 무적시 5초간 효과음, 코인아이템 맞는 효과음 등등|
|애니메이션|달리기, 장애물 맞았을때 캐릭터의 모션,  장애물을 맞았을 때 장애물의 이미지변화|


***
## 6. 게임 개발 계획
|주차|개발내용 |
|:---:|:---:|
|1주차|모든 리소스 수집 - 이미지,사운드 + 게임배경 삽입|
|2주차|게임캐릭터 이미지삽입과 키보드에 의한 좌우 이동처리 + 장애물+아이템 이미지 삽입과 상단에서 랜덤으로 내려오는것 구현 |
|3주차|장애물,아이템과 캐릭터간 충돌 처리 + 충돌 시 이미지 변화 (장애물과 관련된것만, 아이템제외)|   
|4,5주차|스코어 처리  (시간(초)로 살아있는 시간을 스코어로 처리) + 아이템의 경우 충돌시 효과 적용, 장애물 충돌 시 게임오버처리|
|6,7주차| 각종 스테이트 화면 구현과 스테이트간 전환 구현 + Pause state 집중 구현 + 랭킹스테이지에 스코어기록 + 사운드처리 (각종효과음)|    
|8주차|최종점검 및 수정|    



***
## 7. 필요한 기술
- 다른 과목에서 배운 기술
```
없음
```
- 이 과목에서 배울 것으로 기대되는 기술
```
충돌 처리
게임 사운드 처리 
```
- 다루지 않은 것 같아서 수업에 다루어 달라고 요청할 기술
```
없음
```
