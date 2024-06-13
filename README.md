# LINEBOT

Docker for web handler in LineOA chat

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

This project implements a FastAPI-based web application integrated with the LINE Messaging API to create a LINE Bot that responds to text messages. Built in Python, it handles incoming messages from the LINE platform and sends appropriate responses.

## Project Structure

```bash
.
├── dockerfile
├── .env (your own)
├── main.py
└── requirement.txt
```

## Setup
- Python 3.9+
- Docker

### Installation
1. Clone the repository:
```bash
git clone https://github.com/tm-intern-zoon-patcharawiwatpong/LINBOT.git
cd LINBOT
```
2. Install dependencies:
```bash
pip install -r requirement.txt
```

## Environment Variables
Create a `.env` file in the root directory and add the following environment variables:
```makefile
CHANNEL_ACCESS_TOKEN=your_channel_access_token
CHANNEL_SECRET=your_channel_secret
```
Replace `your_channel_access_token` and `your_channel_secret` with your actual LINE Bot credentials.

## Usage
For basic usage just run the main file after dependencies installation
```bash
python main.py
```
or using from `uvicorn` lib
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
The defualt port is on `localhost:8000`. But I recommend using docker to run this
```bash
docker build -t msg-line-app .
docker run -p 8000:8000 --name msg-line-app msg-line-app
```
Which all are expose on `localhost:8000`

## Contributing
If you'd like to contribute to this project, please follow these guidelines:

Fork the repository
Create a new branch (`git checkout -b feature-branch`)
Make your changes
Commit your changes (`git commit -am 'Add new feature'`)
Push to the branch (`git push origin feature-branch`)
Create a new Pull Request
