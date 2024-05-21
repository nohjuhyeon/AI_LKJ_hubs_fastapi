1. docker 설치하기

2. docker의 db_mongodb_7-1 들어가기

3. Exec 들어가기

4. mongo docker 안에서 wget 실행하기
 wget --no-check-certificate 'https://drive.google.com/uc?export=download&id=1hOFZLRkDz-74ZphpoHK0WZfh2uc807TU' -O /home/my_data.archive

5. mongo 복구
mongorestore --uri "mongodb://ai_ikj_third-db_mongodb_7-1:27017/AI_LKJ" --archive=/home/initial_data.archive


* 만약에 mongo를 삭제하고 싶을 경우
mongodump --uri "mongodb://ai_ikj_third-db_mongodb_7-1:27017/AI_LKJ" --archive=/home/initial_data.archive
