tmux
----

tmux may be controlled from an attached client by using a key combination of a prefix key, ‘C-b’ (Ctrl-b) by default, followed by a command key.

Session
```````

| tmux attach || tmux new — attach to the session, if no session found create a new one
| <prefix-key> d — detach

Windows
```````

| <prefix-key> c — create window
| <prefix-key> 0...9 — jump to window
| <prefix-key> p — jump to previous window
| <prefix-key> n — jump to next window
| <prefix-key> l — jump to next active window (from that one you switched to current)
| <prefix-key> & — close window (or just type exit in terminal)
| <prefix-key> , - change window name

Panels
``````

| <prefix-key> % — split current panel in vertical direction
| <prefix-key> " — split current panel across
| <prefix-key> →←↑↓ — move focus between the panels
| <prefix-key>(hold) →←↑↓ — change size of the current panel
| <prefix-key> x — close panel (or just type exit in terminal)
| <prefix-key> z — toggle zoom current panel

Scroll mode
```````````

| <prefix-key> [ — entering to scroll mode
| →←↑↓ — navigate
| q - leave scroll mode
