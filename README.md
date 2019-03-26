<img src="https://cdn.rawgit.com/oh-my-fish/oh-my-fish/e4f1c2e0219a17e2c748b824004c8d0b38055c16/docs/logo.svg" align="left" width="144px" height="144px"/>

#### informatyka

> Auto upload of files from computer science lesson.

[![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat-square)](/LICENSE)
[![Fish Shell Version](https://img.shields.io/badge/fish-v2.2.0-007EC7.svg?style=flat-square)](https://fishshell.com)
[![Oh My Fish Framework](https://img.shields.io/badge/Oh%20My%20Fish-Framework-007EC7.svg?style=flat-square)](https://www.github.com/oh-my-fish/oh-my-fish)

<br/>

## Requirements

- git
- pipenv
- keyring

```fish
$ pip3 install keyring pipenv

# For macOS
$ brew install pipenv
```

## Install and setup

```fish
$ omf install https://github.com/pniedzwiedzinski/plugin-informatyka
```

### Set your password in keyring

```fish
$ keyring set system <YOUR_MAIL> <PASSWORD>
```

### Setup config file

Fill config file `~/.informatyka/config.py`

## Usage

```fish
$ informatyka
```

# License

[MIT][mit] © [Patryk Niedźwiedziński][author] et [al][contributors]

[mit]: https://opensource.org/licenses/MIT
[author]: https://github.com/pniedzwiedzinski
[contributors]: https://github.com/pniedzwiedzinski/plugin-informatyka/graphs/contributors
[omf-link]: https://www.github.com/oh-my-fish/oh-my-fish
[license-badge]: https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat-square
