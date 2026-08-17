---
name: product-definice-problemu-a-hmw
description: První krok produktové práce ve Slevomat Group — rychle zrámovat, co vlastně řešíme. Vede k jasnému popisu problému, jasnému cíli a k HMW otázkám (hlavní a dílčí). Použij vždy, když přichází produktové téma, které ještě není zrámované, ať jde o cokoli — zboží, cestování, zážitky, košík, admin pro partnery, cokoli dalšího. Triggeruj na fráze jako: zrámuj problém, rámování problému, pomoz mi popsat problém, napiš HMW, how might we, jak bychom mohli, jaký je vlastně problém, chci řešit X, máme nápad na Y, začínáme nové téma, definuj cíl, nevím kudy do toho, pojďme si to ujasnit. Použij i sám od sebe, když někdo skočí přímo k řešení nebo k mapování stavu, aniž by bylo jasné, za čím jde. NEPOUŽÍVEJ, když někdo chce od nuly interní nástroj, appku nebo jednorázovku — to není produktové téma platformy a rozhovor o problému tam vede slevomat-product-development.
---
<!-- owner: Romana Trušinová -->
<!-- version: 0.1.0 -->
<!-- updated: 2026-08-14 -->

# Rámování problému

První krok. Než se začne cokoli řešit, musí být jasné tři věci: co je problém, čeho chceme dosáhnout a jaké jsou HMW otázky. Půl hodiny práce a jedna stránka výstupu. Nic víc.

Nepoužívej na opravy chyb, na povinnosti z legislativy a na témata, která už zrámovaná jsou — tam jdi rovnou na mapování současného stavu.

## Jak psát

Tohle je nejdůležitější část, protože podle ní se pozná dobré rámování od nepoužitelného.

- **Česky a lidsky.** Tak, jak bys to vysvětlil kolegovi u kávy. Žádné anglicismy, žádné poučky, žádné tabulky, kde stačí věta.
- **Krátké věty.** Když to jde říct jednodušeji, řekni to jednodušeji.
- **Přiznej, čeho se bojíte** a kam se to může rozšířit, když do toho začnete šťourat. Je lepší to říct hned než to zjistit v půlce.
- **Nevymýšlej si data.** Když číslo nemáš, napiš, že ho nemáš, a jdi dál. Nebrzdi kvůli tomu celé rámování.
- **Příčky důkazů.** U každého tvrzení napiš, na které příčce stojí (od nejsilnější): behaviorální data / tickety zákaznické péče a partnerské podpory / rozhovory / desk research / domněnka. Domněnka je platná příčka, jen ji nevydávej za zjištění.
- **Buď kritický.** Když je v zadání schované řešení nebo se to celé opírá o domněnku, řekni to. U každého rizika, které najdeš, navrhni aspoň jednu cestu, jak ho zmírnit.

## Na co se ptát

**1. Co je problém?** Co se děje, komu to vadí a proč nám na tom záleží. Klidně i to, čeho se u toho bojíte.

Dvě věci hlídej:

- Slyšíš řešení místo problému („chybí nám filtr")? Zeptej se, co uživatel nemůže udělat, když ten filtr nemá.
- Slyšíš metriku místo problému („klesá nám traffic")? Zeptej se, co konkrétně se nedaří uživateli nebo Googlu.

A vždycky se zeptej: **co se stalo, že to řešíme zrovna teď?** Spouštěč a opakovaná potřeba jsou často dvě různé věci — jednorázová dávka teď a nástroj na potom. Ta otázka odděluje akutní od chronického a často změní rozsah; když se spouštěč a potřeba liší, patří do rámování obě.

**2. Čeho chceme dosáhnout?** Jedna, dvě věty. Co má být jinak, až to vyřešíme — v chování uživatelů nebo v byznysu, ne v tom, co dodáme. Když máš po ruce číslo, kde jsme dnes, napiš ho. Když ne, nic se neděje.

**3. Jaké jsou HMW otázky?** Jedna hlavní a k ní dílčí.

Hlavní drží celek pohromadě. Dílčí rozdělují téma na části, které se dají řešit samostatně. Rozděluj tehdy, když mají části jiného uživatele, jiný moment nebo jinou technickou vazbu.

Dílčí otázky piš stejným střihem, ať jsou srovnatelné:

*Jak bychom mohli pomoct (komu, například zákazníkovi / partnerovi) dosáhnout (čeho, co chce udělat, čeho mu pomůžeme dosáhnout), tak aby (co z toho plyne za měřitelný outcome, ideálně byznysový nebo alespoň měřitelný prouživatelský)?*

Tři věci, na kterých ta šablona stojí:

- **Komu pomáháme** je konkrétní člověk v konkrétní situaci, ne „uživatel" obecně. Jinak se řešení navrhuje do prázdna.
- **Konkrétní příklad v závorce.** Bez něj si každý představí něco jiného a na schůzce se pak dohadujete o slovech.
- **Měřitelný outcome na konci.** Ideálně byznysový (AOV, konverze, počet položek v objednávce, náklady na obsluhu), a když takový není po ruce, tak aspoň měřitelně uživatelský (dokončí krok, najde produkt, nemusí volat na péči). Když na konci stojí něco, co se nedá změřit („aby to bylo přehlednější"), nikdo pak nepozná, jestli to zabralo — přepiš to.

Zkouška: jdou na tu otázku vymyslet aspoň tři zásadně různá řešení? Když ne, je moc úzká a už v sobě nese odpověď.

## Jak má vypadat výstup

Napiš ho jako text přímo do odpovědi v chatu. Nevytvářej k tomu žádný soubor, dokument ani artefakt — je to jedna stránka, kterou si člověk přečte hned a zkopíruje si ji, kam potřebuje. Zakládat kvůli tomu přílohu jen zdržuje.

Přesně takhle jednoduše. Tři bloky — problém, cíl, HMW — a nic navíc. Žádné nadpisy, tabulky ani přílohy. Co je fakt a co domněnka a čeho se bojíte napiš dovnitř bloku s problémem, ne jako další sekci. Kontrolní seznam na konci tohohle skillu je pro tebe, ne pro výstup — nevypisuj ho.

```
Problém který řešíš: Dělíme heterogenní dealy ve zboží (protože je to tak mnohem
lepší pro lidi i pro SEO), ale máme u toho strach, že pak lidi nenajdou produkty,
které spolu fakt souvisí. To by škodilo uživatelům i byznysu. Zároveň víme, že když
do toho začneme šťourat, dost možná z toho vznikne redesign produktového detailu
ve zboží, protože problémů má hodně.

Cíl: Zvýšit traffic do zboží (díky rozděleným a lépe zacíleným dealům) a zároveň
udržet dohledatelnost souvisejících produktů a tím zvýšit AOV.

HMW:
Hlavní: Jak bychom mohli efektivně rozdělit heterogenní dealy a zároveň zajistit,
že související produkty budou vždy dobře vidět u sebe?

Dílčí:
Sety: Jak bychom mohli pomoct zákazníkovi, který si vybral jeden kus, koupit ho
i v setu (například k náhrdelníku i náhrdelník s náušnicemi), tak aby vzrostla
průměrná hodnota objednávky ve zboží?

Příslušenství: Jak bychom mohli pomoct zákazníkovi, který si vybral produkt,
doplnit si k němu příslušenství (například k misce na pěstování bylinek i bylinky),
tak aby vzrostl průměrný počet položek v objednávce?

Řady: Jak bychom mohli pomoct zákazníkovi, který si vybral produkt, objevit další
zboží ze stejné řady (například k vanilkovému šamponu vanilkový krém), tak aby
vzrostl podíl objednávek s více než jednou položkou?
```

Tohle je příklad ze zboží, ale struktura je stejná na cokoli — cestování, zážitky, košík, admin pro partnery. Mění se obsah, ne forma.

## Než jdeš dál

- Problém je popsaný lidsky a není v něm schované řešení
- Je jasné, co je fakt a co domněnka
- Je zapsané, co rámování spustilo právě teď — a jestli je spouštěč totéž co opakovaná potřeba
- Cíl říká, co bude jinak, ne co dodáme
- Je jedna hlavní HMW a dílčí jsou psané stejným střihem, každá s konkrétním příkladem
- Každá dílčí HMW končí měřitelným outcomem, ne dojmem
- Na každou HMW jdou vymyslet aspoň tři různá řešení
- Výstup je text v odpovědi, ne soubor ani artefakt

Když něco chybí, řekni konkrétně co. Neposouvej se s tím, že se to dodělá potom.

## Co následuje

Mapování současného stavu — jak to dnes funguje, kde jsou problémy. Pak konkurence a inspirace, zadání pro design (skill design-prototypovani), provozní dopad a zadávání v adminu, a nakonec zadání pro vývoj (skills psani-zadani a kontrola-zadani). Hotový prototyp se projede skillem slevomat-design-principles — ten posuzuje, nenavrhuje.
