# app/Dockerfile

FROM python:3.10-slim

WORKDIR /deploy

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    pandoc \
    && rm -rf /var/lib/apt/lists/*

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list &&\
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Always clone
ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" random
RUN rm -rf random
# Do not use a credential manager. Force ai_web user.
RUN git -c credential.helper="" clone https://github.com/UABPeriopAI/IRB_Assistant.git .
RUN git config --local credential.helper ""

RUN pip3 install -r requirements.txt
RUN pip3 install --user pip setuptools wheel
RUN pip3 install --user -e .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["./startup.sh"]



