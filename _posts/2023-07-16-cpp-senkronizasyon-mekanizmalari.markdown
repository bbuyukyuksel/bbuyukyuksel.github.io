---
layout: post
title: C++ Senkronizasyon Mekanizmaları
date: 2023-07-16 17:44:00 +0200
description: C++ senkronizasyon mekanizmalarının ele alınıp örneklerle incelenmesi
lang: tr
img: post_image_thread.png
tags: ['C++', 'threading', 'multiprocessing', 'senkronizasyon mekanizmaları', 'mutex', 'lock_guard', 'unique_lock', 'condition_variable', 'semafor', 'binary semaphore', 'counting semaphore', 'recursive semaphore', 'deadlock', 'starvation', 'livelock', 'async fonksiyonlar', 'std::future']
contents:
- 'Giriş;giriş'
- 'İçindekiler;i̇çindekiler'
- 'Senkronizasyon Mekanizmaları Hakkında Özet;senkronizasyon-mekanizmaları-hakkında-özet'
- '1. Mutex;1-mutex'
- '2. Recursive Mutex;2-recursive-mutex'
- '2.1. Mutex vs Recursive Mutex;21-mutex-vs-recursive-mutex'
- '3. Lock Guard;3-lock-guard'
- '4. Unique Lock;4-unique-lock'
- '4.1. Unique Lock ve Lock Guard Karşılaştırması;41-unique-lock-ve-lock-guard-karşılaştırması'
- '5. Condition Variable;5-condition-variable'
- '5.1. Timed Condition Variable;51-timed-condition-variable'
- '6. Atomic;6-atomic'
- '6.1. Memory Order Acquire Nedir?;61-memory-order-acquire-nedir'
- '7. Atomic Flag;7-atomic-flag'
- '8. Extra;8-extra'
- '8.1. Thread Local;81-thread-local'
- '8.2. Semaphore;82-semaphore'
- '8.2.1. Binary Semaphore;821-binary-semaphore'
- '8.2.2. Counting Semaphore;822-counting-semaphore'
- '8.2.3. Recursive Semaphore (Yeniden Girişimli Semaphore);823-recursive-semaphore-yeniden-girişimli-semaphore'
- '8.2.4. Timed Semaphore (Zaman Aşımı Olan Semaphore);824-timed-semaphore-zaman-aşımı-olan-semaphore'
- '8.3. Spin Lock;83-spin-lock'
- '8.4. Deadlock, Starvation, Livelock;84-deadlock-starvation-livelock'
- '8.4.1. Deadlock;841-deadlock'
- '8.4.2. Starvation;842-starvation'
- '8.4.2.1. std::this_thread_yield();8421-stdthis_thread_yield'
- '8.4.2.2. Starvation’ı Önlemek için Basit Bir Yaklaşım;8422-starvationı-önlemek-için-basit-bir-yaklaşım'
- '8.4.3. Livelock;843-livelock'
- '8.4.3.1. std::defer_lock;8431-stddefer_lock'
- '8.4.3.2. std::adopt_lock;8432-stdadopt_lock'
- '8.4.3.3. std::scoped_lock;8433-stdscoped_lock'
- '8.7. Async Fonksiyon ve std::future;87-async-fonksiyon-ve-stdfuture'
- '8.6. İmplementasyonlar;86-i̇mplementasyonlar'
- '8.6.1. Thread Pool;861-thread-pool'
- '8.6.2. Consumer-Producer;862-consumer-producer'
- '8.6.2.1. Basit İmplementasyon;8621-basit-i̇mplementasyon'
- '8.6.2.2. Semaphore Kullanımı ile;8622-semaphore-kullanımı-ile'
- '8.6.3 Round Robin Algoritması;863-round-robin-algoritması'
- '8.6.3.1. Basit İmplementasyon;8631-basit-i̇mplementasyon'
- '8.6.3.2. Consumer-Producer Implemantasyonu;8632-consumer-producer-implemantasyonu'

---

# Giriş

Bu yazıda C++ konusunda threading, senkronizasyon mekanizmaları, semaforlar ve async fonksiyonlar gibi konuları ele aldım. Senkronizasyon mekanizmaları arasında mutex, lock_guard, unique_lock ve condition_variable gibi yapıları öğreneceğiz. Aynı zamanda semafor türlerini ve senkronizasyon problemlerini de ele alacağız. Ayrıca, async fonksiyonları ve std::future kütüphanesini kullanarak asenkron işlemleri yönetmeyi öğreneceğiz.

Bu yazı, C++ dilinde çoklu iş parçacıklı ve paralel programlamaya giriş niteliğindedir. Bu konuların anlaşılması, performansı artırmak ve verimli kod yazmak için önemlidir.
___

# İçindekiler

- Senkronizasyon Mekanizmaları Hakkında Özet
1. Mutex
2. Recursive Mutex
	1. Mutex vs Recursive Mutex
3. Lock Guard
4. Unique Lock
	1. Unique Lock ve Lock Guard Karşılaştırması
5. Condition Variable
	1. Timed Condition Variable
6. Atomic
	1. Memory Order Acquire Nedir?
7. Atomic Flag
8. Extra
	1. Thread Local
	2. Semaphore
		1. Binary Semaphore (İkili Semaphore)
		2. Counting Semaphore (Sayım Semaphore)
		3. Recursive Semaphore (Yeniden Girişimli Semaphore)
		4. Timed Semaphore (Zaman Aşımı Olan Semaphore)
	3. Spin Lock
	4. Deadlock, Starvation, Livelock
		1. Deadlock
		2. Starvation
			1. `std::this_thread_yield()`
			2. Starvation'ı Önlemek için Basit Bir Yaklaşım
		3. Livelock
			1. Defer Lock
			2. Adopt Lock
			3. Scoped Lock
	5. Async Fonksiyon ve `std::future`
	6. İmplementasyonlar
		1. Thread Pool
		2. Consumer-Producer
		3. Round Robin
			1. Basit İmplementasyon
			2. Consumer-Prodocer Implementasyonu
___

# Senkronizasyon Mekanizmaları Hakkında Özet

C++ dilindeki senkronizasyon mekanizmaları, farklı senaryolara göre çeşitlilik gösterir. İşte C++'ta kullanılan bazı temel senkronizasyon mekanizmaları:

1. `std::mutex`: `std::mutex` (mutex) bir kilit mekanizmasıdır ve paylaşılan bir kaynağa eşzamanlı erişimi kontrol etmek için kullanılır. İş parçacıklarının bir `std::mutex` kilidini almasına izin verilirken, diğer iş parçacıklarının aynı kilit üzerinde çalışmasını engeller.

2. `std::recursive_mutex`: `std::recursive_mutex` (yeniden girişimli mutex), bir `std::mutex` gibi çalışır, ancak aynı iş parçacığı tarafından birden fazla kez kilitleme yapılmasına izin verir. Yeniden girişimli mutex, aynı iş parçacığı içinde fonksiyon çağrıları veya özyinelemeli işlemler gibi durumlarda kullanışlı olabilir.

3. `std::lock_guard`: `std::lock_guard` bir kilit tutucu sınıftır ve otomatik kilit açma ve kilitleme sağlar. `std::lock_guard` nesnesi, oluşturulduğunda bir `std::mutex`'i kilitleyerek, nesnenin kapsamından çıkıldığında otomatik olarak kilidi açar.

4. `std::unique_lock`: `std::unique_lock`, `std::lock_guard` gibi bir kilit tutucu sınıftır, ancak daha fazla esneklik sağlar. `std::unique_lock`, farklı kilitleme stratejilerini destekler ve kilidin manuel olarak açılıp kapatılmasına izin verir.

5. `std::condition_variable`: `std::condition_variable`, iş parçacıklarının bir olayın gerçekleşmesini beklemesini ve bildirmesini sağlayan bir senkronizasyon mekanizmasıdır. İş parçacıkları, bir koşulu kontrol eder ve o koşulun gerçekleşmesini beklerken `std::condition_variable`'ın `wait` işlevini kullanır. Diğer iş parçacıkları, koşulu sağlayan bir olayın gerçekleştiğini bildirirken `notify_one` veya `notify_all` işlevlerini kullanır.

6. `std::atomic`: `std::atomic` veri türleri, belirli bir bellek konumunda eşzamanlı erişimi sağlamak için kullanılır. Bu türler, belirli bir operasyonu atomik olarak gerçekleştirir ve senkronizasyon mekanizmaları olmadan iş parçacıkları arasında güvenli bir şekilde değiş tokuş yapmayı sağlar.

7. `std::atomic_flag`: `std::atomic_flag`, bir bayrak türüdür ve sadece iki durumu (set ve clear) olan basit bir senkronizasyon mekanizması sağlar. `std::atomic_flag`'ın `test_and_set` veya `clear` işlevleri kullanılarak bayrağın durumu değiştirilir.
    

Bu, C++ dilinde kullanılan bazı temel senkronizasyon mekanizmalarının bir özeti idi. Her senaryo farklı gereksinimler gerektirebilir, bu nedenle doğru senkronizasyon mekanizmasını seçmek önemlidir. C++ standart kütüphanesi bu mekanizmaları sağlar ve bu mekanizmaların kullanımı, paralel programlama ve eşzamanlılık konularında daha fazla bilgi ve anlayış gerektirebilir.
___

# 1. Mutex

C++ programlamasında senkronizasyonu sağlamak için kullanılan bir senkronizasyon mekanizmasıdır. Mutex, bir kilit (lock) olarak da adlandırılır ve paylaşılan bir kaynağa aynı anda sadece bir iş parçacığının erişmesine izin verir. Bu şekilde, senkronizasyon eksikliği nedeniyle kaynakların tutarlılığına veya güvenliğine yönelik sorunlar önlenir.

Mutex'ler, iki temel işlemi destekler:

1. Kilitleme (Locking): Bir iş parçacığı, kaynağa erişmek istediğinde mutex'i kilitleyerek diğer iş parçacıklarının aynı kaynağa erişmesini engeller. Diğer bir deyişle, mutex'i kilitleyen iş parçacığı, kaynağı geçici olarak kendine tahsis eder.
    
2. Kilidi Açma (Unlocking): İş parçacığı, kaynağı kullanımını tamamladıktan sonra mutex'in kilidini açarak diğer iş parçacıklarının kaynağa erişimine izin verir.

C++ dilinde, `std::mutex` sınıfı C++ standart kütüphanesinde mutex'i temsil eder. İşte bir örnek:

```cpp
#include <iostream>
#include <mutex>
#include <thread>

std::mutex mtx;  // Mutex nesnesi

void WorkerThread() {
    mtx.lock();  // Mutex'i kilitle

    // Kritik bölge: Paylaşılan kaynağa erişim
    std::cout << "İş parçacığı çalışıyor..." << std::endl;
    // Kaynağa erişim işlemleri
    std::this_thread::sleep_for(std::chrono::seconds(2));

    mtx.unlock();  // Mutex kilidini aç
}

int main() {
    std::thread t1(WorkerThread);
    std::thread t2(WorkerThread);

    t1.join();
    t2.join();

    return 0;
}
```

Bu örnekte, `std::mutex` sınıfı kullanılarak bir mutex nesnesi oluşturulur. `WorkerThread` işlevi, mutex'i kilitleyerek ve kilidi açarak kritik bölgeye erişir. Kritik bölge, paylaşılan kaynağa erişim sağlayan işlemleri içerir.

Ana iş parçacığı, iki `WorkerThread` işlevini ayrı iş parçacıklarında çalıştırır. Her iş parçacığı sırayla mutex'i kilitleyerek kritik bölgeye erişir ve ardından mutex kilidini açar.

Bu şekilde, mutex kullanarak paylaşılan bir kaynağa eşzamanlı erişimi kontrol edebilir ve senkronizasyon sağlayabilirsiniz. Mutex'ler, paralel programlama ve eşzamanlılık konularında güvenli ve tutarlı bir paylaşımı sağlamak için önemli bir araçtır.
___

# 2. Recursive Mutex

Recursive mutex (yeniden girişimli mutex), bir mutex türüdür ve aynı iş parçacığı tarafından birden fazla kez kilitleme yapılmasına izin verir. Yani, bir iş parçacığı aynı mutex'i tekrar tekrar kilitleyebilir.

C++ dilinde, `std::recursive_mutex` sınıfı C++ standart kütüphanesinde yeniden girişimli mutex'i temsil eder. İşte bir örnek:

```c
#include <iostream>
#include <mutex>
#include <thread>

std::recursive_mutex rmtx;  // Yeniden girişimli mutex nesnesi

void RecursiveFunction(int depth) {
    rmtx.lock();  // Mutex'i kilitle

    // Kritik bölge: Paylaşılan kaynağa erişim
    std::cout << "Derinlik: " << depth << std::endl;

    if (depth > 0) {
        RecursiveFunction(depth - 1);  // Yeniden girişim: Kendi kendini çağır
    }

    rmtx.unlock();  // Mutex kilidini aç
}

int main() {
    RecursiveFunction(3);

    return 0;
}
```

Bu örnekte, `std::recursive_mutex` sınıfı kullanılarak bir yeniden girişimli mutex nesnesi oluşturulur. `RecursiveFunction` işlevi, mutex'i kilitleyerek ve kilidi açarak kritik bölgeye erişir. Kritik bölgede, derinlik seviyesini ekrana yazdırır ve eğer derinlik sıfırdan büyükse, kendini tekrar çağırarak yeniden girişim yapar.

Ana iş parçacığı, `RecursiveFunction` işlevini başlangıç derinliğiyle çağırır. Bu işlev, kendini tekrar çağırdığı için aynı mutex'i tekrar tekrar kilitleyebilir.

Yeniden girişimli mutex, aynı iş parçacığı içinde fonksiyon çağrıları veya özyinelemeli işlemler gibi durumlarda kullanışlı olabilir. Örneğin, bir iş parçacığı bir kaynağa erişim sağlarken birden fazla alt fonksiyon kullanıyorsa, yeniden girişimli mutex ile bu alt fonksiyonların da aynı mutex'i kilitleyerek kaynağa erişim sağlaması mümkündür.

Bu şekilde, yeniden girişimli mutex kullanarak paylaşılan bir kaynağa aynı iş parçacığı içinde birden fazla kez erişim sağlayabilirsiniz. Ancak, dikkat edilmesi gereken nokta, mutex'in her kilitleme işlemine karşılık bir kilidin açılması gerektiğidir. Aksi takdirde, mutex kilidi açılmadan iş parçacığı hala mutex'i kilitleyerek bekleyecektir.

## 2.1. Mutex vs Recursive Mutex

İşte şimdi bir karşılaştırmalı örnek verelim, aşağıdaki örneği recursive mutex (`std::recursive_mutex`) ile normal mutex (`std::mutex`) arasındaki farkı göstermek için kullanacağız:

```cpp
#include <iostream>
#include <mutex>
#include <thread>

std::mutex mtx;  // Normal mutex nesnesi
std::recursive_mutex rmtx;  // Yeniden girişimli mutex nesnesi

void NormalFunction() {
    mtx.lock();  // Normal mutex'i kilitle

    std::cout << "Normal iş parçacığı" << std::endl;

    mtx.unlock();  // Normal mutex kilidini aç
}

void RecursiveFunction(int depth) {
    rmtx.lock();  // Yeniden girişimli mutex'i kilitle

    std::cout << "Derinlik: " << depth << std::endl;

    if (depth > 0) {
        RecursiveFunction(depth - 1);  // Yeniden girişim: Kendi kendini çağır
    }

    rmtx.unlock();  // Yeniden girişimli mutex kilidini aç
}

int main() {
    std::thread t1(NormalFunction);
    std::thread t2(RecursiveFunction, 3);

    t1.join();
    t2.join();

    return 0;
}
```

Bu örnekte, iki farklı fonksiyon olan `NormalFunction` ve `RecursiveFunction` kullanılmıştır. Her iki fonksiyon da farklı bir mutex türü ile çalışır.

`NormalFunction`, normal bir mutex (`std::mutex`) kullanır. Her iş parçacığı, mutex'i kilitleyerek kritik bölgeye erişir. Ancak, aynı iş parçacığı tarafından tekrar çağrılmadığı sürece, mutex'i tekrar kilitleyemez. Bu durumda, aynı iş parçacığı tekrar mutex'i kilitlemeye çalıştığında, bekler ve program deadlock (kitlenme) durumuna düşer.

`RecursiveFunction`, yeniden girişimli bir mutex (`std::recursive_mutex`) kullanır. Bu, aynı iş parçacığı tarafından tekrar tekrar çağrılan alt fonksiyonlarla çalışmak için uygun bir seçenektir. Yeniden girişimli mutex, aynı iş parçacığı tarafından birden fazla kez kilitleme yapılmasına izin verir.

Örnekte, `RecursiveFunction` derinliği azaltarak kendini tekrar tekrar çağırırken, her seferinde aynı mutex'i tekrar kilitleyebilir.

Bu şekilde, normal mutex ve yeniden girişimli mutex arasındaki farkı görebilirsiniz. Normal mutex, aynı iş parçacığı tarafından tekrar kilitleme yapamazken, yeniden girişimli mutex aynı iş parçacığı tarafından birden fazla kez kilitleme yapabilir.
___

# 3. Lock Guard

`std::lock_guard`, C++ standart kütüphanesinde yer alan bir sınıftır ve mutex kilitleme ve kilidi otomatik olarak açma işlemlerini yönetmek için kullanılır. `std::lock_guard`, bir mutex nesnesini kilitleyerek bir kritik bölgeye giriş yapar ve `std::lock_guard` nesnesi kapsamdan çıktığında, otomatik olarak mutex'i serbest bırakır. Böylece, unutulmuş veya hatalı bir şekilde kilidi açmayı önler ve kaynakların doğru şekilde serbest bırakılmasını sağlar.

`std::lock_guard`, `std::mutex` veya `std::recursive_mutex` gibi mutex türlerini destekler.

İşte bir örnek:

```cpp
#include <iostream>
#include <mutex>
#include <thread>

std::mutex mtx;  // Mutex nesnesi

void WorkerThread() {
    std::lock_guard<std::mutex> lock(mtx);  // Mutex'i kilitle

    // Kritik bölge: Paylaşılan kaynağa erişim
    std::cout << "İş parçacığı çalışıyor..." << std::endl;
    // Kaynağa erişim işlemleri
    std::this_thread::sleep_for(std::chrono::seconds(2));

    // Otomatik olarak mutex'i serbest bırakır
}

int main() {
    std::thread t1(WorkerThread);
    std::thread t2(WorkerThread);

    t1.join();
    t2.join();

    return 0;
}
```

Bu örnekte, `std::lock_guard` sınıfı kullanılarak bir `lock` nesnesi oluşturulur. `lock_guard`'ın yapıcı fonksiyonu, verilen mutex'i otomatik olarak kilitleyerek iş parçacığının kritik bölgeye giriş yapmasını sağlar. `lock_guard` nesnesi, kapsamdan çıktığında (yani `WorkerThread` fonksiyonundan çıkıldığında), otomatik olarak mutex'i serbest bırakır ve böylece kaynaklar doğru şekilde temizlenir.

Ana iş parçacığı, iki `WorkerThread` işlevini ayrı iş parçacıklarında çalıştırır. Her iş parçacığı, `std::lock_guard` kullanarak mutex'i kilitleyerek kritik bölgeye erişir ve ardından kapsamdan çıkıldığında otomatik olarak mutex'i serbest bırakır.

`std::lock_guard` sınıfı, RAII (Resource Acquisition Is Initialization) idiyomunu kullanarak, kaynakların otomatik olarak temizlenmesini sağlar. Bu sayede, mutex kilidinin unutulması veya hatalı bir şekilde serbest bırakılması gibi sorunlar ortadan kalkar ve kodun daha güvenli hale gelmesi sağlanır.
___

# 4. Unique Lock

`std::unique_lock`, C++ standart kütüphanesinde yer alan bir sınıftır ve mutex kilitleme ve kilidi açma işlemlerini yönetmek için kullanılır. `std::unique_lock` sınıfı, `std::lock_guard` sınıfına benzer, ancak daha fazla esneklik sunar. `std::unique_lock`, mutex'i kilitleme ve kilidi açma işlemlerini kontrol etmek için manuel olarak kullanılabilir. Ayrıca, kilidi isteğe bağlı olarak serbest bırakabilir ve tekrar kilitleyebilir.

`std::unique_lock`, `std::mutex` veya `std::recursive_mutex` gibi mutex türlerini destekler.

İşte bir örnek:

```cpp
#include <iostream>
#include <mutex>
#include <thread>

std::mutex mtx;  // Mutex nesnesi

void WorkerThread() {
    std::unique_lock<std::mutex> lock(mtx);  // Mutex'i kilitle

    // Kritik bölge: Paylaşılan kaynağa erişim
    std::cout << "İş parçacığı çalışıyor..." << std::endl;
    // Kaynağa erişim işlemleri
    std::this_thread::sleep_for(std::chrono::seconds(2));

    // Mutex kilidini serbest bırakma
    lock.unlock();

    // Diğer işlemler

    // Mutex kilidini tekrar alma
    lock.lock();

    // Yeniden kritik bölgeye erişim
    std::cout << "İş parçacığı devam ediyor..." << std::endl;

    // Otomatik olarak mutex'i serbest bırakır
}

int main() {
    std::thread t1(WorkerThread);
    std::thread t2(WorkerThread);

    t1.join();
    t2.join();

    return 0;
}
```

Bu örnekte, `std::unique_lock` sınıfı kullanılarak bir `lock` nesnesi oluşturulur. `unique_lock`'ın yapıcı fonksiyonu, verilen mutex'i kilitleyerek iş parçacığının kritik bölgeye giriş yapmasını sağlar. `unique_lock` nesnesi, kapsamdan çıktığında (yani `WorkerThread` fonksiyonundan çıkıldığında), otomatik olarak mutex'i serbest bırakır.

Örnekte, `lock.unlock()` kullanarak mutex kilidini serbest bırakıyoruz. Ardından, başka işlemler yapabiliriz. Daha sonra, `lock.lock()` kullanarak mutex kilidini tekrar alabiliriz ve yeniden kritik bölgeye erişebiliriz.

`std::unique_lock`, `lock.unlock()` ve `lock.lock()` gibi işlemleri kullanarak, mutex kilidini kontrol etmek ve tekrar kilitlemek için daha fazla esneklik sağlar. Bu, bazı senaryolarda mutex kilidini isteğe bağlı olarak serbest bırakmak ve tekrar kilitlemek için kullanışlı olabilir.

Şimdi `std::unique_lock`'un `std::guard_lock`'a göre kullanımının esnek yönlerinden bahsederek karşılaştırmalı örnek verelim.

`std::unique_lock` ve `std::lock_guard` arasındaki en önemli fark, `std::unique_lock`'ın daha fazla esneklik sağlamasıdır. İşte `std::unique_lock`'un guard_lock'a göre kullanımının esnek yönleri:

1. Kilidi İstediğiniz Zaman Serbest Bırakabilme: `std::unique_lock`, `unlock()` işlevini kullanarak kilidi istediğiniz zaman serbest bırakmanıza olanak tanır. Bu, kritik bölgenin tamamı yerine sadece bir kısmı üzerinde çalışmanız gerektiğinde veya mutex kilidini diğer işlemlere açmanız gerektiğinde faydalı olabilir.
    
2. Kilidi İstediğiniz Zaman Tekrar Kilitleyebilme: `std::unique_lock`, `lock()` işlevini kullanarak kilidi istediğiniz zaman tekrar kilitleyebilmenize olanak tanır. Bu, kilidin serbest bırakıldığı bir bölge sonrasında tekrar kritik bölgeye erişim sağlamanız gerektiğinde veya kilitli olan kaynağa erişim gerektiren başka bir işlem yapmanız gerektiğinde kullanışlıdır.

## 4.1. Unique Lock ve Lock Guard Karşılaştırması

İşte bir karşılaştırmalı örnek, `std::unique_lock` ve `std::lock_guard`'ın kullanımını göstermek için:

```cpp
#include <iostream>
#include <mutex>
#include <thread>

std::mutex mtx;  // Mutex nesnesi

void UniqueLockExample() {
    std::unique_lock<std::mutex> lock(mtx);  // Mutex'i kilitle

    // Kritik bölge: Paylaşılan kaynağa erişim
    std::cout << "Unique Lock ile çalışan iş parçacığı" << std::endl;
    // Kaynağa erişim işlemleri
    std::this_thread::sleep_for(std::chrono::seconds(2));

    // Kilidi isteğe bağlı olarak serbest bırakma
    if (someCondition) {
        lock.unlock();
        // Diğer işlemler
        lock.lock();  // Kilidi tekrar al
        // Yeniden kritik bölgeye erişim
    }

    // Otomatik olarak mutex'i serbest bırakır
}

void LockGuardExample() {
    std::lock_guard<std::mutex> lock(mtx);  // Mutex'i kilitle

    // Kritik bölge: Paylaşılan kaynağa erişim
    std::cout << "Lock Guard ile çalışan iş parçacığı" << std::endl;
    // Kaynağa erişim işlemleri
    std::this_thread::sleep_for(std::chrono::seconds(2));

    // Kilidi isteğe bağlı olarak serbest bırakma mümkün değil
    // Diğer işlemler

    // Otomatik olarak mutex'i serbest bırakır
}

int main() {
    std::thread t1(UniqueLockExample);
    std::thread t2(LockGuardExample);

    t1.join();
    t2.join();

    return 0;
}
```

Bu örnekte, `UniqueLockExample` işlevi, `std::unique_lock` kullanarak mutex kilidini isteğe bağlı olarak serbest bırakır ve tekrar kilitleme yapabilir. `LockGuardExample` işlevi ise `std::lock_guard` kullanarak mutex kilidini otomatik olarak serbest bırakır, ancak tekrar kilitleme yapma yeteneği yoktur.

Bu örnekte, `UniqueLockExample` işlevi, belirli bir koşulu kontrol ederek mutex kilidini serbest bırakır ve ardından başka işlemler yapar. Daha sonra, mutex kilidini tekrar alarak kritik bölgeye erişir. `LockGuardExample` ise kilidi otomatik olarak serbest bırakır ve başka işlemler yapmaz.

Bu şekilde, `std::unique_lock`'un `unlock()` ve `lock()` işlevlerini kullanarak daha fazla esneklik sağladığını ve mutex kilidini daha ince bir kontrolle yönetmenize olanak tanıdığını görebilirsiniz.

___
# 5. Condition Variable

`std::condition_variable`, C++ standart kütüphanesindeki senkronizasyon mekanizmalarından biridir. `std::condition_variable`, iş parçacıkları arasında iletişim kurmayı sağlar ve iş parçacıklarının birbirlerini beklemesine veya birbirlerini uyandırmasına olanak tanır. Bir iş parçacığı, belirli bir koşulu kontrol ederek diğer iş parçacıklarını uyandırabilir veya bekleyebilir.

`std::condition_variable`, bir mutex ile birlikte kullanılır ve genellikle şu işlemlerle birlikte kullanılır:

- `wait()`: Bir iş parçacığı, belirli bir koşulu kontrol ederek diğer iş parçacıklarının bir olayı veya koşulu beklemesini sağlar. `wait()` işlevi çağrıldığında, mutex kilidi serbest bırakılır ve iş parçacığı uyandırılıncaya kadar bekler.

- `notify_one()`: Bekleyen iş parçacıklarından birini uyandırır. Eğer birden fazla iş parçacığı bekliyorsa, hangi iş parçacığının uyandırılacağı belirsizdir.

- `notify_all()`: Bekleyen tüm iş parçacıklarını uyandırır. Tüm iş parçacıkları tekrar mutex kilidini almaya çalışacaktır.

İşte bir örnek verelim:

```cpp
#include <iostream>
#include <condition_variable>
#include <mutex>
#include <thread>

std::condition_variable cv;  // Condition variable nesnesi
std::mutex mtx;  // Mutex nesnesi
bool ready = false;  // Paylaşılan değişken

void WorkerThread1() {
    std::unique_lock<std::mutex> lock(mtx);  // Mutex'i kilitle

    // Koşulu beklemek için wait()
    cv.wait(lock, []{ return ready; });

    // Koşul gerçekleşti, devam eden işlemler
    std::cout << "WorkerThread1: Koşul gerçekleşti, devam eden işlemler" << std::endl;
}

void WorkerThread2() {
    std::this_thread::sleep_for(std::chrono::seconds(2));

    std::unique_lock<std::mutex> lock(mtx);  // Mutex'i kilitle

    // Koşulu gerçekleştir
    ready = true;

    // Bekleyen iş parçacığını uyandır
    cv.notify_one();
}

int main() {
    std::thread t1(WorkerThread1);
    std::thread t2(WorkerThread2);

    t1.join();
    t2.join();

    return 0;
}
```

Bu örnekte, `std::condition_variable` ve `std::mutex` kullanılarak iki iş parçacığı arasında iletişim sağlanır. `WorkerThread1`, bir koşulu beklerken (`ready` değişkeninin `true` olmasını beklerken) `wait()` işlevini kullanır ve mutex kilidini serbest bırakır. `WorkerThread2`, 2 saniye bekledikten sonra koşulu gerçekleştirir (`ready` değişkenini `true` yapar) ve bekleyen iş parçacığını uyandırmak için `notify_one()` işlevini kullanır.

Bu şekilde, `std::condition_variable` kullanarak bir iş parçacığının diğerini beklemesini sağlayabilir ve belirli bir koşul gerçekleştiğinde uyandırabilirsiniz. `wait()`, `notify_one()` ve `notify_all()` işlevlerini kullanarak iş parçacıkları arasında iletişim ve senkronizasyon sağlayabilirsiniz.

## 5.1. Timed Condition Variable

Aşağıda, C++'ın `std::condition_variable` sınıfını ve `std::chrono` kütüphanesini kullanarak bir timed conditional variable (zamana bağlı koşullu değişken) örneği verilmiştir:

```cpp
#include <iostream>
#include <condition_variable>
#include <mutex>
#include <thread>
#include <chrono>

std::condition_variable cv;
std::mutex mtx;
bool flag = false;

void WorkerThread() {
    std::this_thread::sleep_for(std::chrono::seconds(2));

    {
        std::lock_guard<std::mutex> lock(mtx);
        flag = true;
    }

    cv.notify_one();
}

int main() {
    std::cout << "Ana iş parçacığı başladı" << std::endl;

    std::thread t(WorkerThread);

    {
        std::unique_lock<std::mutex> lock(mtx);

        if (cv.wait_for(lock, std::chrono::seconds(5), [] { return flag; })) {
            std::cout << "Bekleme süresi içinde koşul sağlandı" << std::endl;
        } else {
            std::cout << "Bekleme süresi içinde koşul sağlanmadı" << std::endl;
        }
    }

    t.join();

    std::cout << "Ana iş parçacığı tamamlandı" << std::endl;

    return 0;
}
```

Bu örnekte, `WorkerThread` adlı bir iş parçacığı oluşturulur. Bu iş parçacığı, 2 saniye bekledikten sonra `flag` değişkenini `true` olarak ayarlar ve `cv.notify_one()` işlevini kullanarak bekleyen iş parçacıklarını uyandırır.

Ana iş parçacığında, `std::condition_variable` ve `std::mutex` kullanılarak bir zamana bağlı koşullu değişken senaryosu oluşturulur. `std::unique_lock` sınıfı kullanılarak `std::mutex` kilidi alınır. Ardından, `cv.wait_for()` işlevi çağrılarak bir süre boyunca beklenir ve `flag` koşulunun sağlanması beklenir. Eğer belirtilen süre içinde koşul sağlanırsa, `"Bekleme süresi içinde koşul sağlandı"` mesajı ekrana yazdırılır. Aksi halde, `"Bekleme süresi içinde koşul sağlanmadı"` mesajı ekrana yazdırılır.

Bu şekilde, `std::condition_variable` ve `std::chrono` kütüphanelerini kullanarak zamana bağlı bir koşul kontrolü yapabilir ve belirli bir süre boyunca bekleyebilirsiniz. Bu senaryoda, `wait_for()` işlevi belirtilen süre boyunca bekler ve beklenen koşulun sağlanıp sağlanmadığını kontrol eder.
___

# 6. Atomic

Elbette! `std::atomic`, C++ standart kütüphanesinde yer alan bir sınıftır ve paralel programlamada senkronizasyonu sağlamak için kullanılır. `std::atomic`, belirli bir veri türünü atomik olarak işlem yapılabilen bir veri türü haline getirir. Bu, birden fazla iş parçacığı arasında aynı anda okuma/yazma işlemlerini gerçekleştirirken verinin tutarlılığını sağlar.

`std::atomic`, veri yarışmaları (race conditions) ve senkronizasyon eksiklikleri gibi sorunları önlemek için kullanılır. Bu sınıf, belirli işlemlerin atomik olarak gerçekleştirilmesini sağlamak için donanım veya kompiler destekli atomik operasyonları kullanır.

`std::atomic`, birçok operasyonu destekler, bunlar arasında okuma/yazma işlemleri, artırma/azaltma, takas (swap), karşılaştırma ve daha fazlası bulunur.

İşte bir örnek:

```cpp
#include <iostream>
#include <atomic>
#include <thread>

std::atomic<int> counter(0);  // Atomik sayaç

void WorkerThread() {
    for (int i = 0; i < 10000; ++i) {
        counter.fetch_add(1);  // Atomik artırma işlemi
    }
}

int main() {
    std::thread t1(WorkerThread);
    std::thread t2(WorkerThread);

    t1.join();
    t2.join();

    std::cout << "Sonuç: " << counter << std::endl;

    return 0;
}
```

Bu örnekte, `std::atomic<int>` kullanılarak bir atomik sayaç oluşturulur. İki iş parçacığı, her biri 10.000 kez sayaçı artırmak için `fetch_add()` işlevini kullanır. `fetch_add()` işlevi, veriyi atomik olarak artıran bir işlemdir ve senkronizasyonu sağlar.

Ana iş parçacığı, iki iş parçacığı tamamladıktan sonra sayaç değerini ekrana yazdırır.

Bu şekilde, `std::atomic` kullanarak birden fazla iş parçacığı arasında senkronizasyon sağlanabilir ve veri yarışmaları gibi sorunlar önlenir. Atomik operasyonlar, belirli bir veri türü üzerinde aynı anda yapılan işlemlerin tutarlı ve güvenli bir şekilde gerçekleştirilmesini sağlar.

Ek olarak atomic türdeki bir nesnenin değerini değiştirebilmek için `load` ve `store` işlevlerini de kullanabiliriz.

```cpp
#include <iostream>
#include <atomic>

int main() {
    std::atomic<int> value(10);  // Atomik değer

    // Değeri okuma
    int loadedValue = value.load();
    std::cout << "Yüklenen Değer: " << loadedValue << std::endl;

    // Değeri değiştirme
    value.store(20);
    std::cout << "Yeni Değer: " << value.load() << std::endl;

    return 0;
}
```

Bu örnekte, `std::atomic<int>` türünde bir atomik değer `value` oluşturulur. İlk olarak, `load()` işlevi kullanılarak değer okunur ve `loadedValue` değişkenine atanır. Ardından, `store()` işlevi kullanılarak değer 20 olarak değiştirilir. Son olarak, `load()` işlevi tekrar çağrılarak yeni değer okunur ve ekrana yazdırılır.

`load()` işlevi, atomik değeri okurken senkronizasyonu sağlar. Yani, bir iş parçacığı atomik değeri okurken, başka bir iş parçacığı tarafından değer değiştirilirse, `load()` işlevi güncel değeri döndürür. `store()` işlevi ise atomik değeri güncellerken senkronizasyonu sağlar. Diğer iş parçacıkları, `store()` işlemi tamamlanmadan yeni değeri okuyamaz.

Bu şekilde, `load()` ve `store()` işlevlerini kullanarak `std::atomic` türündeki değerleri güvenli bir şekilde okuyabilir ve değiştirebilirsiniz. Bu işlevler, veri yarışmalarını önler ve tutarlı bir davranış sağlar.

## 6.1. Memory Order Acquire Nedir?

`std::memory_order_acquire`, C++'taki `std::atomic` türünün `load` işlemi sırasında kullanılan bir bellek düzenleme (memory ordering) seçeneğidir. Bu bellek düzenlemesi, iş parçacığının bellekteki veriyi okurken, diğer iş parçacıklarının kendi bellek erişimlerini düzenlemesini sağlar.

`std::memory_order_acquire` bellek düzenlemesi, bir iş parçacığının okuma işlemi sırasında bellek erişimlerinin sıralamasını kontrol etmek için kullanılır. Bu düzenleme seçeneği, okunan verinin iş parçacığı tarafından kullanılabilmesi için, okuma işleminin tamamlandığından ve bellekteki verinin güncel olduğundan emin olunmasını sağlar. Diğer bir deyişle, `std::memory_order_acquire` seçeneği, bellekteki verinin güncel ve tutarlı bir şekilde okunmasını sağlamak için gereken senkronizasyonu sağlar.

Aşağıda, `std::memory_order_acquire` seçeneğini kullanarak bir örnek verilmiştir:

```cpp
#include <atomic>
#include <iostream>
#include <thread>

std::atomic<int> data(0);
std::atomic<bool> ready(false);

void ProducerThread() {
    // Veriyi hazırla
    data.store(42, std::memory_order_release);

    // Hazırlığın tamamlandığını bildir
    ready.store(true, std::memory_order_release);
}

void ConsumerThread() {
    // Hazırlığın tamamlanmasını bekle
    while (!ready.load(std::memory_order_acquire))
        ;

    // Veriyi oku
    int value = data.load(std::memory_order_acquire);

    // Okunan değeri kullan
    std::cout << "Received value: " << value << std::endl;
}

int main() {
    std::thread producer(ProducerThread);
    std::thread consumer(ConsumerThread);

    producer.join();
    consumer.join();

    return 0;
}
```

Bu örnekte, `std::memory_order_acquire` seçeneği `load` ve `store` işlemleri için kullanılmıştır. `ProducerThread` iş parçacığı, `data` değişkenine bir değer atar ve `ready` bayrağını true olarak ayarlar. Bu işlemler, `std::memory_order_release` seçeneğiyle gerçekleştirilir.

`ConsumerThread` iş parçacığı, `ready` bayrağının true olmasını beklerken, `std::memory_order_acquire` seçeneğini kullanır. Bu sayede, `ready` bayrağı true olduğunda, `data` değişkenini okuyarak güncel veriye erişir.

Bu örnekte, `std::memory_order_acquire` kullanarak okuma işlemi sırasında gerekli senkronizasyonu sağlamış oluyoruz, böylece verinin güncel olduğundan emin olabiliriz.
___

# 7. Atomic Flag

`std::atomic_flag`, C++ standart kütüphanesinde yer alan bir sınıftır ve tek bir işlemin atomik bir şekilde gerçekleştirilmesini sağlar. `std::atomic_flag` sınıfı, özellikle senkronizasyon işlemleri için kullanılır ve bir iş parçacığı tarafından kullanıldığında diğer iş parçacıklarının aynı anda aynı işlemi yapmasını engeller.

`std::atomic_flag`, iki durumdan oluşur: set (ayarla) ve clear (temizle). Bu durumlar, iş parçacıklarının bir kritik bölgeye giriş yapmasını ve çıkmasını kontrol etmek için kullanılır.

`std::atomic_flag`'in `test_and_set()` ve `clear()` işlevleri vardır:

- `test_and_set()`: `std::atomic_flag`'in durumunu set (true) olarak ayarlar ve önceki durumunu döndürür. Bu işlev, bir iş parçacığının kritik bölgeye giriş yapmak için kullanılır. Eğer `test_and_set()` işlemi başarılıysa, yani önceki durum `true` ise, iş parçacığı kritik bölgeye girebilir. Eğer önceki durum `false` ise, bir başka iş parçacığı kritik bölgededir ve bu iş parçacığı beklemelidir.

- `clear()`: `std::atomic_flag`'in durumunu clear (false) olarak ayarlar. Bu işlev, bir iş parçacığının kritik bölgeden çıkış yapmak için kullanılır. İş parçacığı kritik bölgeden çıktıktan sonra, `clear()` işlemi ile `std::atomic_flag`'in durumu `false` olarak ayarlanır, böylece başka bir iş parçacığı kritik bölgeye girebilir.

İşte bir örnek:

```cpp
#include <iostream>
#include <atomic>
#include <thread>

std::atomic_flag lock = ATOMIC_FLAG_INIT;  // Atomik bayrak

void WorkerThread() {
    while (lock.test_and_set(std::memory_order_acquire)) {
        // Diğer iş parçacığı kritik bölgede, bekle
    }

    // Kritik bölge: Paylaşılan kaynağa erişim
    std::cout << "İş parçacığı kritik bölgede" << std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(2));

    lock.clear(std::memory_order_release);  // Kritik bölgeden çıkış

    // Kritik bölgeden çıkış yapıldı
    std::cout << "İş parçacığı kritik bölgeden çıkış yaptı" << std::endl;
}

int main() {
    std::thread t1(WorkerThread);
    std::thread t2(WorkerThread);

    t1.join();
    t2.join();

    return 0;
}
```

Bu örnekte, `std::atomic_flag` türünde bir atomik bayrak `lock` oluşturulur. Her iş parçacığı `test_and_set()` işlevini kullanarak bayrağı ayarlamaya çalışır. Eğer bayrak zaten ayarlı ise, yani bir başka iş parçacığı kritik bölgedeyse, iş parçacığı beklemek zorunda kalır. Bayrak başarılı bir şekilde ayarlandığında, iş parçacığı kritik bölgeye girer ve işlemlerini gerçekleştirir. Ardından, `clear()` işlevi kullanılarak bayrak temizlenir ve başka bir iş parçacığı kritik bölgeye girebilir.

Bu şekilde, `std::atomic_flag` kullanarak bir kritik bölgeye giriş ve çıkış kontrolü sağlayabilirsiniz. Bu, senkronizasyonu kontrol etmek ve veri yarışmalarını önlemek için kullanışlı bir mekanizmadır.
___

# 8. Extra

Bu kısımda C++ tarafından direkt olarak desteklenmeyen Semaphore kavramı üzerinde duracağız. Ek olarak `thread_local`, `spin lock`, `defer_lock`, `adopt_lock`, `scoped_lock`, `deadlock`, `starvation`, ve `livelock` konularına değindikten sonra `thread pool`, `consumer-producer`, `Round-Robin` algoritmasının implementasyonunu senkronizasyon yöntemlerini kullanarak gerçekleştireceğiz.
___

## 8.1. Thread Local

thread_local kavramını, en baştan global ve local değişkenlerin tanımlamalarını yaparak açıklamak istiyorum.

1. Global Değişken: Global değişkenler, programın herhangi bir noktasından erişilebilen ve geçerliliği programın ömrü boyunca devam eden değişkenlerdir. Global değişkenler, programın tüm iş parçacıkları veya fonksiyonlar tarafından paylaşılır. Bir global değişkenin bellekteki adresi her zaman sabittir ve programın herhangi bir yerinde erişilebilir.

```cpp
#include <iostream>

int globalVariable = 10;

void Function1() {
    std::cout << "Function1 - Global Değişken: " << globalVariable << std::endl;
}

void Function2() {
    std::cout << "Function2 - Global Değişken: " << globalVariable << std::endl;
}

int main() {
    Function1();
    Function2();

    return 0;
}
```

Bu örnekte, `globalVariable` adlı bir global değişken oluşturulur. `Function1()` ve `Function2()` işlevleri, bu global değişkene erişebilir. Her iki işlev de aynı global değişkeni kullanır ve çıktı olarak aynı değeri verir.

2. Local Değişken: Local değişkenler, bir işlevin içerisinde tanımlanan ve sadece tanımlandıkları blok veya işlev içerisinde geçerli olan değişkenlerdir. Local değişkenler, yalnızca tanımlandıkları işlevin çağrıldığı süre boyunca geçerlidir ve her işlev çağrısı için ayrı bellek alanına sahiptir.

```cpp
#include <iostream>

void Function() {
    int localVariable = 5;
    std::cout << "Local Değişken: " << localVariable << std::endl;
}

int main() {
    Function();

    return 0;
}
```

Bu örnekte, `Function()` adlı bir işlev oluşturulur ve içerisinde `localVariable` adlı bir local değişken tanımlanır. Bu local değişken, yalnızca `Function()` işlevinin çalıştığı süre boyunca geçerlidir ve yalnızca `Function()` işlevi tarafından erişilebilir. `Function()` işlevi her çağrıldığında `localVariable` adlı değişken 5 değeriyle hayata gelecektir.

3. `thread_local` Değişken: `thread_local` anahtar kelimesiyle tanımlanan değişkenler, her iş parçacığı için ayrı bellek alanına sahip olan değişkenlerdir. Bu tür değişkenler, her iş parçacığı tarafından ayrı ayrı tutulur ve her iş parçacığı için farklı değerlere sahip olabilir.

```cpp
#include <iostream>
#include <thread>

thread_local int threadLocalVariable = 3;

void ThreadFunction() {
    threadLocalVariable++;
    std::cout << "Thread - thread_local Değişken: " << threadLocalVariable << std::endl;
}

int main() {
    std::thread t1(ThreadFunction);
    std::thread t2(ThreadFunction);

    t1.join();
    t2.join();

    std::cout << "Main Thread - thread_local Değişken: " << threadLocalVariable << std::endl;

    return 0;
}
```

Bu örnekte, `ThreadFunction()` adlı bir iş parçacığı fonksiyonu oluşturulur. İş parçacığı fonksiyonu içinde `threadLocalVariable` adlı bir `thread_local` değişken tanımlanır ve her iş parçacığı tarafından ayrı ayrı tutulur. Her iş parçacığı, kendi `threadLocalVariable` değişkenine erişir ve değerini değiştirir. Main iş parçacığı da ayrı bir `threadLocalVariable` değişkenine sahiptir ve bu değişkenin değerini yazdırır.

Ekrana yansıyan sonuç aşağıdaki gibi olacaktır:

```
Thread - thread_local Değişken: 4
Thread - thread_local Değişken: 4
Main Thread - thread_local Değişken: 3
```

Sonuç olarak, global değişkenler programın her yerinden erişilebilirken, local değişkenler sadece tanımlandıkları blok veya işlev içerisinde geçerlidir. `thread_local` değişkenler ise her iş parçacığı için ayrı bellek alanına sahip olup her iş parçacığı tarafından ayrı ayrı kullanılır.
___

## 8.2. Semaphore

Semaphore, paralel programlamada senkronizasyon ve eşzamanlılık sağlamak için kullanılan bir senkronizasyon mekanizmasıdır. Semaphore, bir kaynağın aynı anda kaç iş parçacığı tarafından erişilebileceğini kontrol etmek için kullanılır.

Semaphore, bir tam sayı değeri ve iki temel işlemi olan bir veri yapısıdır: "acquire" (al) ve "release" (serbest bırak). Semaphore'un tam sayı değeri, kaynağın mevcut durumunu temsil eder.

- "acquire" işlemi: Bir iş parçacığı, kaynağa erişmek istediğinde "acquire" işlemini kullanır. Eğer semaforun değeri 0 ise, iş parçacığı beklemeye alınır. Değer 0'dan büyük ise, iş parçacığı kaynağa erişir ve semafor değeri bir azaltılır.

- "release" işlemi: Bir iş parçacığı, kaynağı serbest bırakmak istediğinde "release" işlemini kullanır. Semafor değeri bir artırılır ve bekleyen iş parçacıklarından biri serbest bırakılarak kaynağa erişim sağlanır.


Semaphore, çeşitli senaryolarda kullanışlı olabilir. Örneğin, bir sınırlı kaynak havuzunu kontrol etmek, kritik bölgeye aynı anda sadece belirli bir sayıda iş parçacığı izin vermek veya veri yapılarının güvenli bir şekilde paylaşılmasını sağlamak için semaphore kullanılabilir.

Semaphore'lar, paralel programlamada senkronizasyon ve eşzamanlılık sorunlarını çözmek için yaygın olarak kullanılan bir araçtır. Bununla birlikte, doğru kullanımı ve senaryolara özgü gereksinimlerin dikkate alınması önemlidir.

C++ standardı, semaforların doğrudan bir sınıf olarak yer almadığı bir sembolik veri yapısına (sembolik olarak mutex ve condition_variable ile benzetilebilir) sahip olmasına rağmen, semafor benzeri davranışları elde etmek için mevcut senkronizasyon mekanizmaları kullanılarak semafor benzeri bir yapı oluşturulabilir.

Bunun için `std::mutex` ve `std::condition_variable` kullanabiliriz. İşte bir örnek:

```cpp
#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>

class Semaphore {
public:
    explicit Semaphore(int count) : count_(count) {}

    void Acquire() {
        std::unique_lock<std::mutex> lock(mutex_);
        condition_.wait(lock, [this] { return count_ > 0; });
        count_--;
    }

    void Release() {
        std::unique_lock<std::mutex> lock(mutex_);
        count_++;
        condition_.notify_one();
    }

private:
    std::mutex mutex_;
    std::condition_variable condition_;
    int count_;
};

// Kullanım örneği
Semaphore semaphore(2);

void WorkerThread(int id) {
    semaphore.Acquire();

    std::cout << "Thread " << id << " started working." << std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(2));
    std::cout << "Thread " << id << " finished working." << std::endl;

    semaphore.Release();
}

int main() {
    std::thread t1(WorkerThread, 1);
    std::thread t2(WorkerThread, 2);
    std::thread t3(WorkerThread, 3);

    t1.join();
    t2.join();
    t3.join();

    return 0;
}
```

Bu örnekte, `Semaphore` adlı bir sınıf oluşturulmuştur. `Acquire` fonksiyonu, semaforu alırken kaynağın uygun olmasını bekler ve ardından kaynağı kullanır. `Release` fonksiyonu ise kaynağı serbest bırakır ve diğer iş parçacıklarının kaynağı kullanmasına izin verir.

Ana iş parçacığı, 2 adet semafor kaynağına sahip bir semafor oluşturur. Ardından, `WorkerThread` işlevini kullanarak üç iş parçacığı başlatır. Her iş parçacığı semafor kaynağını alır, bir süre çalışır ve ardından semafor kaynağını serbest bırakır.

Bu şekilde, semafor benzeri bir davranışı elde etmek için `std::mutex` ve `std::condition_variable` kullanarak basit bir semafor uygulaması yapabilirsiniz. Daha karmaşık senaryolarda veya özel gereksinimlerde farklı bir yaklaşım izlemek gerekebilir.

### 8.2.1. Binary Semaphore

C++20 standartları ile dile eklenmiştir.

Binary Semaphore, senkronizasyon mekanizmalarından biridir ve iki durumlu (0 ve 1) bir bayrak gibi davranır. İki temel işlemi vardır: "Sinyal Verme" (Signal) ve "Bekleme" (Wait).

- "Sinyal Verme" (Signal): Bayrağı 1'e ayarlar. Bir iş parçacığı veya süreç, diğer iş parçacıklarına veya süreçlere bayrağı ayarlamak ve onları uyandırmak için kullanır. Bu işlem, diğer iş parçacıklarının veya süreçlerin devam etmesini sağlar.

- "Bekleme" (Wait): Bayrağın 1 olmasını bekler. Eğer bayrak 1 ise, bayrağı 0'a ayarlar ve devam eder. Eğer bayrak 0 ise, iş parçacığı veya süreç beklemeye alınır ve diğer iş parçacıkları veya süreçler bayrağın 1 olmasını bekler.


Binary Semaphore, özellikle senkronizasyon ve karşılıklı dışlama (mutual exclusion) durumlarında kullanılır. Örneğin, bir kaynağın aynı anda sadece bir iş parçacığı veya süreç tarafından erişilebilmesini sağlamak için kullanılabilir.

Aşağıda, C++ dilinde `std::binary_semaphore`'ı kullanarak basit bir örnek verilmiştir:

```cpp
#include <iostream>
#include <semaphore>
#include <thread>

std::binary_semaphore sem(0);  // Binary Semaphore

void WorkerThread() {
    std::cout << "İş parçacığı beklemede..." << std::endl;
    sem.acquire();  // Bekleme

    // Bayrak 1 olduğunda devam eden işlemler
    std::cout << "İş parçacığı çalışıyor..." << std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(2));

    std::cout << "İş parçacığı tamamlandı" << std::endl;
}

int main() {
    std::thread t(WorkerThread);

    std::this_thread::sleep_for(std::chrono::seconds(5));

    std::cout << "Bayrağı 1'e ayarla" << std::endl;
    sem.release();  // Sinyal Verme

    t.join();

    return 0;
}
```

Bu örnekte, `std::binary_semaphore` türünde bir binary semaphore olan `sem` oluşturulur. `WorkerThread` iş parçacığı, `acquire()` işlevini kullanarak bayrağın 1 olmasını bekler. Ana iş parçacığı, 5 saniye bekledikten sonra `release()` işlevi ile bayrağı 1'e ayarlar ve `WorkerThread` iş parçacığının devam etmesini sağlar.

İş parçacığı bayrağı beklediği sürece beklemeye alınır ve diğer iş parçacıkları bayrağın 1 olmasını bekler. Bayrak 1 olduğunda, iş parçacığı devam eder ve işlemlerini gerçekleştirir. Bu örnekte, binary semaphore kullanarak iş parçacığının çalışmasını kontrol etmek için basit bir senaryo gösterilmektedir.

### 8.2.2. Counting Semaphore

C++20 standartları ile dile eklenmiştir.

Counting Semaphore, senkronizasyon mekanizmalarından biridir ve belirli bir kaynağın aynı anda birden fazla iş parçacığı veya süreç tarafından erişilebilmesini kontrol etmek için kullanılır. Sayma (counting) semaforu, içerdiği sayaç değeri ile kaynağın mevcut durumunu temsil eder.

Counting Semaphore, iki temel işlemi destekler: "Sinyal Verme" (Signal) ve "Bekleme" (Wait).

- "Sinyal Verme" (Signal): Kaynak sayaç değerini artırır. Bir iş parçacığı veya süreç, diğer iş parçacıklarına veya süreçlere kaynak kullanım hakkını vermek için kullanır. Bu işlem, diğer iş parçacıklarının veya süreçlerin kaynağı kullanabilmesini sağlar.
    
- "Bekleme" (Wait): Kaynak kullanım hakkını bekler. Eğer sayaç değeri 0 ise, iş parçacığı veya süreç beklemeye alınır. Kaynak kullanım hakkı bir başka iş parçacığı veya süreç tarafından serbest bırakıldığında, bekleyen iş parçacığı veya süreç kaynağı kullanabilir.
    

Counting Semaphore, özellikle sınırlı sayıda kaynağın paylaşılması veya senkronizasyon gerektiren senaryolarda kullanılır.

Aşağıda, C++ dilinde `std::counting_semaphore`'ı kullanarak basit bir örnek verilmiştir:

```cpp
#include <iostream>
#include <semaphore>
#include <thread>

std::counting_semaphore<5> sem(0);  // Counting Semaphore

void WorkerThread(int id) {
    std::cout << "İş parçacığı " << id << " kaynağı bekliyor..." << std::endl;
    sem.acquire();  // Bekleme

    // Kaynak kullanımı
    std::cout << "İş parçacığı " << id << " kaynağı kullandı" << std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(2));

    sem.release();  // Kaynak serbest bırakma
    std::cout << "İş parçacığı " << id << " kaynağı serbest bıraktı" << std::endl;
}

int main() {
    std::thread t1(WorkerThread, 1);
    std::thread t2(WorkerThread, 2);
    std::thread t3(WorkerThread, 3);

    std::this_thread::sleep_for(std::chrono::seconds(5));

    for (int i = 0; i < 3; ++i) {
        sem.release();  // İş parçacıklarının beklemesini sonlandırma
    }

    t1.join();
    t2.join();
    t3.join();

    return 0;
}
```

Bu örnekte, `std::counting_semaphore<5>` türünde bir counting semaphore olan `sem` 0 başlangıç değeriyle oluşturulur. `WorkerThread` iş parçacıkları, `acquire()` işlevini kullanarak kaynağı bekler. Ana iş parçacığı, 5 saniye bekledikten sonra `release()` işlevini kullanarak kaynağı serbest bırakır ve bekleyen iş parçacıklarının kaynağı kullanabilmesini sağlar.

İş parçacıkları kaynağı beklediği sürece beklemeye alınır. İlk 5 iş parçacığı kaynağı alır ve kullanır. Sonra, ana iş parçacığı `release()` işlemini kullanarak bekleyen iş parçacıklarının beklemesini sonlandırır ve kaynağın serbest olduğunu belirtir. Böylece, diğer iş parçacıkları kaynağı kullanabilir.

Bu şekilde, counting semaphore kullanarak belirli sayıda kaynağın aynı anda erişilebilmesini kontrol edebilir ve kaynak kullanımını senkronize edebilirsiniz.

### 8.2.3. Recursive Semaphore (Yeniden Girişimli Semaphore)

Maalesef, C++ standart kütüphanesi içerisinde doğrudan "Recursive Semaphore" adında bir sınıf yoktur. Ancak, senkronizasyon mekanizmaları için çeşitli kütüphaneler veya üçüncü taraf kütüphaneler Recursive Semaphore'ları destekleyebilir.

Recursive Semaphore, bir kaynağa sahip olan iş parçacıklarının veya süreçlerin aynı kaynağı birden fazla kez kullanmasına izin veren bir senkronizasyon mekanizmasıdır. Örneğin, bir iş parçacığı bir kaynağı kilitlediğinde ve ardından başka bir kaynak kullanırken aynı kaynağı tekrar kilitlemek isteyebilir. Recursive Semaphore, bu durumu destekler ve aynı iş parçacığı veya süreç tarafından kilitlenen kaynak sayısını takip eder.

Bu özellik bazen karmaşık senaryolarda veya bazı özel durumlarda gerekebilir. Eğer Recursive Semaphore benzeri bir senkronizasyon mekanizması kullanmak isterseniz, ilgili kütüphane veya üçüncü taraf çözümleri inceleyebilirsiniz. Örnek olarak, Boost C++ kütüphanesi, `boost::recursive_mutex` sınıfını içerir, bu da benzer bir işlevselliği sağlar.

İşte Boost C++ kütüphanesi ile `boost::recursive_mutex` kullanarak basit bir örnek:

```cpp
#include <iostream>
#include <boost/thread/recursive_mutex.hpp>
#include <boost/thread/thread.hpp>

boost::recursive_mutex mtx;  // Recursive Mutex

void WorkerThread(int id, int count) {
    mtx.lock();  // Mutex kilidi

    std::cout << "İş parçacığı " << id << " çalışıyor..." << std::endl;

    if (count > 0) {
        WorkerThread(id, count - 1);  // Kendi kendini çağırma
    }

    std::cout << "İş parçacığı " << id << " tamamlandı" << std::endl;

    mtx.unlock();  // Mutex kilidini serbest bırak
}

int main() {
    boost::thread t1(WorkerThread, 1, 2);
    boost::thread t2(WorkerThread, 2, 1);

    t1.join();
    t2.join();

    return 0;
}
```

Bu örnekte, Boost C++ kütüphanesinin `boost::recursive_mutex` sınıfı kullanılarak bir recursive mutex olan `mtx` oluşturulur. `WorkerThread` iş parçacıkları, `lock()` ve `unlock()` işlevlerini kullanarak mutex kilidini alır ve serbest bırakır.

Örnekte, `WorkerThread` fonksiyonu kendini tekrar çağırarak özyinelemeli bir şekilde çalışır. Bu durumda, her iş parçacığı kendini bir kez daha çağırır ve kendisi tarafından kilitlenen mutex'i tekrar kilitlemek için `boost::recursive_mutex` kullanır. Bu, aynı iş parçacığı tarafından kilitlenen kaynak sayısını takip edebilmenizi sağlar.

Bu şekilde, Boost C++ kütüphanesinin `boost::recursive_mutex` sınıfı ile bir Recursive Mutex kullanarak özyinelemeli bir iş parçacığı senaryosunu ele alabilirsiniz.

veya POSIX senkronizasyon mekanizmaları olan `pthread_mutex_t` ve `pthread_cond_t` kullanılarak Recursive Semaphore'ı uygulamak mümkündür.

Aşağıda, POSIX senkronizasyon mekanizmaları kullanılarak basit bir Recursive Semaphore örneği:

```cpp
#include <iostream>
#include <pthread.h>

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t condition = PTHREAD_COND_INITIALIZER;
int resourceCount = 0;

void RecursiveSemaphoreLock() {
    pthread_mutex_lock(&mutex);
    resourceCount++;
    pthread_mutex_unlock(&mutex);
}

void RecursiveSemaphoreUnlock() {
    pthread_mutex_lock(&mutex);
    resourceCount--;
    if (resourceCount == 0) {
        pthread_cond_signal(&condition);
    }
    pthread_mutex_unlock(&mutex);
}

void* WorkerThread(void* arg) {
    int threadId = *((int*)arg);

    RecursiveSemaphoreLock();

    std::cout << "Thread " << threadId << " entered critical section" << std::endl;

    // Recursive call
    if (threadId > 1) {
        WorkerThread((void*)&threadId);
    }

    std::cout << "Thread " << threadId << " exited critical section" << std::endl;

    RecursiveSemaphoreUnlock();

    return nullptr;
}

int main() {
    pthread_t thread1, thread2;

    int threadId1 = 1, threadId2 = 2;

    pthread_create(&thread1, nullptr, WorkerThread, (void*)&threadId1);
    pthread_create(&thread2, nullptr, WorkerThread, (void*)&threadId2);

    pthread_join(thread1, nullptr);
    pthread_join(thread2, nullptr);

    return 0;
}
```

Bu örnekte, POSIX senkronizasyon mekanizmaları olan `pthread_mutex_t` ve `pthread_cond_t` kullanılarak Recursive Semaphore benzeri bir senaryo oluşturulur. `RecursiveSemaphoreLock()` işlevi, kaynağı kilitlemek için mutex'i kullanır ve kaynak sayacını artırır. `RecursiveSemaphoreUnlock()` işlevi ise kaynağı serbest bırakmak için mutex'i kullanır ve kaynak sayacını azaltır. İş parçacığı, `WorkerThread()` işlevi içerisinde kendini tekrar çağırarak özyinelemeli bir şekilde çalışır.

Bu örnekte, iki iş parçacığı oluşturulur ve her biri Recursive Semaphore benzeri senaryoyu gerçekleştirir. İş parçacıkları sırayla kritik bölgeye girer ve çıkar. İş parçacığı, `WorkerThread()` işlevi içerisinde kendini tekrar çağırarak kritik bölgede özyinelemeli bir şekilde çalışır.

### 8.2.4. Timed Semaphore (Zaman Aşımı Olan Semaphore)

Maalesef, C++ standart kütüphanesi içerisinde doğrudan "Timed Semaphore" adında bir sınıf yoktur. Ancak, senkronizasyon mekanizmaları için çeşitli kütüphaneler veya üçüncü taraf kütüphaneler Timed Semaphore'ları destekleyebilir.

Timed Semaphore, belirli bir süre boyunca iş parçacıklarının veya süreçlerin bir kaynağı kullanmasına izin veren bir senkronizasyon mekanizmasıdır. Bu, bir iş parçacığının bir kaynağı beklerken belirli bir süre içinde kaynağın serbest bırakılmaması durumunda beklemeyi sonlandırmasını sağlar.

Bu tür senaryolar, bir iş parçacığının veya sürecin belirli bir kaynağa erişimini sınırlamak ve aşırı beklemeyi önlemek için kullanılabilir. Timed Semaphore, belirli bir zaman aşımı süresiyle beklemeyi yönetir.

Eğer Timed Semaphore benzeri bir senkronizasyon mekanizması kullanmak isterseniz, ilgili kütüphane veya üçüncü taraf çözümleri inceleyebilirsiniz. Örneğin, Boost C++ kütüphanesi, `boost::interprocess::interprocess_semaphore` sınıfını içerir, bu da zaman aşımıyla beklemeyi sağlar.

Aşağıda, Boost C++ kütüphanesi ile `boost::interprocess::interprocess_semaphore` kullanarak basit bir örnek:

```cpp
#include <iostream>
#include <boost/interprocess/sync/interprocess_semaphore.hpp>
#include <boost/thread/thread.hpp>

boost::interprocess::interprocess_semaphore sem(0);  // Timed Semaphore

void WorkerThread(int id) {
    std::cout << "İş parçacığı " << id << " kaynağı bekliyor..." << std::endl;
    if (sem.timed_wait(boost::posix_time::seconds(3))) {
        // Kaynak kullanımı
        std::cout << "İş parçacığı " << id << " kaynağı kullandı" << std::endl;
    } else {
        // Zaman aşımı durumunda
        std::cout << "İş parçacığı " << id << " zaman aşımı!" << std::endl;
    }
}

int main() {
    boost::thread t1(WorkerThread, 1);
    boost::thread t2(WorkerThread, 2);

    t1.join();
    t2.join();

    return 0;
}
```

Bu örnekte, Boost C++ kütüphanesinin `boost::interprocess::interprocess_semaphore` sınıfı kullanılarak bir Timed Semaphore olan `sem` oluşturulur. `WorkerThread` iş parçacıkları, `timed_wait()` işlevini kullanarak kaynağı belirli bir süre boyunca bekler. Eğer belirtilen süre içinde kaynak serbest bırakılmazsa, zaman aşımı durumu gerçekleşir.

`timed_wait()` işlevi, beklenen sürenin yanı sıra `boost::posix_time::seconds` kullanarak zaman aşımı süresini belirtir. İş parçacığı kaynağı başarıyla kullanabilirse, kaynak kullanımını gerçekleştirir. Zaman aşımı durumunda ise, ilgili mesajı ekrana yazdırır.

Bu şekilde, Boost C++ kütüphanesinin `boost::interprocess::interprocess_semaphore` sınıfı ile Timed Semaphore kullanarak belirli bir süre boyunca kaynak bekleyen iş parçacıklarını ele alabilirsiniz.
___

## 8.3. Spin Lock

Spin Lock, bir senkronizasyon mekanizmasıdır ve bir mutex benzeri bir işlevi yerine getirir. Spin lock, bir iş parçacığı, bir kaynağa erişim sağlamak istediğinde sürekli bir döngü içinde kaynağın serbest bırakılmasını bekler. Yani, diğer iş parçacıkları kaynağı serbest bırakana kadar sürekli olarak tekrar tekrar deneme yapar. Bu, iş parçacıkları arasında geçiş yapmak yerine aktif olarak beklemeyi içerir.

Spin lock'lar, kısa süreli kritik bölgeler veya düşük yoğunluklu iş yükleri gibi senaryolarda faydalı olabilir. Ancak, yüksek yoğunluklu iş yükleri veya uzun süreli beklemeler gerektiren senaryolarda, spin lock'ların kullanılması performans sorunlarına yol açabilir. Bu nedenle, spin lock'lar dikkatlice kullanılmalı ve senaryoya göre değerlendirilmelidir.

işte basit bir spin lock örneği:

```cpp
#include <atomic>

class SpinLock {
public:
    void Lock() {
        while (flag_.test_and_set(std::memory_order_acquire))
            ;
    }

    void Unlock() {
        flag_.clear(std::memory_order_release);
    }

private:
    std::atomic_flag flag_ = ATOMIC_FLAG_INIT;
};

// Kullanım örneği
SpinLock spinLock;
int sharedVariable = 0;

void WorkerThread() {
    spinLock.Lock();

    // Kritik bölge
    sharedVariable++;
    // Diğer işlemler

    spinLock.Unlock();
}

int main() {
    // İş parçacıklarını başlat
    std::thread t1(WorkerThread);
    std::thread t2(WorkerThread);

    // İş parçacıklarının tamamlanmasını bekle
    t1.join();
    t2.join();

    // Sonuç kontrolü
    std::cout << "Shared variable value: " << sharedVariable << std::endl;

    return 0;
}
```
___

## 8.4. Deadlock, Starvation, Livelock

Bu kısımda deadlock, starvation ve livelock kavramlarını açıklayıp, örnekler vereceğiz.

### 8.4.1. Deadlock

Deadlock, birbirini bekleyen iki veya daha fazla iş parçacığının veya sürecin, bir kaynağı elinde tutması ve diğerinin serbest bırakmasını beklemesi durumudur. Hiçbiri ilerleyemez ve program durur. Deadlock genellikle dört temel özelliğe sahip oluşur:

- Karşılıklı Bekleme (Mutual Exclusion): Kaynaklar, yalnızca tek bir iş parçacığı veya süreç tarafından kullanılabilir. Diğer iş parçacıkları veya süreçler kaynağın serbest bırakılmasını bekler.

- Kaynak Yaratma ve Tutma (Hold and Wait): Bir iş parçacığı veya süreç, sahip olduğu kaynağı serbest bırakmadan başka bir kaynağı talep eder ve bu talep karşılanana kadar bekler.

- Kaynakların Önceden Talep Edilmesi (Preemption): Bir iş parçacığı veya süreç, elindeki kaynağı bırakmadan başka bir iş parçacığı veya süreç tarafından kaynağa müdahale edilemez.

- Döngüsel Bekleme (Circular Wait): İş parçacıkları veya süreçler arasında döngüsel bir beklemeler zinciri oluşur, yani her biri diğerinin serbest bırakmasını bekler.

Örnek Deadlock Senaryosu:
```cpp
#include <iostream>
#include <mutex>
#include <thread>

std::mutex mutex1;
std::mutex mutex2;

void Thread1() {
    std::unique_lock<std::mutex> lock1(mutex1);
    std::this_thread::sleep_for(std::chrono::milliseconds(100));
    std::unique_lock<std::mutex> lock2(mutex2);
    
    // Bu noktaya asla ulaşılmaz
    std::cout << "Thread 1 çalışıyor" << std::endl;
}

void Thread2() {
    std::unique_lock<std::mutex> lock2(mutex2);
    std::this_thread::sleep_for(std::chrono::milliseconds(100));
    std::unique_lock<std::mutex> lock1(mutex1);
    
    // Bu noktaya asla ulaşılmaz
    std::cout << "Thread 2 çalışıyor" << std::endl;
}

int main() {
    std::thread t1(Thread1);
    std::thread t2(Thread2);
    
    t1.join();
    t2.join();
    
    return 0;
}
```
Bu örnekte, `Thread1` ve `Thread2` adlı iki iş parçacığı oluşturulur. Her bir iş parçacığı, önce bir mutex'i kilitleyip ardından diğer mutex'i bekler. İş parçacıkları birbirini beklerken, deadlock oluşur ve her iki iş parçacığı da ilerleyemez. Program donar ve hiçbir çıktı üretilmez.

### 8.4.2. Starvation

Starvation, bir iş parçacığının veya sürecin gereken kaynaklara erişim hakkını sürekli olarak diğer iş parçacıklarından veya süreçlerden daha düşük bir öncelikle veya hiç alamaması durumudur. Bir iş parçacığı veya süreç, diğerleri tarafından sürekli olarak engellenir ve kaynakları kullanma imkanı olmaz. Sonuç olarak, iş parçacığı veya süreç hiçbir zaman tamamlanmaz veya ilerlemez.

Örnek Starvation Senaryosu:
```cpp
#include <iostream>
#include <mutex>
#include <thread>

std::mutex mutex;

void WorkerThread(int id) {
    while (true) {
        std::unique_lock<std::mutex> lock(mutex);
        std::cout << "İş parçacığı " << id << " çalışıyor" << std::endl;
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }
}

int main() {
    std::thread t1(WorkerThread, 1);
    std::thread t2(WorkerThread, 2);
    std::thread t3(WorkerThread, 3);
    
    t1.join();
    t2.join();
    t3.join();
    
    return 0;
}
```
Bu örnekte, `WorkerThread` adlı üç iş parçacığı oluşturulur. Her bir iş parçacığı, bir mutex'i kilitleyip çalışır, ardından mutex'i serbest bırakır ve tekrar kilitleyerek çalışır. Ancak, iş parçacıkları arasında öncelik farkı olmadığından, her seferinde aynı iş parçacığı çalışırken diğerleri beklemek zorunda kalır. Bu durumda, örneğin `İş parçacığı 1` diğer iş parçacıklarından daha önceki bir zamanda çalışırken, diğer iş parçacıkları sürekli olarak beklemek zorunda kalır ve starvation durumu oluşur.

Bir başka starvation (açlık) senaryosu örneği daha verilebilir:

```cpp
#include <iostream>
#include <thread>
#include <mutex>

std::mutex mutex;
int sharedResource = 0;

void WorkerThread(int id) {
    while (true) {
        std::lock_guard<std::mutex> lock(mutex);
        if (sharedResource < 10) {
            sharedResource++;
            std::cout << "İş parçacığı " << id << " paylaşılan kaynağı artırdı: " << sharedResource << std::endl;
        }
        else {
            break;
        }
    }
}

int main() {
    std::thread t1(WorkerThread, 1);
    std::thread t2(WorkerThread, 2);
    
    t1.join();
    t2.join();
    
    return 0;
}
```

Bu örnekte, `WorkerThread` adlı iki iş parçacığı oluşturulur. Her bir iş parçacığı, bir mutex kullanarak `sharedResource` adlı bir paylaşılan değişkeni artırır. Ancak, `if` koşulu içerisinde kontrol edilen `sharedResource` değeri 10'a eşit olduğunda, iş parçacığı döngüden çıkar ve sonlanır.

Eğer `WorkerThread` iş parçacıklarından biri diğerinden daha hızlı çalışıyorsa ve `sharedResource` değişkeni hızlı bir şekilde 10'a ulaşırsa, diğer iş parçacığı sürekli olarak döngüde beklemek zorunda kalır. Bu durumda, iş parçacığı 1 hızlı bir şekilde çalışırken, iş parçacığı 2 hiçbir zaman döngüden çıkamaz ve kaynak açlığı yaşar.

Starvation durumu, bir iş parçacığının diğer iş parçacıklarının veya süreçlerin önceliklerine göre sürekli olarak engellendiği bir durumdur. Bu durum, kaynakların adaletsiz bir şekilde tahsis edildiği veya önceliklerin yanlış şekilde ayarlandığı senaryolarda ortaya çıkabilir.

Yukarıdaki örnekteki starvation sorununu çözmek için bazı stratejiler şunlar olabilir:

1. Öncelik Sırası: İş parçacıklarına veya süreçlere öncelik sırası vermek, her birinin kaynaklara erişimi konusunda adil bir şekilde rekabet etmelerini sağlar. Öncelikli iş parçacıklar veya süreçler, diğerlerinden daha önce kaynakları talep edebilir ve böylece starvation durumu azaltılabilir.

2. Kaynakları Paylaşma: İş parçacıkları veya süreçler arasında kaynakları paylaşmak, tek bir iş parçacığının veya sürecin sürekli olarak tüm kaynakları kontrol etmesini önler. Böylece, kaynakların daha dengeli bir şekilde kullanılması sağlanır ve starvation durumu azaltılır.

3. Adil Sıra: Bir kuyruk veya sıra yapısı kullanarak iş parçacıklarının veya süreçlerin kaynaklara erişimini düzenlemek, starvation durumunu önlemeye yardımcı olabilir. Her bir iş parçacığı veya süreç, sıradaki en eski talebe göre kaynaklara erişim hakkı alır ve bu şekilde adaletli bir sıra oluşturulur.

4. Önceden Allokasyon: Kaynakları iş parçacıkları veya süreçler arasında önceden tahsis etmek, starvation durumunu azaltabilir. Her bir iş parçacığı veya süreç, başlangıçta belirli bir miktar kaynağa sahip olabilir ve bu kaynakları işlem süresi boyunca kullanabilir. Bu şekilde, kaynaklara olan talepler daha adil bir şekilde dağıtılabilir.

Örnek olarak, yukarıdaki örnekte starvation sorununu çözmek için öncelik sırası verilebilir veya bir kuyruk yapısı kullanılabilir. Öncelikli iş parçacıklar veya süreçler, kaynakları talep etme önceliğine göre sırayla erişim hakkı alır. Böylece, her bir iş parçacığı veya süreç adil bir şekilde kaynakları kullanır ve starvation durumu önlenir.

#### 8.4.2.1. `std::this_thread_yield()`

Şimdi `std::this_thread::yield()` işlevinden bahsettikten sonra `starvation` durumunu önleyebilecek basit bir yaklaşım örneği vereceğim.

`std::this_thread::yield` işlevi, çalışan bir iş parçacığının diğer iş parçacıklarına CPU zaman dilimi vermesini sağlar. Diğer bir deyişle, iş parçacığı geçici olarak CPU'yu serbest bırakır ve diğer iş parçacıklarının çalışmasına izin verir.

`std::this_thread::yield` işlevi şu şekilde kullanılır:

```cpp
#include <iostream>
#include <thread>

void WorkerThread() {
    // Bazı işlemler yapılır

    std::this_thread::yield();

    // Diğer işlemler yapılır
}

int main() {
    std::thread t(WorkerThread);
    t.join();

    return 0;
}
```

Yukarıdaki örnekte, `WorkerThread` adlı bir iş parçacığı oluşturulur. İş parçacığı bazı işlemleri gerçekleştirir ve ardından `std::this_thread::yield()` işlevini kullanarak CPU zaman dilimini serbest bırakır. Böylece, iş parçacığı diğer iş parçacıklarının çalışmasına fırsat verir.

`std::this_thread::yield` işlevi, iş parçacığının CPU zaman dilimini serbest bırakmasını sağlasa da, işletim sistemi bu talebi tam olarak garanti etmez. Bu nedenle, `std::this_thread::yield` işlevinin kullanımı iş parçacığı davranışını doğrudan kontrol etmek için değil, iş parçacıkları arasında işlemci kullanımını daha adil bir şekilde paylaşmak için tercih edilir.

`std::this_thread::yield` işlevi, `<thread>` başlığı altında tanımlanır ve iş parçacığı tarafından doğrudan çağrılabilir. Bu işlev, o anki iş parçacığının CPU zaman dilimini serbest bırakmasını sağlar ve işlemi diğer iş parçacıklarına geçer.

#### 8.4.2.2. Starvation'ı Önlemek için Basit Bir Yaklaşım

```cpp
#include <iostream>
#include <thread>
#include <mutex>
#include <vector>

std::mutex mutex;
int sharedResource = 0;

void WorkerThread(int id, int priority) {
    while (true) {
        {
            std::unique_lock<std::mutex> lock(mutex);
            if (sharedResource < 10) {
                sharedResource++;
                std::cout << "İş parçacığı " << id << " paylaşılan kaynağı artırdı: " << sharedResource << std::endl;
            }
            else {
                break;
            }
        }
        std::this_thread::sleep_for(std::chrono::milliseconds(100));

        // İş parçacığı önceliğine göre yield yapar
        std::this_thread::yield();
    }
}

int main() {
    std::vector<std::thread> threads;
    threads.emplace_back(WorkerThread, 1, 1);
    threads.emplace_back(WorkerThread, 2, 2);

    for (auto& thread : threads) {
        thread.join();
    }

    return 0;
}
```

Bu örnekte, `WorkerThread` adlı iki iş parçacığı oluşturulur ve her biri bir öncelik değeriyle çağrılır. İş parçacıkları paylaşılan kaynağı artırmak için mutex kullanır ve ardından `std::this_thread::yield()` işlevini kullanarak önceliğine göre yield yapar. Böylece, öncelikli iş parçacığı bir süreliğine diğerine öncelik tanır ve starvation durumu önlenir.

Not: İş parçacığı önceliklerini doğrudan C++ standart kütüphanesi sağlamaz. İş parçacığı önceliklerini yönetmek için platforma özgü veya üçüncü taraf kütüphaneler kullanabilirsiniz. Yukarıdaki örnek, iş parçacığı önceliklerini göstermek için basit bir örnek olarak verilmiştir. Gerçek dünyada, iş parçacığı önceliklerini yönetirken dikkatli olmalı ve uygun bir yaklaşım kullanmalısınız.

### 8.4.3. Livelock

Livelock, iş parçacıklarının veya süreçlerin ilerlemek için çalışmalarına rağmen, sürekli olarak birbirlerine engel olması sonucu ortaya çıkan durumdur. İş parçacıkları veya süreçler birbirlerini beklerken sürekli olarak adım atarlar, ancak hiçbiri ilerleyemez. Bu durum, genellikle karşılıklı olarak birbirlerine yanıt vermeleriyle ilişkilidir.

Livelock durumu, deadlock durumuna benzese de, temel fark livelock'ta iş parçacıkları veya süreçler hareket halindedir ve çalışmaya devam ederken bir ilerleme sağlanamaz. İş parçacıkları veya süreçler, birbirlerine cevap vermek için adımlar atmaya devam ederler, ancak hiçbir işlem tamamlanmaz.

Livelock durumu genellikle iki veya daha fazla iş parçacığının veya sürecin birbirlerini beklemeleriyle ortaya çıkar. Örneğin, bir iş parçacığı veya süreç, başka bir iş parçacığı veya sürecin kaynakları serbest bırakmasını beklerken, diğer iş parçacığı veya süreç tam tersini yaparak aynı kaynakları serbest bırakmaya çalışır. Bu durumda, her ikisi de ilerlemek için adımlar atmaya devam ederken, birbirlerini engelleyerek livelock durumu oluşur.

Livelock durumunu çözmek zor olabilir. Genellikle, iş parçacıklarının veya süreçlerin davranışlarını kontrol etmek, karar verme mantığını değiştirmek veya senkronizasyon mekanizmalarını değiştirmek gerekebilir.

Aşağıda bir livelock örneği verilmiştir:

```cpp
#include <iostream>
#include <thread>
#include <mutex>

std::mutex mutex1;
std::mutex mutex2;

void Thread1() {
    while (true) {
        std::unique_lock<std::mutex> lock1(mutex1);
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
        std::unique_lock<std::mutex> lock2(mutex2);

        // İşlemler yapılır

        lock2.unlock();
        lock1.unlock();
    }
}

void Thread2() {
    while (true) {
        std::unique_lock<std::mutex> lock2(mutex2);
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
        std::unique_lock<std::mutex> lock1(mutex1);

        // İşlemler yapılır

        lock1.unlock();
        lock2.unlock();
    }
}

int main() {
    std::thread t1(Thread1);
    std::thread t2(Thread2);

    t1.join();
    t2.join();

    return 0;
}
```

Bu örnekte, `Thread1` ve `Thread2` adlı iki iş parçacığı oluşturulur. Her bir iş parçacığı sırasıyla `mutex1` ve `mutex2` mutex'lerini kilitlemeye çalışır. Ancak, her iki iş parçacığı da mutex'leri farklı sıralarla kilitlemeye çalışır. Bu durumda, her iki iş parçacığı da birbirlerini beklerken sürekli olarak mutex kilitleme işlemi gerçekleştirir, ancak hiçbiri ilerleme kaydedemez. İş parçacıkları birbirlerini beklerken sıkışıp kalır ve livelock durumu ortaya çıkar.

Livelock durumu, iş parçacıklarının veya süreçlerin birbirlerini engellemeleriyle ortaya çıkar. Önlemek için senkronizasyon mantığını ve mutex kilitleme sıralarını dikkatli bir şekilde düzenlemek gerekir.

Yukarıdaki livelock durumunu önlemek için düzenlenmiş bir örnek:

```cpp
#include <iostream>
#include <thread>
#include <mutex>

std::mutex mutex1;
std::mutex mutex2;

void Thread1() {
    while (true) {
        std::unique_lock<std::mutex> lock1(mutex1, std::defer_lock);
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
        std::unique_lock<std::mutex> lock2(mutex2, std::defer_lock);

        // Mutex'leri aynı anda kilitle
        std::lock(lock1, lock2);

        // İşlemler yapılır

        lock2.unlock();
        lock1.unlock();
    }
}

void Thread2() {
    while (true) {
        std::unique_lock<std::mutex> lock1(mutex1, std::defer_lock);
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
        std::unique_lock<std::mutex> lock2(mutex2, std::defer_lock);

        // Mutex'leri aynı anda kilitle
        std::lock(lock1, lock2);

        // İşlemler yapılır

        lock2.unlock();
        lock1.unlock();
    }
}

int main() {
    std::thread t1(Thread1);
    std::thread t2(Thread2);

    t1.join();
    t2.join();

    return 0;
}
```

Bu örnekte, `std::lock` işlevi kullanılarak mutex'ler aynı anda kilitleme işlemi gerçekleştirilir. Her iki iş parçacığı da mutex'leri aynı sıralarla kilitleyerek livelock durumunu önler. `std::lock` işlevi, tüm mutex'leri başarılı bir şekilde kilitleyene kadar bekler ve ardından iş parçacıklarına ilerlemelerine izin verir. Böylece, her iki iş parçacığı da mutex'leri aynı anda kilitleyerek birbirlerini beklemek yerine ilerleme kaydedebilir.

Bu düzenleme sayesinde, iş parçacıklarının mutex kilitleme sırasını düzenlemek yerine, aynı anda kilitlemeyi sağlayan `std::lock` işlevini kullanarak livelock durumu önlenir.

#### 8.4.3.1. `std::defer_lock`

`std::defer_lock`, bir `std::unique_lock` nesnesini, bir mutex'i hemen kilitlemek yerine erteleme (defer) etmek için kullanılan bir özelliktir. Kilitleme işlemi, `std::unique_lock` nesnesi üzerindeki `lock()` işlevi çağrıldığında gerçekleştirilir.

`std::defer_lock` kullanıldığında, mutex hemen kilitlemez ve `std::unique_lock`nesnesi, nesne oluşturulduğunda mutex üzerinde kilitleme işlemini gerçekleştirmez. Bu sayede, mutex kilitleme işlemi daha sonradan kontrol edilebilir ve istenildiği zaman gerçekleştirilebilir.

Aşağıda `std::defer_lock` kullanımını gösteren bir örnek verilmiştir:

```cpp
#include <iostream>
#include <thread>
#include <mutex>

std::mutex mutex;

void Thread1() {
    std::unique_lock<std::mutex> lock(mutex, std::defer_lock);

    // Kilitleme işlemini erteledik

    // İşlemler yapılır

    // Mutex'i kilitle
    lock.lock();

    // Mutex kilidini serbest bırakır
    lock.unlock();
}

void Thread2() {
    std::unique_lock<std::mutex> lock(mutex, std::defer_lock);

    // Kilitleme işlemini erteledik

    // İşlemler yapılır

    // Mutex'i kilitle
    lock.lock();

    // Mutex kilidini serbest bırakır
    lock.unlock();
}

int main() {
    std::thread t1(Thread1);
    std::thread t2(Thread2);

    t1.join();
    t2.join();

    return 0;
}
```

Yukarıdaki örnekte, `Thread1` ve `Thread2` adlı iki iş parçacığı oluşturulur. Her bir iş parçacığı, `std::unique_lock` nesnesini `std::defer_lock` ile oluşturur, yani mutex'i hemen kilitleme işlemini ertelemiş olur. Daha sonra, işlemler yapılır ve mutex kilitleme işlemi istenildiği zaman gerçekleştirilir. `lock()` işlevi çağrıldığında, mutex kilitleme işlemi gerçekleşir ve ilgili iş parçacığı mutex'i kilitleyebilir. Ardından, `unlock()` işlevi çağrılarak mutex kilidi serbest bırakılır.

`std::defer_lock` kullanımı, mutex kilitleme işlemini kontrol etmek ve kilitleme işlemini belli bir kod bloğuna odaklamak istediğimiz durumlarda faydalı olabilir. Bu sayede, kilitleme işlemi, diğer işlemler tamamlandıktan sonra ve istenilen zamanda gerçekleştirilebilir.

#### 8.4.3.2. `std::adopt_lock`

Tabii! `std::adopt_lock` bir argümandır ve `std::unique_lock` veya `std::lock_guard` nesneleriyle birlikte kullanılarak mutex kilidinin sahipliğini devralmayı ifade eder. Bu argüman, ilgili mutex'i kilitleyen iş parçacığı tarafından sahiplenilen bir mutex'i temsil eder.

`std::adopt_lock` ifadesinin kullanımı, özellikle birden fazla mutexin kilidini aynı anda elde edilmesi gereken senaryolarda yararlıdır. Bir iş parçacığı önce bir mutexi kilitleyip ardından başka bir mutexi kilitleyorsa, `std::adopt_lock` ifadesini kullanarak mutex kilidini devralabilir.

Bu ifade, iş parçacıkları arasında tutarlı bir şekilde mutex kilidi devralmayı sağlar ve senkronizasyonu düzgün bir şekilde yönetir. Ayrıca, başka bir iş parçacığı tarafından önceden kilitleme yapılmış bir mutexin kilidini almak için kullanılırken, deadlock veya yaşama kilitlenme gibi sorunlara neden olmaz.

Örneğin, aşağıdaki kod parçası `std::unique_lock` kullanarak `std::adopt_lock` ifadesini göstermektedir:

```cpp
#include <iostream>
#include <thread>
#include <mutex>

std::mutex mutex1;
std::mutex mutex2;

void Thread1() {
    std::unique_lock<std::mutex> lock1(mutex1, std::defer_lock);
    std::unique_lock<std::mutex> lock2(mutex2, std::defer_lock);

    // Mutex'leri aynı anda kilitle
    std::lock(lock1, lock2);

    // İşlemler yapılır

    lock2.unlock();
    lock1.unlock();
}

void Thread2() {
	// Mutex'leri aynı anda kilitle
	std::lock(mutex1, mutex2);

	// Zaten kilitli olan her iki muteksin de kapsamın sonunda kilidinin açık olduğundan emin olun
	std::lock_guard lock1{mutex1, std::adopt_lock};
	std::lock_guard lock2{mutex2, std::adopt_lock};
	
    // İşlemler yapılır

    lock2.unlock();
    lock1.unlock();
}

int main() {
    std::thread t1(Thread1);
    std::thread t2(Thread2);

    t1.join();
    t2.join();

    return 0;
}
```

Yukarıdaki örnekte, `Thread1` ve `Thread2` adlı iki iş parçacığı oluşturulur. Her bir iş parçacığı `std::unique_lock` nesnelerini `std::defer_lock` ile oluşturur ve `std::lock` işlevini kullanarak mutex'leri aynı anda kilitleyerek `std::adopt_lock` ifadesiyle mutex kilidini devralır. Ardından, işlemler yapılır ve `unlock()` işleviyle mutex kilidinin serbest bırakılması gerçekleştirilir.

`std::adopt_lock` ifadesi, iş parçacığı tarafından mutex kilidi devralmak için kullanılır ve daha önce başka bir iş parçacığı tarafından kilitleme yapılmış bir mutexi güvenli bir şekilde kullanmayı sağlar.

Şimdi bir başka kod örneği verelim:

```cpp
#include <mutex>
#include <thread>
#include <iostream>
 
struct bank_account {
    explicit bank_account(int balance) : balance{balance} {}
    int balance;
    std::mutex m;
};
 
void transfer(bank_account &from, bank_account &to, int amount)
{
    if(&from == &to) return; // avoid deadlock in case of self transfer
 
    // lock both mutexes without deadlock
    std::lock(from.m, to.m);
    // make sure both already-locked mutexes are unlocked at the end of scope
    std::lock_guard lock1{from.m, std::adopt_lock};
    std::lock_guard lock2{to.m, std::adopt_lock};
 
	// equivalent approach:
	//    std::unique_lock<std::mutex> lock1{from.m, std::defer_lock};
	//    std::unique_lock<std::mutex> lock2{to.m, std::defer_lock};
	//    std::lock(lock1, lock2);
 
    from.balance -= amount;
    to.balance += amount;
}
 
int main()
{
    bank_account my_account{100};
    bank_account your_account{50};
 
    std::thread t1{transfer, std::ref(my_account), std::ref(your_account), 10};
    std::thread t2{transfer, std::ref(your_account), std::ref(my_account), 5};
 
    t1.join();
    t2.join();
 
    std::cout << "my_account.balance = " << my_account.balance << "\n"
                 "your_account.balance = " << your_account.balance << '\n';
}
```

Bu kod, iki banka hesabı arasında para transferi yapan bir senaryoyu simüle etmektedir. Her bir banka hesabı `bank_account` yapısı ile temsil edilmekte ve `balance` adında bir tamsayı değişkeni ile bakiyesini tutmaktadır. Ayrıca, her bir banka hesabı için bir mutex (`m`) kullanılmaktadır.

`transfer` fonksiyonu, `from` hesabından `to` hesabına belirli bir miktarı aktarır. Fonksiyonun işleyişi şu şekildedir:

- İlk olarak, `from` ve `to` hesapları aynı hesap ise (kendine para aktarımı), fonksiyon direkt olarak sonlanır ve deadlock durumunu önlemek için işlem yapmadan geri döner.

- `from` ve `to` hesapları arasında mutex kilitleme işlemi gerçekleştirilir. `std::lock` işlevi, her iki mutex'i de aynı anda kilitleyerek deadlock durumunu önler. Mutex'lerin kilitleme sırası belirli bir algoritma tarafından belirlenir, bu durumda `from` ve `to` hesaplarının adreslerinin karşılaştırması kullanılır.

- `std::lock_guard` nesneleri kullanılarak mutex'lerin kilidi güvence altına alınır ve `std::adopt_lock` argümanıyla mutex kilidinin devralındığı belirtilir. Bu sayede, mutex'lerin kilidi, `std::lock_guard` nesnelerinin kapsamı sona erdiğinde otomatik olarak serbest bırakılır. Bu yaklaşım, güvenli ve temiz bir şekilde mutex kilitleme ve kilidi serbest bırakma işlemlerini yönetmeyi sağlar.

- Son olarak, `from` hesabından `amount` miktarı düşülür ve `to` hesabına `amount` miktarı eklenir. Böylece para transferi işlemi tamamlanmış olur.

`main` fonksiyonunda ise, iki banka hesabı (`my_account` ve `your_account`) oluşturulur. Ardından, `std::thread` kullanılarak iki ayrı iş parçacığı başlatılır ve her bir iş parçacığı üzerinde `transfer` fonksiyonu çağrılır. Her bir iş parçacığı, farklı banka hesapları arasında para transferini gerçekleştirir.

Son olarak, iş parçacıklarının tamamlanması beklenir (`t1.join()` ve `t2.join()`) ve her bir banka hesabının bakiyesi `std::cout` ile ekrana yazdırılır.

Bu kod örneği, paralel işlem yaparken mutex'lerin uygun bir şekilde kullanılmasıyla deadlock durumlarını önlemeyi ve güvenli bir şekilde senkronizasyon sağlamayı göstermektedir.

Kodun çıktısı aşağıdaki gibi olacaktır:

```
my_account.balance = 95
your_account.balance = 55
```

#### 8.4.3.3. `std::scoped_lock`

`std::scoped_lock`, C++17 standardıyla birlikte tanıtılan bir sınıftır ve birden fazla mutex'i atomik bir şekilde kilitlemek için kullanılır. Bu sınıf, `std::unique_lock` veya `std::lock_guard` yerine kullanılarak, daha güvenli ve kolay bir şekilde mutex'leri kilitleme işlemini gerçekleştirir.

`std::scoped_lock`, `std::mutex` veya `std::recursive_mutex` türünden birden fazla mutex'i alabilir ve bu mutex'leri aynı anda kilitleyerek deadlock durumlarını önler. Mutex'lerin kilitleme sırası belirli bir algoritma tarafından belirlenir.

`std::scoped_lock` sınıfı, `std::lock()` işlevini kullanarak mutex'leri kilitleme işlemini gerçekleştirir. Bununla birlikte, `std::lock_guard` veya `std::unique_lock` nesnelerinden farklı olarak, `std::scoped_lock` nesnesinin kendisi, mutex kilitleme ve kilidi serbest bırakma işlemlerini yönetir. Yani, `std::scoped_lock` nesnesi, kapsamı sona erdiğinde otomatik olarak mutex'leri serbest bırakır.

Aşağıda `std::scoped_lock` kullanımını gösteren bir örnek verilmiştir:

```cpp
#include <iostream>
#include <thread>
#include <mutex>

std::mutex mutex1;
std::mutex mutex2;

void Thread1() {
    std::scoped_lock lock(mutex1, mutex2);

    // İşlemler yapılır

    // Mutex kilidi otomatik olarak serbest bırakılır
}

void Thread2() {
    std::scoped_lock lock(mutex1, mutex2);

    // İşlemler yapılır

    // Mutex kilidi otomatik olarak serbest bırakılır
}

int main() {
    std::thread t1(Thread1);
    std::thread t2(Thread2);

    t1.join();
    t2.join();

    return 0;
}
```

Yukarıdaki örnekte, `Thread1` ve `Thread2` adlı iki iş parçacığı oluşturulur. Her bir iş parçacığı, `std::scoped_lock` nesnesini kullanarak `mutex1` ve `mutex2` mutex'lerini aynı anda kilitleyerek işlemleri gerçekleştirir. `std::scoped_lock` nesnesi, kapsamı sona erdiğinde (yani işlemler tamamlandığında) otomatik olarak mutex kilidini serbest bırakır. Bu, mutex kilitleme ve kilidi serbest bırakma işlemlerini güvenli ve kolay bir şekilde yönetir.

Bir diğer örnek olarak:

```cpp
#include <chrono>
#include <functional>
#include <iostream>
#include <mutex>
#include <string>
#include <thread>
#include <vector>
using namespace std::chrono_literals;
 
struct Employee
{
    std::vector<std::string> lunch_partners;
    std::string id;
    std::mutex m;
    Employee(std::string id) : id(id) {}
    std::string partners() const
    {
        std::string ret = "Employee " + id + " has lunch partners: ";
        for (const auto& partner : lunch_partners)
            ret += partner + " ";
        return ret;
    }
};
 
void send_mail(Employee &, Employee &)
{
    // simulate a time-consuming messaging operation
    std::this_thread::sleep_for(1s);
}
 
void assign_lunch_partner(Employee &e1, Employee &e2)
{
    static std::mutex io_mutex;
    {
        std::lock_guard<std::mutex> lk(io_mutex);
        std::cout << e1.id << " and " << e2.id << " are waiting for locks" << std::endl;
    }
 
    {
        // use std::scoped_lock to acquire two locks without worrying about
        // other calls to assign_lunch_partner deadlocking us
        // and it also provides a convenient RAII-style mechanism
 
        std::scoped_lock lock(e1.m, e2.m);
 
        // Equivalent code 1 (using std::lock and std::lock_guard)
        // std::lock(e1.m, e2.m);
        // std::lock_guard<std::mutex> lk1(e1.m, std::adopt_lock);
        // std::lock_guard<std::mutex> lk2(e2.m, std::adopt_lock);
 
        // Equivalent code 2 (if unique_locks are needed, e.g. for condition variables)
        // std::unique_lock<std::mutex> lk1(e1.m, std::defer_lock);
        // std::unique_lock<std::mutex> lk2(e2.m, std::defer_lock);
        // std::lock(lk1, lk2);
        {
            std::lock_guard<std::mutex> lk(io_mutex);
            std::cout << e1.id << " and " << e2.id << " got locks" << std::endl;
        }
        e1.lunch_partners.push_back(e2.id);
        e2.lunch_partners.push_back(e1.id);
    }
 
    send_mail(e1, e2);
    send_mail(e2, e1);
}
 
int main()
{
    Employee alice("Alice"), bob("Bob"), christina("Christina"), dave("Dave");
 
    // assign in parallel threads because mailing users about lunch assignments
    // takes a long time
    std::vector<std::thread> threads;
    threads.emplace_back(assign_lunch_partner, std::ref(alice), std::ref(bob));
    threads.emplace_back(assign_lunch_partner, std::ref(christina), std::ref(bob));
    threads.emplace_back(assign_lunch_partner, std::ref(christina), std::ref(alice));
    threads.emplace_back(assign_lunch_partner, std::ref(dave), std::ref(bob));
 
    for (auto &thread : threads)
        thread.join();
    std::cout << alice.partners() << '\n'  << bob.partners() << '\n'
              << christina.partners() << '\n' << dave.partners() << '\n';
}
```

Bu kod, bir şirketteki çalışanların öğle yemeği ortaklarını atamak için kullanılan bir senaryoyu simüle eder. `Employee` adlı bir yapı, her bir çalışanın kimlik bilgilerini, öğle yemeği ortaklarını ve bir mutex'i içerir. `send_mail` işlevi, zaman alıcı bir mesajlaşma işlemini temsil eder.

`assign_lunch_partner` işlevi, iki çalışana öğle yemeği ortağı atamak için kullanılır. İşleyiş şu şekildedir:

- İlk olarak, iki çalışanın mutex'lerini kilitleme işlemi gerçekleştirilir. `std::scoped_lock` kullanılarak iki mutex aynı anda kilitleyebilir. Bu, deadlock durumunu önlemek için uygun bir şekilde mutex'leri kilitleme işlemi yapar. Mutex kilitleme işlemi gerçekleşmeden önce, ilgili mutex'lerin kilidi bekletilmektedir.

- Ardından, iki mutex'in de başarılı bir şekilde kilidi alındığında, `io_mutex` adlı bir mutex kullanılarak bir konsol çıktısı yazdırılır.

- Daha sonra, `std::lock_guard` kullanılarak mutex'lerin kilidi otomatik olarak serbest bırakılır ve her iki çalışanın `lunch_partners` vektörlerine birbirlerinin kimlik bilgileri eklenir.

- `send_mail` işlevi, iki çalışana birbirlerine e-posta göndermeyi simüle eder.

`main` işlevinde, `Employee` yapısından dört çalışan oluşturulur. Ardından, `std::thread` kullanılarak dört farklı iş parçacığı başlatılır ve her bir iş parçacığı üzerinde `assign_lunch_partner` işlevi çağrılır. İş parçacıkları paralel olarak çalışır ve çalışanlara öğle yemeği ortakları atanır.

Son olarak, iş parçacıklarının tamamlanması beklenir (`thread.join()`) ve her bir çalışanın öğle yemeği ortakları `std::cout` ile ekrana yazdırılır.

Bu kod örneği, birden fazla mutex'i aynı anda kilitlemek için `std::scoped_lock` sınıfını kullanmanın yanı sıra, mutex kilitleme ve serbest bırakma işlemlerini güvenli bir şekilde yönetmeyi ve deadlock durumlarını önlemeyi göstermektedir. Ayrıca, öğle yemeği atama işlemi gibi uzun süren işlemlerin paralel olarak çalışabilmesini sağlar.

Kodun çıktısı aşağıdaki gibi olacaktır:

```
Alice and Bob are waiting for locks
Alice and Bob got locks
Christina and Bob are waiting for locks
Christina and Alice are waiting for locks
Dave and Bob are waiting for locks
Dave and Bob got locks
Christina and Alice got locks
Christina and Bob got locks
Employee Alice has lunch partners: Bob Christina
Employee Bob has lunch partners: Alice Dave Christina
Employee Christina has lunch partners: Alice Bob
Employee Dave has lunch partners: Bob
```
___

## 8.7. Async Fonksiyon ve `std::future`

C++'ta `async` fonksiyonları ve `std::future` sınıfını kullanarak asenkron programlama yapabiliriz. Bu bize paralel veya beklemeli işlemleri daha verimli bir şekilde yönetme imkanı sunar. 

`std::async` fonksiyonu, bir işlevi asenkron olarak çağırmak için kullanılır ve `std::future` sınıfı, bir işlemin sonucunu veya durumunu almak için kullanılır.

Öncelikle `std::async` fonksiyonunu inceleyelim:

```cpp
#include <iostream>
#include <future>

int foo(int x, int y) {
    std::cout << "foo() started" << std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(2));
    std::cout << "foo() finished" << std::endl;
    return x + y;
}

int main() {
    std::future<int> result = std::async(foo, 2, 3);
    std::cout << "Main thread continues its execution" << std::endl;
    int sum = result.get();
    std::cout << "Result: " << sum << std::endl;
    return 0;
}
```

Yukarıdaki örnekte, `foo` adlı işlevi `std::async` ile asenkron olarak çağırıyoruz. İşlev, iki parametre alır ve bu parametrelerin toplamını hesaplar. İşlevin içinde 2 saniye uyku süresi simüle edilmiştir. `std::async` fonksiyonu, işlevin asenkron olarak çağrılmasını sağlar ve bir `std::future` nesnesi döndürür. Bu nesne, işlemin sonucunu tutar.

Ana iş parçacığı `std::cout` ile "Main thread continues its execution" mesajını yazdırırken, `result.get()` çağrısı sonucun tamamlanmasını bekler ve sonucu elde eder. Sonucu `sum` değişkenine atayarak kullanabiliriz.

Çıktı şu şekilde olacaktır:

```
foo() started
Main thread continues its execution
foo() finished
Result: 5
```

Görüldüğü gibi, ana iş parçacığı `foo` işlevinin tamamlanmasını beklemek yerine iş parçacığını başlatır ve ardından devam eder. Sonucu elde etmek için `result.get()` çağrısı, sonucun tamamlanmasını bekler.

`std::async` fonksiyonunun yanı sıra, `std::future` sınıfı da önemlidir. Bu sınıf, asenkron işlemlerin sonucunu tutmak ve sonuçla ilgili operasyonlar yapmak için kullanılır.

```cpp
#include <iostream>
#include <future>

int foo(int x, int y) {
    std::cout << "foo() started" << std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(2));
    std::cout << "foo() finished" << std::endl;
    return x + y;
}

int main() {
    std::future<int> result = std::async(foo, 2, 3);
    std::cout << "Main thread continues its execution" << std::endl;
    if (result.valid()) {
        std::cout << "Result is valid" << std::endl;
    }
    int sum = result.get();
    std::cout << "Result: " << sum << std::endl;
    if (!result.valid()) {
        std::cout << "Result is no longer valid" << std::endl;
    }
    return 0;
}
```

Yukarıdaki örnekte, `std::future` sınıfının `valid()` üye işlevini kullanarak sonucun geçerli olup olmadığını kontrol ediyoruz. Sonuç başarılı bir şekilde alındıktan sonra `valid()` yanıtı `false` olur. Bu nedenle, sonuç alındıktan sonra `result` nesnesi geçersiz hale gelir ve tekrar kullanılamaz.

Çıktı şu şekilde olacaktır:

```
foo() started
Main thread continues its execution
Result is valid
foo() finished
Result: 5
Result is no longer valid
```

Bu örnekte, `result.valid()` kontrolü sayesinde sonucun geçerli olduğunu ve işlemin tamamlandığını doğrulayabiliyoruz.

`std::async` ve `std::future`, C++'ta asenkron programlama yapmak için kullanılan güçlü araçlardır. Bu araçlar, hesaplama yoğunluğu olan işlemleri paralel olarak yürütmek, beklemeli işlemleri verimli bir şekilde yönetmek ve paralel hesaplamaların sonuçlarını kullanmak için idealdir.

C++'ta `std::async` fonksiyonu, farklı politikalarla kullanılabilmektedir. Bu politikalar, işlemlerin nasıl yürütüleceğini ve hangi iş parçacığı veya iş parçacığı havuzu kullanılacağını belirler. `std::async` fonksiyonunun varsayılan politikası, sistem tarafından belirlenen bir politikadır. Ancak, C++17'den itibaren kullanıcılar, özelleştirilmiş politikaları da belirleyebilirler.

C++17'de sunulan politikalar aşağıdaki gibidir:

1. `std::launch::async`: İşlemi hemen başlatır ve yeni bir iş parçacığında çalıştırır. Bu, işlemi paralel olarak yürütmek için uygun bir seçenektir.

```cpp
#include <iostream>
#include <future>

int foo(int x, int y) {
    std::cout << "foo() started" << std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(2));
    std::cout << "foo() finished" << std::endl;
    return x + y;
}

int main() {
    std::future<int> result = std::async(std::launch::async, foo, 2, 3);
    std::cout << "Main thread continues its execution" << std::endl;
    int sum = result.get();
    std::cout << "Result: " << sum << std::endl;
    return 0;
}
```

Yukarıdaki örnekte, `std::launch::async` politikası kullanılarak `std::async` fonksiyonu çağrılmaktadır. Bu, işlemi hemen başlatır ve yeni bir iş parçacığında çalıştırır.

2. `std::launch::deferred`: İşlemi erteleyerek işlevi çağıran iş parçacığında çalıştırır. İşlev, `get()` çağrısı yapıldığında yürütülür.

```cpp
#include <iostream>
#include <future>

int foo(int x, int y) {
    std::cout << "foo() started" << std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(2));
    std::cout << "foo() finished" << std::endl;
    return x + y;
}

int main() {
    std::future<int> result = std::async(std::launch::deferred, foo, 2, 3);
    std::cout << "Main thread continues its execution" << std::endl;
    int sum = result.get();
    std::cout << "Result: " << sum << std::endl;
    return 0;
}
```

Yukarıdaki örnekte, `std::launch::deferred` politikası kullanılarak `std::async` fonksiyonu çağrılmaktadır. İşlem ertelenir ve işlev, `get()` çağrısı yapıldığında çağıran iş parçacığında çalıştırılır.

3. `std::launch::async | std::launch::deferred`: Bu, sistem tarafından belirlenen politikayı kullanır. Bu, hem asenkron hem de ertelenmiş yürütme için uygun olan en iyi seçeneği sağlar.

```cpp
#include <iostream>
#include <future>

int foo(int x, int y) {
    std::cout << "foo() started" << std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(2));
    std::cout << "foo() finished" << std::endl;
    return x + y;
}

int main() {
    std::future<int> result = std::async(std::launch::async | std::launch::deferred, foo, 2, 3);
    std::cout << "Main thread continues its execution" << std::endl;
    int sum = result.get();
    std::cout << "Result: " << sum << std::endl;
    return 0;
}
```

Yukarıdaki örnekte, `std::launch::async | std::launch::deferred` politikası kullanılarak `std::async` fonksiyonu çağrılmaktadır. Bu, hem asenkron hem de ertelenmiş yürütme için en iyi seçeneği sistem tarafından belirler.

Bu politikalar, `std::async` fonksiyonunu kullanırken işlemlerin nasıl yürütüleceğini belirlememizi sağlar. Bu sayede, paralel işlemler oluşturabilir, iş parçacığı havuzlarını kullanabilir ve beklemeli işlemleri yönetebiliriz.
___

# 8.6. İmplementasyonlar

Bu kısımda `thread-pool`, `consumer-producer`, ve `Round Robin` algoritmasının implementasyonları gerçekleştirilecektir.

### 8.6.1. Thread Pool

Elbette! İşte C++20 özelliklerini kullanarak bir thread havuzu (thread pool) implementasyonu örneği:

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <functional>
#include <thread>
#include <condition_variable>

class ThreadPool {
public:
    ThreadPool(size_t numThreads) : stop(false) {
        for (size_t i = 0; i < numThreads; ++i) {
            threads.emplace_back([this] {
                while (true) {
                    std::function<void()> task;

                    {
                        std::unique_lock<std::mutex> lock(queueMutex);
                        condition.wait(lock, [this] { return stop || !tasks.empty(); });
                        
                        if (stop && tasks.empty()) {
                            return;
                        }
                        
                        task = std::move(tasks.front());
                        tasks.pop();
                    }

                    task();
                }
            });
        }
    }

    ~ThreadPool() {
        {
            std::unique_lock<std::mutex> lock(queueMutex);
            stop = true;
        }
        
        condition.notify_all();
        
        for (std::thread& thread : threads) {
            thread.join();
        }
    }

    template <typename Func, typename... Args>
    void enqueue(Func&& func, Args&&... args) {
        auto task = std::bind(std::forward<Func>(func), std::forward<Args>(args)...);

        {
            std::unique_lock<std::mutex> lock(queueMutex);
            tasks.emplace([task] { task(); });
        }

        condition.notify_one();
    }

private:
    std::vector<std::thread> threads;
    std::queue<std::function<void()>> tasks;

    std::mutex queueMutex;
    std::condition_variable condition;
    bool stop;
};

// Kullanım örneği
void printNumber(int number) {
    std::cout << "Thread ID: " << std::this_thread::get_id() << ", Number: " << number << std::endl;
}

int main() {
    ThreadPool pool(4);

    // İş parçacıklarını havuza ekleyelim
    for (int i = 0; i < 10; ++i) {
        pool.enqueue(printNumber, i);
    }

    // Tüm iş parçacıklarının tamamlanmasını bekleyelim
    std::this_thread::sleep_for(std::chrono::seconds(2));

    return 0;
}
```

Bu örnek, `std::function`, `std::bind`, `std::thread`, `std::mutex`, `std::condition_variable` ve `std::unique_lock` gibi bileşenleri kullanarak basit bir thread havuzu (thread pool) implementasyonu sağlar. `ThreadPool` sınıfı, belirli bir sayıda iş parçacığı oluşturur ve iş parçacığı havuzuna iş parçacıklarını eklemek ve çalıştırmak için `enqueue` işlevini sağlar.

İşte kodun açıklaması:

- `ThreadPool` sınıfı, önceden belirlenmiş bir sayıda iş parçacığı oluşturur. Bu sayı, sınıfın yapıcı fonksiyonuna verilen `numThreads` parametresiyle belirlenir.

- `enqueue` işlevi, thread havuzuna bir iş parçacığı eklemek için kullanılır. Bu işlev, farklı parametre türleriyle çağrılabilen bir şablon işlevdir.

- Thread havuzunun oluşturulduğu yapıcı fonksiyonda, her iş parçacığı için bir lambda ifadesi oluşturulur. Bu lambda ifadesi, iş parçacığı tarafından sürekli olarak çalıştırılacak bir döngüye sahiptir.

- İş parçacığı döngüsü, thread havuzunun durdurulmadığı sürece çalışır. Döngüde, önce bir `std::function<void()>` görevi tanımlanır.

- Ardından, görevi almak için bir `std::unique_lock<std::mutex>` oluşturulur ve `std::condition_variable` üzerinde beklenir. `condition.wait()` işlevi, bir lambda ifadesi kullanarak, havuzun durdurulması veya görevlerin boşaltılması durumunda beklemeyi sonlandırır.

- Döngü, havuz durdurulduğunda veya görevler bittiğinde sonlanır.

- `enqueue` işlevi, bir görevi thread havuzuna eklemek için kullanılır. İşlev, görevi bir `std::function<void()>` nesnesine bağlar ve bu görevi bir kuyruğa ekler.

- Ardından, `std::condition_variable` üzerinde bir `condition.notify_one()` işlemi gerçekleştirerek bekleyen bir iş parçacığın uyandırılmasını sağlar.

- `~ThreadPool` yapıcısı, thread havuzu nesnesi sona erdiğinde çalışır. İlk olarak, havuzu durdurmak için `stop` bayrağı ayarlanır.

- Ardından, `std::condition_variable` üzerinde bir `condition.notify_all()` işlemi gerçekleştirerek tüm bekleyen iş parçacıklarını uyandırır.

- Son olarak, tüm iş parçacıklarının tamamlanmasını beklemek için `std::thread::join()` işlevi kullanılır.

- `printNumber` işlevi, her bir iş parçacığı tarafından çalıştırılan basit bir işlevdir. İş parçacığı kimliğini ve bir sayıyı ekrana yazdırır.

- `main` fonksiyonunda, bir `ThreadPool` nesnesi oluşturulur ve `enqueue` işlevi kullanılarak iş parçacıkları havuza eklenir.

- Son olarak, tüm iş parçacıklarının tamamlanmasını beklemek için `std::this_thread::sleep_for()` işlevi kullanılır ve program sonlanır.

Bu örnek, basit bir thread havuzu implementasyonunu göstermektedir. Thread havuzları, aynı anda çok sayıda görevi paralel olarak çalıştırmak için kullanılabilir ve iş parçacıklarının yönetimi ve senkronizasyonu gibi karmaşık detayları gizler. Bu sayede, çoklu iş parçacığı uygulamalarında performansı artırabilir ve kaynakları daha verimli bir şekilde kullanabilirsiniz.

### 8.6.2. Consumer-Producer

#### 8.6.2.1. Basit İmplementasyon

Basit bir Consumer-Producer kodu:

```cpp
#include <iostream>
#include <thread>
#include <queue>
#include <mutex>
#include <condition_variable>

std::queue<int> buffer;
const int BUFFER_SIZE = 10;

std::mutex mutex;
std::condition_variable cv;

void Producer()
{
    for (int i = 1; i <= 20; ++i) {
        std::this_thread::sleep_for(std::chrono::milliseconds(500)); // Üretim süresi
        std::unique_lock<std::mutex> lock(mutex);

        // Buffer dolu ise bekle
        cv.wait(lock, [] { return buffer.size() < BUFFER_SIZE; });

        buffer.push(i); // Üretim
        std::cout << "Producer produced: " << i << std::endl;

        lock.unlock(); // Mutex kilidini aç
        cv.notify_all(); // Tüketicilere haber ver
    }
}

void Consumer()
{
    while (true) {
        std::this_thread::sleep_for(std::chrono::milliseconds(800)); // Tüketim süresi
        std::unique_lock<std::mutex> lock(mutex);

        // Buffer boş ise bekle
        cv.wait(lock, [] { return !buffer.empty(); });

        int value = buffer.front(); // Tüketim
        buffer.pop();
        std::cout << "Consumer consumed: " << value << std::endl;

        lock.unlock(); // Mutex kilidini aç
        cv.notify_all(); // Üreticiye haber ver

        if (value == 20) {
            break; // Tüketim tamamlandı, döngüyü sonlandır
        }
    }
}

int main()
{
    std::thread producerThread(Producer);
    std::thread consumerThread(Consumer);

    producerThread.join();
    consumerThread.join();

    return 0;
}
```

Bu kodda, basit bir Consumer-Producer senaryosu gerçekleştirilir. `buffer` adlı bir kuyruk yapısı kullanarak üretici işlem tarafından üretilen değerlerin tüketici işlem tarafından tüketilmesi sağlanır.

`Producer` işlevi, 1'den 20'ye kadar olan sayıları üretir ve `buffer` kuyruğuna ekler. Her bir üretim arasında bir süre beklenir. Eğer `buffer` kuyruğu dolu ise, üretici işlem `cv.wait()` ile beklemeye alınır. Üretim gerçekleştikten sonra mutex kilidi açılır, tüketici işlemlere haber verilir ve işlem tekrar beklemeye alınır.

`Consumer` işlevi, `buffer` kuyruğundan değerleri tüketir. Eğer `buffer` kuyruğu boş ise, tüketici işlem `cv.wait()` ile beklemeye alınır. Değer tüketildikten sonra mutex kilidi açılır, üretici işleme haber verilir ve işlem tekrar beklemeye alınır. Son olarak, tüketim tamamlandığında döngüden çıkılır ve işlem sonlandırılır.

Ana işlevde, üretici ve tüketici işlemler oluşturulur, beklenir ve ardından program sonlandırılır.

Bu örnek kod, basit bir Consumer-Producer senaryosunu semafor olmadan gerçekleştirir. İki işlem arasında veri paylaşımını kontrol etmek için mutex ve condition variable kullanılır.

#### 8.6.2.2. Semaphore Kullanımı ile

```cpp
#include <iostream>
#include <thread>
#include <vector>
#include <condition_variable>

class Semaphore {
public:
    explicit Semaphore(int count = 0) : count_(count) {}

    void Notify() {
        std::unique_lock<std::mutex> lock(mutex_);
        ++count_;
        cv_.notify_one();
    }

    void Wait() {
        std::unique_lock<std::mutex> lock(mutex_);
        cv_.wait(lock, [this] { return count_ > 0; });
        --count_;
    }

private:
    std::mutex mutex_;
    std::condition_variable cv_;
    int count_;
};

const int BUFFER_SIZE = 5;
std::vector<int> buffer(BUFFER_SIZE);
Semaphore emptySlots(BUFFER_SIZE);
Semaphore fullSlots;
std::mutex mutex;

void Producer(int producerId)
{
    for (int i = 1; i <= 10; ++i) {
        emptySlots.Wait();  // Boş yuva sayısını kontrol et
        std::lock_guard<std::mutex> lock(mutex);  // Buffer'ı kilitle
        buffer[i % BUFFER_SIZE] = i;  // Üretilen veriyi buffer'a ekle
        std::cout << "Producer " << producerId << " produced: " << i << std::endl;
        fullSlots.Notify();  // Dolu yuva sayısını artır
        std::this_thread::sleep_for(std::chrono::milliseconds(500));  // Biraz bekle
    }
}

void Consumer(int consumerId)
{
    for (int i = 1; i <= 10; ++i) {
        fullSlots.Wait();  // Dolu yuva sayısını kontrol et
        std::lock_guard<std::mutex> lock(mutex);  // Buffer'ı kilitle
        int value = buffer[i % BUFFER_SIZE];  // Buffer'dan veriyi al
        std::cout << "Consumer " << consumerId << " consumed: " << value << std::endl;
        emptySlots.Notify();  // Boş yuva sayısını artır
        std::this_thread::sleep_for(std::chrono::milliseconds(800));  // Biraz bekle
    }
}

int main()
{
    std::thread producerThread(Producer, 1);
    std::thread consumerThread(Consumer, 1);

    producerThread.join();
    consumerThread.join();

    return 0;
}
```

Bu kod, Consumer-Producer senaryosunu semaforlar kullanarak gerçekleştirir.

`Semaphore` adlı bir sınıf tanımlanır. Bu sınıf, mutex ve condition variable kullanarak semafor işlevselliğini sağlar. `Notify()` işlevi semaforu artırır ve bekleyen iş parçacıklarını uyarır. `Wait()` işlevi ise semaforu kontrol eder ve uygun koşulu bekleyerek azaltır.

Ana fonksiyon olan `main()` işlevi, bir üretici ve bir tüketici iş parçacığı oluşturur. Bu iş parçacıkları `producerThread` ve `consumerThread` olarak adlandırılır.

`Producer` işlevi, 1'den 10'a kadar olan sayıları üretir ve buffer'a ekler. İlk olarak, `emptySlots.Wait()` işlevi kullanılarak boş yuva sayısı kontrol edilir. Eğer boş yuva mevcut değilse, üretici beklemek zorunda kalır. Ardından, `std::lock_guard` kullanılarak `mutex` kilidi alınır ve buffer'a veri eklenir. Üretilen değer ekrana yazdırılır. Son olarak, `fullSlots.Notify()` işlevi kullanılarak dolu yuva sayısı artırılır ve bir süre beklenir.

`Consumer` işlevi, 1'den 10'a kadar olan sayıları tüketir. İlk olarak, `fullSlots.Wait()` işlevi kullanılarak dolu yuva sayısı kontrol edilir. Eğer dolu yuva mevcut değilse, tüketici beklemek zorunda kalır. Ardından, `std::lock_guard` kullanılarak `mutex` kilidi alınır ve buffer'dan veri alınır. Tüketilen değer ekrana yazdırılır. Son olarak, `emptySlots.Notify()` işlevi kullanılarak boş yuva sayısı artırılır ve bir süre beklenir.

Son olarak, `producerThread` ve `consumerThread` iş parçacıkları `join()` işlevi ile beklenir ve program sonlanır.

Bu kod, semaforları kullanarak üretici ve tüketici iş parçacıkları arasında senkronizasyon sağlar. Semaforlar, boş yuva ve dolu yuva sayılarını kontrol ederek üretici ve tüketici işlemlerin senkronize bir şekilde çalışmasını sağlar. Mutex, buffer'a eşzamanlı erişimi kontrol eder ve veri bütünlüğünü sağlar.

### 8.6.3 Round Robin Algoritması

Round Robin (RR), bir işlemci zaman paylaşımı (scheduling) algoritmasıdır. Bu algoritma, bir dizi işlem arasında zamanı eşit bir şekilde böler ve işlemcilere sırayla paylaştırır. Her bir işlem belirli bir zamana kadar çalışır ve ardından işlemci diğer işleme geçer. Bu şekilde, işlemciler arasında adil bir dağılım sağlanır ve her bir işlem belirli bir zaman diliminde çalışma fırsatı bulur.

Round Robin algoritmasının temel özellikleri şunlardır:

- İşlemciler arasında zaman dilimleri eşit olarak paylaştırılır. Her bir işlem, belirli bir zaman diliminde çalışır (sabit bir zaman dilimi veya kuantum olarak adlandırılır).
- İşlemciler, sırayla işlemleri çalıştırır. İlk işlem tamamlanmadan diğer işleme geçilmez, kuantum süresi dolduğunda işlemci diğer işleme geçer.
- İşlemciler arasında adil bir zaman paylaşımı sağlar. Her işlem, aynı miktarda işlemci zamanı alır ve öncelikli bir işlemi diğerlerinden ayırt etmez.

Round Robin algoritması, çoklu kullanıcılı işletim sistemlerinde ve zaman paylaşımı gerektiren ortamlarda yaygın olarak kullanılır. Özellikle interaktif uygulamalar ve çoklu iş parçacıklı programlar için uygundur. Bu algoritma, işlemciler arasında iş yükünün dengeli bir şekilde dağıtılmasını sağlar ve cevap süresini adil bir şekilde dağıtır.

Örneğin, bir Round Robin algoritmasıyla çalışan bir işletim sistemi, her bir kullanıcıya sırayla zaman paylaştırabilir. Her kullanıcı, belirli bir kuantum süresi boyunca işlemciyi kullanabilir ve ardından diğer kullanıcıya geçiş yapılır. Bu şekilde, kullanıcılar arasında eşit ve adil bir işlemci kullanımı sağlanır.

Round Robin algoritması, basit ve adil bir işlemci zaman paylaşımı yöntemi sağlar. Ancak, tüm işlemlerin aynı öneme sahip olduğunu varsayar ve işlem sürelerinin sabit olduğunu varsayarak çalışır. Gerçek dünya senaryolarında, bazı işlemler diğerlerinden daha fazla işlemci zamanı talep edebilir veya işlem süreleri değişkenlik gösterebilir. Bu durumda, Round Robin algoritması optimize edilmiş diğer zaman paylaşımı algoritmalarıyla değiştirilebilir.

#### 8.6.3.1. Basit İmplementasyon

Bu kod, Round Robin algoritmasının basit bir örneğini göstermektedir. Kod, kullanıcı tarafından tanımlanan görevleri temsil eden `Task` yapısını kullanır ve bu görevleri Round Robin algoritmasına göre zaman paylaşımı ile sırayla çalıştırır.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

struct Task {
    int id;
    int remainingTime;
    int priority;
    void (*executeFunction)();
};

void taskFunction1() {
    std::cout << "Executing Task 1 function" << std::endl;
}

void taskFunction2() {
    std::cout << "Executing Task 2 function" << std::endl;
}

void taskFunction3() {
    std::cout << "Executing Task 3 function" << std::endl;
}

void roundRobin(std::vector<Task>& tasks, int quantum) {
    int numTasks = tasks.size();
    int currentTime = 0;
    bool isCompleted = false;

    while (!isCompleted) {
        isCompleted = true;

		// Sort tasks based on priority 
		std::sort(tasks.begin(), tasks.end(), [](const Task &t1, const Task &t2){
			return t1.priority < t2.priority;
		});
        
        for (auto& task : tasks) {
            if (task.remainingTime > 0) {
                isCompleted = false;
                int executeTime = std::min(quantum, task.remainingTime);
                task.remainingTime -= executeTime;
                currentTime += executeTime;
                std::cout << "Task " << task.id << " executed for " << executeTime << " units. Current time: " << currentTime << std::endl;
                task.executeFunction();
            }
        }
    }
}

int main() {
    std::vector<Task> tasks = {
        {1, 10, 2, taskFunction1},
        {2, 4, 1, taskFunction2},
        {3, 5, 3, taskFunction3}
    };
    int quantum = 3;

    roundRobin(tasks, quantum);

    return 0;
}
```

Kodun açıklaması:

- İlk olarak, `Task` yapısı tanımlanır. Bu yapı, görevin kimliği (`id`), kalan süresi (`remainingTime`), önceliği (`priority`) ve yürütme fonksiyonunu (`executeFunction`) içerir.
- Ardından, her bir görevin yürütülmesini sağlayan üç adet örnek yürütme fonksiyonu (`taskFunction1`, `taskFunction2`, `taskFunction3`) tanımlanır. Bu fonksiyonlar sadece ilgili görevin yürütüldüğünü ekrana yazdırır.
- `roundRobin` işlevi tanımlanır. Bu işlev, görevleri Round Robin algoritması kullanarak zaman paylaşımı ile sırayla çalıştırır. İşlev, görevlerin listesini (`tasks`) ve kuantum süresini (`quantum`) parametre olarak alır.
- `roundRobin` işlevi içinde, görevlerin sayısı (`numTasks`), geçerli zamanı (`currentTime`) ve tüm görevlerin tamamlandığını belirten bir bayrak (`isCompleted`) tanımlanır.
- Döngü içinde, görevlerin sırasını önceliklerine göre sıralamak için `std::sort` kullanılır. Bu şekilde, her turda öncelikli görevlerin önce çalıştırılması sağlanır.
- Döngü içinde, her bir görevin süresi (`remainingTime`) kontrol edilir. Eğer süre sıfırdan büyük ise görev henüz tamamlanmamış demektir. Bu durumda, en fazla kuantum süresi kadar çalışma yapılır. Görevin kalan süresi ve geçerli zaman güncellenir. Ayrıca, çalıştırma süresi ve geçerli zaman ekrana yazdırılır.
- Son olarak, görevin ilgili yürütme fonksiyonu çağrılır.
- Döngü, tüm görevlerin tamamlandığı (`isCompleted` bayrağı `true` olduğu) duruma kadar devam eder.
- `main` işlevinde, örnek görevler (`tasks`) ve kuantum süresi (`quantum`) tanımlanır.
- `roundRobin` işlevi çağrılır ve görevler Round Robin algoritmasıyla sırayla çalıştırılır.
- Program sonlanır.

Bu kod, basit bir şekilde Round Robin algoritmasını uygulamaktadır. Önceliklere göre sıralama ve kuantum süresine göre işlem sürelerini belirleme gibi algoritmanın temel prensiplerini içerir. Daha gerçekçi senaryolar için farklı optimizasyonlar ve senkronizasyon mekanizmaları gerekebilir.

#### 8.6.3.2. Consumer-Producer Implemantasyonu

Bu kod, Consumer-Producer modelini kullanarak Round Robin algoritmasını simüle eder. 

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <thread>
#include <mutex>
#include <condition_variable>

struct Task {
    int id;
    int remainingTime;
    int priority;
    void (*executeFunction)();
};

void taskFunction1() {
    std::cout << "Executing Task 1 function" << std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(1));  // Simulating task execution time
}

void taskFunction2() {
    std::cout << "Executing Task 2 function" << std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(2));  // Simulating task execution time
}

void taskFunction3() {
    std::cout << "Executing Task 3 function" << std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(3));  // Simulating task execution time
}

bool comparePriority(const Task& task1, const Task& task2) {
    return task1.priority < task2.priority;
}

std::mutex mtx;
std::condition_variable cv;
std::vector<Task> taskQueue;
bool isCompleted = false;

void producer() {
    std::this_thread::sleep_for(std::chrono::seconds(1));  // Simulating task arrival time

    std::lock_guard<std::mutex> lock(mtx);
    taskQueue.push_back({1, 10, 2, taskFunction1});
    taskQueue.push_back({2, 4, 1, taskFunction2});
    taskQueue.push_back({3, 5, 3, taskFunction3});

    std::cout << "Tasks produced." << std::endl;

    cv.notify_one();
}

void consumer(int quantum) {
    while (true) {
        std::unique_lock<std::mutex> lock(mtx);
        cv.wait(lock, [] { return !taskQueue.empty() || isCompleted; });

        if (isCompleted && taskQueue.empty()) {
            break;
        }

        Task task = taskQueue.front();
        taskQueue.erase(taskQueue.begin());
        lock.unlock();

        int executeTime = std::min(quantum, task.remainingTime);
        task.remainingTime -= executeTime;

        std::cout << "Task " << task.id << " executed for " << executeTime << " units." << std::endl;
        task.executeFunction();

        if (task.remainingTime > 0) {
            lock.lock();
            taskQueue.push_back(task);
            lock.unlock();
        }
        else {
            std::cout << "Task " << task.id << " completed." << std::endl;
        }
    }
}

int main() {
    int quantum = 3;
    std::thread producerThread(producer);
    std::thread consumerThread(consumer, quantum);

    producerThread.join();
    isCompleted = true;
    cv.notify_all();
    consumerThread.join();

    std::cout << "All tasks completed." << std::endl;

    return 0;
}
```

Kodun açıklaması:

- `Task` yapısı, görevin kimliği (`id`), kalan süresi (`remainingTime`), önceliği (`priority`) ve yürütme fonksiyonunu (`executeFunction`) içerir.
- `taskFunction1`, `taskFunction2` ve `taskFunction3` fonksiyonları, her bir görevin yürütme işlevini temsil eder ve sadece görevin yürütüldüğünü ekrana yazdırır. Aynı zamanda, `std::this_thread::sleep_for` işlevini kullanarak görevin yürütme süresini simüle eder.
- `comparePriority` işlevi, görevleri önceliğe göre sıralamak için kullanılan karşılaştırma fonksiyonudur.
- `mtx` (mutex) ve `cv` (condition_variable) değişkenleri, senkronizasyon ve senkronizasyon olaylarını yönetmek için kullanılır.
- `taskQueue` vektörü, üretilen görevlerin depolandığı kuyruğu temsil eder.
- `isCompleted` bayrağı, tüm görevlerin tamamlandığını belirtmek için kullanılır.
- `producer` işlevi, üretici iş parçacığı tarafından çağrılır ve belirli bir süre bekledikten sonra görevleri üretir. Üretilen görevler `taskQueue` kuyruğuna eklenir ve `cv.notify_one()` çağrısı ile tüketici iş parçacığına haber verilir.
- `consumer` işlevi, tüketici iş parçacığı tarafından çağrılır ve görevleri tüketir. `cv.wait()` işlevi ile görevlerin üretilmesini bekler ve uyandırıldığında `taskQueue` kuyruğunda görevlerin olup olmadığını kontrol eder. Görev varsa, en öncelikli görevi alır ve yürütür. Görevin kalan süresi hesaplanır ve `std::this_thread::sleep_for` işleviyle yürütme süresi simüle edilir. Eğer görevin kalan süresi sıfırdan büyükse, kuyruğa geri eklenir, aksi halde tamamlandığı ekrana yazdırılır. Daha sonra, işlemci kilitlenmesi çözülerek diğer görevlere erişim sağlanır.
- `main` işlevi, kuantum süresini belirler ve üretici ve tüketici iş parçacıklarını başlatır. İşlemler tamamlandığında bayrak ve `cv.notify_all()` çağrısı kullanılarak tüketici iş parçacığına haber verilir. Son olarak, program tamamlanmış görevleri ekrana yazdırır.

Bu kod, bir görev kuyruğu üzerinde Round Robin algoritmasını simüle etmektedir. Üretici iş parçacığı görevleri üretirken, tüketici iş parçacığı da görevleri alarak belirli bir süreyle çalıştırır. Her görevin kuantum süresi kullanılarak adil bir şekilde işlem paylaşımı sağlanır.
