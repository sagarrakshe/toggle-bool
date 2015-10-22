" --------------------------------
" Add our plugin to the path
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

" --------------------------------
"  Function(s)
" --------------------------------
function! TemplateExample()
python << endOfPython

from toggle_bool import toggle_bool_value

# get word under cursor
wordUnderCursor = vim.eval('expand("<cword>")')

if len(wordUnderCursor):
  # get the toggle value of word under cursor
  toggleValue = toggle_bool_value(wordUnderCursor)

  # replace the current word with new toggled value
  vim.command('normal viwc%s' % toggleValue)
  vim.command('normal b')

endOfPython
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! ToggleBool call TemplateExample()

" key mapping
noremap <leader>r :ToggleBool<CR>
