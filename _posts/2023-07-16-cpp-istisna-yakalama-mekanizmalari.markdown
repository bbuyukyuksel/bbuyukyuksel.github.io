---
layout: post
title: C++ İstisna Yakalama Mekanizmaları
date: 2023-07-19 00:15:00 +0200
description: C++ istisna yakalama mekanizmalarının ele alınıp örneklerle incelenmesi
lang: tr
img: post_images/exception-handling.png
tags: ['C++ exception handling', 'try-catch blokları', 'throw ifadesi', 'catch(...) bloğu', 'std::exception sınıfı', 'static_assert', 'assert', 'function try-catch', 'constructor initializer list', 'hata kontrol mekanizmaları', 'derleme zamanı hata kontrolü', 'çalışma zamanı hata kontrolü', 'istisnalar', 'exception türleri', 'hata durumu ele alma', 'temel istisna sınıfı', 'hata mesajları', 'hata raporlama', 'hata ayıklama', 'güvenli kodlama', 'program hataları', 'hata yönetimi'] 
contents:
- 'Giriş;giriş'
- 'C++ Exception Handling ve Hata Kontrol Mekanizmaları;c-exception-handling-ve-hata-kontrol-mekanizmaları'
- 'C++ Exception Handling Mekanizmaları;c-exception-handling-mekanizmaları'
- 'try-catch Blokları;try-catch-blokları'
- 'throw İfadesi;throw-i̇fadesi'
- 'catch(…) Bloğu;catch-bloğu'
- 'std::exception Sınıfı;stdexception-sınıfı'
- 'Derleme Zamanı Hata Kontrolü;derleme-zamanı-hata-kontrolü'
- 'static_assert;static_assert'
- 'Çalışma Zamanı Hata Kontrolü;çalışma-zamanı-hata-kontrolü'
- 'assert;assert'
- 'Kullanım Alanları;kullanım-alanları'
- 'try-catch Blokları;try-catch-blokları-1'
- 'Function try-catch;function-try-catch'
- 'Constructor Initializer List’te Exception Yakalama;constructor-initializer-listte-exception-yakalama'
- 'Özet;özet'

---

# Giriş

Bu yazıda, C++ exception handling mekanizmaları, `static_assert`, `assert`, try-catch kullanım alanları, function try-catch, constructor initializer list'te exception yakalama konularında örneklerle dolu bir içerik hazırlamaya çalıştım.

# C++ Exception Handling ve Hata Kontrol Mekanizmaları

C++ programlamada, hata durumlarını ele almak ve programın düzgün çalışmasını sağlamak için bir dizi mekanizma bulunmaktadır. Bu mekanizmalar, programın derleme zamanında (compile-time) veya çalışma zamanında (runtime) hataları tespit etmek, işlemek ve gerekli aksiyonları almak için kullanılır. Bu yazıda, C++ exception handling mekanizmalarını ve diğer hata kontrol yöntemlerini detaylı bir şekilde inceleyeceğiz.

## C++ Exception Handling Mekanizmaları

### try-catch Blokları

C++ exception handling, `try-catch` bloklarıyla sağlanır. `try` bloğu içinde potansiyel bir hata meydana gelebilecek kod parçacığı yer alır. Eğer bir hata meydana gelirse, `catch` bloğu içerisindeki kod çalışır. `catch` bloğu, fırlatılan exception (istisna) türüne göre eşleşme yapar ve ilgili işlemleri gerçekleştirir.

```cpp
try {
    // Hata meydana gelebilecek kod parçacığı
} catch (ExceptionType1 e) {
    // ExceptionType1 tipindeki hata durumunda çalışacak kod parçacığı
} catch (ExceptionType2 e) {
    // ExceptionType2 tipindeki hata durumunda çalışacak kod parçacığı
} catch (...) {
    // Diğer tüm hata durumlarında çalışacak kod parçacığı
}
```

`try` bloğu içindeki kod parçacığı hata fırlattığında, `catch` blokları sırasıyla kontrol edilir ve eşleşen `catch` bloğu çalıştırılır. Eğer hiçbir `catch` bloğu eşleşmezse, programın çalışması durdurulur ve hata mesajı gösterilir.

### throw İfadesi

Hata durumunu belirlemek ve istisna fırlatmak için `throw` ifadesi kullanılır. İstisna fırlatıldığında, program akışı ilgili `catch` bloğuna geçer.

```cpp
throw ExceptionType(argument);
```

`throw` ifadesi, belirli bir istisna türü ve gerekli argümanlarla kullanılır. Fırlatılan istisna, uygun `catch` bloğu tarafından yakalanana kadar programın yukarı doğru yığın (stack) yapısını izler.

### catch(...) Bloğu

`catch(...)` bloğu, herhangi bir türdeki exception'ları yakalamak için kullanılır. Ancak, bu blokta yakalanan exception'lar hakkında spesifik bilgilere erişmek mümkün değildir. Bu tür bir catch bloğu, genellikle beklenmeyen hata durumlarını ele almak için kullanılır.

```cpp
try {
    // Hata meydana gelebilecek kod parçacığı
} catch (...) {
    // Herhangi bir türdeki exception durumunda çalışacak kod parçacığı
}
```

### std::exception Sınıfı

`std::exception` sınıfı, C++ standart kütüphanesinde yer alan bir temel istisna sınıfıdır. Diğer istisna sınıfları, bu sınıftan türetilir ve genellikle hata durumuyla ilgili bilgileri tutmak için kullanılır. `std::exception` sınıfı, `what()` adında bir işlev sağlar ve bu işlev türetilen sınıflar tarafından aşırı yüklenir.

```cpp
#include <exception>

class MyException : public std::exception {
public:
    const char* what() const noexcept {
        return "Bu bir özel istisnadır.";
    }
};
```

## Derleme Zamanı Hata Kontrolü

### static_assert

`static_assert`, C++11 standardıyla birlikte tanıtılan bir derleme zamanı (compile-time) kontrol mekanizmasıdır. Bu mekanizma, belirli bir koşulun derleme aşamasında doğru olup olmadığını kontrol etmek için kullanılır. Eğer koşul doğruysa, derleme işlemi normal şekilde devam eder. Ancak koşul yanlışsa, derleyici derleme hatası verir ve programın derlenmesini engeller.

```cpp
static_assert(sizeof(int) == 4, "int tipinin boyutu 4 byte olmalı!");
```

`static_assert` ifadesi, koşulun doğru olmasını bekler. Eğer koşul yanlışsa, derleyici hatayı rapor eder ve belirtilen mesajı gösterir. Bu mekanizma, derleme sürecinde belirli koşulların doğruluğunu kontrol etmek için kullanışlıdır.

## Çalışma Zamanı Hata Kontrolü

### assert

`assert`, C++ programlarında hata durumlarını kontrol etmek için kullanılan bir çalışma zamanı (runtime) kontrol mekanizmasıdır. `assert` ifadesi, bir koşulun doğru olup olmadığını kontrol eder. Eğer koşul doğruysa, programın çalışması normal şekilde devam eder. Ancak koşul yanlışsa, bir `assertion failure` (doğrulama hatası) oluşur ve program çalışması durdurulur.

```cpp
#include <cassert>

int main() {
    int x = 5;
    int y = 10;

    assert(x == y); // x ve y eşit değilse, program burada durur.

    return 0;
}
```

`assert` ifadesi, programcının belirli bir koşulun her zaman doğru olmasını beklediği yerlerde kullanılır. Eğer

 koşul yanlışsa, `assert` ifadesi hata mesajıyla birlikte programın çalışmasını durdurur. Bu mekanizma, programın doğru bir şekilde çalıştığından emin olmak için hata kontrolü yaparken kullanılır.

## Kullanım Alanları

### try-catch Blokları

`try-catch` blokları, hata durumlarını ele almanın en yaygın yoludur. Aşağıdaki durumlarda kullanılırlar:

- Bir fonksiyonun içindeki belirli bir kod parçacığının çalışması sırasında oluşabilecek hataları ele almak için `try-catch` blokları kullanılır. Örneğin, dosya okuma veya yazma işlemleri sırasında meydana gelebilecek hataları ele alabiliriz.

- Bir sınıfın constructor veya destructor fonksiyonları içinde hata durumlarını kontrol etmek için `try-catch` blokları kullanılabilir. Özellikle, sınıfın veri elemanlarının başlatılması veya temizlenmesi sırasında hataların ele alınması önemlidir.

- Template fonksiyonlarında `try-catch` blokları kullanılarak hata durumları ele alınabilir. Örneğin, bir template fonksiyonun içinde çalışan algoritmanın hata durumlarını ele almak için `try-catch` blokları kullanabiliriz.

### Function try-catch

Function try-catch, fonksiyonlara veya bir sınıfın üye fonksiyonlarına uygulanan bir `try-catch` mekanizmasıdır. Bu yapı, sınıfın constructor veya destructor fonksiyonları içinde kullanılır. İlgili fonksiyonun başarısız olması durumunda `catch` bloğu içindeki işlemler gerçekleştirilir. Örneğin:

```cpp
class MyClass {
public:
    MyClass() try {
        // Hata meydana gelebilecek kod parçacığı
    } catch (ExceptionType e) {
        // Hata durumunda çalışacak kod parçacığı
    }

    ~MyClass() try {
        // Hata meydana gelebilecek kod parçacığı
    } catch (ExceptionType e) {
        // Hata durumunda çalışacak kod parçacığı
    }
};
```

Bu yapı, sınıfın constructor veya destructor fonksiyonlarında hata durumlarına karşı korunmayı sağlar.

Function-Try bloğu normal fonksiyonlar içinde kullanılabilir, örneğin:

```cpp
int f(int n = 2) try
{
    ++n; // increments the function parameter
    throw n;
}
catch(...)
{
    ++n; // n is in scope and still refers to the function parameter
    assert(n == 4);
    return n;
}
```
Yukarıdaki örnekte de görüldüğü gibi, `"n"` nesnesinin kapsam alanı genişletilmiş ve catch bloğundan da erişilebilir haldedir.

### Constructor Initializer List'te Exception Yakalama

Constructor initializer list'te exception yakalamak için ilgili veri elemanlarını başlatan ifadeler içinde `try-catch` blokları kullanılır. Bu şekilde, her bir veri elemanı başlatma ifadesi için ayrı ayrı `try-catch` blokları kullanarak hata durumlarını ele alabilirsiniz. Örneğin:

```cpp
class MyClass {
public:
    MyClass() 
		try : member1(), member2() {
    	// member1 veya member2'nin başlatılması sırasında hata meydana gelebilecek kod parçacığı
    }
		catch(const std::exception & e)
		{
			std::cout << e.what() << '\n';
		}
    
private:
    int member1;
    int member2;
};
```

Bu yapı, sınıfın veri elemanlarının başlatılması sırasında meydana gelebilecek hataları ele almak için kullanılır.

## Özet

Bu yazıda, C++ exception handling mekanizmalarını ve hata kontrol yöntemlerini ayrıntılı bir şekilde inceledik. `try-catch` blokları, `throw` ifadesi, `catch(...)` blokları ve `std::exception` sınıfı gibi mekanizmalar, hata durumlarını tespit etmek ve uygun işlemleri gerçekleştirmek için kullanılır. Ayrıca, `static_assert` ve `assert` gibi derleme ve çalışma zamanı hata kontrol mekanizmaları da programın doğru çalışmasını sağlamak için kullanılır.

Hata durumlarını doğru bir şekilde ele almak ve programın güvenliğini ve hatasız çalışmasını sağlamak önemlidir. Bu mekanizmaları kullanarak C++ programlarında hata durumlarını kontrol edebilir, uygun işlemleri gerçekleştirebilir ve hatasız bir kod tabanı oluşturabilirsiniz.

Umarım bu yazı, C++ exception handling ve hata kontrol mekanizmaları hakkında daha detaylı bir anlayış sağlamıştır..
