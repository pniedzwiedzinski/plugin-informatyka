![meme](https://tr3.cbsistatic.com/hub/i/2017/03/23/ac406fbc-e3c1-4eba-9717-6854efd46c7f/cce53b95907bc6a657c0b5f6de78d757.jpg)

# Informatyka

Auto upload of `.cpp` files. Just type <s>`informatyka`</s>, sorry a little more complex (use alias)

## Requirements

- Docker
- Docker Compose

## Install

```bash
$ docker pull pniedzwiedzinski/informatyka
```

## Setup

This script requires, that you have all your `.cpp` files in separate directory and should not contain much
of different files, i.e. desktop would be a bad idea, but separate folder on desktop will work well.

Config file - `config.py`

```
sender_email = "your_email"

receiver_email = "target_email"

message_subject = "Subject"
message_body = "Nice"
```

## Usage

### Init

```bash
$ docker run -it -d -v /path/to/folder:/app/informatyka -v /path/to/config.py:/app/config.py -v /path/to/some/folder/that/you/wont/remove/:/app/git --name informatyka informatyka sh
$ docker exec informatyka init
```
- `/path/to/folder/` - path to folder with cpp files
- `/path/to/config.py/` - path to config.py
- `/path/to/some/folder/that/you/wont/remove/` - git folder, if you don't know what git is: this folder is something like backup

#### My setup

```bash
~
├── .informatyka
│   ├── config.py
│   ├── git # git-dir
├── Documents
│   ├── Informatyka # *.cpp files
```

### Daily usage

```bash
$ alias informatyka="docker start informatyka && docker exec -it informatyka commit && docker stop informatyka"
$ informatyka # You will be asked for your email password
```

### How it works

Script is running in docker container, so it is independent from operating system. You can run
linux commands like this `docker exec informatyka echo o`. This script recognize new files because it
actually uses Git. That means you can check new files with `docker exec informatyka git --git-dir="/app/git" status`.
`git-dir` option is used to move git files to another directory, that's why it's important not to delete
the third path.
