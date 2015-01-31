Movements
---------

| ``h j i k`` - left, down, up, right

| ``w`` (or ``W``) - word forward (to the head)
| ``b`` (or ``B``) - word backward (to the head)
| ``e`` (or ``E``) - word forward (to the tail)
| ``ge`` - word backward (to the tail)
| ``x`` - deletes a char

| ``f symbol`` - move cursor on the symbol (; repeats the search)
| ``t symbol`` - move cursor before the symbol

| ``0`` - beginning of the line
| ``$`` - end of the line

| ``Ctrl-F`` / ``Ctrl-B`` - page up / page down
| ``Ctrl-U`` / ``Ctrl-D`` - half page up / half page down
| ``H`` / ``M`` / ``L`` - head / middle / last line of the screen
| ``gg`` / ``G`` - top / bottom of the file
| ``number G`` - go to line number (:number is the same)


Tabs
----
| ``gt`` - :tabnext
| ``gT`` - :tabprevious


Search
------

| ``* on a word`` makes it a search criteria (like /something)
| ``# on a word`` makes it a search criteria in backward direction (like ?something)
| ``g*`` makes the same without boundaries
| ``n`` / ``N`` - move down / up through the searches

| ``[[`` / ``]]`` - move to previous / next curly brace (class definition in Python)


Insertion
---------

| ``i`` - start insert mode at cursor
| ``I`` - insert at the beginning of the line
| ``a`` - append after the cursor
| ``A`` - append at the end of the line


Tags
----
| ``Ctrl-]`` - go to function/method/class definition
| ``Ctrl-T`` - jump to older entry in the tag stack
