# 10 Steps to Writing Grammar in Steps With Lark


## 1. Start with the primatives first.

In our case that was essentially everything up to `_comp_op`.



```dart
!_comp_op: "<"|">"|"=="|">="|"<="|"<>"|"!="

num_list: "[" _sep{NUMBER, ","} "]"

?atom: NUMBER           -> number
     | "-" atom         -> neg
     | NAME             -> var
     | "(" complex_expr ")"
     | string
     | num_list

string : ESCAPED_STRING

IF: "if" 
ELSE: "else"


// Core functons
_sep{x, sep}: x (sep x)*



%ignore WS_INLINE
%ignore WS
%ignore _CPC

%import common.CNAME -> NAME
%import common.NUMBER
%import common.WS_INLINE
%import common.WS
%import common.NEWLINE -> _NL
%import common.CPP_COMMENT -> _CPC
%import common.ESCAPED_STRING

COMMENT: "#" /[^\n]/*
```


What are we seeing here? 

### Imports - They're at the bottom.

```dart
%ignore WS_INLINE
%ignore WS
%ignore _CPC

%import common.CNAME -> NAME
%import common.NUMBER
%import common.WS_INLINE
%import common.WS
%import common.NEWLINE -> _NL
%import common.CPP_COMMENT -> _CPC
%import common.ESCAPED_STRING

COMMENT: "#" /[^\n]/*
```
This is only default information telling us to remove whitespace between words, and import statements. Though the order of the graph is rather important. 

**It would seem as if the graph loads information from the bottom, but prioritizes from the parent.**

### Atoms - The absolute primatives

```dart
?atom: NUMBER           -> number
     | "-" atom         -> neg
     | NAME             -> var
     | "(" complex_expr ")"
     | string
     | num_list

string : ESCAPED_STRING

IF: "if" 
ELSE: "else"


// Core functons
_sep{x, sep}: x (sep x)*
```


### Logic - So Many Logic Bombs

