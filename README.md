# Slevomat Product Development

Pět skillů pro produktovou práci ve Slevomatu, připravených pro Skill Hub. Od zrámování problému přes mapování stavu a konkurenci až po zadání pro design a kontrolu výsledku proti sedmi principům.

Vlastníci: Romana Trušinová (kroky 1–3), Michal Strnadel (prototypování, principy).

## K čemu to je

Stavět už není problém. Problém je vědět co.

Produkťák dnes napíše „chceme filtr podle značky" a za dva dny existuje prototyp, který někdo ukáže na poradě, kde se přečte jako rozhodnutí — přitom to byl nápad ze schůzky, za kterým nikdo nestál. Tyhle skilly jsou tu proto, aby se před tím prototypem stalo něco jiného: aby byl pojmenovaný problém, aby bylo jasné, co už v systému je, a aby zadání pro design říkalo, **co se z prototypu chceme dozvědět a co by ten koncept zabilo.**

Ambice není proces. Ambice je, že člověk odejde s tím, že o svém tématu ví něco, co nevěděl, když přišel — a že se postaví jen to, co za postavení stojí.

## Pět skillů

| Skill | Kdy | Co z něj leze |
|---|---|---|
| `product-definice-problemu-a-hmw` | přichází téma, které není zrámované | problém, cíl, HMW otázky — jedna stránka v odpovědi |
| `product-mapovani-stavu` | před návrhem řešení je potřeba vědět, jak to dnes funguje | popis ze všech stran, otázky na kolegy, mezery vůči HMW |
| `product-konkurence-inspirace` | je zmapováno a chybí inspirace | jak stejné HMW řeší jinde, členěné podle otázek |
| `design-prototypovani` | koncept je rozmyšlený a má se nakreslit | samonosný brief pro Claude Design, jeden blok ke zkopírování |
| `slevomat-design-principles` | je co posoudit — nápad, obrazovka, hotový prototyp | verdikt po principech: Drží / Riziko / Porušuje / Nejde posoudit |

Kroky 5 a 6 procesu (provozní dopad, zadání pro vývoj) už v Hubu žijí jako `psani-zadani` a `kontrola-zadani`.

## Čtyři věci, na kterých to stojí

**Spouštěč není totéž co potřeba.** „Přegenerujeme všechny obrázky kvůli nové kreativě" je jednorázová dávka; „občas potřebuju nový obrázek" je nástroj. Když se ty dvě věci liší, patří do rámování obě a člověk rozhodne, které z nich má stavba sloužit. Stálo nás to jedno zadání, které vyloučilo přesně to, co celý požadavek spustilo.

**Povinný řádek „Co nevíme".** Každý nález má tři řádky: co vidím, kde to vidím, co nevíme. Ten třetí nutí přiznat mezeru ve chvíli zápisu — jinak se nález tváří hotově a za týden ho někdo cituje jako fakt.

**„Existuje, ale nepoužívá se."** Mechanismy, které v systému už jsou a nikdo je nevyužívá, patří hned pod shrnutí. Když se ukáže, že polovina řešení už leží v systému, je to nejlepší možný výsledek mapování.

**Příčky důkazů, jednotné napříč kroky.** U každého tvrzení stojí, na čem stojí: behaviorální data / tickety zákaznické péče a partnerské podpory / rozhovory / desk research / domněnka. Domněnka je platná příčka — jen se nesmí vydávat za zjištění. Validátor kontroluje, že je ta formulace všude doslova stejná, protože jinak přestanou být tvrzení srovnatelná mezi kroky.

## Jak psát

Česky a lidsky, tak, jak bys to vysvětlil kolegovi u kávy. Tykání. Krátké věty. Slovníkem firmy — nabídka, výpis, košík, partner, ne „PDP" a „landing". Žádné emoji.

Assertions v evalech jsou anglicky, protože je čte model, ne člověk.

A pravidlo, které drží zbytek: **u každého pravidla stojí důvod hned pod ním.** Pravidlo bez důvodu odargumentuje první člověk, který to zkusí.

## Kontrola

```
python3 validate.py
```

Osm kontrol, každá z toho, co se reálně rozbilo: frontmatter, pojmenování podle pravidel Hubu, hranice „kdy NEpoužívat" v description, odkazy mezi skilly, meze Hubu (jen textové formáty, nejvýš tři úrovně cesty), firemní slovník a emoji, doslovná shoda příček důkazů, a struktura evalů. CI to pouští na každý push.

Strukturální kontrola ale nepozná, jestli se skill chová jako kolega. Na to jsou evaly v `skills/evals/` — pět scénářů, každý z toho, co už jednou selhalo, hraných jako skutečný rozhovor. Podrobně v [skills/evals/README.md](skills/evals/README.md).

## Kde to je

```
skills/product/    kroky 1–3, a README pro Romču s tím, co se změnilo a proč
skills/design/     prototypování a principy (s přílohou sedmi principů)
skills/evals/      scénáře, jeden soubor na skill, plus runner
```

Zdroj pravdy je Skill Hub, tenhle repozitář je pracovní verze. Do Hubu se nahrává obsah odsud; když se rozejdou, platí Hub.

## Stav

Pět skillů leží v Hubu jako **drafty** — vidí je jen autor, dokud je Andre neschválí. Kroky 1–3 vycházejí z Romčiných osobních skillů, které používá; verze v tomhle repu je přepracovaná (hubová jména, hranice, příčky důkazů, otázka spouštěče) a **tuhle verzi zatím nikdo neprovozoval.**

Kritérium, podle kterého se pozná, že to funguje: do týdne po zveřejnění dvě zrámovaná témata od někoho jiného než od nás dvou. Když nepřijdou, není to o rozšiřování — je potřeba se ptát, proč to nikdo nepoužil.

Historie: Claude Code plugin s třinácti skilly na stavbu prototypů žil v tomhle repu do 17. 8. 2026 a je v tagu `plugin-archive-v0.24.0`. Vrátit ho jde jedním příkazem: `git checkout plugin-archive-v0.24.0 -- plugin .claude-plugin`.

## Interní nástroj

Neobsahuje přihlašovací údaje, citlivá data ani cesty k datům, a nesmí je obsahovat ani po jakékoli úpravě.
