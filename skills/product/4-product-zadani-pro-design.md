---
name: product-zadani-pro-design
description: "Čtvrtý krok produktové práce ve Slevomat Group — handoff z produktu do designu. Napíše zadání pro Claude Design (nebo pro designéra) na prototyp konceptu, který už má někdo rozmyšlený — produkťák, designér nebo výzkumník. Výstupem je samonosný brief: problém, cíl a HMW, kontext systému, skutečné příklady, tvrdá omezení, stavy, co má prototyp ověřit a co by koncept zabilo. Použij vždy, když chce někdo nechat nakreslit nebo naprototypovat produktový koncept. Triggeruj na fráze jako: zadání pro design, prompt pro claude design, brief pro designéra, chci to nadesignovat, chci prototyp, nech to nakreslit, připrav zadání designérovi, jdeme prototypovat, zadání na prototyp, hoď to do claude design. Navazuje na skilly product-definice-problemu-a-hmw, product-mapovani-stavu a product-konkurence-inspirace. NEPOUŽÍVEJ, když člověk nemá za sebou rámování a mapování — tam patří nejdřív product-definice-problemu-a-hmw; a NEPOUŽÍVEJ na hotový rozhodnutý tvar, kde jde jen o sepsání — tam je psani-zadani."
---
<!-- owner: Michal Strnadel -->
<!-- version: 0.6.0 -->
<!-- renamed from: design-prototypovani -->
<!-- updated: 2026-08-19 -->

# Zadání pro design

Čtvrtý krok. Cíl je předat designu problém, omezení a kritérium úspěchu — ne tvar.

Vstup: zrámování z kroku 1 (problém, cíl, HMW), mapování z kroku 2 (tvrdá omezení, datový model, co dnes existuje) a vzory z kroku 3 (co se kde osvědčilo a co jsme zavrhli). Bez nich vznikne brief, který designéra pošle hádat — vrať se na kroky 1 až 3.

Tenhle skill zadání píše, nevymýšlí ho.

## Zadání není tvar

Dvě věci, které se pletou:

- **Zadání** říká, jaký je problém, co je pevné a podle čeho se pozná dobrý výsledek.
- **Tvar** říká, jak to má vypadat. Ten vzniká až v Claude Design nebo u designéra.

Když ti někdo rovnou diktuje tvar — „udělej modál se třemi dlaždicemi" — neber to jako hotovou věc, ale ani ho neposílej pryč. Zeptej se, odkud ten tvar je a co by ho zabilo. Většinou se ukáže, že rozhodnutý není a je to nápad ze schůzky. Pak píšeš normální brief a tvar do něj nedáváš. Když rozhodnutý opravdu je, na kreslení už designéra nepotřebuješ — jdi na psani-zadani.

Nakreslit to dnes umí kdokoli za deset minut. Vědět co, je ta drahá část. Celý brief je o tom druhém.

## Jak psát

- **Samonosně.** Designér nezná z vaší konverzace ani slovo. Žádné „jak jsme se bavili", žádné „ten problém, co řešíme", žádné interní zkratky bez vysvětlení. Přečti si to po sobě jako někdo, kdo o tématu slyší poprvé — kde chybí kontext tobě, chybí i jemu.
- **Česky a lidsky.** Tak, jak bys to vysvětlil kolegovi u kávy. Slovníkem firmy — nabídka, varianta, voucher, partner, výpis, košík, provize.
- **Krátké věty.** Tak dlouhý brief, kolik je kontextu. Délka není známka důkladnosti.
- **Nevymýšlej si.** Co nevíš, nedomýšlej. Když do „tohle nevíme" napíšeš svůj odhad, Claude Design ho přečte jako zadání — bude to nejkonkrétnější věta v celém briefu a bude se jí držet. Napiš tam jen, co chybí a co to pro návrh znamená.
- **Trvej na svém i za dvě zprávy.** Když řekneš „bez tohohle brief nenapíšu", tak ho pak bez toho nenapiš.

Brief napiš jako text přímo do odpovědi v chatu. Nevytvářej k tomu žádný soubor, dokument ani artefakt — je to jeden blok, který se celý zkopíruje do nové konverzace s Claude Design. Rozdělený na tři zprávy se z něj půlka ztratí. Kontrolní seznam na konci tohohle skillu je pro tebe, ne pro brief — nevypisuj ho.

A hotový brief neodesílej, nabídni ho: *„Napsal jsem brief — projdi ho a řekni, co doplnit nebo změnit."* Když produkťák řekne „tohle jsem neřekl", přepiš to jeho slovy a nehádej se o tom, co bylo řečeno. Je to rozdíl mezi briefem, za kterým člověk stojí, a briefem, který mu někdo vnutil.

## Na co se ptát

Pět věcí. Bez nich bude brief vágní.

**1. Pro koho to je.** Zákaznická část, admin, nebo Padmin? Tohle rozhoduje o všem ostatním a plete se to nejčastěji.

Zákazník přijde jednou, z mobilu, rozhoduje se rychle a nic se neučí. Partner je v Padminu opakovaně, jde mu o rychlost a přehled, snese hustotu dat a naučí se i věci, které nejsou na první pohled jasné. Interní admin je zase jiný případ — uživatel je kolega, chyba je drahá a rychlost zadávání je důležitější než dojem.

Když tohle v briefu nestojí, Claude Design nakreslí obecný e-shop na všechno.

**2. Co se designuje.** Nová feature, nebo celá flow? A designuje se celá obrazovka, nebo jen ta jedna feature v ní? Když se něco přidává do existující stránky, obvykle je správné vzít ji celou — hierarchii nejde rozhodnout po částech.

**3. Jak daleko.** Neptej se na wireframe. Komponenty Mini\*S jsou v Claude Design a hrubá verze se dělá taky z nich, jen míň dotažená. Wireframe by dneska byla práce navíc, ne úspora.

Ptej se na dvě jiné věci:

- **Šířka, nebo hloubka.** Rychlý návrh, který má rozhodnout směr a nejde do detailů? Nebo dotažená obrazovka se stavy, prázdnem a hraničními případy?
- **Jaká data.** Vymyšlený obsah, nebo skutečné nabídky a skutečná čísla? Skutečná data mění návrh víc než cokoli jiného. Když je produkťák má, chtěj je vždycky.

Že se staví v Mini\*S, je dané — jmenuj ho a vizuální pravidla nepopisuj, ta má v sobě. Ověř ale, co z Mini\*S na dané ploše reálně je. V zákaznické části obvykle všechno, v Padminu a v adminu je část ploch starší a komponenta nemusí existovat. Pak to do briefu napiš, ať designér nenavrhne z něčeho, co se nedá postavit.

**4. Zařízení.** Mobil, tablet, desktop, nebo kombinace. U zákaznické části je výchozí mobil, u Padminu a adminu desktop. Napiš to explicitně i tak — výjimky jsou právě tam, kde je to zajímavé.

**5. Kolik směrů.** Jeden dotažený návrh, nebo dva až tři odlišné vedle sebe? Volba je na produkťákovi, ty mu k ní dej doporučení.

Když se na HMW otázku dá odpovědět víc způsoby a z kroků 1 až 3 žádný nevyhrál, doporuč dva až tři směry, každý jen rychle a hrubě, ať je co porovnat. Když je koncept rozhodnutý a jde už jen o provedení, doporuč jeden a dotažený.

Nenech to nevyřčené. Claude Design nakreslí první rozumné řešení, které ho napadne, a od druhé zprávy dolaďuje už jenom to. Od té chvíle se bavíte o provedení, ne o směru.

A když to produkťák škrtá jako zdržení, řekni proč. Nakreslit tři směry stojí dneska skoro nic, vybrat z nich stojí pořád stejně — a to druhé je ta práce, kterou nechcete přeskočit. Čím víc času do jednoho návrhu nasypete, tím hůř se opouští. Pak už se netestuje, jestli je dobrý, ale hledá se důvod, proč ho nechat.

## Odkud brát podklady

- HMW, cíl a metriku z kroku 1
- Tvrdá omezení, datový model a co dnes existuje z kroku 2
- Vzory a zavržené vzory z kroku 3

**Příčky důkazů.** U každého tvrzení napiš, na které příčce stojí (od nejsilnější): behaviorální data / tickety zákaznické péče a partnerské podpory / rozhovory / desk research / domněnka. Domněnka je platná příčka, jen ji nevydávej za zjištění. Označení se nese z kroků 1 až 3, ať Claude Design ví, čemu může věřit. Celý krok 3 stojí na příčce desk research — zapiš to tak, ať se cizí vzor necituje jako ověřený fakt.

**Řekni produkťákovi, co od něj potřebuješ, hned na začátku.** Napiš mu seznam: skutečné příklady nabídek se jmény a cenami, screenshoty ploch, kterých se to týká, tvrdá omezení a datový model z mapování. Tohle musí dohledat a málokdy to má po ruce.

Když to nedodá, brief napsat můžeš — jen ať nahoře stojí, co v něm chybí a že se takhle nemá posílat dál. Když ale chybí skoro všechno, žádný brief z toho není. Řekni mu to a počkej, až podklady sežene.

**Tři věty si vytáhni z produkťáka rovnou.** Nikde je nehledá, ví je hned:

- **Co je problém a proč to řešíte.** Jedna věta. Když nemá zrámování z kroku 1, tohle je minimum, bez kterého Claude Design kreslí do prázdna.
- **Co jdete prototypem testovat.** Co konkrétně se z něj chcete dozvědět.
- **Co by koncept zabilo.** Výsledek, po kterém nepokračujete.

Bez těch tří vět brief nepiš. Prototyp, u kterého nikdo předem neřekl, kdy je špatně, dopadne dobře vždycky. To není testování, to je sbírání potvrzení pro něco, do čeho jste už zamilovaní.

Když je produkťák říct nechce, nabídni mu dvě jiné cesty: buď je tvar rozhodnutý a stačí psani-zadani, nebo se prototyp na tenhle termín dělat nemá. Řekni to jednou a rozhodnutí nech na něm.

## Co v briefu stojí

Čtyři bloky v tomhle pořadí: proč to děláte, co se designuje, mantinely, co chcete zpátky.

### Blok A · Proč to děláte

**1. Problém, cíl a metrika.** Všechno z kroku 1 pohromadě, krátce a bez marketingu: problém, cíl, čím ho změříte a co se přitom nesmí zhoršit. HMW otázky vlož tak, jak vznikly, hlavní i dílčí, beze změn. Klidně napiš i to, čeho se u toho bojíte.

Čísla sem patří i tehdy, když jsou nepěkná. Bez metriky a bez toho, kde jste dnes, nemá designér podle čeho vážit, co je důležité.

**2. Co má prototyp ověřit a co by koncept zabilo.** Jednou větou, co se z prototypu chcete dozvědět. A druhou, co by vás přesvědčilo, že koncept nefunguje. Obojí se píše teď — po ukázání už si to každý přizpůsobí tomu, co viděl.

Napiš, co má člověk v testování udělat, ne co má říct. „Zjistíme, jestli partner v prototypu sám najde a založí variantu" je zadání. „Zjistíme, jestli se partnerům líbí nový výpis" není — na to ti odpoví každý mile a nedozvíš se nic.

K tomu komu a kdy se prototyp ukáže: jména a termín, ne „plánujeme testování". U Padminu připiš, kdo partnery sežene a přes koho to jde. Samo se to nestane a bývá to delší než samotný design.

**3. Kdo rozhoduje.** Jedno jméno. Člověk, který po testování řekne, jestli se pokračuje, mění směr, nebo končí. Tady výjimečně jméno, ne role — rozhodnutí dělá člověk. Bez toho se o výsledku hlasuje na schůzce a vyhraje ten, kdo mluví poslední.

### Blok B · Co se designuje

**4. Rozsah.** Jeden odstavec: pro koho to je (zákaznická část, admin, Padmin), jaká feature, kolik obrazovek, jak velký rozsah.

Když je toho na jednu obrazovku hodně, napiš rovnou, co s tím — jestli chceš vidět všechno a škrtat až potom, nebo jestli má designér sám vybrat, co je důležitější. Když mu to nenapíšeš, rozhodne to za tebe a nedozvíš se o tom.

**5. Jak je systém postavený.** Tohle se vynechává nejčastěji a stojí to nejvíc. Designér, který nechápe, jak je produkt postavený, nakreslí obecný e-shop.

Vysvětli v pár odrážkách, co se u nás liší od běžné intuice: co je vlastně nabídka, co varianta, co vidí zákazník ve výpisu, kdo je partner, co vzniká ručně v Padminu a co se děje automaticky, jak dlouho věci žijí a co se s nimi stane, když doběhnou.

**6. Skutečné příklady.** Tři až pět reálných nabídek se jmény, počty variant a cenami. Designér pak kreslí na skutečném obsahu, ne na lorem ipsum — a hned je vidět, že „výběr varianty" pro tři velikosti a pro 62 druhů koření není totéž.

Vyber je tak, aby pokryly krajnosti: nejkratší a nejdelší název, nejmíň a nejvíc variant, nejlevnější a nejdražší.

**7. Obrazovky: co kam, proč a čím se plní.** U každé obrazovky tři věci: co na ní je, proč právě tam, a čím se to plní — ručně, pravidlem, nebo automaticky.

To „proč" je nejdůležitější. Bez něj ti designér obrazovku zaplní. Nenavrhne ji.

Způsob plnění rozhoduje o rozvržení. Když vazby zakládá partner ručně, počet položek kolísá a bývá jich málo — pevná mřížka pak nesedí.

Když se přidává do něčeho, co existuje, nenech ho kreslit od nuly a nevypisuj mu, co na stránce dnes je. Řekni mu, ať si načte screenshoty současného stavu a upravuje je; screenshoty dodá produkťák. A připoj, ať se ptá, když mu není jasné, proč tam prvek je, čím se plní nebo co se stane po kliknutí. Ze screenshotu se logika nepozná a právě v ní bývají chyby, které nemá zopakovat.

### Blok C · Mantinely

**8. Tvrdá omezení.** Číslovaný seznam. U každého napiš fakt i to, co z něj plyne pro návrh — samotný fakt designér přečte a jede dál.

Špatně: „Poštovné se platí za každého partnera zvlášť."
Dobře: „Poštovné se platí za každého partnera zvlášť a většina košíků má stejně jen jeden produkt. Nekresli mechaniku přidej všechno do košíku napříč partnery."

A u každého jedno slovo: **dané**, nebo **k diskusi**. Rozdíl mezi „takhle to máme" a „takhle to musí zůstat" designér sám nepozná. Když ho nenapíšeš, stane se jedna ze dvou věcí — buď obchází i to, co obcházet nemusí, nebo navrhne něco, co se nedá postavit.

**9. Vzory z kroku 3.** To, co vyšlo z konkurence a inspirace. Vždycky s číslem a se zdrojem a vždycky s tím, co na nás nesedí — to už je z kroku 3 napsané, jen se to nese dál.

Bez čísla je to názor. A o názorech se rozhoduje na schůzce podle toho, kdo je nejhlasitější.

**10. Stavy, na které se zapomíná.** Designér nakreslí ideální stav. Ten v produkci skoro nikdy nenastane.

U každé obrazovky vyjmenuj: prázdno, jedna položka, hodně položek, a navázaná věc, která skončila nebo je nedostupná. Když vazby zadává někdo ručně, je „jedna položka" nejčastější stav a poloprázdná obrazovka vypadá nedodělaně.

K tomu obsahové stavy, které u nás padají pravidelně: dlouhý název nabídky, chybějící fotka, vyprodaná varianta, nabídka po expiraci, cena s dopravou navíc.

**11. Co nedělat.** Konkrétně, ne obecně. Rozliš dvě věci, které vypadají stejně: „tohle u nás existuje a je to špatně, nekopíruj to" a „tohle existuje a je to v pořádku". Z produktu to designér nepozná, protože obojí je nasazené.

Vzory zavržené v kroku 3 sem patří jmenovitě a s důvodem. Ne „nedělej FOMO", ale „odpočet do konce nabídky jsme zavrhli, protože u opakovaných nákupů zvyšoval storna". Bez důvodu je designér za tři týdny navrhne znovu a nikdo si nevzpomene, proč vypadly.

### Blok D · Co chcete zpátky

**12. Co je na prototypu nafejkované.** Prototyp z Claude Design vypadá hotově. Ze schůzky se pak snadno odchází s rozhodnutím, které nikdo nechtěl udělat.

Napiš, co bude vymyšlené (data, čísla, obsah) a co nikam nevede (mrtvá tlačítka). A dopiš dvě věci: ať to Claude Design označí i uvnitř prototypu, ne jen v odpovědi, a co to znamená pro ukazování. Jinak lidi hlásí slepé uličky jako chyby a řeší se ony místo konceptu.

**13. Co chcete dostat zpátky.** Seznam: obrazovky, zařízení, stavy, celý kontext obrazovky. A pět věcí, které se vyplatí chtít vždycky:

- **Kolik směrů, napsané číslem.** Ne „udělej varianty", ale „dva směry, které řeší HMW #2 každý jinak". Ať se liší v tom, jak řeší problém, ne v barvě tlačítka.
- **U víc směrů větu, ať je nejdřív nakreslí hrubě** a nechá vybrat, než začne cokoli dotahovat. Jinak dostaneš jeden hotový a dva odbyté.
- **Názor, co ubrat**, když je rozsah vědomě velký.
- **Otázky, které má vyhodit nahoru, ne rozhodnout sám.** Věci produktové a obchodní, ne designové.
- **Seznam míst, kde mu chyběla komponenta** nebo kde si musel něco vymyslet mimo Mini\*S. Není to zadání na novou komponentu. Je to hypotéza, která se ověří na dalších dvou třech použitích, a teprve pak se řeší systém.

## Co do briefu nepatří

Rozvržení a tvar. Kde co na obrazovce leží, je odpověď, ne zadání.

Odhady náročnosti a provozní dopad. To je krok 5.

Technické zadání. To je krok 6, skill psani-zadani.

Tvůj vlastní odhad na místě chybějící informace. Ten se čte jako fakt a nikdo už se nedozví, že jsi ho vymyslel.

## Než jdeš dál

- Hned na začátku je, jestli jde o zákaznickou část, admin, nebo Padmin
- Přečteno očima někoho, kdo o tématu slyší poprvé, a nikde nechybí kontext
- Jsou tam skutečné příklady nabídek včetně krajností, ne obecné popisy
- Je napsané, co má prototyp ověřit, co by koncept zabilo, komu se ukáže a kdo rozhoduje
- U testování je napsané, co má člověk udělat, ne co má říct
- U každé obrazovky je „proč tam" a „čím se plní"
- U omezení je i důsledek pro návrh a slovo dané / k diskusi
- U každého tvrzení je příčka důkazů
- Jsou vyjmenované stavy včetně prázdna a jedné položky
- Je napsané, co bude nafejkované a že to má být označené i uvnitř prototypu
- Zavržené vzory z kroku 3 jsou jmenovitě a s důvodem
- Je napsané, kolik směrů chceš a v čem se mají lišit
- Nikde není rozvržení a nikde není odhad místo chybějící informace

## Co následuje

Hotový prototyp se projede skillem design-check proti sedmi principům — ten posuzuje, nenavrhuje. Pak provozní dopad a zadávání v adminu, a nakonec zadání pro vývoj (skills psani-zadani a kontrola-zadani).
