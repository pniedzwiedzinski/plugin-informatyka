![meme](https://tr3.cbsistatic.com/hub/i/2017/03/23/ac406fbc-e3c1-4eba-9717-6854efd46c7f/cce53b95907bc6a657c0b5f6de78d757.jpg)

# Informatyka

Auto send files with mail. Just type <s>`informatyka`</s>, sorry a little more complex (use alias)

## Requirements

- Docker

## Install

```bash
$ docker pull pniedzwiedzinski/informatyka
```

## Setup

This script requires, that you have all your `.cpp` files in separate directory and should not contain much
of different files, i.e. desktop would be a bad idea, but separate folder on desktop will work well.

Config file - `config.json`

```js
{
  "sender_email": "your_email",

  "receiver_email": "target_email",

  "message_subject": "Subject",
  "message_body": "Nice",

  "re": ".cpp|.xlsx" // pattern for files
}
```

## Usage

### Init

It looks scary 😰, sorry. This two command hopefully differs only at first and last line.

```bash
$ docker run -it --rm \
    -v /path/to/folder:/app/informatyka \
    -v /path/to/config.json:/app/config.json \
    -v /path/to/some/folder/that/you/wont/remove/:/app/git \
    -v /path/to/.gitconfig:/root/.gitconfig \
    informatyka init

$ docker run -it \
    -v /path/to/folder:/app/informatyka \
    -v /path/to/config.json:/app/config.json \
    -v /path/to/some/folder/that/you/wont/remove/:/app/git \
    -v /path/to/.gitconfig:/root/.gitconfig \
    --name informatyka informatyka commit
```

- `/path/to/folder/` - path to folder with \* files
- `/path/to/config.json/` - path to config.json
- `/path/to/some/folder/that/you/wont/remove/` - git folder, if you don't know what git is: this folder is something like backup
- `/path/to/.gitconfig` - path to `.gitconfig` file, default is `~/.gitconfig`, if you don't have one create one with this content:

  ```
  [user]
      name = <your_name>
      mail = <your_mail>
  ```

#### My setup

```bash
-v ~/Documents/informatyka:/app/informatyka \
-v ~/.informatyka/config.json:/app/config.json \
-v ~/.informatyka/git/:/app/git \
-v ~/.gitconfig:/root/.gitconfig \


~
├── .informatyka
│   ├── config.json
│   ├── git # git-dir
├── Documents
│   ├── Informatyka # * files
```

### Daily usage

```bash
$ alias informatyka="docker start -i informatyka"
$ informatyka # You will be asked for your email password and GitHub credentials if you have origin set
```

### How it works

Script is running in docker container, so it is independent from operating system. You can run
linux commands like this `docker exec informatyka echo o`. This script recognize new files because it
actually uses Git. That means you can check new files with `docker exec informatyka git --git-dir="/app/git" status`.
`git-dir` option is used to move git files to another directory, that's why it's important not to delete
the third path.
