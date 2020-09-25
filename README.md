# 2DGP-Project

# 1. 게임의 소개
+ 제목: 똥 피하기(Avoiding Poop)
```
단순하게 날아오는 장애물을 피하거나 맞추어 없애는 게임입니다.
장애물을 맞으면 게임이 종료되고 최대한 많은시간을 버티는것이 게임 점수로 연결되며 그 기록이 랭킹에 저장되어 순위로 기록됩니다.
결국 높은 랭킹 순위에 드는 것이 목적입니다.
같은시간을 버티더라도 특정 물건을 던져 장애물을 맞춘 갯수가 많을 수록 게임 점수가 높아져 랭킹 순위가 높아집니다.
게임은 방향키를 이용하여 이동해서 장애물을 피하고  space bar를 누르면 특정 물건을 던져 장애물을 맞출 수 있습니다.
```

# 2. GameState (Scene)의 수 및 각각의 이름
+ state의 수는 총 6개
```
- 1.start state 
- 2.title state 
- 3.main state 
- 4.pause state 
- 5.result state 
- 6.score state
```

# 3. 각 GameState 별 다음 항목
+ start state: 게임 최초 실행, 한번만 학교 로고를 보여준다.
  
  -화면에 표시할 객체: 학교 타이틀 이미지   
  -처리할 키/마우스: 없음  
  -다른 state로 이동 조건 및 방법 : 정해진 시간 대기 후 자동으로 title state로 넘어간다.    
 
+ title state: 내 게임의 메인 이미지를 보여준다.  
  
  -화면에 표시할 객체: 메인게임 이미지, 폰트  
  -처리할 키/마우스: space bar , s  
  -다른 state로 이동 조건 및 방법 : space bar 눌렀을 때 main state로 이동 , s키 누르면 score state로 넘어간다.  
 
+ main state: 게임을 플레이하는 주 화면   
  
  -화면에 표시할 객체: 플레이어, 장애물, 아이템, 배경화면, 사운드 , 점수  
  -처리할 키/마우스: 방향키, space bar, esc  
  -다른 State로 이동 조건 및 방법: Esc키를 누르면 Pause state로 이동, 장애물에 맞으면 게임이 종료되어 result state로 넘어간다   
  
+ Pause state: 사운드를 조정하거나 게임 재시작, title state로 돌아가기 기능이있다.  
  
  -화면에 표시할 객체: pause state 화면이미지, 폰트  
  -처리할 키/마우스: s (사운드 끄기/켜기) , space bar , esc   
  -다른 state 이동 조건 및 방법: space bar를 누르면 게임을 재시작하는 main state로 넘어가고 esc를 누르면 title  state로 돌아간다.  
  
+ result state: 게임 결과 창 , 최종 스코어 점수를 보여준다.  
  
  -화면에 표시할 객체: 결과창 화면이미지, 플레이어 이미지, 폰트  
  -처리할 키/마우스: space bar, esc  
  -다른 State로 이동 조건 및 방법: esc를 누르면 title  state로 돌아가고 space bar를 누르면 score state로 넘어간다.  
  
+ score state: 게임 랭킹 창 , 랭킹 순위 기록을 보여준다.  
  
  -화면에 표시할 객체: 랭킹 창 화면이미지, 플레이어 이미지, 폰트  
  -처리할 키/마우스: esc  
  -다른 State로 이동 조건 및 방법: esc를 누르면 title  state로 돌아간다.  
  
  
# 4. 필요한 기술
- 다른 과목에서 배운 기술
```
없음
```
- 이 과목에서 배울 것으로 기대되는 기술
```
물체를 원하는 방향으로 날리는 방법
충돌 처리
게임 사운드 처리 
```
- 다루지 않은 것 같아서 수업에 다루어 달라고 요청할 기술
```
물체를 원하는 방향으로 날리는 방법
충돌 처리
게임 사운드 처리 
```


















