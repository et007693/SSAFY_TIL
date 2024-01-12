## day1 : 챗봇 프로그래밍(0110)

검색 엔진과 gpt의 차이는 존재하는 것과 존재하지 않는 것을 보여준다는 차이가 있음

## day2 : Markdown, CLI, GIT
### CLI
- GUI는 CLI에 비해 사용하기 쉽지만 단계가 많고 상대적으로 성능을 더 많이 소모
- 수 많은 서버 / 개발 시스템이 CLI를 통한 조작 환경을 제공함
- 명령어
  - mkdir
  - ls
  - cd
  - pwd
  - touch
  - rm(-r)
  - start
- 절대경로 : c/users/ssafy/desktop
- 상대경로 : ./practice.txt ../

### Git
- 명령어
  - git init : 로컬 저장소 최고하
  - git status
  - git add 'file'
  - git commit -m 'msg' : staging area에 있는 파일들을 저장소에 기록 (--ammend : 마지막 커밋 메시지 변경)
 
- 실습
  1. 바탕화면에 git_commit 폴더를 만들고 git 저장소 생성
  2. 해당 폴더 안에 a.txt라는 텍스트 파일을 만들고, “add a.txt”라는 커밋 메시지로 커밋 생성
  3. 이번에는 b.txt라는 텍스트 파일을 만들고, “add b.txt”라는 커밋 메세지로 커밋 생성
  4. a.txt 파일을 수정하고, “update a.txt”라는 커밋 메세지로 커밋 생성
  5. 커밋 목록 확인

## day3 : Github
### Github
- 명령어
  - git remote -v
  - git clone 'remote_repo_url'
  - git remote add 'origin' 'remote_repo_url'
  - git push -u origin master
  - git pull 'remote_repo_url'
  ! pull과 clone의 차이점은 local에 없을 때만 가능(.git 파일이 없을 때)

.gitignore - 이미 git의 관리를 받은 파일이나 디렉토리는 나중에 gitignore에 작성해도 적용되지 않음

[gitignore 목록을 만들어주는 사이트](https://www.toptal.com/developers/gitignore/)
  
