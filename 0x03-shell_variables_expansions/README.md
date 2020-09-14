# Shell, init files, variables and expansions

- **printenv**: list names and values of all environment variables or, with VARIABLE, the value of the environment variable name. printenv [option]... [variable]...
- **set**: change the value of a shell option and set the positional parameters, or display the names and values of shell variables. set [--abefhkmnptuvxBCEHPT] [-o options-name] [argument ...] OR set [+abefhkmnptuvxBCEHPT] [+o option-name] [argument ...]
- **unset**: remove variable or function names unset [-fv] [name]
- **export**: set an environmental variable. The supplied names are marked for automatic export to the environment of subsequently executed commands. export [-fn] [name[=value]] export -p
- **alias**: create an alias, aliases allow a string to be substituted for a word when it is used as the first word of a simple command. alias [-p] [name[=value] ...] unalias [-a] [name ...]
- **unalias**: remove an alias, see above.
- **.**: source or dot operator see below
- **source**: read and execute commands from the filename argument in the current shell context. .filename [arguments] source filename [arguments]
- **printf**: format and print data. Write formatted arguments to the standard output under the control of the format. printf format [argument]... printf--help printf --version