FROM python:3.11

# install any packages
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk fonts-nanum wget unzip

# setup JAVA_HOME configuration
ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64

# Install Chrome and related dependencies
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | tee /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
    
# setup fastapi
WORKDIR /apps

ARG APP_DIR_NAME_FASTAPI

# Clone the Git repository. Here we dynamically specify the repository name using the variable defined earlier.
RUN git clone -b main https://github.com/nohjuhyeon/AI_LKJ_hubs_fastapi ${APP_DIR_NAME_FASTAPI}

# Changes the working directory to /apps/${REPO_NAME}. This uses the variable to dynamically set the directory path.
WORKDIR /apps/${APP_DIR_NAME_FASTAPI}

RUN pip install --no-cache-dir -r ./requirements.txt

# RUN rm -rf .git

# setup springboots
WORKDIR /apps

ARG APP_DIR_NAME_SPRINGBOOT

# Clone the Git repository. Here we dynamically specify the repository name using the variable defined earlier.
RUN git clone -b main https://github.com/nohjuhyeon/AI_LKJ_hubs_spring ${APP_DIR_NAME_SPRINGBOOT}

# Changes the working directory to /app/${REPO_NAME}. This uses the variable to dynamically set the directory path.
WORKDIR /apps/${APP_DIR_NAME_SPRINGBOOT}

# RUN rm -rf .git