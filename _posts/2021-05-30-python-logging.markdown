---
layout: post
title: Python3 - Logging
date: 2021-05-30 00:00:00 +0300
description: Python'da logging modülünün kullanımı ve hazır template'inin sunulması amaçlanmaktadır.
lang: tr
img: software.jpg
tags: [Python, Logging]
contents: 
- 1;Standart Seviyeler;standart-seviyeler'
- 1;Basit Konfigürasyonlar;basit-konfigürasyonlar'
- 1;Çıktının Formatlanması;çıktının-formatlanması'
- 1;Değişkenlerin Kullanımı;değişkenlerin-kullanımı'
- 2;% Formatlama;-formatlama'
- 2;F-String;f-string'
- 2;Format Fonksiyonu;format-fonksiyonu'
- 1;Hata Mesajlarının Yakalanması;hata-mesajlarının-yakalanması'
- 1;Konfigürasyonlar;konfigürasyonlar'
- 2;Kaynak Kod Tabanlı;kaynak-kod-tabanlı'
- 2;Dosya Tabanlı;dosya-tabanlı'
- 2;Üretim Şablonu;üretim-şablonu'
---

# Giriş

Log'lama yazılım mühendislerinin en iyi debug araç-gereçleri arasında yer almaktadır. Uzun bir süre koşacak kodunuz için *(servis uygulaması olabilir)*  ön görülmeyen durumlarda ki çökmeler veya hataların saptanmasında yardımcı olabilmektedir.

Kısaca log'lamayı, uygulamamızın tuttuğu günlük defterlerine benzetebiliriz. Biraz daha açmak gerekirse, karşılaştığı bütün durumları, durum etiketleriyle birlikte içini bir dosyaya dökmesi olarak betimleyebiliriz.

------

# Standart Seviyeler

Olayların durum önceliğine göre *(yukarıdan-aşağıya doğru öncelikler artmaktadır)* 5 standart seviye yer almaktadır.

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

Standart durumların entegrasyonu aşağıdaki gibi sağlanmaktadır.

```python
import logging

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
```

```shell
WARNING:root:This is a warning message
ERROR:root:This is an error message
CRITICAL:root:This is a critical message
```

------

# Basit Konfigürasyonlar

`basicConfig()` fonksiyonu için yer alan bazı parametreler:

- `level`: The root logger will be set to the specified severity level.
- `filename`: This specifies the file.
- `filemode`: If `filename` is given, the file is opened in this mode. The default is `a`, which means append.
- `format`: This is the format of the log message.

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')
```

```shell
DEBUG:root:This will get logged
```

Yukarıda yer aldığı gibi, DEBUG takma ismi ile gerçekleşen bütün olaylar kayıt altına alınacaktır.

```python
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')
```

```shell
root - ERROR - This will get logged to a file
```

Olay mesajı yukarıdaki gibi görünecektir, ancak konsol yerine app.log adlı bir dosyaya yazılacaktır.
Dosya modu `w` olarak ayarlanmıştır, yani `basicConfig()` her çağrıldığında günlük dosyası "yazma modunda" açılır ve programın her çalışması dosyayı yeniden yazar. Dosya modu için varsayılan yapılandırma, eklemeli kayıt olan `a`'dır.

> Parametrelerin detayı için [dökümantasyon](https://docs.python.org/3/library/logging.html#logging.basicConfig)'a bakabilirsiniz.

___

# Çıktının Formatlanması

Günlük dosyasına kaydedilecek mesajların, formatını belirtebiliriz. 

Aşağıdaki örnekte `process id (int)- levelname (string) - message (string)` olacak şekilde formatlandırma gerçekleştirilmektedir.  

```python
import logging
logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning('Bu bir uyarıdır.')
```



```shell
18472-WARNING-Bu bir uyarıdır.
```

> Parametrelerin detayı için [dökümantasyon](https://docs.python.org/3/library/logging.html#logrecord-attributes)'a bakabilirsiniz.

Bir başka örnek olarak, `asctime (string) - message (string)` formatı  verildiğinde sistem zamanının insanın anlayacağı format olan `yıl-ay-gün saat:dakika:saniye,milisaniye` şeklinde zaman etiketi ve mesajın konsola yazdırıldığını göreceğiz.

```python
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Yönetici giriş yaptı')
```



```shell
2018-07-11 20:12:06,288 - Yönetici giriş yaptı
```

`%(asctime)s`,  `LogRecord`un gerçekleştiği tarihi ekler. Format `datefmt` özelliği kullanılarak değiştirilebilir, bu özellik datetime modülündeki, formatlama fonksiyonlarından biri olan `time.strftime()` kullanımı ile benzerlik göstermektedir.

```python
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.warning('Yönetici çıkış yaptı')
```



```shell
12-Jul-18 20:53:19 - Yönetici çıkış yaptı
```

___

# Değişkenlerin Kullanımı

Günlük dosyaları içerisinde değişkenlerin kullanılması mesajın formatlanmasıyla eşdeğer bir durumdur.

Python programlama dilinde,

- % formatlama 
- F-String
- Format Fonksiyonu

yöntemleri ile mesaj içerisine değişkenlerimizi yerleştirebiliriz.



## % Formatlama

```python
import logging

name = 'Burak'
logging.error('%s raised an error', name)
```



```shell
ERROR:root:Burak raised an error
```

## F-String

```python
import logging

name = 'Burak'
logging.error(f'{name} raised an error')
```

```shell
ERROR:root:Burak raised an error
```

## Format Fonksiyonu

```python
import logging

name = "Burak"
logging.error("{} raised an error".format(name))
```

```
ERROR:root:Burak raised an error
```

___

# Hata Mesajlarının Yakalanması

Günlük dosyalarına yakananan hataların detayları ile kaydedilmesine değineceğiz.

Python'da try-catch bloğu ile yakanan bir hatanın detayını aşağıdaki gibi öğrenebilmekteyiz.

```python
import sys

a = 5
b = 0

try:
    c = a / b
except Exception as e:
    print("Hata Mesajı:", e) # Hata mesajını yazdır
    print("Hata Mesajı Detayı:", sys.exc_info()) # Hata mesajının detayını yazdır
```

```shell
Hata Mesajı: division by zero 
Hata Mesajı Detayı: (<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero'), <traceback object at 0x0000025101DA7780>)
```



Benzer şekilde günlük kayıtlarımızı tutarken karşılaşılan hataları detayları ile birlikte kayıt almamız mümkün.

```python
import logging

a = 5
b = 0

try:
  c = a / b
except Exception as e:
  logging.error("Exception occurred", exc_info=True)
```

```shell
ERROR:root:Exception occurred
Traceback (most recent call last):
  File "exceptions.py", line 6, in <module>
    c = a / b
ZeroDivisionError: division by zero
[Finished in 0.2s]
```

exc_info True olarak ayarlanmazsa, yukarıdaki programın çıktısı, gerçek dünya senaryosunda ZeroDivisionError kadar basit olmayabilecek istisna hakkında bize hiçbir şey söylemez. 

Yalnızca şunu gösteren bir günlükle karmaşık bir kod tabanındaki bir hatayı ayıklamaya çalıştığınızı düşünün:

```shell
ERROR:root:Exception occurred
```

İşte size kısa bir ipucu: Bir istisna işleyiciden giriş yapıyorsanız, ERROR düzeyine sahip bir mesajı günlüğe kaydeden ve mesaja istisna bilgisi ekleyen logging.exception() yöntemini kullanabilirsiniz. 

Daha basit ifade etmek gerekirse, logging.exception() öğesini çağırmak, logging.error(exc_info=True) öğesini çağırmak gibidir. Ancak bu yöntem her zaman istisna bilgilerini döktüğünden, yalnızca bir istisna işleyicisinden çağrılmalıdır. Bu örneğe bir göz atın:

```python
import logging

a = 5
b = 0
try:
  c = a / b
except Exception as e:
  logging.exception("Exception occurred")
```

```shell
ERROR:root:Exception occurred
Traceback (most recent call last):
  File "exceptions.py", line 6, in <module>
    c = a / b
ZeroDivisionError: division by zero
[Finished in 0.2s]
```

logging.exception() kullanılması, ERROR seviyesinde bir günlük kaydı gösterir. Bunu istemiyorsanız, debug() ile critical() arasındaki yöntemlerden herhangi birini çağırırken exc_info parametresini True olarak olarak belirtebilirsiniz.

___

# Konfigürasyonlar

Bu bölümde, günlük kayıtlarının python programlama dili kullanılarak üretim kodunda nasıl kullanacağının anlatılması hedeflenmektedir.

Gerekli konfigürasyonlarının programlama dili üzerinden gerçekleştirilmesi (handler) ve konfigürasyon dosyalarının kullanımı ile konfigürasyonun direk yazılımın içeri alınıp üretim kodları içerisinde kullanılması anlatılacaktır.



## Kaynak Kod Tabanlı

Günklük dosyalarımızın konfigürasyonlarının gerçekleştirilmesi ve günlüklerimizi birden çok yere göndermek istediğinizde handler'lar devreye girer. 

Handler'lar, günlük mesajlarını standart çıkış akışı *(STDOUT)* veya bir dosya gibi yapılandırılmış hedeflere veya HTTP üzerinden veya SMTP aracılığıyla e-postanıza gönderebilir. Oluşturulan bir kaydedicinin birden fazla handler'a sahip olabilir; Kısaca, mesajlarımızı bir günlük dosyasına kaydedebileceğimiz gibi ayrıca e-postayla gönderebileceğiniz anlamına gelir.



[^Note]: Günlük fonksiyonlarında olduğu gibi, handler'larda da önem düzeyini ayarlayabilmekteyiz.



Bu, aynı günlük fonksiyonuna birden fazla handler atayıp, her birinin farklı durum düzeylerinde çalışması istendiğinde kullanışlıdır.

Örneğin,

Günlük fonksiyonumuz kodun her durum düzeyindeki bilgiyi konsole ekranımıza yazdırılması istenirken, sadece HATA düzeyindeki mesajların dosyaya kaydedilmesini aşağıdaki gibi gerçekleştirebiliriz:

```python
# logging_example.py

import logging

# Günlük Fonksiyonu Türetelim
logger = logging.getLogger(__name__)

# Günlük fonksiyonlarının, 
# konsol ve dosyaya kayıtlarını gerçekleştirebilmeleri için handler atamlarını gerçekleştirelim
c_handler = logging.StreamHandler()			# Console Handler
f_handler = logging.FileHandler('file.log')	# File Handler

c_handler.setLevel(logging.NOTSET)
f_handler.setLevel(logging.ERROR)

# Handler'lar günlük verilerini kayıt altına alırken,
# kullanacakları formatları belirtelim
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.info('This is a warning')
logger.error('This is an error')
```

```shell
__main__ - WARNING - This is a warning
__main__ - ERROR - This is an error
```



## Dosya Tabanlı

Kaynak kod içerisinde konfigürasyon ayarı yapmak yerine, kendinize özel bir konfigürasyon dosyası oluşturduktan sonra bundan sonraki bütün projelerinizde benzer konfigürasyonları kullanabilirsiniz.

Örnek olarak aşağıdaki gibi bir konfigürasyon dosyası verilebilir.

> Daha fazla handler bilgisi için [dökümantasyon](https://docs.python.org/3/library/logging.handlers.html)'a bakabilirsiniz.

```bash
# logging.conf

[loggers]
keys=root, mylogger

[handlers]
keys=consoleHandler, fileHandler

[formatters]
keys=simple, complex

# Günlük Fonksiyonlarının Tanımlanması
[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_mylogger]
level=DEBUG
handlers=consoleHandler, fileHandler
qualname=mylogger
propagate=0

# Handler'ların Tanımlanması
[handler_consoleHandler]
class=StreamHandler
level=NOTSET
formatter=simple
args=(sys.stdout,)

[handler_fileHandler]
class=FileHandler
level=ERROR
formatter=complex
args=('/logs/log.out', 'a', 'utf8')

# Formatlayıcılar
[formatter_simple]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s

[formatter_complex]
format=%(asctime)s - %(name)s - %(levelname)-5s - %(module)-10s : %(lineno)3d - %(message)s
```

Konfigürasyon dosyasının kaynak kod üzerinden çağrılması için,

```python
import logging
import logging.config

logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)

# Get the logger specified in the file
logger = logging.getLogger(__name__)
logger_mylogger = logging.getLogger('mylogger')

logger.debug('This is a debug message')
logger_mylogger.debug('This is a debug message')
```

___

## Üretim Şablonu

Üretim şablonunda dosya handler'ı olarak, `handlers.TimedRotatingFileHandler`'ı kullanılmıştır. Bunun sebebi, argüman olarak verilen zaman işlevinin gerçekleşmesi durumunda günlük kaydının yedeği alınarak, yeni bir günlük kaydının açılıp, yeni olan kayıttan devam ediliyor olmasıdır. 

Üretim şablonunda zaman işlevi olarak 'midnight' ayarlanmıştır. Böylece her gece yarısına ulaşılması durumunda günlük kaydının yenisi alınarak, yeni kayıt üzerinden kayıtlar günlüğe kaydedilecektir.



```shell
# filename: logging.conf
# Loggers
[loggers]
keys=root

# Handlers
[handlers]
keys=consoleHandler, fileHandler

# Formatters
[formatters]
keys=simple, complex

# Looger: Root
[logger_root]
level=DEBUG
handlers=consoleHandler, fileHandler

# Console Handler
[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simple
args=(sys.stdout,)

# File Handler
[handler_fileHandler]
## https://docs.python.org/3/library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler
## Seconds
#args=('./log.out','S',1,5)
## Minutes
#args=('./log.out','M',1,5)
## Hours
#args=('./log.out','H',1,5)
#args=('./log.out','S',1,5)
class=handlers.TimedRotatingFileHandler
level=DEBUG
formatter=complex
args=('./log-saver.out', 'midnight', 0, 5)

# Formatters
[formatter_simple]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s

[formatter_complex]
format=%(asctime)s - %(name)s - %(levelname)-10s - %(module)s : %(lineno)4d - %(message)s
```

```python
# filename: main.py
import logging
import logging.config

logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)

logging.debug("This is a debug.")
logging.error('This is an error.')
```



*Bol kodlamalar..* :smile:

**Burak Büyükyüksel**

___



<img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="&quot;Buy Me A Coffee&quot;" style="zoom:120%;" />



|                                                              |                                            |                                                  |           |                                           |
| ------------------------------------------------------------ | ------------------------------------------ | ------------------------------------------------ | --------- | :---------------------------------------- |
| <img src="https://115101-327832-raikfcquaxqncofqfm.stackpathdns.com/wp-content/uploads/2018/03/Bitcoin_Gorsel.png?x95418" alt="Türkiye&#39;de Bitcoin (Kripto Para) Alım Satımı Yasal mı? – ProCompliance" style="zoom: 5%;" /> Ağ | Adres                                      | QR-Code                                          | MEMO      | QR                                        |
| BTC                                                          | 186uJCSDAHCS9E5cJsUAxAShBMaWeNqX8W         | ![BTC](/assets/img/wallet/BTC.png)               |           |                                           |
| BEP2                                                         | bnb136ns6lfw4zs5hg4n85vdthaad7hq5m4gtkgf23 | ![BEP2](/assets/img/wallet/BEP2.png)             | 101411074 | ![BEP2](/assets/img/wallet/BEP2-MEMO.png) |
| BEP20                                                        | 0x3b21d403c2a4714534b2322de199c029e87b2b78 | ![BEP20](/assets/img/wallet/BEP20.png)           |           |                                           |
| BTC(SegWit)                                                  | bc1quwf6ryasqxy8s075prare2hcgux3zhcsj2zqjw | ![BTC-SegWit](/assets/img/wallet/BTC-SegWit.png) |           |                                           |









