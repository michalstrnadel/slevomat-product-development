# Slevomat Product Development

Pět skillů pro produktovou práci ve Slevomatu. Provedou člověka od prvního nápadu až po zadání pro design.

Vlastníci: Romana Trušinová (kroky 1–3), Michal Strnadel (prototypování, principy).

## K čemu to je

Postavit prototyp je dneska rychlé. Těžší je vědět, co stavět.

Obvykle to jde takhle: někdo řekne „chceme filtr podle značky", za dva dny je hotový prototyp a na poradě se z něj stane rozhodnutí. Přitom to byl jen nápad ze schůzky, za kterým nikdo nestál.

Tyhle skilly do toho vkládají jeden krok navíc. Nejdřív se pojmenuje problém, pak se zjistí, jak to funguje dnes, a teprve potom se kreslí.

## Pět skillů

| Skill | Kdy ho použít | Co vrátí |
|---|---|---|
| `product-definice-problemu-a-hmw` | máš téma, ale ještě nevíš, co je na něm ten problém | problém, cíl a HMW otázky na jednu stránku |
| `product-mapovani-stavu` | potřebuješ vědět, jak to funguje dnes | popis ze všech stran, otázky na kolegy, chybějící místa |
| `product-konkurence-inspirace` | máš zmapováno a chybí ti inspirace | jak to samé řeší jinde, seřazené podle HMW otázek |
| `product-zadani-pro-design` | koncept je hotový a jde se designovat | zadání pro Claude Design, jeden blok ke zkopírování |
| `slevomat-design-principles` | máš co posoudit — nápad, obrazovku, prototyp | verdikt: Drží / Riziko / Porušuje / Nejde posoudit |

Kroky 5 a 6, tedy provozní dopad a zadání pro vývoj, už v Hubu jsou jako `psani-zadani` a `kontrola-zadani`.

## Na čem to stojí

**Spouštěč není totéž co potřeba.** „Přegenerujeme všechny obrázky" je jednorázová dávka. „Občas potřebuju nový obrázek" je nástroj. Když se to liší, musí být v zadání obojí a člověk rozhodne, čemu má stavba sloužit.

**Povinný řádek „Co nevíme".** Každý nález má tři řádky: co vidím, kde to vidím, co nevíme. Bez toho třetího vypadá nález hotově a za týden ho někdo cituje jako fakt.

**„Existuje, ale nepoužívá se."** Když se ukáže, že půlka řešení už v systému leží, je to nejlepší možný výsledek mapování. Proto to má svoje místo hned pod shrnutím.

**U každého tvrzení je vidět, odkud je.** Data / tickety podpory / rozhovory / desk research / domněnka. Domněnka je v pořádku, jen se nesmí vydávat za zjištění.

## Jak jsou skilly psané

Česky a lidsky, jako bys to vysvětloval kolegovi u kávy. Tykání, krátké věty, slovník firmy — nabídka, výpis, košík, partner, ne „PDP" a „landing". Bez emoji.

U každého pravidla stojí důvod hned pod ním. Pravidlo bez důvodu ti odargumentuje první člověk, který to zkusí.

## Kontrola

```
python3 validate.py
```

Osm kontrol formy: frontmatter, pojmenování, hranice „kdy NEpoužívat", odkazy mezi skilly, limity Hubu, slovník a emoji, jednotné názvy zdrojů a struktura evalů. Pouští se na každý push.

Jestli se skill chová jako kolega, tohle nepozná. Na to jsou evaly v [`skills/evals/`](skills/evals/README.md) — pět nahraných rozhovorů, které se dají kdykoli přehrát.

## Co kde leží

```
skills/product/    kroky 1–4
skills/design/     principy (včetně textu sedmi principů)
skills/evals/      testovací scénáře, jeden na skill
```

## Interní nástroj

Neobsahuje přihlašovací údaje ani citlivá data a nesmí je obsahovat ani po jakékoli úpravě.
