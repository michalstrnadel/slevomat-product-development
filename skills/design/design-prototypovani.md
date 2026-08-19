---
name: design-prototypovani
description: "Předávací bod mezi produktem a designem (krok 4 produktové práce) — napíše zadání pro Claude Design (nebo pro designéra) na prototyp konceptu, který už má někdo rozmyšlený — produkťák, designér nebo výzkumník. Výstupem je samonosný brief, se kterým se dá odstartovat konverzace s designem — obsahuje HMW, cíl, kontext systému, tvrdá omezení, ověřená doporučení, stavy a co má prototyp ověřit. Použij vždy, když chce někdo nechat nakreslit nebo naprototypovat produktový koncept. Triggeruj na fráze jako: zadání pro design, prompt pro claude design, brief pro designéra, chci to nadesignovat, chci prototyp, nechte to nakreslit, připrav zadání designérovi, jdeme prototypovat, chci si to nakreslit, zadání na prototyp. Navazuje na skilly product-definice-problemu-a-hmw, product-mapovani-stavu a product-konkurence-inspirace. NEPOUŽÍVEJ, když člověk nemá za sebou rámování a mapování — tam patří nejdřív product-definice-problemu-a-hmw."
---
<!-- owner: Michal Strnadel -->
<!-- version: 0.4.0 -->
<!-- updated: 2026-08-18 -->

# Zadání pro design

Čtvrtý krok. Koncept je rozmyšlený a jde se designovat a prototypovat — je jasné, jaká feature vzniká, jaké obrazovky k ní patří a kudy jimi člověk projde. Sepiš design brief, se kterým se dá otevřít konverzace s Claude Design. Tenhle skill zadání sepisuje, nevymýšlí ho.

Nepoužívej, když koncept ještě není. Bez zrámovaného problému a bez znalosti současného stavu vznikne brief, který designéra pošle hádat — vrať se na kroky 1 až 3.

Když ti někdo rovnou diktuje tvar — „udělej modál se třemi dlaždicemi" — neber to jako hotovou věc, ale ani ho neposílej pryč. Zeptej se, odkud ten tvar je a co by ho zbouralo. Většinou se ukáže, že rozhodnutý není a je to nápad z porady; pak píšeš normální brief a tvar do něj nedáváš. Když rozhodnutý opravdu je, na kreslení už designéra nepotřebuješ — jdi na psani-zadani, nebo si k tomu vyžádej feedback od designéra.

Brief říká, jaký je problém, jaká jsou omezení a podle čeho se pozná dobrý výsledek. Neříká, jak to má vypadat.

## Jak psát

- **Samonosně.** Designér nezná z vaší konverzace ani slovo. Žádné „jak jsme se bavili", žádné „ten problém, co řešíme", žádné interní zkratky bez vysvětlení. Přečti si to po sobě jako někdo, kdo o tématu slyší poprvé — kde chybí kontext tobě, chybí i jemu.
- **Česky a lidsky.** Krátké věty. Slovníkem firmy — nabídka, výpis, košík, partner. Ať se to dá skenovat.
- **Tak dlouhé, kolik je kontextu.** Délka není známka důkladnosti. Dlouhý brief znamená jen to, že se toho hodně přenáší.
- **Celý brief v jednom bloku přímo v chatu.** Nevytvářej k tomu žádný soubor, dokument ani artefakt — vypiš ho v odpovědi vcelku, jako jeden blok ke zkopírování. Vkládá se do nové konverzace s Claude Design a rozdělený do tří zpráv by se z půlky ztratil. Zkopírovat se ale nemá dřív, než si ho produkťák přečte, proto ho nabídni k projití, ne k odeslání.

## Na co se ptát

Čtyři věci. Bez nich bude brief vágní.

**1. Co se designuje.** Nová feature, nebo celý flow? A designuje se celá obrazovka, nebo jen ta jedna feature v ní? Když se něco přidává do existující stránky, obvykle je správné vzít ji celou — hierarchii nejde rozhodnout po částech.

**2. Jak daleko.** Hrubý wireframe, který má rozhodnout směr, nebo rovnou návrh v komponentách? Víc se neptej: že se staví v **Mini*S**, z jeho komponent a tokenů, je dané. Jmenuj ho a vizuální pravidla nepopisuj, ta má v sobě.

**3. Zařízení.** Mobil, tablet, desktop, nebo kombinace.

**4. Kolik směrů.** Jeden dotažený návrh, nebo dva až tři odlišné vedle sebe? Volba je na produkťákovi, ty mu k ní dej doporučení. Když se na HMW otázku dá odpovědět víc způsoby a z kroků 1 až 3 žádný nevyhrál, doporuč dva až tři směry, každý jen ve wireframu, ať je co porovnat. Když je koncept rozhodnutý a jde už jen o provedení, doporuč jeden a dotažený. Nenech to ale nevyřčené — Claude Design pak nakreslí první rozumné řešení, které ho napadne, a od druhé zprávy dolaďuje už jenom to. Od té chvíle se bavíte o provedení, ne o směru.

## Odkud brát obsah

- HMW, cíl a metriku z kroku 1
- Tvrdá omezení, datový model a co dnes existuje z kroku 2
- Ověřená doporučení s čísly a zdroji z kroku 3

**U každého tvrzení napiš, odkud je.** Od nejsilnějšího: behaviorální data / tickety zákaznické péče a partnerské podpory / rozhovory / desk research / domněnka. Domněnka je v pořádku, jen ji nevydávej za zjištění. Označení se nese z kroků 1 až 3, ať Claude Design ví, čemu může věřit.

**Řekni produkťákovi, co od něj potřebuješ, hned na začátku.** Napiš mu seznam: skutečné příklady nabídek se jmény a cenami, screenshoty ploch, kterých se to týká, tvrdá omezení a datový model z mapování. Tohle musí dohledat a málokdy to má po ruce.

Když to nedodá, brief napsat můžeš — jen ať nahoře stojí, co v něm chybí a že se takhle nemá posílat dál. Když ale chybí skoro všechno, žádný brief z toho není. Řekni mu to a počkej, až podklady sežene.

**Tři věty si vytáhni z produkťáka rovnou.** Nikde je nehledá, ví je hned:

- **Co je problém a proč to řešíte.** Jedna věta. Když nemá zrámování z kroku 1, tohle je minimum, bez kterého Claude Design kreslí do prázdna.
- **Co jdete prototypem testovat.** Co konkrétně se z něj chcete dozvědět.
- **Co by koncept zabilo.** Výsledek, po kterém nepokračujete.

Bez těch tří vět brief nepiš. Prototyp, u kterého nikdo předem neřekl, kdy je špatně, dopadne dobře vždycky.

Když je produkťák říct nechce, nabídni mu dvě jiné cesty: buď je tvar rozhodnutý a stačí psani-zadani, nebo se prototyp na tenhle termín dělat nemá. Řekni to jednou a rozhodnutí nech na něm.

**Co nevíš, si nedomýšlej.** Když do sekce „tohle nevíme" napíšeš svůj odhad, Claude Design ho přečte jako zadání — bude to nejkonkrétnější věta v celém briefu a bude se jí držet. Napiš tam jen, co chybí a co to pro návrh znamená.

A na čem trváš, na tom trvej i za dvě zprávy. Když řekneš „bez tohohle brief nenapíšu", tak ho pak bez toho nenapiš.

## Co v briefu stojí

### 1. Co se designuje

Jeden odstavec. Jaká feature, kolik obrazovek, jak velký rozsah.

Když je toho na jednu obrazovku hodně, napiš rovnou, co s tím: jestli chceš vidět všechno a škrtat až potom, nebo jestli má designér sám vybrat, co je důležitější. Když mu to nenapíšeš, rozhodne to za tebe a nedozvíš se o tom.

### 2. Jak je systém postavený

Tohle se vynechává nejčastěji a stojí to nejvíc. Designér, který nechápe, jak je produkt postavený, nakreslí obecný e-shop. Vysvětli v pár odrážkách, co se u vás liší od běžné intuice — co je vlastně produkt, co varianta, co vidí zákazník ve výpisu, kdo je partner, jak dlouho věci žijí.

### 3. Skutečné příklady

Tři až pět reálných nabídek se jmény, počty variant a cenami. Designér pak kreslí na skutečném obsahu, ne na lorem ipsum — a hned je vidět, že „výběr varianty" pro tři velikosti a pro 62 druhů koření není totéž.

### 4. Proč to řešíte

Všechno z kroku 1 pohromadě, krátce a bez marketingu: problém, cíl, čím ho změříte a co se přitom nesmí zhoršit. HMW otázky vlož tak, jak vznikly, hlavní i dílčí, beze změn. Klidně napiš i to, čeho se u toho bojíte.

Čísla sem patří i tehdy, když jsou nepěkná. Bez metriky a bez toho, kde jste dnes, nemá designér podle čeho vážit, co je důležité.

### 5. Co má prototyp ověřit a co by koncept zabilo

Jednou větou, co se z prototypu chcete dozvědět. A druhou, co by vás přesvědčilo, že koncept nefunguje. Obojí se píše teď — po ukázání už si to každý přizpůsobí tomu, co viděl.

K tomu komu a kdy prototyp ukážete: jména a termín, ne „plánujeme testování".

### 6. Obrazovky: co kam, proč a čím se plní

U každé obrazovky tři věci: co na ní je, proč právě tam, a čím se to plní — ručně, pravidlem, nebo automaticky.

To „proč" je nejdůležitější. Bez něj designér obrazovku vyzdobí, místo aby ji navrhl. A způsob plnění rozhoduje o rozvržení: když vazby zakládá partner ručně, počet položek kolísá a bývá jich málo, takže pevná mřížka nesedí.

Když se přidává do něčeho, co existuje, nenech ho kreslit od nuly a nevypisuj mu, co na stránce dnes je. Řekni mu, ať si načte screenshoty současného stavu a upravuje je — screenshoty dodá produkťák. A připoj, ať se ptá, když mu není jasné, proč tam prvek je, čím se plní nebo co se stane po kliknutí. Ze screenshotu se logika nepozná a právě v ní bývají chyby, které nemá zopakovat.

### 7. Tvrdá omezení

Číslovaný seznam. U každého nestačí fakt, napiš i důsledek pro návrh: „Většina košíků má jeden produkt a poštovné se platí za každého partnera zvlášť, takže nekresli mechaniku přidej všechno do košíku napříč partnery."

A u každého řekni, jestli je nepřekročitelné, nebo je to k diskusi. Designér ten rozdíl mezi „takhle to máme" a „takhle to musí zůstat" sám nepozná.

### 8. Ověřená doporučení s čísly a zdroji

To, co vyšlo z kroku 3. S čísly a se zdrojem — pak se dá výsledek posoudit, aniž by to byla otázka vkusu.

### 9. Stavy, na které se zapomíná

U každé obrazovky: prázdno, jedna položka, hodně položek, a navázaná věc, která skončila nebo je nedostupná. Když vazby zadává někdo ručně, je „jedna položka" nejčastější stav a poloprázdná obrazovka vypadá nedodělaně.

### 10. Co je na prototypu nafejkované

Prototyp z Claude Design vypadá hotově a na poradě se z něj snadno stane rozhodnutí. Napiš, co bude vymyšlené (data, čísla, obsah) a co nikam nevede (mrtvá tlačítka). A dopiš, co to znamená pro ukazování, ať nikdo nehlásí slepé uličky jako chyby.

### 11. Co nedělat

Konkrétně. Rozliš „tohle u nás existuje a je to špatně, nekopíruj to" od „tohle existuje a je to v pořádku". Vzory zavržené v kroku 3 sem patří **jmenovitě a s důvodem**, ne jako obecné „nedělej FOMO" — jinak je designér za tři týdny navrhne znovu a nikdo si nevzpomene, proč vypadly.

### 12. Co chceš dostat zpátky

Seznam: obrazovky, zařízení, stavy, celý kontext obrazovky. A čtyři věci, které se vyplatí chtít vždycky:

- **Kolik směrů, napsané číslem.** Ne „udělej varianty", ale „dva směry, které řeší HMW #2 každý jinak". Ať se liší v tom, jak řeší problém, ne v barvě tlačítka.
- **U víc směrů větu, ať je nejdřív nakreslí hrubě** a nechá vybrat, než začne cokoli dotahovat. Jinak dostaneš jeden hotový a dva odbyté.
- **Názor, co ubrat**, když je rozsah vědomě velký.
- **Otázky, které má vyhodit nahoru, ne rozhodnout sám** — věci produktové a obchodní, ne designové. A seznam míst, kde mu chyběla komponenta nebo kde musel rozhodnout za vás.

## Než to pošleš

Hotový brief neodesílej, nabídni ho: *„Napsal jsem brief — projdi ho a řekni, co doplnit nebo změnit."* Když produkťák řekne „tohle jsem neřekl", přepiš to jeho slovy a nehádej se o tom, co bylo řečeno. Je to rozdíl mezi briefem, za kterým člověk stojí, a briefem, který mu někdo vnutil.

Než ho vypíšeš, projdi si:

- Přečteno očima někoho, kdo o tématu slyší poprvé, a nikde nechybí kontext
- Jsou tam skutečné příklady nabídek, ne obecné popisy
- Je napsané, co má prototyp ověřit, co by koncept zabilo, a komu se ukáže
- U každé obrazovky je „proč tam" a „čím se plní"
- U omezení je i důsledek pro návrh a to, jestli je nepřekročitelné
- Jsou vyjmenované stavy včetně prázdna a jedné položky
- Je napsané, co bude na prototypu nafejkované
- Zavržené vzory z kroku 3 jsou jmenovitě a s důvodem
- Je napsané, kolik směrů chceš a v čem se mají lišit
- Nikde není rozvržení a nikde není odhad místo chybějící informace

## Co následuje

Až prototyp přijde, projeď ho skillem slevomat-design-principles proti sedmi principům. Pak krok 5, provozní dopad a zadávání v adminu, a krok 6 zadání pro vývoj (psani-zadani, kontrola-zadani).
