The original code use python instead of python3, causing something annoying.  
Since I don not use python2, I just modify python to python3, not caring python2 projects

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
```

## Usage

To invoke you need to call `:ToggleBool`. You can map accordingly.
For example, to map to `<leader>r` you need to add following to your *.vimrc*

    noremap <leader>r :ToggleBool<CR>

## Todo

1. When word is replaced with the toggled value, it eats leading and trailing
   spaces.
2. Support more for more values and logical operators.
