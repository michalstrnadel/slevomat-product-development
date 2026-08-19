---
name: product-zadani-pro-design
description: "Čtvrtý krok produktové práce ve Slevomatu — handoff z produktu do designu. Napíše zadání pro Claude Design nebo pro designéra na koncept, který už má někdo rozmyšlený: produkťák, designér nebo výzkumník. Výstupem je jeden blok textu, který se dá poslat samostatně — problém, cíl a HMW, jak je systém postavený, skutečné příklady nabídek, tvrdá omezení, stavy, co má prototyp ověřit a co by koncept zabilo. Použij, když chce někdo nechat nakreslit nebo naprototypovat produktový koncept. Triggeruj na fráze: zadání pro design, prompt pro claude design, brief pro designéra, chci to nadesignovat, chci prototyp, nech to nakreslit, připrav zadání designérovi, jdeme prototypovat, chci si to nakreslit, zadání na prototyp, hoď to do claude design. Navazuje na skilly product-definice-problemu-a-hmw, product-mapovani-stavu a product-konkurence-inspirace. NEPOUŽÍVEJ bez rámování a mapování — tam patří nejdřív product-definice-problemu-a-hmw. A NEPOUŽÍVEJ, když je řešení rozhodnuté a jde jen o sepsání — tam je psani-zadani."
---
<!-- owner: Michal Strnadel -->
<!-- version: 1.0.0 -->
<!-- renamed from: design-prototypovani -->
<!-- updated: 2026-08-19 -->

# Zadání pro design

Čtvrtý krok. Cíl je předat designu problém, mantinely a to, podle čeho se pozná dobrý výsledek. Ne hotové řešení.

Vstup: zrámování z kroku 1 (problém, cíl, HMW), mapování z kroku 2 (co dnes existuje, datový model, tvrdá omezení) a vzory z kroku 3 (jak to řeší jinde a co jsme zavrhli). Když některý chybí, brief napsat jde, ale designér bude hádat přesně to, co jste přeskočili. Radši se vrať.

Tenhle skill zadání sepisuje. Nevymýšlí ho.

## Kam ten brief jde

Do nové konverzace v Claude Design. Ten už má Mini\*S — komponenty, tokeny, typografii, barvy i stavy. Nedostává obecné zadání na kreslení, ale zadání na stavbu z toho, co má.

Z toho plynou tři věci pro brief:

- **Vizuální pravidla nepopisuj.** Barvy, spacing, velikosti, kontrast a fokus jsou v systému. Když je do briefu napíšeš, přebiješ systém a vznikne odchylka, kterou pak někdo řeší v design reviewu.
- **Řekni, ať staví z existujících komponent** a použije k tomu skilly, které v Claude Design k Mini\*S jsou. Nová komponenta se nekreslí, dokud není jasné, že se ty stávající použít nedají.
- **Vlož odkaz na systém:** https://github.com/slevomat/minis-design-system

Ověř ale, co z Mini\*S na té konkrétní ploše reálně je. V zákaznické části obvykle všechno, v Padminu a v adminu je část ploch starší a komponenta nemusí existovat. To do briefu napiš, ať designér nestaví z něčeho, co tam není.

## Zadání není řešení

Dvě věci, které se pletou:

- **Zadání** popisuje problém, mantinely a měřítko úspěchu. Píše ho produkt.
- **Řešení** říká, jak to má vypadat. Vzniká až v Claude Design nebo u designéra.

Nakreslit obrazovku dnes zvládne kdokoli za deset minut. Těžké je vědět, co se má nakreslit. O tom je celý brief.

Když ti produkťák rovnou popíše, jak to má vypadat — „udělej modál se třemi dlaždicemi" — neodmítej to, ale ani to nezapisuj. Zeptej se na dvě věci: odkud to má a co by ho přesvědčilo, že je to špatně. Většinou se ukáže, že to nikdo nerozhodl a je to nápad ze schůzky. Pak píšeš normální brief a modál v něm není. Když je to opravdu rozhodnuté, na kreslení už designéra nepotřebuješ a jdeš na psani-zadani.

## Jak psát

- **Pro cizího člověka.** Designér nezná z vaší konverzace ani slovo. Žádné „jak jsme se bavili", žádné „ten problém, co řešíme", žádné zkratky bez vysvětlení. Přečti si to po sobě jako někdo, kdo o tom slyší poprvé.
- **Česky a lidsky.** Tak, jak bys to vysvětlil kolegovi u kávy. Slovníkem firmy: nabídka, varianta, voucher, čerpání, partner, výpis, košík, provize.
- **Krátké věty.** Brief je tak dlouhý, kolik je kontextu. Délka není známka důkladnosti.
- **Nevymýšlej si.** Když něco nevíš, napiš, že to nevíte, a co to pro návrh znamená. Nikdy tam nepiš svůj odhad — v briefu plném kontextu to bude ta nejkonkrétnější věta a Claude Design se jí bude držet nejvíc.
- **Trvej na svém i za dvě zprávy.** Když řekneš „bez tohohle brief nenapíšu", tak ho pak bez toho nenapiš.

Brief patří do odpovědi v chatu jako jeden souvislý blok. Nezakládej k němu soubor, dokument ani artefakt — celý se kopíruje do nové konverzace s Claude Design a rozsekaný na tři zprávy se z něj půlka ztratí. Kontrolní seznam na konci tohohle skillu je pro tebe, ne pro brief.

## 1 · Zjisti čtyři věci, které rozhodují o všem ostatním

**Pro koho a kde.** Zákaznická část, interní admin, nebo Padmin? A která vertikála — zboží, cestování, zážitky? Tohle se plete nejčastěji a přitom to určuje všechno další.

Zákazník přijde jednou, z mobilu, rozhoduje se za pár vteřin a nic se neučí. Partner sedí v Padminu opakovaně, chce rychlost a přehled, unese víc informací najednou a naučí se i to, co není na první pohled jasné. Interní admin je ještě jinde: uživatel je kolega, chyba stojí peníze a rychlost zadávání je důležitější než dojem.

Zařízení z toho většinou vyplyne — zákaznická část mobil, Padmin a admin desktop. Napiš ho stejně, protože zajímavé případy jsou právě ty výjimky.

**Co a jak velké.** Jedna feature, nebo celá flow? A kreslí se celá obrazovka, nebo jen ta jedna věc v ní? Když se něco přidává na existující stránku, ber ji obvykle celou. Kam co patří a co má být vidět první, se nedá rozhodnout po částech.

**Jak daleko.** Neptej se na wireframe. Komponenty Mini\*S jsou v Claude Design a i hrubá verze vzniká z nich, jen míň dotažená. Wireframe by dneska byla práce navíc.

Ptej se na dvě jiné věci. Jak dotažené: rychlý návrh, který má rozhodnout směr, nebo hotová obrazovka i se stavy a hraničními případy? A na jakých datech: vymyšlený obsah, nebo skutečné nabídky a skutečná čísla? Skutečná data mění návrh víc než všechno ostatní. Když je produkťák má, vždycky si je vyžádej.

**Kolik směrů.** Jeden dotažený návrh, nebo dva až tři odlišné vedle sebe? Rozhoduje produkťák, ty mu k tomu dej doporučení.

Když se na hlavní HMW dá odpovědět víc způsoby a z kroků 1 až 3 žádný nevyhrál, doporuč dva až tři směry, každý jen hrubě, ať je co porovnat. Když je koncept rozhodnutý a jde už jen o provedení, doporuč jeden a dotažený.

Hlavně to napiš. Když v briefu číslo nestojí, nakreslí Claude Design první rozumné řešení, které ho napadne, a od druhé zprávy už jenom dolaďuje. Od té chvíle se bavíte o provedení, ne o směru.

A když to produkťák škrtá jako zdržení, řekni proč. Nakreslit tři směry stojí dneska skoro nic, vybrat z nich stojí pořád stejně, a to druhé je ta práce, kterou nechcete přeskočit. Čím víc času do jednoho návrhu dáte, tím těžší je ho pak zahodit. Přestane se ověřovat, jestli je dobrý, a začne se hledat důvod, proč ho nechat.

## 2 · Vytáhni z produkťáka tři věty

Nemusí je nikde hledat, ví je hned:

- **Co je problém a proč to řešíte.** Jedna věta. Když nemá zrámování z kroku 1, tohle je minimum, bez kterého Claude Design kreslí do prázdna.
- **Co se chcete z prototypu dozvědět.** Konkrétně, ne „jestli to funguje".
- **Co by koncept zabilo.** Výsledek, po kterém nepokračujete.

Bez těch tří vět brief nepiš. Prototyp, u kterého nikdo předem neřekl, kdy je špatně, dopadne dobře pokaždé. To pak není ověřování, ale sbírání důkazů pro řešení, do kterého jste se mezitím zamilovali.

Když to produkťák říct nechce, nabídni mu dvě cesty: buď je řešení rozhodnuté a stačí psani-zadani, nebo se prototyp na tenhle termín dělat nemá. Řekni to jednou a rozhodnutí nech na něm.

## 3 · Posbírej podklady

Z kroků: HMW, cíl a metriku z jedničky. Co dnes existuje, datový model a tvrdá omezení z dvojky. Vzory a zavržené vzory z trojky.

Od produkťáka to, co v žádném dokumentu není. Řekni mu to hned na začátku jako seznam, protože to musí dohledat: skutečné nabídky se jmény, počty variant a cenami, screenshoty ploch, kterých se to týká, a jména lidí, kterým se prototyp ukáže.

Když něco nedodá, brief napsat můžeš. Nahoru pak napiš, co v něm chybí a že se takhle nemá posílat dál. Když chybí skoro všechno, žádný brief z toho není. Řekni to a počkej, až podklady sežene.

**Příčky důkazů.** U každého tvrzení napiš, na které příčce stojí (od nejsilnější): behaviorální data / tickety zákaznické péče a partnerské podpory / rozhovory / desk research / domněnka. Domněnka je platná příčka, jen ji nevydávej za zjištění. Označení se nese z kroků 1 až 3. Celý krok 3 stojí na desk research, takže i cizí vzor se do briefu zapisuje na téhle příčce, ne jako ověřený fakt.

## 4 · Napiš brief

Čtyři bloky v tomhle pořadí: proč to děláte, co se designuje, mantinely, co chcete zpátky.

### Blok A · Proč to děláte

**Problém, cíl a metrika.** Všechno z kroku 1 pohromadě, krátce a bez marketingu: problém, cíl, čím ho změříte a co se přitom nesmí zhoršit. HMW otázky vlož beze změn, jak vznikly. Klidně napiš i to, čeho se u toho bojíte.

Čísla sem patří, i když jsou nepěkná. Bez metriky a bez toho, kde jste dnes, nemá designér jak poznat, co je na obrazovce důležité.

**Co má prototyp ověřit a co by koncept zabilo.** Obojí jednou větou a obojí se píše teď. Po ukázání už si to každý přizpůsobí tomu, co viděl.

Piš, co má člověk v testování udělat, ne co má říct. „Zjistíme, jestli partner v prototypu sám najde a založí variantu" je zadání. „Zjistíme, jestli se partnerům líbí nový výpis" není — na to ti odpoví každý mile a nedozvíš se nic.

K tomu jména a termín, ne „plánujeme testování". U Padminu připiš, kdo partnery sežene a přes koho to jde. Samo se to nestane a trvá to dýl než samotný design.

**Kdo rozhoduje.** Jedno jméno. Člověk, který po testování řekne, jestli se pokračuje, mění směr, nebo končí. Tady výjimečně jméno, ne role. Bez toho se o výsledku hlasuje na schůzce a vyhraje ten, kdo mluví poslední.

### Blok B · Co se designuje

**Rozsah.** Jeden odstavec: pro koho to je, jaká vertikála, jaká feature, kolik obrazovek.

Když je toho na jednu obrazovku moc, rozhodni to hned. Buď chceš vidět všechno a škrtat až potom, nebo má designér sám vybrat, co je důležitější. Když to nenapíšeš, vybere za tebe a nedozvíš se o tom.

**Jak je systém postavený.** Tohle se vynechává nejčastěji a stojí to nejvíc. Designér, který nechápe, jak je produkt postavený, nakreslí obecný e-shop.

Vysvětli v pár odrážkách, co u nás funguje jinak, než by člověk čekal: co je nabídka a co varianta, co z toho vidí zákazník ve výpisu, kdo je partner a co zakládá ručně, co se děje automaticky, jak dlouho nabídka běží, dokdy platí voucher a co se stane, když se nevyčerpá.

**Z čeho se staví.** Do briefu napiš odstavec v tomhle smyslu, ať se to nemusí dohadovat:

> Staví se z Mini\*S — https://github.com/slevomat/minis-design-system. Komponenty, tokeny a stavy máš v Claude Design, použij je a použij k tomu i skilly, které tam k systému jsou. Nekresli vlastní barvy, spacing ani typografii. Když ti komponenta chybí, poskládej to z existujících a napiš mi, kde ti chyběla.

Když je na dané ploše systém jen částečně, dopiš to sem konkrétně: co z Mini\*S tam je a co je starší.

**Skutečné příklady.** Tři až pět reálných nabídek se jmény, počty variant a cenami. Designér pak kreslí na skutečném obsahu, ne na lorem ipsum, a hned je vidět, že výběr varianty pro tři velikosti a pro 62 druhů koření není totéž.

Vyber je tak, aby pokryly krajnosti: nejkratší a nejdelší název, nejmíň a nejvíc variant, nejlevnější a nejdražší.

**Obrazovky.** U každé tři věci: co na ní je, proč právě tam, a čím se to plní — ručně, pravidlem, nebo automaticky.

To „proč" je nejdůležitější. Bez něj ti designér obrazovku zaplní, ale nenavrhne ji. A způsob plnění rozhoduje o rozvržení: když vazby zakládá partner ručně, počty kolísají a bývají malé, takže pevná mřížka nesedí.

Když se přidává do něčeho, co existuje, nevypisuj mu, co na stránce dnes je. Řekni mu, ať si načte screenshoty současného stavu a upravuje je; screenshoty dodá produkťák. A připiš, ať se ptá, když mu není jasné, proč tam prvek je, čím se plní nebo co se stane po kliknutí. Ze screenshotu se logika nepozná a právě v ní bývají chyby, které nemá zopakovat.

### Blok C · Mantinely

**Tvrdá omezení.** Číslovaný seznam. U každého napiš fakt i to, co z něj plyne pro návrh — samotný fakt designér přečte a jede dál. A připoj jedno slovo: **dané**, nebo **k diskusi**. Rozdíl mezi „takhle to máme" a „takhle to musí zůstat" sám nepozná, a když mu to nenapíšeš, buď obchází i to, co obcházet nemusel, nebo navrhne něco, co se nedá postavit.

> **Špatně:** Poštovné se platí za každého partnera zvlášť.
>
> **Dobře:** Poštovné se platí za každého partnera zvlášť a většina košíků má stejně jen jeden produkt. Nekresli mechaniku přidej všechno do košíku napříč partnery. (dané)

Pět omezení, o která zakopne skoro každý koncept, tak je projdi vždycky: velikost košíku, doprava, rozdíl mezi dealem a produktem, obměna portfolia a cena práce v adminu.

**Vzory z kroku 3.** To, co vyšlo z konkurence a inspirace. Vždycky s číslem, se zdrojem a s tím, co na nás nesedí. Všechno tři už je z kroku 3 napsané, jen se to nese dál. Bez čísla je to názor a o názorech se na schůzce rozhoduje podle toho, kdo je nejhlasitější.

**Stavy.** Designér nakreslí ideální stav. Ten v provozu skoro nikdy nenastane.

U každé obrazovky vyjmenuj prázdno, jednu položku, hodně položek a navázanou věc, která skončila nebo je nedostupná. Když vazby zadává někdo ručně, je jedna položka nejčastější stav a poloprázdná obrazovka vypadá nedodělaně.

K tomu obsah, který u nás dělá problémy pořád: dlouhý název nabídky, chybějící fotka, vyprodaná varianta, nabídka po expiraci, cena bez dopravy.

**Co nedělat.** Konkrétně, ne obecně. Rozliš dvě věci, které vypadají stejně: „tohle u nás existuje a je to špatně, nekopíruj to" a „tohle existuje a je to v pořádku". Z produktu to designér nepozná, protože obojí je nasazené.

Vzory zavržené v kroku 3 sem patří jmenovitě a s důvodem. Ne „nedělej FOMO", ale „odpočet do konce nabídky jsme zavrhli, protože u opakovaných nákupů zvyšoval storna". Bez důvodu je designér za tři týdny navrhne znovu a nikdo si nevzpomene, proč vypadly.

### Blok D · Co chcete zpátky

**Co je nafejkované.** Prototyp z Claude Design vypadá hotově a na schůzce z něj snadno vznikne rozhodnutí, které nikdo udělat nechtěl. Napiš, co bude vymyšlené (data, čísla, obsah) a co nikam nevede (mrtvá tlačítka), a nech to označit i uvnitř prototypu, ne jen v odpovědi. Jinak lidi hlásí slepé uličky jako chyby a místo konceptu se pak řeší ony.

**Výstup.** Obrazovky, zařízení, stavy, celý kontext obrazovky. A pět věcí, které se vyplatí chtít pokaždé:

- **Počet směrů napsaný číslem.** Ne „udělej varianty", ale „dva směry, které řeší HMW #2 každý jinak". Ať se liší v tom, jak řeší problém, ne v barvě tlačítka.
- **U víc směrů větu, ať je nejdřív nakreslí hrubě** a nechá vybrat, než začne cokoli dotahovat. Jinak dostaneš jeden hotový a dva odbyté.
- **Názor, co ubrat**, když víš, že je toho hodně.
- **Otázky, které má poslat zpátky, ne rozhodnout sám.** Věci produktové a obchodní, ne designové.
- **Seznam míst, kde chyběla komponenta** nebo kde musel něco vymyslet mimo Mini\*S. Není to objednávka nové komponenty, je to hypotéza. Ověří se na dalších dvou třech použitích a teprve pak se řeší systém.

## 5 · Nabídni ho k projití

Hotový brief neposílej dál. Napiš: *„Napsal jsem brief — projdi ho a řekni, co doplnit nebo změnit."*

Když produkťák řekne „tohle jsem neřekl", přepiš to jeho slovy a nehádej se o tom, co bylo řečeno. Je to rozdíl mezi briefem, za kterým člověk stojí, a briefem, který mu někdo vnutil.

## Co do briefu nepatří

Rozvržení a vzhled. Kde co na obrazovce leží, je odpověď, ne zadání.

Odhady náročnosti a provozní dopad. To je krok 5.

Technické zadání. To je krok 6, skill psani-zadani.

Tvůj odhad na místě chybějící informace. Čte se jako fakt a nikdo se pak nedozví, že sis ho vymyslel.

## Než jdeš dál

- Na začátku je, jestli jde o zákaznickou část, admin, nebo Padmin, a o kterou vertikálu
- Přečteno očima někoho, kdo o tom slyší poprvé, a nikde nechybí kontext
- Jsou tam skutečné nabídky včetně krajností, ne obecné popisy
- Je napsané, co má prototyp ověřit, co by koncept zabilo, komu se ukáže a kdo rozhoduje
- U testování je napsané, co má člověk udělat, ne co má říct
- Je napsané, že se staví z Mini\*S, i s odkazem na repo
- U každé obrazovky je „proč tam" a „čím se plní"
- U každého omezení je důsledek pro návrh a slovo dané / k diskusi
- U každého tvrzení je příčka důkazů
- Jsou vyjmenované stavy včetně prázdna a jedné položky
- Je napsané, co bude nafejkované a že to má být označené i v prototypu
- Zavržené vzory z kroku 3 jsou jmenovitě a s důvodem
- Je napsaný počet směrů a v čem se mají lišit
- Nikde není rozvržení a nikde není odhad místo chybějící informace

## Co následuje

Hotový prototyp se projede skillem design-check proti sedmi principům — ten posuzuje, nenavrhuje. Pak provozní dopad a zadávání v adminu, a nakonec zadání pro vývoj (skills psani-zadani a kontrola-zadani).
