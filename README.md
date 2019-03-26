![meme](https://tr3.cbsistatic.com/hub/i/2017/03/23/ac406fbc-e3c1-4eba-9717-6854efd46c7f/cce53b95907bc6a657c0b5f6de78d757.jpg)

# Informatyka

Auto upload of `.cpp` files. Just type <s>`informatyka`</s>, sorry a little more complex (use alias):

```
docker run -it -v /path/to/folder:/app/informatyka -v /path/for/config.py:/app/config.py -v /path/to/some/folder/that/you/won't/remove/:/app/git --name informatyka informatyka
```

and let the magic happen.

## Requirements

- Docker
- Docker Compose

## Install

```bash
$ docker pull pniedzwiedzinski/informatyka
```

## Setup

This script requires, that you have all your `.cpp` files in seperate directory and should not contain much of different files, i.e. desktop would be a bad idea, but seperate folder on desktop will work well.

## Usage

```bash
$ alias informatyka="docker run -it -v /path/to/folder:/app/informatyka -v /path/for/config.py:/app/config.py -v /path/to/some/folder/that/you/won't/remove/:/app/git --name informatyka informatyka"
$ informatyka
```

### How it works

Script is running in docker container, so it is independent from operating system. You can run
linux commands like this `informatyka echo o`. This script recognize new files because it
actually uses Git. That means you can check new files with `informatyka git status`.
