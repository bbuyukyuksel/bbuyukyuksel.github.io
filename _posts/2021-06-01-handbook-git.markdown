---
layout: post
title: Git - El Kitapçığı
date: 2021-06-01 00:00:00 +0300
description: Git kullanımında pratikliğin sağlanabilmesi için oluşturulmuş el kitapçığıdır.
lang: tr
img: git.png
tags: [Git, Handbook]
toc: true
contents: 
- 'Giriş;giriş'
- 'Nedir Bu Kavramlar?;nedir-bu-kavramlar'
- 'Yardım mı lazım?;yardım-mı-lazım'
- 'Versiyon Öğrenme;versiyon-öğrenme'
- 'Konfigürasyon;konfigürasyon'
- 'Kendini tanıtmak;kendini-tanıtmak'
- 'Editör Ayarı Yapmak;editör-ayarı-yapmak'
- 'Parametrelerin tanımlandığı dosyaları öğrenmek;parametrelerin-tanımlandığı-dosyaları-öğrenmek'
- 'Tanımlı parametreleri listelemek;tanımlı-parametreleri-listelemek'
- 'Tüm parametreleri listelemek;tüm-parametreleri-listelemek'
- 'Global düzeyde parametreleri listelemek;global-düzeyde-parametreleri-listelemek'
- 'Parametre ismine göre değeri görüntülemek;parametre-ismine-göre-değeri-görüntülemek'
- 'Temel Komutlar;temel-komutlar'
- '$ git status;-git-status'
- '$ git add <DOSYA>;-git-add-dosya'
- '$ git add .;-git-add-'
- '$ git add *.cs;-git-add-cs'
- '$ git add -p <DOSYA>;-git-add--p-dosya'
- '$ git rm <DOSYA>;-git-rm-dosya'
- '$ git commit -m “<COMMIT MESAJI>”;-git-commit--m-commit-mesaji'
- '**$ git commit –allow-empty -m “”**;-git-commit-allow-empty--m-'
- '$ git log;-git-log'
- '$ git log –oneline;-git-log-oneline'
- '$ git log –all –decorate –oneline –graph;-git-log-all-decorate-oneline-graph'
- '.gitignore Dosyası;gitignore-dosyası'
- 'Etiketleme – Tagging;etiketleme--tagging'
- 'Etiketleri Listeleme – Listing Tags;etiketleri-listeleme--listing-tags'
- 'Etiketleri Oluşturma – Creating Tags;etiketleri-oluşturma--creating-tags'
- 'Açıklamalı Etiketler – Annotated Tags;açıklamalı-etiketler--annotated-tags'
- 'Hafif Etiketler – Lightweight Tags;hafif-etiketler--lightweight-tags'
- 'Sonradan Etiketleme – Tagging Later;sonradan-etiketleme--tagging-later'
- 'Tag Paylaşma – Sharing Tags;tag-paylaşma--sharing-tags'
- 'Etiketleri Silme – Deleting Tags;etiketleri-silme--deleting-tags'
- 'Etiketler Arasında Geçiş Yapmak – Checking out Tags;etiketler-arasında-geçiş-yapmak--checking-out-tags'
- 'Takma İsimler – Aliases;takma-i̇simler--aliases'
- 'Geçici Kaydetme – Stash;geçici-kaydetme--stash'
- '$ git stash;-git-stash'
- '$ git stash save “<STASH MESAJI>”;-git-stash-save-stash-mesaji'
- '$ git stash list;-git-stash-list'
- '$ git stash pop;-git-stash-pop'
- '$ git stash apply stash@{<ID>};-git-stash-apply-stashid'
- 'Backtracking;backtracking'
- 'Staging alanına taşınmış dosyaların Unstage edilmesi;staging-alanına-taşınmış-dosyaların-unstage-edilmesi'
- 'Dosya Değişiklerinin Geri Alınması;dosya-değişiklerinin-geri-alınması'
- 'Commitler Arası Gezinme;commitler-arası-gezinme'
- 'SOFT Reset;soft-reset'
- 'HARD Reset;hard-reset'
- 'Branches;branches'
- 'Branchleri Listeleme;branchleri-listeleme'
- '$ git branch;-git-branch'
- '$ git branch -a;-git-branch--a'
- '$ git branch -va‌;-git-branch--va'
- '$ git branch -vva‌;-git-branch--vva'
- 'Branch Oluşturma;branch-oluşturma'
- '$ git branch -b <BRANCH NAME>;-git-branch--b-branch-name'
- 'Branchler Arasında Geçiş Yapmak;branchler-arasında-geçiş-yapmak'
- '$ git checkout <BRANCH NAME>;-git-checkout-branch-name'
- 'Branch Silmek;branch-silmek'
- '$ git branch -d <BRANCH NAME>;-git-branch--d-branch-name'
- '$ git branch -D <BRANCH NAME>;-git-branch--d-branch-name-1'
- 'Branch Adını Değiştirmek;branch-adını-değiştirmek'
- '**$ git branch -m **;-git-branch--m-'
- 'Branch Değişikliklerini Başka Bir Branche Aktarmak;branch-değişikliklerini-başka-bir-branche-aktarmak'
- '$ git merge <BRANCH NAME>;-git-merge-branch-name'
- 'Takım İşi;takım-i̇şi'
- '$ git clone <REMOTE REPO> <CLONE NAME>;-git-clone-remote-repo-clone-name'
- '$ git remote -v;-git-remote--v'
- '$ git fetch;-git-fetch'
- '$ git push origin <BRANCH NAME>;-git-push-origin-branch-name'
- '$ git merge origin/master;-git-merge-originmaster'
- '$ git rebase;-git-rebase'
- 'Rebase Senaryosu;rebase-senaryosu'
- '$ git merge –abort;-git-merge-abort'
- '! Git: fetch and merge, don’t pull;-git-fetch-and-merge-dont-pull'
- 'Remote;remote'
- '$ git remote;-git-remote'
- '$ git remote -v;-git-remote--v-1'
- '$ git remote add <kısa yol adı> <uzak depo adresi>;-git-remote-add-kısa-yol-adı-uzak-depo-adresi'
- '$ git remote rm <kısa yol adı>;-git-remote-rm-kısa-yol-adı'
- '$ git remote rename  ;-git-remote-rename--'
- 'PULL;pull'
- '$ git pull;-git-pull'
- '$ git pull ;-git-pull-'
- '$ git pull –rebase ;-git-pull-rebase-'
- 'PUSH;push'
- '$ git push;-git-push'
- '$ git push  ;-git-push--'
- '$ git push  -- all;-git-push-----all'
- '$ git push  -- tags;-git-push-----tags'
- 'Shortcuts;shortcuts'
- 'Merge İşlemi;merge-i̇şlemi'
- 'Yanlış Atılan Commit Mesajını Düzeltmek;yanlış-atılan-commit-mesajını-düzeltmek'
- 'Yanlış Branch’e Atılan Commit;yanlış-branche-atılan-commit'
- 'Commitler Arası Gezinme;commitler-arası-gezinme-1'
- 'Kaybedilen Commit’i Geri Almak;kaybedilen-commiti-geri-almak'
- 'Git Mimarisi;git-mimarisi'
- 'Hash İlişkileri;hash-i̇lişkileri'
- 'Manuel Commit;manuel-commit'
- 'Blob Eklemek;blob-eklemek'
- 'Tree Eklemek;tree-eklemek'
- 'Commit Atmak;commit-atmak'
- 'HEAD Pointer’ı Güncellemek;head-pointerı-güncellemek'
- 'Commit Gerçekleştirilmiş Dosyayı Çalışma Alanına Getirmek;commit-gerçekleştirilmiş-dosyayı-çalışma-alanına-getirmek'
- 'Git Log-Live;git-log-live'

---
# Giriş

‌

Bu el kitabı bir çok kaynak ve şahsi tecrübelerimden de yararlanılarak hazırlanmıştır. Olabildiğince kısa metin içerikleri ile Git komutlarının kullanımı ve gündelik hayat senaryolarını sizlere aktarmaya çalışacağım.

___

# Nedir Bu Kavramlar?

<img src="https://gblobscdn.gitbook.com/assets%2F-MG7vMhQXE0OFgTr4Cjx%2F-MWW6kr-M8soXTjO_fyT%2F-MWW6rrg6njiRwkrEzjI%2Fimage.png?alt=media&token=e6f0666a-eeaf-4b17-b7a4-cbd4479fc8a0" alt="img" style="zoom: 33%;" />

‌

Nedir bu working directory, staging area, repository kelimelerinin anlamları?



**Working Directory** çalıştığımız dosyaların fiziksel olarak bulunduğu, henüz versiyon kontrol sistemi olan Git'in henüz dosya takibi yapmadığı alandır.

‌

**Staging area** git add veya git rm ile Git'e takibini yapmasını veya daha önceden takibi yapılmış ve artık yapılması istenmeyen dosyaların bulunduğu ortamdır. Bu ortamda yer alan dosyalarda herhangi bir değişiklik, silme gibi işlemler yapıldığında bu değişiklikleri Git bizim için takip eder ve git status komutunu kullandığımızda bu değişiklikleri bize bildirir.

‌

**Repository** yani git veri tabanı ismini verdiğimiz bu bölgede ise staging area'ya atılmış dosyaların o an ki hallerinin dondurulmuş ve içeriklerinin git commit komutu ile git veritabınında saklandığı bölgedir.

___

# Yardım mı lazım?



```shell
$ git help <verb>
$ git <verb> --help
```

___

# Versiyon Öğrenme

```shell
$ git --version
git version 2.24.0.windows.2
```

___

# Konfigürasyon

> 1. Seviye (/etc/gitconfig dosyası) : Tüm kullanıcı ve projeler için geçerli olan ayarlar bu dosyada kaydedilir. **git config** komutunu **--system** seçeneği ile çalıştırırsanız ayarlar bu dosyada kaydedilecek ve bu dosyadan okunacaktır
> 2. Seviye (/.gitconfig dosyası) : Sadece sizin kullanıcınız için tanımlanan ayarların kaydedildiği dosyadır. **git config** komutunu **--global** seçeneği ile çalıştırısanız ayarlar bu dosyaya kaydedilecek ve bu dosyadan okunacaktır
> 3. Seviye : Proje klasörünüzün (projenizin Git ile versiyon kontrolüne alınmış olması gerekiyor) altında yer alan **.git/config** dosyasında ise proje bazındaki git ayarlarınız yer alır.

‌

## **Kendini tanıtmak**

```shell
$ git config --global user.name "Burak Büyükyüksel"
$ git config --global user.email buyukyukselburak@gmail.com
```

‌

## Editör Ayarı Yapmak

‌Bu işlem tercihen uygulanabilmektedir.

```shell
$ git config --global core.editor emacs
# or
$ git config --global core.editor "'C:/Program Files/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"
```

‌

## Parametrelerin tanımlandığı dosyaları öğrenmek

```shell
$ git config --list --show-origin

file:C:/Program Files/Git/etc/gitconfig http.sslcainfo=C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt
file:C:/Program Files/Git/etc/gitconfig http.sslbackend=openssl
file:C:/Program Files/Git/etc/gitconfig diff.astextplain.textconv=astextplain
file:C:/Program Files/Git/etc/gitconfig core.autocrlf=true
file:C:/Program Files/Git/etc/gitconfig core.fscache=true
file:C:/Program Files/Git/etc/gitconfig core.symlinks=false
file:C:/Program Files/Git/etc/gitconfig credential.helper=manager
file:C:/Users/otklocal/.gitconfig       user.email=buyukyukselburak@gmail.com
file:C:/Users/otklocal/.gitconfig       user.name=bbuyukyuksel
```

‌

## Tanımlı parametreleri listelemek

‌

### Tüm parametreleri listelemek

```shell
$ git config --list

http.sslcainfo=C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt
http.sslbackend=openssl
diff.astextplain.textconv=astextplain
core.autocrlf=true
core.fscache=true
core.symlinks=false
credential.helper=manager
user.email=buyukyukselburak@gmail.com
user.name=bbuyukyuksel
```

‌

### Global düzeyde parametreleri listelemek

```shell
$ git config --global --list

user.email=buyukyukselburak@gmail.com
user.name=bbuyukyuksel
```

‌

### Parametre ismine göre değeri görüntülemek

```shell
$ git config user.name
bbuyukyuksel
```

___

# Temel Komutlar

‌

## $ git status

Çalışma alanında gerçekleştirilen değişikleri bildiren, bu değişikler sonucunda kullanılabilecek komut ipuçlarını veren oldukça sık kullanılan bir komuttur.

```shell
$ git status
```

‌

## $ git add &lt;DOSYA&gt;

‌Staging area'ya takip edilecek dosyayı ekler.

```shell
$ git add main.py
```

‌

## $ git add .

‌ Staging area’ya bulunulan dizindeki tüm dosya ve klasörleri ekler.

```shell
$ git add .
```

‌

## $ git add *.cs

RegExp kullanarak, reg-exp deyimine uygun dosyaları staging area’ya ekleme işlemi gerçekleştirilir.

```shell
$ git add *.py
```

‌

## $ git add -p &lt;DOSYA&gt;

Staging area’ya dosya üzerindeki değişikliklerin sadece istenilen kısımlarının eklenmesi gerçekleştirilir.

```shell
$ git add -p main.py
```

‌

## **$ git rm &lt;DOSYA&gt;**

Staging area’ya bir sonraki commit’te takipi yapılmayacak, silinmiş dosya bilgisini ekler.

```shell
$ git rm test.py
```

‌

## $ git commit -m "&lt;COMMIT MESAJI&gt;"

Yukarıdaki komutta yer alan **-m** parametresi ile yaptığınız değişiklikleri özetleyen bir mesajı da commit'inize ekleyebilirsiniz. Eğer birden fazla satırı olan bir commit mesajı gireceksiniz **-m** parametresini kaldırmanız yeterli olacaktır. Default metin editörünüz açılır ve bu editöre mesajınızı istediğimiz uzunlukta girebilirsiniz.

```shell
$ git commit -m "main.py scriptindeki #8 numaralı bug çözüldü"
```

‌

***İyi Bir Commit Nasıl Olmalı?***

‌

- *Commit'inizde sadece kavramsal olarak ilişkili değişiklikleri içermeye özen göstermelisiniz. Zaman zaman iki farklı konu veya sorun ile ilgili aynı anda veya çok kısa aralıklarla değişimli olarak çalışmak zorunda kalabilirsiniz. Bu şekilde yapılan bir çalışma sonrasında commit zamanı geldiğinde mümkün ise iki konu ile ilgili değişikliklerinizi bir defada commit etmek yerine iki defada ayrı ayrı commit edin. Bu çok zor oluyorsa kısa yoldan bir anda tek bir değişikliğe odaklanmayı da düşünebilirsiniz.*
- *Tamamlanmamış değişikliklerinizi kesinlikle commit etmemeye özen gösterin. Eğer zaman zaman değişikliklerinizi kayıt altına almak istiyorsanız commit işlemi yerine Git'in Stash özelliğini/komutunu kullanabilirsiniz.*
- *Test edilmemiş değişiklikleri commit etmemeye özen gösterin. Bu öneri aslında bir önceki önerimiz ile pratikte aynı anlama geliyor*
- *Commit'leriniz kısa ve açıklayıcı mesajlar içermeli.*
- *Son olarak da sık sık commit işlemi yapmayı alışkanlık haline getirmenizi önerebiliriz. Bu alışkanlık ile birlikte yukarıdaki maddeleri de yerine getirebilirseniz iş yapma şekliniz ve konsantrasyonunuz da olumlu yönde etkilenecektir.*

‌

## **$ git commit --allow-empty -m “<COMMIT Mesajı>”**

‌Boş commit mesajı atılmak istendiğinde kullanılır.

```shell
$ git commit --allow-empty -m "Bu bir boş commit mesajıdır"
```

‌

## $ git log

‌Commit geçmişini görüntülemek için kullanılır, git log komutu ile birlikte commit işlemi ile ilgili bilgilendirici çoğu bilgiyi görmekle birlikte parametre olarak -p değerini kullanırsanız dosyalarda yapılan değişiklikler de ayrıntılı olarak listelenecektir.

‌

## $ git log --oneline

‌Commit geçmişini tek satırda görüntülemek için kullanılır

‌

## $ git log --all --decorate --oneline --graph

‌Commit geçmişinizi tüm branchler ile ilişkilerine yönelik, ASCII grafik olarak gösterir. Akılda kalıcı olması için şu şekilde kodlanabilir: "**A Dog**" = git log --**a**ll --**d**ecorate --**o**neline --**g**raph

___

# .gitignore Dosyası

‌

Takip edilmesi istenmeyen dosyalar için çalışma dizininde .gitignore dosyası oluşturulmalı ve içerisinde takip edilmesi istenmeyen dosyalara yer verilmelidir.

‌

Örnek bir .gitignore dosyası

```shell
# filename: .gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class
​
# C extensions
*.so
​
# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
```

‌

Yukarıda görüldüğü gibi .gitignore dosyasında takibi istenmeyen dosyaları belirtirken düzenli ifadelerden (regular expressions) yararlanabiliriz.

‌

Daha fazla gitignore örneği için https://github.com/github/gitignore sayfasını ziyaret edebiliriz.

___

# Etiketleme -- Tagging

‌

Çoğu VCS gibi Git, bir arşivin geçmişindeki belirli noktaları önemli olarak etiketleme yeteneğine sahiptir. Tipik olarak, insanlar bu işlevi sürüm noktalarını işaretlemek için kullanır (v1.0, v2.0 vb.). Bu bölümde, mevcut etiketlerin nasıl listeleneceğini, etiketlerin nasıl oluşturulup silineceğini ve farklı etiket türlerinin neler olduğunu öğreneceğiz.



https://git-scm.com/book/tr/v2/Git-Basics-Tagging

‌

## Etiketleri Listeleme -- Listing Tags

Mevcut etiketleri Git'te listelemek basittir.  **$ git tag** yazmanız yeterlidir (isteğe bağlı -l veya --list ile)

```shell
$ git tag
v1.0
v2.0
```

‌

Bu komut, etiketleri alfabetik sırada listeler; gösterildikleri sıranın gerçek bir önemi yoktur.

‌

Belirli bir düzenli ifade ile eşleşen etiketleri de arayabilirsiniz. Örneğin Git kaynak deposunda 500'den fazla etiket yer alıyor ve yalnızca 1.8.5 serisine bakmakla ilgileniyorsanız, şunu çalıştırabilirsiniz:



```shell
$ git tag -l "v1.8.5*"
v1.8.5
v1.8.5-rc0
v1.8.5-rc1
v1.8.5-rc2
v1.8.5-rc3
v1.8.5.1
v1.8.5.2
v1.8.5.3
v1.8.5.4
v1.8.5.5
```

‌

## Etiketleri Oluşturma -- Creating Tags

Git iki tür etiketi destekler: lightweight (hafif) ve annotated (açıklamalı).

‌

 lightweight bir etiket, değişmeyen bir branch'e çok benzer; yalnızca belirli bir kaydetmeye yönelik bir göstericidir.

‌

Ancak annotated (açıklamalı) etiketler, Git veritabanında tam nesneler olarak saklanır. Bunlar checksummed olarak; etiketleyicinin adını, e-postasını ve tarihini içerir; bir etiketleme mesajına sahip olmak; ve GNU Privacy Guard (GPG) ile imzalanabilir ve doğrulanabilir. Genel olarak, tüm bu bilgilere sahip olabilmeniz için ek açıklamalı etiketler oluşturmanız önerilir; ancak geçici bir etiket istiyorsanız veya herhangi bir nedenle diğer bilgileri saklamak istemiyorsanız, lightweight etiketler de mevcuttur.

‌

### Açıklamalı Etiketler -- Annotated Tags

Git'te açıklamalı bir etiket oluşturmak basittir. En kolay yol, tag komutunu çalıştırdığınızda -a'yı belirtmektir:



```shell
$ git tag -a v1.4 -m "my version 1.4"
$ git tag
v0.1
v1.3
v1.4
```

‌

**-m** etiketi ile saklanan bir etiketleme mesajını belirtir. Ek açıklamalı bir etiket için bir mesaj belirtmezseniz, Git, yazabilmeniz için düzenleyicinizi başlatır.

‌

Git show komutunu kullanarak etiketlenen işlemle birlikte etiket verilerini görebilirsiniz:



```shell
$ git show v1.4
tag v1.4
Tagger: Ben Straub <ben@straub.cc>
Date:   Sat May 3 20:19:12 2014 -0700

my version 1.4

commit ca82a6dff817ec66f44342007202690a93763949
Author: Scott Chacon <schacon@gee-mail.com>
Date:   Mon Mar 17 21:52:11 2008 -0700

    changed the version number
```

‌

Bu, etiketleyici bilgilerini, commit'in etiketlendiği tarihi ve kaydetme bilgilerini göstermeden önce ek açıklama mesajını gösterir.

‌

### Hafif Etiketler -- Lightweight Tags

Kaydetmeleri etiketlemenin başka bir yolu da hafif bir etiket kullanmaktır. Bu temelde bir dosyada saklanan checksum'dır - başka hiçbir bilgi tutulmaz. Hafif bir etiket oluşturmak için -a, -s veya -m seçeneklerinden herhangi birini sağlamayın, sadece bir etiket adı sağlayın:



```shell
$ git tag v1.4-lw
$ git tag
v0.1
v1.3
v1.4
v1.4-lw
v1.5
```

‌

Bu sefer, etiket üzerinde git show çalıştırırsanız, fazladan etiket bilgilerini görmezsiniz. Komut sadece commit'i gösterir:



```shell
$ git show v1.4-lw
commit ca82a6dff817ec66f44342007202690a93763949
Author: Scott Chacon <schacon@gee-mail.com>
Date:   Mon Mar 17 21:52:11 2008 -0700

    changed the version number
```

‌

### Sonradan Etiketleme -- Tagging Later

Kaydetmeleri geçtikten sonra da etiketleyebilirsiniz. Kaydetme geçmişinizin şöyle göründüğünü varsayalım:



```shell
$ git log --pretty=oneline
15027957951b64cf874c3557a0f3547bd83b3ff6 Merge branch 'experiment'
a6b4c97498bd301d84096da251c98a07c7723e65 beginning write support
0d52aaab4479697da7686c15f77a3d64d9165190 one more thing
6d52a271eda8725415634dd79daabbc4d9b6008e Merge branch 'experiment'
0b7434d86859cc7b8c3d5e1dddfed66ff742fcbc added a commit function
4682c3261057305bdd616e23b64b0857d832627b added a todo file
166ae0c4d3f420721acbb115cc33848dfcc2121a started write support
9fceb02d0ae598e95dc970b74767f19372d61af8 updated rakefile
964f16d36dfccde844893cac5b347e7b3d44abbc commit the todo
8a5cbc430f1a9c3d00faaeffd07798508422908a updated readme
```

‌

Şimdi, projeyi "güncellenmiş komisyon dosyası" kaydında olan v1.2'de etiketlemeyi unuttuğunuzu varsayalım. Gerçekten sonra ekleyebilirsiniz. Bu kaydetmeyi etiketlemek için, komutun sonunda commit checksum (veya bir kısmını) belirtirsiniz:



```shell
$ git tag -a v1.2 9fceb02
```

‌

Şimdi commitinin etiketlendiğini görebilirsin



```shell
$ git tag
v0.1
v1.2
v1.3
v1.4
v1.4-lw
v1.5
```



```shell
$ git show v1.2
tag v1.2
Tagger: Scott Chacon <schacon@gee-mail.com>
Date:   Mon Feb 9 15:32:16 2009 -0800

version 1.2
commit 9fceb02d0ae598e95dc970b74767f19372d61af8
Author: Magnus Chacon <mchacon@gee-mail.com>
Date:   Sun Apr 27 20:43:35 2008 -0700

    updated rakefile
...
```

‌

## Tag Paylaşma -- Sharing Tags

‌

Varsayılan olarak git push komutu, etiketleri uzak sunuculara aktarmaz. Etiketleri oluşturduktan sonra açıkça paylaşılan bir sunucuya iletmek gerekecektir. Bu işlem, uzak branchleri paylaşmak gibidir - git push origin komutunu çalıştırabilirsiniz.



```shell
$ git push origin v1.5
Counting objects: 14, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (12/12), done.
Writing objects: 100% (14/14), 2.05 KiB | 0 bytes/s, done.
Total 14 (delta 3), reused 0 (delta 0)
To git@github.com:schacon/simplegit.git
 * [new tag]         v1.5 -> v1.5
```

‌

Aynı anda iletmek istediğiniz çok sayıda etiketiniz varsa, git push komutunda --tags seçeneğini de kullanabilirsiniz. Bu, tüm etiketlerinizi halihazırda orada olmayan uzak sunucuya aktaracaktır.



```shell
$ git push origin --tags
Counting objects: 1, done.
Writing objects: 100% (1/1), 160 bytes | 0 bytes/s, done.
Total 1 (delta 0), reused 0 (delta 0)
To git@github.com:schacon/simplegit.git
 * [new tag]         v1.4 -> v1.4
 * [new tag]         v1.4-lw -> v1.4-lw
```

‌

Şimdi, başka biri deponuzdan klonladığında veya pull işlemini gerçekleştirdiğinde, tüm etiketlerinizi de alacak.

> Git push  --tags kullanılarak etiketlerin itilmesi, hafif ve açıklamalı etiketler arasında ayrım yapmaz; İtme için yalnızca bir tür seçmenize izin veren basit bir seçenek yoktur.

‌

## Etiketleri Silme -- Deleting Tags

‌

Yerel deponuzdaki bir etiketi silmek için git tag -d  kullanabilirsiniz. Örneğin, yukarıdaki hafif etiketimizi aşağıdaki gibi kaldırabiliriz:



```shell
$ git tag -d v1.4-lw
Deleted tag 'v1.4-lw' (was e7d5add)
```

‌

Bunun etiketi herhangi bir uzak sunucudan kaldırmadığını unutmayın. Uzak bir sunucudan bir etiketi silmenin iki yaygın çeşidi vardır. İlk varyasyon git push : refs / tags /  şeklindedir:



```shell
$ git push origin :refs/tags/v1.4-lw
To /git@github.com:schacon/simplegit.git
 - [deleted]         v1.4-lw
```

‌

Yukarıdakileri yorumlamanın yolu, iki nokta üst üste uzak etiket adına itilmeden önce onu boş değer olarak okumak ve etkin bir şekilde silmektir.

‌

Uzak bir etiketi silmenin ikinci (ve daha sezgisel) yolu şudur:



```shell
$ git push origin --delete <tagname>
```

‌

## Etiketler Arasında Geçiş Yapmak -- Checking out Tags

‌

Bir etiketin işaret ettiği dosyaların sürümlerini görüntülemek istiyorsanız, bu etiketin bir git kontrolünü yapabilirsiniz, ancak bu, deponuzu bazı yan etkileri olan "detached HEAD" durumuna getirir:



```shell
$ git checkout 2.0.0Note: checking out '2.0.0'.
You are in 'detached HEAD' state. You can look around, make experimentalchanges and commit them, and you can discard any commits you make in thisstate without impacting any branches by performing another checkout.
If you want to create a new branch to retain commits you create, you maydo so (now or later) by using -b with the checkout command again. Example:
  git checkout -b <new-branch>
HEAD is now at 99ada87... Merge pull request #89 from schacon/appendix-final
```



```shell
$ git checkout 2.0-beta-0.1
Previous HEAD position was 99ada87... Merge pull request #89 from schacon/appendix-final
HEAD is now at df3f601... add atlas.json and cover image
```

‌

"detached HEAD" durumunda, değişiklik yapıp ardından bir kaydetme oluşturursanız, etiket aynı kalır, ancak yeni kaydetmeniz herhangi bir şubeye ait olmaz ve kesin kaydetme karması haricinde ulaşılamaz. Bu nedenle, değişiklik yapmanız gerekirse - örneğin eski bir sürümdeki bir hatayı düzelttiğinizi varsayalım - genellikle bir branch oluşturmak isteyeceksiniz:



```shell
$ git checkout -b version2 v2.0.0
Switched to a new branch 'version2'
```

‌

Bunu yaparsanız ve bir kesinleştirme yaparsanız, sürüm2 dalınız, yeni değişikliklerinizle birlikte ilerleyeceği için v2.0.0 etiketinizden biraz farklı olacaktır, bu yüzden dikkatli olun.

___

# Takma İsimler -- Aliases



https://git-scm.com/book/tr/v2/Git-Basics-Git-Aliases

‌

Temel Git ile ilgili bu bölümü bitirmeden önce, Git deneyiminizi daha basit, daha kolay ve daha tanıdık hale getirebilecek küçük bir ipucu var: takma adlar. Onlara atıfta bulunmayacağız veya kitapta daha sonra kullandığınızı varsaymayacağız, ancak muhtemelen onları nasıl kullanacağınızı bilmelisiniz. Kısmen yazarsanız Git, komutunuzu otomatik olarak anlamaz. Git komutlarının her birinin metninin tamamını yazmak istemiyorsanız, git config'i kullanarak her komut için kolayca bir takma ad ayarlayabilirsiniz. İşte oluşturmak isteyebileceğiniz birkaç örnek:

‌

- $ git config --global alias.co checkout
- $ git config --global alias.br branch 
- $ git config --global alias.ci commit 
- $ git config --global alias.st status

‌

Bu, örneğin  **"$ git commit"** yerine **"$ git co"** yazmanız gerektiği anlamına gelir.  Git'i kullanmaya devam ederken, muhtemelen diğer komutları da sık sık kullanacaksınız; yeni takma adlar oluşturmaktan çekinmeyin. Bu teknik, olması gerektiğini düşündüğünüz komutların oluşturulmasında da çok yararlı olabilir. Örneğin, bir dosyanın aşamalarını kaldırırken karşılaştığınız kullanılabilirlik sorununu düzeltmek için Git'e kendi unstage takma adınızı ekleyebilirsiniz:

‌

```shell
$ git config --global alias.unstage 'reset HEAD --'
```

‌

Bu, aşağıdaki iki komutu eşdeğer kılar:

‌

- `$ git unstage fileA`
- `$ git reset HEAD -- fileA`

‌

Bu biraz daha net görünüyor. Şunun gibi son bir komut eklemek de yaygındır: $ git config --global alias.last 'log -1 HEAD' Bu şekilde, son commit'i kolayca görebilirsiniz:



```shell
$ git lastcommit 66938dae3329c7aebe598c2246a8e6af90d04646Author: Josh Goebel <dreamer3@example.com>Date:   Tue Aug 26 19:48:51 2008 +0800
    test for current head
    Signed-off-by: Scott Chacon <schacon@example.com>
```

‌

Anlayabileceğiniz gibi Git, yeni komutu, takma ad verdiğiniz şeyle değiştirir. Ancak, bir Git alt komutu yerine harici bir komut çalıştırmak isteyebilirsiniz. Bu durumda, komutu a ile başlatırsınız! karakter. Bu, Git deposuyla çalışan kendi araçlarınızı yazarsanız kullanışlıdır. Gitk'i çalıştırmak için git görselini takma ad vererek gösterebiliriz:

‌

```shell
$ git config --global alias.visual '! gitk'
```

___

# Geçici Kaydetme -- Stash

‌

Stash "**last in - first out**" yani "**son giren - ilk çıkar**" mantığına göre çalışmaktadır.

‌

Stash'e anlık çalışma alanındaki değişiklikler atıldığında daha önceki stash kayıtları bir kaydırılıp son kayıt **stash@{0}**'da tutulur.

‌

## $ git stash

Çalışma alanı (working directory) 'nda  gerçekleştirilen değişiklikleri geçici olarak kaydeder.

‌

## $ git stash save "&lt;STASH MESAJI&gt;"

Çalışma alanındaki değişiklikleri bilgilendirme mesajı ile geçici kayıt alanına kaydeder.

‌

## $ git stash list

Geçici alana taşınmış değişiklikleri listeler.

‌

## $ git stash pop

stash@{0}'da yer alan geçici çalışmayı çalışmana alanına aktarır ve stash kayıtlarından bu geçici çalışma kaydının silinmesi gerçekleştirilir.

‌

## $ git stash apply stash@{&lt;ID&gt;}

`stash@{<ID>}` kayda alınmış geçici çalışmayı çalışma alanına aktarır fakat **stash kayıtlarından bu geçici çalışma kaydının silinmesi gerçekleşmez**



```shell
$ git stash apply stash@{5}
```

___

# Backtracking

‌

## Staging alanına taşınmış dosyaların Unstage edilmesi

‌

```shell
$ git reset HEAD <DOSYA ADI>
```

‌

Staging alanına *(Git tarafından takibi gerçekleştirilmesi istenen dosya alanı)* taşınmış dosyaları, unstage eder. Bu işlem sonrasında dosyalarda değişiklik yapmaz.

‌

## Dosya Değişiklerinin Geri Alınması

‌

- $ git checkout HEAD &lt;DOSYA ADI&gt;
- $ git checkout -- &lt;DOSYA ADI&gt;
- $ git restore &lt;DOSYA ADI&gt;

‌

## Commitler Arası Gezinme

‌

`$ git checkout <COMMIT CHECKSUM>` komutu ile commitler arasında  geçişler gerçekleştirilebilir. Son commit'e geri dönülmek istendiğinde `$ git checkout master`  komutu çalıştırılabilir.

‌

## SOFT Reset

‌

Commit checksum'ı verilen commit değerine geri dönüş sağlanır. Bu işlem **çalışma alanındaki dosyaları değişikliğe uğratmadan** HEAD pointer'ının ilgili commit'e ait checksum gösterilmesi ile sonuçlanır.

‌

Git geçmişinde ilgili commit'e geri dönüş sağlanıp, çalışma alanındaki dosyalarda değişiklik yapmadığı için buna soft reset denmektedir.



```shell
$ git reset <COMMIT CHECKSUM>
```

‌

## HARD Reset



Bu komut kullanılmadan önce dikkat edilmesi gerekmektedir.

‌

Commit checksum'ı verilen commit değerine geri dönüş sağlanır. Bu işlem **çalışma alanındaki dosyaları değişikliğe uğratarak** HEAD pointer'ının ilgili commit'e ait checksum gösterilmesi ile sonuçlanır.

‌

Git geçmişinde ilgili commit'e geri dönüş sağlanıp, çalışma alanındaki dosyalar commit'in içeriğindeki dosyalar ile güncellendiği, değiştiği için buna hard reset denmektedir.



```shell
$ git reset --hard <COMMIT CHECKSUM>
```

___

# Branches

‌

## Branchleri Listeleme

‌

### $ git branch

Var olan branch'leri listeler. Yer alınan branch'i başına * (asterisk) koyarak belirtir. Bulunulan branch'i öğrenmek için "$ git status" komutu da kullanılabilir.

```shell
$ git branch
* master
  tes
```

Başka bir branch'e checkout işlemi gerçekleştirildiğinde $ git branch komutu tekrar kullanılırsa, checkout işleminde yeni bir branch oluştuğu gözlemlenecektir.

```shell
$ git checkout 28718c2f764f350a94f489954b6289401b646e54
$ git branch
* (HEAD detached at 28718c2)
  master
  test
```

‌

### $ git branch -a

Tüm branchler listelenir

```shell
$ git branch -a
* master
  test
  remotes/origin/master
```

‌

### $ git branch -va‌

Yer alan tüm branchler son commit değerleri ile listelenir

```shell
$ git branch -va
* master                     8067a82 update readme
  test                       c252241 test
  remotes/origin/master      8067a82 update readme
```

‌

### $ git branch -vva‌

Branchler takip linkleri ile listelenir.

```shell
$ git branch -vva
* master                8067a82 [origin/master] update readme
  test                  c252241 test
  remotes/origin/master 8067a82 update readme
```

‌

## Branch Oluşturma

‌

### $ git branch -b &lt;BRANCH NAME&gt;

‌Yeni bir branch oluşturur eğer [-b] parametresi kullanılırsa branch oluşturulduktan sonra aktifleştirilir.

‌

## Branchler Arasında Geçiş Yapmak

‌

### $ git checkout &lt;BRANCH NAME&gt;

&lt;BRANCH NAME&gt; isimli branch’e geçiş yapar.

‌

## Branch Silmek

‌

### $ git branch -d &lt;BRANCH NAME&gt;

‌<BRANCH_NAME> isimli branch’i siler.

‌

### $ git branch -D &lt;BRANCH NAME&gt;

‌Commit atılmış ve merge işlemi gerçekleştirilmemiş &lt;BRANCH NAME&gt; isimli branch'i siler.

‌



## Branch Adını Değiştirmek

‌

### **$ git branch -m <NEW_BRANCH_NAME>**

‌

Bulunulan branch'in adını &lt;NEW BRANCH NAME&gt; ile değiştirir.

‌

## Branch Değişikliklerini Başka Bir Branche Aktarmak

‌

### $ git merge &lt;BRANCH NAME&gt;

‌Bulunulan branch'e &lt;BRANCH NAME&gt; adındaki branch'teki değişiklikleri aktarır.

___

# Takım İşi

‌

## $ git clone &lt;REMOTE REPO&gt; &lt;CLONE NAME&gt;

‌Uzak repodaki projeyi local'e çeker.

‌

## $ git remote -v

‌Projede kayıtlı olan uzak repo adreslerini listeler.

‌

## $ git fetch

‌Uzak repodaki değişimleri locale çeker, bu değişiklikler `<remote>/<branch>`'nde bulunur. Ana branch'e direk olarak merge işlemi fars-forward olarak gerçekleşmez.

‌

## $ git push origin &lt;BRANCH NAME&gt;

‌Uzak repoya branchteki değişiklikler yollanır. Remota branch yer almıyorsa oluşturulur.

‌

## $ git merge origin/master 

‌Uzak repodan fetch edilen değişimleri local master’a merge etmek için kullanılır. merge işlemi için default olarak fast-forward yöntemi kullanılır.

‌

## $ git rebase

‌rebase komutu merge'den farklı olarak fast-forward şeklinde işlem yapmamaktadır.

Uygulanan değişiklikler commit tarihlerine göre gerçekleştirilir. Merge'de ise ana branch'in commitleri dikkate alındıktan sonra dahil edilecek branch'in değişiklikleri fast-forward şeklinde birleştirilecek branch'e uygulanır.

‌

### Rebase Senaryosu

```shell
$ git init

# Master Branch'ine lisans.txt dosyasını commitle
$ echo "lisans: GNU" > lisans.txt
$ git add lisans.txt
$ git commit -m "lisans dosyası eklendi"
[master (root-commit) 6718f8f] lisans dosyası eklendi
 1 file changed, 1 insertion(+)
 create mode 100644 lisans.txt

# Main isminde yeni bir branch aç
$ git branch main
$ git branch
  main
* master

# Master Branch'ine README.md dosyasını commitle
$ echo "Read me!" > README.md
$ git add README.md
$ git commit -m "test commit"
[master 9e715d1] test commit
 1 file changed, 1 insertion(+)
 create mode 100644 README.md

$ git log --oneline
ab42316 (HEAD -> master) test commit
ea397e1 (main) lisans dosyası eklendi
 
# Main Branch'ine geçiş yap
$ git checkout main

# Main Branch'ine README.md dosyasını commitle
$ echo "#main script file" > main.py
$ git add main.py
$ git commit -m "main.py scripti eklendi"
[main b27be02] main.py scripti eklendi
 1 file changed, 1 insertion(+)
 create mode 100644 main.py

# Main
$ git log --oneline
e1806f0 (HEAD -> main) main.py scripti eklendi
ea397e1 lisans dosyası eklendi


$ git log --all --decorate --oneline --graph
* e1806f0 (HEAD -> main) main.py scripti eklendi
| * ab42316 (master) test commit
|/
* ea397e1 lisans dosyası eklendi
```



```shell
# MERGE
$ git branch
* main
  master
  
$ git merge master
Merge made by the 'recursive' strategy.
 README.md | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 README.md

$ git log --all --decorate --oneline --graph
*   0f77a3b (HEAD -> main) Merge branch 'master'
|\
| * ab42316 (master) test commit
* | e1806f0 main.py scripti eklendi
|/
* ea397e1 lisans dosyası eklendi
```



```shell
# REBASE
$ git branch
* main
  master

$ git rebase master
Successfully rebased and updated refs/heads/main.

$ git log --all --decorate --oneline --graph
* 0091fe4 (HEAD -> main) main.py scripti eklendi
* ab42316 (master) test commit
* ea397e1 lisans dosyası eklendi


```

Yukarıdaki örneğimiz incelendiğinde,

`$ git merge` ile birleştirme yapıldığında, branch içerisindeki değişiklikler bir başka branch'e aktarılmak istendiğinde genellikle bulunulan branch'in commit geçmişinin üzerine değişiklikler kaydedilir ve son olarak birleşim branch'inin commit'i kaydedilir. `$ git rebase` ile birleştirme yapıldığında, branch içerisindeki değişiklikler bir başka branch'e aktarılmak istendiğinde, bulunulan branch'in commit geçmişi öne çıkmayarak, değişiklikler commit tarihlerine bakılarak işleme sokulur.

‌

## $ git merge --abort

‌Gerçekleştirilen merge işlemini geri kalır.

___

# ! Git: fetch and merge, don't pull



https://longair.net/blog/2009/04/16/git-fetch-and-merge/

> In the simplest terms, `git pull` does a `git fetch` followed by a `git merge`. You can do a `git fetch` at any time to update your remote-tracking branches under `refs/remotes/<remote>/`. This operation never changes any of your own local branches under `refs/heads`, and is safe to do without changing your working copy. I have even heard of people running `git fetch` periodically in a cron job in the background (although I wouldn't recommend doing this). A `git pull` is what you would do to bring a local branch up-to-date with its remote version, while also updating your other remote-tracking branches.

> From the Git documentation for [**git pull**](http://git-scm.com/docs/git-pull): In its default mode, `git pull` is shorthand for `git fetch` followed by `git merge FETCH_HEAD`.

___

# Remote

‌

## $ git remote

‌Uzak depo kısa yol isimlerini listele

‌

## $ git remote -v

 Uzak depo ilişkilerini daha ayrıntılı listele

‌

## $ git remote add &lt;kısa yol adı&gt; &lt;uzak depo adresi&gt;

‌ Uzak depo ilişkisi tanımla

‌

## $ git remote rm &lt;kısa yol adı&gt;

‌Uzak depo ilişkisini sil

‌

## $ git remote rename <kısa yol adı> <kısa yol yeni adı>

‌ Uzak depo kısa yolunun adını değiştir

___

# **PULL**

‌

## $ git pull

Uzak depodaki (origin) değişiklikleri almak için kullanılır

‌

## $ git pull <uzak depo kısa yolu>

 Uzak depo kısa yolu ile ilişkilendirilmiş konumdan değişiklikleri almak için

‌

## $ git pull –rebase <uzak depo kısa yolu>

 Merge yerine rebase kullanarak değişiklikleri almak için

___

# PUSH

‌

## $ git push

Yerel daldaki değişiklikleri uzak depoya gönder 

‌

## $ git push <uzak depo kısa yolu> <dalın adı>

Bir daldaki değişiklikleri uzak depo kısa yolu ile ilişkilendirilmiş uzak depoya gönder

‌

## $ git push <uzak depo kısa yolu> -- all

Tüm yerel dallardaki değişiklikleri uzak depo kısa yolu ile ilişkilendirilmiş uzak depoya gönder

‌

## $ git push <uzak depo kısa yolu> -- tags

Yerel depodaki tag’leri uzak depoya gönder

___

# **Shortcuts**

‌

## **Merge İşlemi**

- $ git checkout master
- $ git merge <BRANCH_NAME>

‌

## **Yanlış Atılan Commit Mesajını Düzeltmek**

‌

- **Çözüm-1** 
  - **$ git commit --amend -m “<NEW_COMMIT_MESSAGE>”**
- **Çözüm-2**
  - **$ git reset <SHA_OF_BEFORE_THE_LAST_COMMIT_SHA>**
  - **$ git add .**
  - **$ git commit -m “<COMMIT_MESSAGE>”**

‌

## **Yanlış Branch'e Atılan Commit**

‌

- **$ git reset <SHA_OF_BEFORE_THE_LAST_COMMIT_SHA>**
- **$ git stash**
- **$ git checkout <BRANCH_NAME>**
- **$ git pop**
- **$ git commit -m "<COMMIT_MESSAGE>"**

‌

## **Commitler Arası Gezinme**

‌`**$ git checkout <SHA>**`

İlgili committeki dosyaları working directory’e geçirir. (Working directory’deki çalıştığınız dosyalar gidecektir)

Bu gezinme sonrası geçici bir branch oluşacaktır. Son haline dönmek isterseniz eğer `$ git checkout <BRANCH_NAME>` tekrar kullanabilirsiniz.

___

# Kaybedilen Commit'i Geri Almak

‌

Az önce bir $ git reset --hard HEAD^ işlemini gerçekleştirdiniz ve üzerinizde çalıştığınız son işlemleri çöpe attınız. Biraz sonrasında gerçekten ihtiyacınız olan bir bilgiyide çöpe attığınızın farkına vardınız. Peki şimdi ne olacak? Eğer ki commit checksum değerini bilseydiniz belki git checkout ile son commit değerine geri dönebilecektiniz..

‌

Çöpe giden o algoritmayı belkide asla ikinci kez mükemmel olarak uygulayamayacaksınız, bu yüzden ona ihtiyacınız olacak.

‌

"Don't fear, git should still have your commit"  Korkmayın, git bir yerlere bu commit'i hala saklıyor olabilmeli :) Bir resetleme işlemi gerçekleştiğinde, resetlenen commit bir "dangling" durumuna geçer. Yani commit'iniz hala git reposunda bir yerlerde, temizlenmek için bir sonraki garbage collection işlemini bekliyor. Yani commit'inizi attığınızdan beri git garbage collector'ü çalıştırmadığınız sürece endişelenmenize gerek yok.

‌

Şuanki HEAD pointer'ın gösterdiği checksum değeri için: **$ git show-ref -h HEAD** **7c61179cbe51c050c5520b4399f7b14eec943754 HEAD** **$ git reset --hard HEAD^** HEAD pointer şimdi 39ba87b checksum'ını göstermekte  Bu işlemle birlikte en azından çalışan bir koda geri dönüş sağlayabildik, o kadar da aptalca gözükmüyor. **$ git show-ref -h HEAD 39ba87bf28b5bb223feffafb59638f6f46908cac HEAD**

‌

Görüldüğü gibi HEAD pointer'ımız artık bir commit geriyi işaret etmekte.

‌

Bu durumda geri dönmek istediğimizde git pull işlemini kullanarak uzak repodaki değişiklikleri yerel dosyalarımızda güncelleyebilirdik, farz edelim ki geri almış olduğumuz, çöpe giden commit'i sadece yerel depomuz biliyor olsun.

‌

Peki şimdi ne olacak?

‌

Commit'i geri getirebilmek için commit'e ait SHA1 checksum değerine ihtiyacımız var.

‌

Git'in commit'i hala fsck komutuyla bildiğini ispatlayabiliriz

‌

**$ git fsck --lost-found** [... some blobs omitted ...] dangling commit 7c61179cbe51c050c5520b4399f7b14eec943754 Reflog komutunu kullanarak git'in commit ile ilgili bildiklerini de görebilirsiniz:

‌

**$ git reflog   39ba87b... HEAD@{0}: HEAD~1: updating HEAD 7c61179... HEAD@{1}: pull origin master: Fast forward [... lots of other refs ...]**

‌

Şimdi SHA1: 7c61179 commit checksum'ına sahibiz. Hemen mevcut değşiklikleri geri uygulamak istiyorsak, git merge işlemi mükemmel algoritmamızı kurtaracaktır.

‌

**$ git merge 7c61179 Updating 39ba87b..7c61179 Fast forward css/screen.css |    4 ++++ submit.html       |    4 ++-- 2 files changed, 6 insertions(+), 2 deletions(-)**

‌

Sanırım kaybolmuş commit'imizi geri alabildik :)

___

# Git Mimarisi

‌

## Hash İlişkileri

‌Bitcoin mi kazıyoruz? Nedir bu iç içe hashler böyle?

![img](https://lh3.googleusercontent.com/7Z8Wf9zndKly0rSgeW-WzJjnoodhttEkG6t-MvNwbojzoEnZ6srVDIcVKYjMm3Ephejty3Nvt-U-01DJUgWepfpbxzzbP9v_gs0y4ZfqAAHvMMyiL0-uQBVw2CBSGx_AjV4KcqJO)

‌Blob : Dosya 

Tree : Dizinler

‌

## Manuel Commit

$ git add - $ git commit komutlarını kullanmadan da commit eklemek mümküm. Hadi nasıl gerçekleştiğine bakalım.

‌

### Blob Eklemek

```shell
$ echo "Hello World!" | git hash-object -w --stdin980a0d5f19a64b4b30a87d4206aade58726b60e3
$ git cat-file -p 980a0d5f19a64b4b30a87d4206aade58726b60e3Hello World!
$ git cat-file -t 980a0d5f19a64b4b30a87d4206aade58726b60e3blob
$ git update-index --add --cacheinfo 100644 980a0d5f19a64b4b30a87d4206aade58726b60e3 beawulf.txt
```

‌

### Tree Eklemek

```shell
$ git write-tree2d3417788c3f37815df9b34c433eddc67d197ea7
$ git cat-file -p 2d3417788c3f37815df9b34c433eddc67d197ea7100644 blob 980a0d5f19a64b4b30a87d4206aade58726b60e3    beawulf.txt
$ git cat-file -t 2d3417788c3f37815df9b34c433eddc67d197ea7tree
```

‌

### Commit Atmak

```shell
$ git commit-tree 2d3417788c3f37815df9b34c433eddc67d197ea7 -m "Hello World beawulf.txt'ye kaydedildi"
fe2896b8433a639b874fc4917ea6b12755497e74
```

‌

### HEAD Pointer'ı Güncellemek

```shell
$ cat .git/HEADref: refs/heads/master
$ git logfatal: bad default revision ‘HEAD’
$ git update-ref refs/heads/master fe2896b8433a639b874fc4917ea6b12755497e74
$ git logcommit fe2896b8433a639b874fc4917ea6b12755497e74 (HEAD -> master)Author: bbuyukyuksel <buyukyukselburak@gmail.com>Date:   Fri Oct 9 11:47:58 2020 +0300
    Hello World beawulf.txt'ye kaydedildi
```

‌

### Commit Gerçekleştirilmiş Dosyayı Çalışma Alanına Getirmek

```shell
$ ls .
$ git checkout -- beawulf.txt
$ ls .beawulf.txt
$ cat beawulf.txtHello World!
```

‌

Artık manuel olarak commit atma işlemini gerçekleştirebiliyoruz :)

___

# Git Log-Live

‌Bu script linux sistemlerde gerçek zamanlı olarak log takibi yapabilmek için kullanılmaktadır.



```shell
#!/bin/bash
while :
do
   clear
   git --no-pager log --graph --pretty=oneline --abbrev-commit --decorate --all $*
   sleep 1
done
```
