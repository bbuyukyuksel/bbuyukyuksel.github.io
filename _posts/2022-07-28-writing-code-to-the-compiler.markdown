---
layout: post
title: Writing code to the c++ compiler
date: 2022-07-28 00:00:00 +0300
description: C++ Templates
lang: en
img: software.jpg
tags: [C++, Templates, Compiler]
contents: 
- 1;Introduction;introduction'
- 1;Starting;starting'
- 2;Let's let the compiler write the code.;...'

---

# Introduction

This post aims to show how c++ compiler codes at run-time.

------------------------------------------------------------------------------

# Starting

Before we start the post, we need to talk about c++ templates. 

The C++ templates, the codes which is written at run-time by compiler. We can take advantage of some C++ usefull syntax knowladges as like function overloading, type-independent function or class definitions

# Some Code Tricks

## print function

Now, we will code a print function which prints all given arguments to standart output stream. When we code that function, we will use 2 seperate tecnique to implement this function.

### First one, subtraction technique:

```cpp
#include <iostream>

template<typename T>
void print(T x){
    std::cout << x << '\n';
}

template<typename T, typename ...Args>
void print(T x, Args ...args){
    std::cout << x << ", ";
    print(args...);
}
```

As seen above, we have implemented `subtraction technique` using `variadic` and `T` overloaded functions.

if we use print function as like below,

```cpp
print(5, 2.3, 4.7f, "hello world", 'c');
```

Compiler writes the code below,

```cpp
void print(int, double, float, const char*, char);
void print(double, float, const char*, char);
void print(float, const char*, char);
void print(const char*, char);
void print(char);
```

### Second one, using comma operator

Before we apply this technique, we need to mention comma operator. Comma operator gives us the guarantee which is processed arguments until last arguments.

```cpp
int x = 10, y = 20, z = 30;

(++x, ++y, z = x + y);
std::cout << z;          // x = 11, y = 21, z = 33
```

We can use the technique;

```cpp
#include <iostream>
template<typename ...Tpacks>
void print(Tpacks ...packs){
    int a[]{
        (std::cout << packs << ", ", 0)...
    };
}
```

or,

```cpp
#include <iostream>
#include <initializer_list>

template<typename ...Tpacks>
void print(Tpacks ...packs){
    (void)std::initializer_list<int>{
        (std::cout << packs << ", ", 0)...
    };
}
```

Now compiler writes code  for us as like below,

```cpp
void print(T1 p1, T2 p2, T3 p3){
    (void)std::initializer_list<int>{
        (std::cout << p1 << ", " ,0 ),
        (std::cout << p2 << ", " ,0 ),
        (std::cout << p3 << ", " ,0 ),
    };
}
```


