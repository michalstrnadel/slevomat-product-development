---
name: product-konkurence-inspirace
description: "Třetí krok produktové práce ve Slevomat Group — zjistit, jak stejné HMW otázky řeší jinde. Prochází reálné cizí weby, popisuje co na nich uživatel dnes vidí, odhaduje jak to nejspíš funguje, a odpovídá otázku po otázce. Výstupem je HTML stránka s obrázky z těch webů a s popisem, jak to kdo řeší. Použij vždy, když je zmapovaný současný stav a je potřeba inspirace nebo srovnání s trhem. Triggeruj na fráze jako: konkurenční analýza, jak to řeší konkurence, jak to dělají jinde, inspirace z trhu, benchmark, podívej se na konkurenci, projdi cizí weby, co dělá Alza a Notino, best practice, jak to řeší ostatní. Navazuje na skill product-mapovani-stavu. NEPOUŽÍVEJ na výběr řešení — krok sbírá, co existuje, a nerozhoduje, co uděláme; a NEPOUŽÍVEJ ho bez mezer z mapování, jinak z toho vyjde prohlídka cizích webů. Naplno běží v Claude Code nebo v Coworku (řídí agenty v prohlížeči) — v chatu claude.ai jede jen ze screenshotů a odkazů od produkťáka."
---
<!-- owner: Romana Trušinová -->
<!-- version: 0.1.0 -->
<!-- updated: 2026-08-14 -->

# Konkurence a inspirace

Třetí krok. Cíl je odpovědět otázku po otázce, jak stejné HMW řeší jinde — ne udělat prohlídku cizích webů.

Vstup: HMW otázky z rámování a sloupec „co chybí" z tabulky mezer z mapování. Bez mezer z kroku 2 nevíš, na co se u referentů ptát, a vrátí se turistika.

## Referent není konkurent

Dvě různé práce, které se pletou:

- **Konkurent** nám bere zákazníky. Zajímá nás, protože nás s ním zákazník srovnává.
- **Referenční řešení** vyřešilo stejný problém, i když je z jiného oboru. Zajímá nás jen ten vzor.

U jednoho tématu jsou to obvykle úplně jiné firmy. Piš u každého referenta, který z těch dvou to je.

## Jak psát

- Česky a lidsky, krátké věty, bez anglicismů, kde existuje české slovo.
- Nevymýšlej si. Co jsi neviděl, netvrď.
- Buď kritický. U každého vzoru napiš i to, co na nás nesedí.

## 1 · Sestav rubriku, než otevřeš první web

Z každé mezery z kroku 2 udělej jednu otázku, kterou se pak ptáš u všech referentů stejně. K tomu přidej řádky, které se hodí vždycky:

- Kde ta vazba na stránce žije a jak je pojmenovaná
- Kolik kliknutí je od produktu
- Kdo ji plní — ručně, automaticky, algoritmem
- Co se stane, když je navázaná věc nedostupná
- Jak to funguje na mobilu

Bez rubriky se každý referent popíše svými slovy a nic se nedá srovnat.

## 2 · Domluv s produkťákem referenty i konkrétní stránky

Neptej se jen „na koho se podívat". Vyžádej si přímé odkazy na konkrétní stránky, ideálně takové, kde je to chování vidět. Hledání té správné stránky na cizím webu spolyká víc času než všechno ostatní dohromady.

Navrhni sadu sám, u každého referenta napiš, kterou otázku z rubriky má zodpovědět, a nech produkťáka upravit. Dvě pravidla k výběru:

- Aspoň jeden referent z jiného oboru. Stejný obor konverguje ke stejnému lokálnímu optimu.
- Aspoň jeden strukturně podobný nám — marketplace s mnoha malými prodejci, ne katalogový e-shop.

Když produkťák sadu změní, řekni nahlas, jakou mezeru ta nová sada nechává. Nespolkni to.

Než začneš procházet, napiš seznam záběrů: co přesně chceš z každé stránky vyfotit. Rozsah, který se dá udělat v jednom sezení: 4–6 referentů, 2–3 stránky na každého, 10–15 obrázků celkem.

## 3 · Procházej weby úsporně

Nejdřív si ověř, kde běžíš. Agenty s taby v prohlížeči máš v Claude Code a v Coworku — v obyčejném chatu claude.ai nejsou. Když prohlížeč nemáš, řekni to hned a přejdi na záložní cestu: rubrika a seznam záběrů vzniknou stejně, ale obrázky a odkazy dodá produkťák — stejná předávka jako u nedostupného webu níž. Nezaseknout se, neobcházet.

Rozešli agenty — jednoho na referenta. Ne na stránku a nikdy dva referenty do jednoho agenta. Odhad „jak to nejspíš funguje" vzniká z porovnání víc stránek téhož webu; když každou stránku dělá jiný agent, rubrika se vyplní, ale mechanismu nikdo neporozumí. A slepit dva nesouvisející referenty do jednoho agenta z něj udělá kritickou cestu celého kroku, aniž by z toho něco získal. Když má referent hodně stránek, rozděl ho podle otázek z rubriky, ne podle stránek.

Strop je asi pět současných agentů v prohlížeči. Každý si udělá vlastní tab, ale všichni jedou přes jeden Chrome, takže se jejich akce nakonec řadí za sebe. Nad pět už zrychlení nepřijde, jen roste šance, že si při zakládání tabů vlezou do cesty. Každému agentovi řekni, ať si založí vlastní tab a pracuje jen v něm.

K tomu pusť jednoho agenta bez prohlížeče na výzkum a ověřená doporučení (Baymard, NN Group, obecné e-commerce patterny). Nekoliduje s ničím, běží zdarma vedle ostatních a jeho výstup patří pod jednotlivé HMW otázky, ne do vlastní sekce na konci. Bez něj bude analýza stát jen na tom, co dělá konkurence — a to není totéž jako co je ověřeně dobré.

Nikdy neotvírej stránku, aniž bys věděl, který řádek rubriky tím zavíráš.

- Slučuj kroky do jednoho volání — otevřít stránku, udělat screenshot a přečíst text stránky jde naráz. Nedělej to na tři volání.
- Pravidlo zastavení: jakmile je řádek rubriky u daného referenta zodpovězený, přestaň se dívat. Nedoplňuj matici pro krásu — napiš „nezjištěno" a jdi dál.
- Neopakuj se. Když dva referenti řeší věc stejně, napiš to jednou a u druhého odkaž.
- Když je web nedostupný (blokace, přihlášení, souhlasy), nezasekni se — řekni to produkťákovi a vyžádej si screenshoty. Stejná předávka jako u kódu v kroku 2.
- Souhlasy s cookies odklikávej co nejvíc odmítavě a nezakládej účty.

Zásadní: „nenašel jsem to ve zdrojovém HTML" neznamená „není to tam". Bloky se souvisejícím obsahem se často donačítají až po vykreslení stránky, takže ve zdroji nejsou. Absence ve statickém načtení není důkaz — musíš to vidět v prohlížeči.

## 4 · Odhadni, jak to funguje — ze stopy, ne z domýšlení

Zvenčí vidíš co, ne jak. Odhad je v pořádku, ale musí stát na pozorovatelném signálu a musí být označený.

Užitečné stopy:

| Co udělat | Co z toho plyne |
|---|---|
| Přepni variantu nebo velikost | Změní se blok? Pak je vazba na úrovni varianty, ne produktu. |
| Podívej se, kdo prodává položky v bloku | Stejný prodejce nebo značka → seskupení podle prodejce. |
| Otevři dva nesouvisející produkty | Stejný obsah bloku → není to vazba, ale obecné doporučení. |
| Spočítej položky, opakovaně | Pořád stejný počet → tvrdý limit, tedy dotaz, ne kurátorství. |
| Načti znovu a v anonymním okně | Mění se → personalizace nebo náhoda. Stálý obsah → uložená vazba nebo deterministický dotaz. |
| Zkus nedostupný nebo vyprodaný produkt | Chování prozradí, jestli je vazba pevná, nebo se dopočítává. |
| Přečti, jak je blok pojmenovaný | „Často kupováno spolu" ukazuje na data o nákupech, „Doplňky k produktu" na redakční vazbu. |
| Podívej se, jestli má blok cenu celku a jedno tlačítko | Pak je to balíček jako samostatný produkt, ne odkaz. |

U každého zjištění napiš „vidím", nebo „odhaduju". U odhadu ještě jednou větou, jak by se dal ověřit. Bez toho se z analýzy stane sbírka domněnek, které za týden někdo cituje jako fakt.

Celý tenhle krok stojí na příčce důkazů desk research — tak se taky zapíše do zadání v kroku 4, ať se cizí vzor necituje jako ověřený fakt. „Vidím", nebo „odhaduju" říká, jak pevně na té příčce zjištění stojí.

## 5 · Výstup

Členěný podle HMW otázek, ne podle referentů. To je celý smysl — čtenář se ptá „jak tuhle věc řeší jinde", ne „co dělá Notino".

Ke každé HMW:

- **Srovnávací tabulka na výšku** — řádek je otázka z rubriky, sloupec referent. Na výšku proto, že široká tabulka se nedá číst. „Nezjištěno" je platná buňka i tady — nedoplňuj ji dojmem.
- **Obrázky s popiskem** — u každého referenta výřez a pod ním, jak to tedy řeší. Ne celá obrazovka: výřez toho bloku. Obrázek bez popisku je dekorace.
- **Vzory, které z toho vypadly** — u každého co řeší, čím se plní, a co na nás nesedí a proč.
- **Jedna věta na závěr:** existuje na tuhle mezeru vzor, nebo ne. Když to nikdo neřeší, je to taky nález — buď to není skutečný problém, nebo je to opravdu těžké.

Každý vzor projeď proti známým omezením z předchozích kroků (velikost košíku, doprava, dealy versus produkty, obměna portfolia, cena práce v adminu). Vzor, který některé porušuje, označ — nepropašuj ho dál potichu.

Výstupem je HTML stránka s obrázky vloženými přímo v ní, protože markdown obrázky neunese. Do projektu ulož textový záznam a odkaž z něj na tu stránku.

## Co do výstupu nepatří

Rozhodnutí. Tady se hranice posouvá proti kroku 2: vzory jsou výstup, ale volba není. Sbíráme, co existuje, nevybíráme, co uděláme — žádné „udělejme to jako X". To je krok 4.

Odhady náročnosti. To je krok 5.

## Než jdeš dál

- Rubrika vznikla z mezer z kroku 2, ne z obecného seznamu
- U každého referenta je napsané, jestli je konkurent, nebo jen vzor
- Je řečeno, jakou mezeru výběr referentů nechává
- Každé zjištění je označené jako „vidím", nebo „odhaduju", a u odhadu je, jak ho ověřit
- U každého referenta je aspoň jeden výřez s popiskem
- Výstup je členěný podle HMW otázek
- U každého vzoru je napsané, co na nás nesedí
- Není tam vybrané řešení

## Co následuje

Zadání pro design — skill design-prototypovani. Hotový prototyp se pak projede skillem slevomat-design-principles proti sedmi principům. Pak provozní dopad a zadávání v adminu, a nakonec zadání pro vývoj (psani-zadani, kontrola-zadani).
