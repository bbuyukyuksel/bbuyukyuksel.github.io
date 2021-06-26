---
layout: post
title: Madencilik - RandomX CPU
date: 2021-06-14 00:00:00 +0300
description: Filtre boyutu, kaydırma adımı ve dolgulamanın imge boyutuna etkileri açıklanmaktadır.
lang: tr
img: cpu-mining.jpg
tags: [cnn, stride, filter, konvolüsyon, filtre, dolgulama, padding, image size]
contents: 
- 'Giriş;giriş'
- 'RandomX Algoritması;randomx-algoritması'
- 'Gereksinimler;gereksinimler'
- 'Kazalım;kazalım'
---

# Giriş

Bugün ki yazımızda konvolüsyonel sinir ağlarının temelinde yer alan kavramların; kaydırma adımı (stride) ve filte boyutun (filter size) ve dolgulama (padding) parametrelerin imge boyutuna etkilerini ele alacağız.

Öncelikle kavramlardan bahsetmek gerekirse;

- Filtre Boyutu (Filter Size): Görüntü ile konvolüsyon işlemine sokulacak filtre veya çekirdeğin (kernel) boyutudur.

  <img src="D:\03#PERSONAL\Projects\bbuyukyuksel.github.io\assets\img\post_images\konvolusyon-ve-image-boyutu-conv.png" alt="filepath" style="zoom:50%;" />
  Yukarıdaki gibi sobel veya prewitt filtresini örnek gösterecek olursak, filtre boyutunun (3x3 matris) 3 olduğu görülmektedir. 

- Dolgulama (Padding): 
  <img src="D:\03#PERSONAL\Projects\bbuyukyuksel.github.io\assets\img\post_images\konvolusyon-ve-image-boyutu-padding-0.png" alt="filepath" style="zoom:50%;" />
  <img src="C:\Users\otklocal\AppData\Roaming\Typora\typora-user-images\image-20210618003503244.png" alt="image-20210618003503244" style="zoom:50%;" />

- Stride..



https://jamesmccaffrey.wordpress.com/2018/05/30/convolution-image-size-filter-size-padding-and-stride/





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









