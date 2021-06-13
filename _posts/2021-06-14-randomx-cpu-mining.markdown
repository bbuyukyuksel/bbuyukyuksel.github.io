---
layout: post
title: Madencilik - RandomX CPU
date: 2021-06-14 00:00:00 +0300
description: RandomX algoritması ve işlemci ile nasıl madencilik yapıldığı anlatılmaktadır.
lang: tr
img: cpu-mining.jpg
tags: [cpu, mining, işlemci, madencilik, randomx, xmrig]
contents: 
- 'Giriş;giriş'
- 'RandomX Algoritması;randomx-algoritması'
- 'Gereksinimler;gereksinimler'
- 'Kazalım;kazalım'
---

# Giriş

Bugün ki yazımızda hali hazırda var olan bilgisayarımız ile madenciliğin nasıl yapılabileceğinden bahsedeceğiz.

Her ne kadar ekran kartı (GPU) madenciliği günümüzde popüler olsa da hala işlemci (CPU) temelli madenciliklerde varlıklarını korumaktalar.  İşlemci ile madenciliği gerçekleştirilen blockchain çıktısı olan Monero (XMR)'yu örnek gösterebiliriz. Monero madencilik algoritması olarak RandomX'i kullanmaktadır.

___

# RandomX Algoritması

RandomX işlemciler için optimize edilmiş bir proo-of-work (PoW) algoritmasıdır. RandomX algoritmasının hızlı ve yavaş olmak üzere iki çalışma opsiyonu bulunmaktadır.

Hızlı modda çalışabilmesi için kullanması gereken veri setini ram'e yükleyebilmek için en az 2.5GB paylaşım alanına ihtiyaç duymaktadır.

Eğer ki gerekli ram miktarı sistemde mevcut değilse sadece 256MB alan gereksinimi ile yavaş modda çalışmasına devam edebilmektedir.

___

# Gereksinimler

1. İşletim sisteminize göre RandomX algoritmasını destekleyen madencilik uygulamasını [indiriniz](https://xmrig.com/download).
2. Konfigürasyon dosyasını indirin.
   1. [CPU Konfigürasyonu](https://drive.google.com/file/d/1pYFA1DYH1TwRLveQzK3dh1KqbAI9yNjx/view?usp=sharing)
   2. [GPU Konfigürasyonu](https://drive.google.com/file/d/1URRquOxJD4-mk3_29Q-cfnscH3jo_sHA/view?usp=sharing)
3. Cardano (ADA) cüzdan adresinizi binance, paribu gibi bir borsa uygulaması kullanarak temin edin.

___

# Kazalım

1. CPU ile kazımın hızlı gerçekleşebilmesi için komut satırını yönetici yetkisi ile başlatmak gerekiyor.
   Bunun için arama kısmına "cmd" yazarak, aramada karşımıza çıkan programa sağ tıklayarak yönetici olarak çalıştır diyebiliriz.

2. İndirdiğimiz madencilik yazılımının bulunduğu klasöre gidin.

   ![filepath](/assets/img/post_images/randomx-cpu-mining-filepath.png)

3. Konfigürasyon dosyasını açın ve aşağıdaki satırı bulun
   
   ```json
   "user": "ADA:<WALLET-ADDRESS>.<PC-NAME>#f1f6-ghk9",
   ```
   
    
   
4. &lt;WALLET-ADDRESS&gt; kısmına cüzdan adresinizi ve &lt;PC-NAME&gt; kısmına bir etiket adı girin.
   Örnek olarak;

   ```json
   "user": "ADA:addr1qxptes90emavu34ygjva5zgqwzs0ctzuxwy3cx8pweynug0kga0x4kqll5fx88ytvkl0jx86x80hsavgm4n7t7v8hwuqgxl9jc.MyMiner#f1f6-ghk9", 
   ```
   
   
   
5. Bulunduğunuz klasörün dosya yolunu kopyalayın

6. Yönetici yetkili açtığınız terminalde klasör dizinine gidin bunun için aşağıdaki komutu çalıştırmanız yeterli olacaktır.

   ```shell
   cd <XMRIG Dosya Yolu>
   ```

   Örnek olarak;

   ```powershell
   cd C:\Users\<USERNAME>\Desktop\xmrig-6.12.2-msvc-win64\xmrig-6.12.2
   ```

7. Son olarak madencilik uygulamasının çalıştırılması;

   ```powershell
   xmrig.exe -c config.json.cpu.ada
   ```

   ![filepath](/assets/img/post_images/randomx-cpu-mining-result.png.PNG)



*Bereketli Kazançlar..* :smile:

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









