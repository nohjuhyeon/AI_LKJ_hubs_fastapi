## Clouds‐GCP

### create vm instance and than connect SSH in GCP
```
@ new project with ['rare-field']
@ Compute Engine > VM instance with ['rare-field'] (basic) > Disk size : 50G, Choose all with Firewall
@ click 'SSH' with 'rare-field'
~$ sudo apt-get update && sudo apt install -y unzip docker-compose nginx certbot python3-certbot-nginx

~$ lscpu
~$ df -h
~$ sudo systemctl status nginx
```

### DNS management (need login) with extenal IP on vm instance GCP
```
@https://dns.gabia.com/ > get Domain 
> DNS Managerment 'rare-field.shop': Host - setup extenal IP with '@' and 'www' 

@ http://34.123.194.224:80/
```

### install Docker with containers in GCP
```
~$ sudo docker system prune

~$ wget https://github.com/nohjuhyeon/AI_LKJ_HUB_third/raw/main/AI_LKJ_THIRD.zip
~$ unzip AI_LKJ_THIRD.zip
~$ unzip AI_LKJ_THIRD.zip -d docker_folder && cd ./docker_folder
~/docker_folder$ sudo docker-compose build --no-cache
~/docker_folder$ sudo docker-compose --project-name teams_java_jupyterlab_mysql up -d

~$ sudo docker ps
~$ sudo docker exec -it teams_java_jupyterlab_mysql_springboot_3.1.1_fastapi_1 bash
```

### start fastapi server in docker
```
~# ps aux | grep uvicorn 
~# kill -9 [PID]
~# apt-get update && apt install -y nano
~# cd /apps/fastapis/apps && nano .env
/apps/fastapis# cd ../ && git pull
/apps/fastapis# nohup uvicorn main:app --host 0.0.0.0 --port 8000 --workers 2 & 
/apps/fastapis# exit

outside_docker:~$ wget http://localhost:8000
```

### start springboots server in docker
```
~# ps aux | grep gradlew 
~# kill -9 [PID]
~# cd /apps/springboots && nano ./src/main/resources/application.properties
  ...
server.address=0.0.0.0
  ...
spring.datasource.url=jdbc:mysql://teams_java_jupyterlab_mysql_8_1:3306/AI_LKJ
  ...
remote.server.url=http://path-finder.shop:80/       
root.file.folder=/apps/fastapis/data/img   

/apps/springboots# chmod +x ./gradlew && nohup ./gradlew bootRun 
/apps/springboots# exit

outside_docker:~$ wget http://localhost:8080
```

### setup https certification and start nginx in GCP
<details>

<summary>sudo nano /etc/nginx/sites-available/default</summary>

    server {
        listen 80;
        server_name path-finder.store www.path-finder.store;
        #return 301 https://$server_name$request_uri; # Redirect all HTTP requests to HTTPS
        location / {
            proxy_pass http://localhost:8000; # Forward all requests to localhost:8000
            proxy_set_header Host $host; # Pass the current host and port
            proxy_set_header X-Real-IP $remote_addr; # Pass the client's real IP
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; # Pass the real user IP read by the proxy or load balancer
            proxy_set_header X-Forwarded-Proto $scheme; # The protocol being used (http or https)
        }
    }

    server {
        # SSL configuration
        listen 443 ssl;
        server_name path-finder.store www.path-finder.store;

        ssl_certificate /etc/letsencrypt/live/path-finder.store/fullchain.pem; # Certificate path
        ssl_certificate_key /etc/letsencrypt/live/path-finder.store/privkey.pem; # Key path

        ssl_session_cache shared:SSL:1m;
        ssl_session_timeout 10m;
        ssl_ciphers HIGH:!aNULL:!MD5;
        ssl_prefer_server_ciphers on;

        location / {
            proxy_pass http://localhost:8080; # Forward requests to the WAS running in Docker
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }

</details>

```
~$ sudo certbot --nginx -d path-finder.store.shop -d www.path-finder.store.shop
~$ sudo rm /etc/nginx/sites-available/default
~$ sudo nano /etc/nginx/sites-available/default
  ... 
~$ sudo nginx -t
~$ sudo systemctl restart nginx

@ https://path-finder.store/
@ https://www.path-finder.store/
@ http://www.path-finder.store:80/
@ http://path-finder.store:80/
