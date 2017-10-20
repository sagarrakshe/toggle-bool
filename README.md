# toggle-bool

Vim plugin to toggle boolean values.


## List of boolean values supported

- true <-> false 
- yes <-> no 
- on <-> off
- 0 <-> 1
- enable(d) <-> disable(d)


## Installation

Use your plugin manager of choice.

- [Pathogen](https://github.com/tpope/vim-pathogen)
  - `git clone https://github.com/sagarrakshe/toggle-bool ~/.vim/bundle/toggle-bool`
- [Vundle](https://github.com/gmarik/vundle)
  - Add `Bundle 'https://github.com/sagarrakshe/toggle-bool'` to .vimrc
  - Run `:BundleInstall`
- [NeoBundle](https://github.com/Shougo/neobundle.vim)
  - Add `NeoBundle 'https://github.com/sagarrakshe/toggle-bool'` to .vimrc
  - Run `:NeoBundleInstall`
- [vim-plug](https://github.com/junegunn/vim-plug)
  - Add `Plug 'https://github.com/sagarrakshe/toggle-bool'` to .vimrc
  - Run `:PlugInstall`


## Usage

By default the key mapping is `<leader>r`. When cursor is on the word which you
want to toggle, press `<leader>r` or you can call `:ToggleBool`.


## Todo

1. When word is replaced with the toggled value, it eats leading and trailing
   spaces.
2. Support more for more values and logical operators.
