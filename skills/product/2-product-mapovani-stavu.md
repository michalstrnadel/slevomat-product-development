---
name: product-mapovani-stavu
description: "Druhý krok produktové práce ve Slevomat Group — popsat, jak něco dnes funguje, a to ze všech stran: pro zákazníka na webu, při zakládání a nastavení nabídky, pro partnera, v kódu na backendu a pro vyhledávače. Výstupem je popis současného stavu, otázky na kolegy a mezery vůči HMW otázkám z rámování. Použij vždy, když je potřeba zmapovat současný stav nějaké části Slevomatu před návrhem řešení. Triggeruj na fráze jako: zmapuj současný stav, jak to dnes funguje, popiš současné řešení, jak to máme dneska, as is, service blueprint, projdi dokumentaci a kód, co na to říká backend, jak se to nastavuje v adminu, co vidí zákazník, zmapuj to ze všech stran. Navazuje na skill product-definice-problemu-a-hmw. NEPOUŽÍVEJ na hledání řešení ani na hodnocení současného stavu — mapování popisuje, jak to dnes funguje, a řešení se navrhuje až v product-zadani-pro-design."
---
<!-- owner: Romana Trušinová -->
<!-- version: 0.1.0 -->
<!-- updated: 2026-08-14 -->

# Mapování současného stavu

Druhý krok. Cílem je popsat, jak to dnes funguje — ne hodnotit a rozhodně ne navrhovat řešení. Výstup může být delší než stránka, protože se dívá z několika stran.

Vstup: zrámování z kroku jedna (problém, cíl, HMW otázky). Když ho nemáš, vrať se ke skillu product-definice-problemu-a-hmw. Bez HMW otázek mapování neví, co má hledat, a skončí jako obecný popis systému, který nikdo nepoužije.

## Jak psát

Stejně jako v celém procesu:

- **Česky a lidsky.** Tak, jak bys to vysvětlil kolegovi u kávy. Bez anglicismů, kde existuje české slovo.
- **Krátké věty.** Tabulku dělej jen tam, kde opravdu pomůže.
- **Nevymýšlej si.** Když něco nevíš, napiš to jako otázku. Odhad vydávaný za zjištění je tady nejhorší možná chyba, protože na tomhle popisu pak stojí celé zadání.
- **Nehodnoť a nenavrhuj.** Žádné „to je špatně", žádné „mohli bychom to udělat takhle". Jakmile do mapování pustíš jeden nápad na řešení, zbytek se začne podvědomě sbírat na jeho podporu. Nápady, které cestou vzniknou, si odlož do poznámky na konec.

## Nejdřív se rozhodni, které strany mapovat

Neběhej všechny vždycky. Kdo mapuje změnu textu v e-mailu, nemá hrabat v datovém modelu. Zeptej se, čeho se téma týká, a vyber:

| Strana | Kdy ji mapovat |
|---|---|
| Zákazník na webu | skoro vždy |
| Zakládání a nastavení nabídky | vždy, když se to dotkne nabídek nebo jejich obsahu |
| Partner | když to zasáhne jeho práci — objednávky, doprava, fakturace, jeho administrace |
| Backend a datový model | když není jasné, co systém vůbec umožňuje |
| Vyhledávače | když jde o dohledatelnost, vstupní stránky nebo strukturu URL |
| Data | téměř vždy, protože „kolika nabídek se to týká" mění řešení |

Když téma zasahuje ještě někoho dalšího — zákaznickou péči, účetnictví, obchod — přidej si vlastní stranu. Seznam není uzavřený.

## Odkud brát podklady

Hned na začátku si ověř, na které zdroje vůbec dosáhneš, a řekni produkťákovi, co od něj budeš potřebovat. Zkus si zavolat skilly pro dokumentaci, kód a data ještě předtím, než začneš pracovat. Některé smí spustit jen člověk, jiné nemají napojení na databázi. Když to zjistíš až v půlce, produkťák neví, proč to stojí — a junior si bude myslet, že něco pokazil. Rovnou mu napiš seznam: „tohle si spusť ty, tohle mi pošli, tohle přeskočíme".

Nejdřív si zkus zavolat skill sám. Když ti to systém odmítne, předej práci produkťákovi a napiš mu přesně, co má spustit a jaké otázky tam vložit. Nikdy neobcházej odmítnutí tím, že si totéž zjistíš jinudy. Která nastavení jsou zapnutá se v čase mění, proto se to nehádá dopředu — vždycky se to zkusí.

**Dokumentace** — skill slevomat-documentation:slevomat-docs. Čte interní netechnickou dokumentaci nasynchronizovanou v pluginu, nic se neklonuje. Tímhle vždycky začni, protože z dokumentace vzniknou konkrétní otázky do kódu.

**Kód** — skill slevomat-code. Spouštěj ho až po dokumentaci a s konkrétními otázkami, ne naslepo. Když ho nesmíš zavolat, připrav produkťákovi seznam otázek a řekni mu, ať spustí /slevomat-code a odpověď vloží zpátky.

**Data** — skill data-chat. Stejný postup, stejná záložní cesta.

**Zákazník na webu** — potřebuješ od produkťáka odkazy i screenshoty. Vyžádej si seznam ploch, ne jednu obrazovku, jinak zmapuješ jeden detail a mineš celou cestu. Screenshot řekne, co přesně má produkťák na mysli; odkaz ukáže to, co na screenshotu není — co je pod okrajem, co se stane po přepnutí, jak to vypadá na mobilu.

**Zakládání nabídky a partnerská administrace** — do adminu nikdy nechoď sám. Jsou tam živá data a živí partneři. Vyžádej si screenshoty relevantních kroků za sebou a k každému jednu větu, co tam ten člověk dělá. Screenshot ukáže, jak to vypadá, ale ne pravidla — co je povinné, co se validuje, kdo to smí. Na to se musíš zeptat.

Když někdo nemá naklonovaný kód ani přístup do adminu, není to důvod skončit. Tu stranu přeskoč, napiš, že chybí, a připoj konkrétní otázky, které má položit vývojáři nebo člověku od nabídek.

## Jak psát zjištění

Celý výstup se skládá ze dvou malých jednotek.

### Nález

> **Nález:** Varianta nabídky má příznak „doplňková varianta", tedy varianta, která slouží jako příplatek k hlavní variantě.
> **Kde to vidím:** docs/slevomat/products/product-variants.md
> **Co nevíme:** Jestli se to ve zboží vůbec používá a jak se to chová na webu.

Ten třetí řádek je povinný. Nutí přiznat mezeru místo toho, aby se nález tvářil hotově — a rovnou z něj vzniká otázka do další strany.

Zdroj podle strany: kód → konkrétní soubor. Zákazník a admin → screenshot. Dokumentace → cesta k dokumentu. Data → číslo i s dotazem, kterým vzniklo. Bez zdroje to není nález, ale dojem.

**Příčky důkazů.** U každého tvrzení napiš, na které příčce stojí (od nejsilnější): behaviorální data / tickety zákaznické péče a partnerské podpory / rozhovory / desk research / domněnka. Domněnka je platná příčka, jen ji nevydávej za zjištění.

Dvě pravidla, na kterých hodně záleží:

- U backendu odděluj „datový model to dovoluje" od „je to naimplementované". Jsou to dvě úplně jiné zprávy a je to nejčastější místo, kde se produkťák sekne.
- Když se dokumentace a kód rozejdou, platí kód a rozpor se zapíše jako samostatný nález. Není to šum, je to zjištění a někdo pak má opravit dokumentaci.

### Otázka na lidi

> **Otázka:** Používá se ve zboží příznak doplňkové varianty? A pokud ne, proč?
> **Na koho:** tvorba a správa nabídek
> **Proč to potřebujeme:** Pokud se to nepoužívá kvůli nějakému známému problému, nemá smysl na tom stavět.
> **Brzdí další krok:** ano

Piš role, ne jména — jména se mění. Když produkťák jméno zná, doplní si ho sám.

## Struktura výstupu

### 1. Shrnutí na stránku

Lidsky, pět až sedm vět: jak to dnes v hrubých obrysech funguje a co je na tom nejpodstatnější. Tohle si přečte designér, vývojář nebo kolega, který nemá čas na zbytek. Píše se jako poslední, i když stojí první.

Pod shrnutí patří jedna krátká věc: seznam **„existuje, ale nepoužívá se"**. Tedy mechanismy, které v systému už jsou a nikdo je nevyužívá. Když se ukáže, že polovina řešení už leží v systému, je to nejlepší možný výsledek mapování — proto to nesmí být schované uprostřed textu.

### 2. Jak to dnes funguje

Nejdřív mapa, potom text.

Mapa je tabulka na výšku — řádek je krok cesty, sloupec je strana. Na výšku proto, že široká tabulka se nedá číst. Sloupce si uprav podle stran, které mapuješ:

| Krok cesty | Co vidí zákazník | Kde se to nastavuje | Co drží backend | Co vidí vyhledávače |
|---|---|---|---|---|
| Přijde z vyhledávání | | | | |
| Vidí výpis | | | | |
| Otevře nabídku | | | | |
| Vybírá variantu | | | | |
| Dá do košíku | | | | |

Mapa je k tomu, aby bylo vidět, kde se strany potkávají a kde se míjejí. Přesně v těch místech obvykle leží podstata.

Pod mapou ke každé straně krátký text lidsky — co tam reálně je.

U zákazníka a u zakládání nabídky patří do výstupu obrázky, ne jen popis. Bez nich si to nikdo nepředstaví a mapování se nedá předat designérovi ani vývojáři. Dvě pravidla:

- **Výřez, ne celá obrazovka.** Celá stránka adminu je nečitelná. Výřez řádku s příznaky varianty řekne všechno. Ze screenshotů i z PDF exportů si výřezy udělej sám.
- **Ke každému obrázku popisek**, na co se má člověk podívat. Obrázek bez popisku je dekorace.

Jakmile má mapování obrázky, výstupem je HTML stránka — jeden samostatný soubor s obrázky vloženými přímo v něm. Markdown obrázky neunese. Do projektu ulož textový záznam a odkaž z něj na tu stránku, ať se hledá na jednom místě. Do HTML dej i obsah s odkazy, protože mapování bývá dlouhé.

### 3. Co se dá ještě dohledat

Věci, na které existuje odpověď v dokumentaci, kódu nebo datech, jen jsme se k nim nedostali. U každé jak a kde.

### 4. Otázky na lidi ve firmě

Věci, které se dohledat nedají, protože to je rozhodnutí, historický kontext nebo zkušenost v hlavě konkrétního člověka. Seskupené podle role, aby to šlo použít jako agenda na schůzku. Nahoru ty, které brzdí další krok.

### 5. Mezery vůči HMW

Pro každou HMW otázku z rámování tři věci: co už dnes máme, co chybí, co ještě nevíme. Nic víc.

Tohle je ta část, která se nejspíš vynechá, a zároveň ta nejdůležitější. Bez ní vznikne pěkný dokument, ke kterému se nikdo nevrátí. S ní je z mapování odpaliště pro návrh řešení.

### Na konci: poznámka s odloženými nápady

Cokoli, co cestou vypadlo jako nápad na řešení. Neztrácí se, ale ani to neovlivní popis. Otevře se v kroku čtyři.

## Co do výstupu nepatří

Řešení. Ani jedna věta. Odhady náročnosti. Na to je krok pět; tady stačí popsat, co je hotové a co ne. Hodnocení a seznamy problémů. Mezery vůči HMW jsou odečet, ne rozsudek.

## Než jdeš dál

- Na začátku bylo řečeno, na které zdroje dosáhneš a co je potřeba od člověka
- Je jasné, které strany se mapovaly a proč zbylé ne
- U zákazníka a u adminu jsou ve výstupu výřezy s popisky, ne jen text
- Každý nález má zdroj a řádek „co nevíme"
- U backendu je odděleno, co model dovoluje, a co je naimplementované
- Rozpory mezi dokumentací a kódem jsou zapsané
- Otázky na lidi jsou seskupené podle role a je u nich, proč je potřebujeme
- U každé HMW je vidět, co máme, co chybí a co nevíme
- V celém dokumentu není ani jedno navržené řešení

## Co následuje

Konkurence a inspirace — jak to řeší ostatní a co z toho platí pro nás. Pak zadání pro design (skill product-zadani-pro-design), provozní dopad a zadávání v adminu, a nakonec zadání pro vývoj (skills psani-zadani a kontrola-zadani). Hotový prototyp se projede skillem slevomat-design-principles — ten posuzuje, nenavrhuje.
