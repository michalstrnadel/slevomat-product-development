---
name: design-prototypovani
description: "Předávací bod mezi produktem a designem (krok 4 produktové práce) — napíše zadání pro Claude Design (nebo pro designéra) na prototyp konceptu, který už má někdo rozmyšlený — produkťák, designér nebo výzkumník. Výstupem je samonosný brief, se kterým se dá odstartovat konverzace s designem — obsahuje HMW, cíl, kontext systému, tvrdá omezení, ověřená doporučení, stavy a co má prototyp ověřit. Použij vždy, když chce někdo nechat nakreslit nebo naprototypovat produktový koncept. Triggeruj na fráze jako: zadání pro design, prompt pro claude design, brief pro designéra, chci to nadesignovat, chci prototyp, nechte to nakreslit, připrav zadání designérovi, jdeme prototypovat, chci si to nakreslit, zadání na prototyp. Navazuje na skilly product-definice-problemu-a-hmw, product-mapovani-stavu a product-konkurence-inspirace. NEPOUŽÍVEJ, když člověk nemá za sebou rámování a mapování — tam patří nejdřív product-definice-problemu-a-hmw."
---
<!-- owner: Michal Strnadel -->
<!-- version: 0.2.0 -->
<!-- updated: 2026-08-18 -->

# Zadání pro design

Krok 4 produktového procesu. Cílem je samonosný brief, se kterým produkťák odstartuje konverzaci s Claude Design a dostane prototyp.

## Kdy to použít a kdy ne

Použij, když je koncept už rozmyšlený — je jasné, jaké plochy nebo obrazovky mají vzniknout a co na nich má být. Tenhle skill zadání sepisuje, nevymýšlí ho.

Nepoužívej, když koncept ještě není. Když produkťák neví, co má vzniknout, vrať ho na krok 1 až 3 — bez zrámovaného problému a bez znalosti současného stavu vznikne brief, který designéra pošle hádat.

Nepoužívej ani na interní nástroje a jednorázovky stavěné od nuly, bez procesu za sebou. Tenhle skill předpokládá, že rozhovor o problému už proběhl v krocích 1 až 3 — když ne, začni krokem 1, product-definice-problemu-a-hmw.

A jedna hranice, na kterou pozor: když v zadání píšeš rozvržení, píšeš už specifikaci, ne brief pro design. Brief říká jaký problém, jaká omezení a jak pozná dobrý výsledek. Neříká „udělej modál se třemi dlaždicemi". Když produkťák přesně ví, jak to má vypadat, nepotřebuje designéra a má jít na skill psani-zadani.

## Pravidlo, na kterém všechno stojí

Brief musí být samonosný. Designér nezná z vaší konverzace ani slovo. Žádné „jak jsme se bavili", žádné „ten problém, co řešíme", žádné interní zkratky bez vysvětlení. Když si to po sobě přečteš jako někdo, kdo o tématu slyší poprvé, a někde ti chybí kontext, chybí i designérovi.

Délku tomu podřiď. Dlouhý brief není známka důkladnosti, ale toho, kolik kontextu je potřeba přenést. Struktura ať se dá skenovat.

A celý brief vypiš jako **jeden blok ke zkopírování**. Produkťák ho vkládá do nové konverzace v Claude Design — skládání ze tří zpráv je přesně to místo, kde se půlka ztratí.

## Nejdřív se zeptej na čtyři věci

Bez nich bude zadání vágní:

- **Rozsah** — jen nové věci, nebo i to, co už existuje? Kreslit celou obrazovku, nebo výřezy? (Když se přidává něco do existující stránky, obvykle je správné kreslit ji celou, protože rozhodnutí o hierarchii nejde udělat po částech.)
- **Věrnost** — drátěný model, nebo vizuál? Design systém se neřeší otázkou: prototypy se u nás stavějí v **Mini*S**. Brief ho jmenuje a vizuální pravidla nepopisuje — ta jsou v instrukcích design systému, ne v briefu.
- **Zařízení** — mobil, desktop, nebo obojí.
- **Kolik směrů** — jeden dotažený návrh, nebo dva až tři odlišné směry vedle sebe? Neptej se naprázdno, rovnou doporuč: když má HMW otázka víc rozumných odpovědí a z kroků 1 až 3 žádná nevyšla jako vítěz, chtěj víc směrů v hrubé věrnosti. Když je koncept rozhodnutý a jde už jen o provedení, chtěj jeden a dotažený.

Ta čtvrtá otázka tam je proto, že Claude Design ti sám od sebe nakreslí první řešení, které mu přijde dobré, a od druhé zprávy dál už jen vylepšuje jeho. Debata se tím posune z „je tohle správný směr?" na „co s ním ještě uděláme" — a to je tiché rozhodnutí, které nikdo neudělal.

## Odkud brát obsah briefu

- HMW, cíl a metriku z kroku 1
- Tvrdá omezení, datový model a co dnes existuje z kroku 2
- Ověřená doporučení s čísly a zdroji z kroku 3

**Příčky důkazů.** U každého tvrzení napiš, na které příčce stojí (od nejsilnější): behaviorální data / tickety zákaznické péče a partnerské podpory / rozhovory / desk research / domněnka. Domněnka je platná příčka, jen ji nevydávej za zjištění. Tvrzení si příčku nesou z kroků 1 až 3 — designér pak ví, o co se smí opřít.

Když některý krok neproběhl, napiš to do briefu jako chybějící vstup a řekni, co z toho plyne. Brief bez omezení z mapování vede k designu, který se nedá postavit.

## Struktura briefu

### 1. Co designuješ

Jeden odstavec. Co, kolik ploch, jaký rozsah. A když je rozsah vědomě velký, řekni to hned — viz pravidlo o napětí níž.

### 2. Kontext systému, lidsky

Tohle se nejčastěji vynechá a je to nejdražší chyba. Designér, který nechápe, jak je produkt postavený, nakreslí obecný e-shop. Vysvětli v pár odrážkách to, co se u vás liší od běžné intuice — co je vlastně produkt, co varianta, co vidí zákazník ve výpisu, kdo je partner, jak dlouho věci žijí.

### 3. Reálné příklady z katalogu

Vždycky. Dej tři až pět skutečných příkladů se jmény, počty variant a cenami. Designér pak kreslí na reálném obsahu, ne na lorem ipsum — a hned vyjde najevo, že „výběr varianty" pro tři velikosti a pro 62 druhů koření není totéž.

### 4. Proč to řešíme

Krátce a bez marketingu. Klidně i to, čeho se bojíte.

### 5. Cíl, metrika, guardrail

Co má být jinak, čím to změříme, a co se nesmí zhoršit.

### 6. Co má prototyp ověřit a co by koncept zabilo

Jednou větou, co se z prototypu chceme dozvědět. A předem napsaný výsledek, po kterém koncept nepokračuje — napsaný teď, protože po ukázání už to bude racionalizace. Prototyp je experiment, a experiment bez předem napsané podmínky selhání nemůže selhat — vyrobí mandát místo odpovědi.

Komu to ukážeme a kdy: jména a termín, ne „plánujeme testování".

### 7. HMW otázky

Hlavní i dílčí, tak jak vznikly v kroku 1. Beze změn.

### 8. Plochy nebo obrazovky: co kam a proč

U každé plochy tři věci: co tam patří, proč právě tam, a jak se to bude plnit (ručně, pravidlem, automaticky).

To „proč" je klíčové. Bez něj designér plochu vyzdobí, místo aby ji navrhl. A informace o tom, jak se to plní, rozhoduje o rozvržení — ruční vazby znamenají málo položek a proměnlivý počet, tedy nikdy pevnou mřížku.

### 9. Začni od screenshotů současného stavu

Když plochy přidáváš do něčeho, co už existuje, nenech designéra kreslit od nuly a nevypisuj mu, co na stránce je. Řekni mu, ať si načte screenshoty dnešního stavu a upravuje je. Screenshoty dodá produkťák.

A připoj instrukci, ať se ptá, když mu na screenshotu není jasné, proč tam prvek je, čím se plní nebo co se stane po kliknutí. Ze screenshotu se nepozná logika a právě v ní bývají chyby, které nemá zopakovat.

### 10. Tvrdá omezení

Číslovaný seznam. U každého napiš, co z něj pro design plyne — ne jen fakt, ale i jeho důsledek. „Většina košíků má jeden produkt a poštovné se platí za každého partnera zvlášť, takže nekresli mechaniku přidej všechno do košíku napříč partnery."

### 11. Ověřená doporučení s čísly a zdroji

To, co vyšlo z kroku 3. S čísly a se zdrojem, protože podle toho se pak výsledek dá hodnotit, aniž by to byla otázka vkusu.

### 12. Stavy, na které nesmí zapomenout

Nikdy nevynechávej. U každé plochy: prázdno, jedna položka, hodně položek, navázaná věc skončila nebo je nedostupná. U ručně zadávaných vazeb je „jedna položka" nejčastější stav a poloprázdná plocha vypadá nedodělaně.

### 13. Co je v prototypu nafejkované

Prototyp z Claude Design vypadá hotově a někdo ho ukáže na poradě, kde se přečte jako rozhodnutí. Napiš, co bude vymyšlené (data, čísla, obsah), co nikam nevede (mrtvá tlačítka) — a co z toho plyne pro ukazování, aby session nenarazila na zeď a reviewer nehlásil slepé uličky jako chyby.

### 14. Co nedělat

Konkrétně. A rozlišuj „tohle u nás existuje a je to špatně, nekopíruj to" od „tohle existuje a je to v pořádku". Referenci u konkurence taky klidně označ za varovný příklad.

Vzory zavržené v kroku 3 sem patří **jmenovitě a s důvodem**, ne jako obecné „nedělej FOMO". Jinak je designér za tři týdny navrhne znovu a nikdo si nevzpomene, proč vypadly.

### 15. Co chceš dostat

Seznam. Plochy, zařízení, stavy, celý kontext obrazovky. A dvě věci, které se vyplatí chtít vždycky:

- Názor, co ubrat, když je rozsah vědomě velký
- Seznam míst, kde mu chyběla komponenta v design systému nebo kde musel něco rozhodnout za vás

**Kolik směrů, napsané číslem.** Ne „udělej varianty", ale „dva směry, které řeší HMW #2 každý jinak". Když chceš jeden, napiš i to — bez téhle věty si počet vybere designér za tebe. A ať se směry liší v tom, jak řeší problém, ne v barvě tlačítka; tři odstíny téhož nejsou volba.

Když chceš víc směrů, přidej do briefu i tuhle větu: *„Nakresli směry nejdřív hrubě a nech mě vybrat, než začneš cokoli dotahovat."* Jinak dostaneš jeden hotový a dva odbyté.

### 16. Otázky, které má vyhodit nahoru, ne rozhodnout sám

Věci, které nejsou designové, ale produktové nebo obchodní. Bez tohohle seznamu je designér rozhodne potichu a vy to zjistíte pozdě.

## Tři pravidla, která oddělují dobrý brief od průměrného

**Pojmenuj napětí, které vědomě přijímáš.** Když víš, že rozsah je proti pravidlu nebo proti doporučení, napiš to. „Adobe doporučuje maximálně tři doporučovací plochy na stránku, nám jich vychází sedm. Je to vědomé, proto kreslíme všechno a proto budeme škrtat." Bez toho designér buď potichu škrtne sám a vy přijdete o možnosti, nebo dodá něco slabého a nebude vědět proč.

**Řekni, co je nepřekročitelné a co je k diskusi.** Designér nepozná rozdíl mezi „takhle to máme" a „takhle to musí zůstat".

**Nechtěj po designérovi, aby dohadoval čísla.** Když v zadání není baseline ani metrika, nemůže vážit, co je důležité.

## Nabídni a počkej

Hotový brief se neodešle, nabídne se: *„Napsal jsem zadání — projdi ho a řekni, co doplnit nebo změnit."* A když produkťák řekne „tohle jsem neřekl", přepiš pole jeho opravou — bez hádání o tom, co bylo řečeno. Je to rozdíl mezi zadáním, za kterým člověk stojí, a zadáním, které mu někdo vnutil.

## Než to pošleš

- Přečteno očima někoho, kdo o tématu slyší poprvé, a nikde nechybí kontext
- Jsou tam reálné příklady z katalogu, ne obecné popisy
- Je napsané, co má prototyp ověřit, co by koncept zabilo, a komu se ukáže — jména a termín
- U každé plochy je „proč tam" a „čím se plní"
- Omezení mají napsaný důsledek pro design, ne jen fakt
- Jsou vyjmenované stavy včetně prázdna a jedné položky
- Je napsané, co bude v prototypu nafejkované
- Zavrhnuté vzory z kroku 3 jsou v „Co nedělat" jmenovitě, s důvodem
- Je řečeno, co je nepřekročitelné
- Je vyjmenované, co má vyhodit nahoru místo rozhodnutí
- Není tam napsané rozvržení — to už by byla specifikace
- Je napsané, kolik směrů chceš a v čem se mají lišit
- Brief je jeden blok ke zkopírování a byl nabídnut k projití, ne odeslán

## Co následuje

Až prototyp přijde, projeď ho skillem slevomat-design-principles proti sedmi principům. Pak krok 5, provozní dopad a zadávání v adminu, a krok 6 zadání pro vývoj (psani-zadani, kontrola-zadani).
