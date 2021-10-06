# toggle-bool

Vim plugin to toggle boolean values.


## List of boolean values supported

- true <-> false 
- yes <-> no 
- on <-> off
- 0 <-> 1


## Installation

Use your plugin manager of choice.

- [vim-plug](https://github.com/junegunn/vim-plug)
  - Add `Plug 'https://github.com/sagarrakshe/toggle-bool'` to .vimrc
  - Run `:PlugInstall`


put this to your .vimrc
```
let g:python3_host_prog = "F:\\python3.9\\python.exe"  " Your own path. ToggleBool needs this
let g:python_host_prog = "F:\\python3.9\\python.exe"   " ToggleBool needs this
```

## Usage

To invoke you need to call `:ToggleBool`. You can map accordingly.
For example, to map to `<leader>r` you need to add following to your *.vimrc*

    noremap <leader>r :ToggleBool<CR>

## Todo

1. When word is replaced with the toggled value, it eats leading and trailing
   spaces.
2. Support more for more values and logical operators.
