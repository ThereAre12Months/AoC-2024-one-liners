# Some bad one-liners for the problems of AoC 2024

I make heavy use of lambda's in some of these problems. For those who consider this cheating, I've also created `lambdaless.py` files, which do not contain any lambda functions.

## File structure

For every day and problem there is a folder called `d{day}p{problem}`. Every folder contains an `input.txt` file containing the input for that problem (every solution assumes that file is present in cwd), a `oneline.py` file, which contains the one-liner. Some problems also have a `lambdaless.py` file, this is for when the original solution makes to much use of lambda's.
```
root
├── d1p1  
│   ├── oneline.py  
│   └── input.txt  
├── d1p2  
│   ├── oneline.py  
│   ├── lambdaless.py  
│   └── input.txt  
├── d2p1  
│   ├── oneline.py  
│   ├── lambdaless.py  
│   └── input.txt   
├── d2p2  
│   ├── oneline.py  
│   └── input.txt 
├── d3p1  
│   ├── oneline.py  
│   ├── lambdaless.py  
│   └── input.txt   
├── d3p2  
│   ├── oneline.py  
│   └── input.txt 
└── README.md  
```

## Running the code
All the code has been verified with CPython 3.12.3 on Windows 11, but the code _should_ work on 3.8+ on any platform.