FROM python:3.9-slim
WORKDIR /app
COPY . /app
COPY . /app

RUN apt-get update && apt-get install -y \
    wget \
    ca-certificates \
    fonts-liberation \
    libappindicator3-1 \
    libnss3 \
    libxss1 \
    libxtst6 \
    xdg-utils \
    libasound2 \
    curl \
    gnupg2 \
    lsb-release \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs

RUN npx playwright install-deps

RUN pip install --no-cache-dir playwright pytest

RUN python -m playwright install


RUN pip install -r requirements.txt

CMD ["pytest"]