# Evals

## Proč existují

`validate.py` ověří, že soubory drží formu. Nepozná, jestli se skill chová jako kolega — a to je na něm to jediné, co rozhoduje. Skill je prompt: rozbije se potichu, rozbije se po částech, a rozbije se způsobem, který v diffu není vidět. Jediná cesta, jak to zjistit, je pustit ho a přečíst, co z toho vylezlo.

Každý scénář tady je proto **způsob, jakým to už jednou selhalo**, nebo červená vlajka, kterou si skill sám o sobě píše. Rámování, které dostalo hotové řešení a zrámovalo ho. Zadání, které vyloučilo přesně to, co celý požadavek spustilo. Napsané dolů přestávají být historkou a stávají se něčím, co jde po každé změně spustit znovu.

Pět scénářů, jeden na skill:

| Soubor | Co zkouší |
|---|---|
| `product-definice-problemu-a-hmw.json` | „chybí nám filtr" jako hotové řešení, chybějící číslo, nedoložené „obchod to říká" |
| `product-mapovani-stavu.json` | přímá žádost o návrh řešení, bez přístupu do kódu i adminu |
| `product-konkurence-inspirace.json` | tři e-shopy ze stejného oboru, žádné mezery z mapování, žádný prohlížeč, pozvání „odhadni podle toho, co víš" |
| `design-prototypovani.json` | zadání, které si předepisuje modál se třemi dlaždicemi a neplánuje ověření kromě porady |
| `slevomat-design-principles.json` | blikající odpočet a počet dívajících se lidí — koncept, který projde každou mechanickou kontrolou a je to dark pattern |

## Jak je pustit

```
Workflow({ scriptPath: "skills/evals/run.js", args: { ids: ["hub-ramovani-schovane-reseni"] } })
```

`run.js` je role-play a jeho tvar je celý vtip. Čtyři agenti:

0. **Loader** jednou přečte scénáře a nahlásí jen cesty — kde který skill leží. Skript sám na disk nedosáhne a žádná assertion se přes něj nedostane dál.
1. **Kolega** drží scénář. První tah je `query` doslova, dál odpovídá v roli podle `follow_ups` — krátce, neochotně, ve spěchu.
2. **Skill** čte jen svůj vlastní text a konverzaci. Otevřít cokoli v `skills/evals/` má zakázané.
3. **Grader** přečte scénář a hotový transkript a u každého tvrzení, které označí za splněné, musí citovat řádek.

Ta separace je to, čím běh něco znamená. Dej jednomu modelu scénář i konverzaci naráz a vidí odpovědi dřív, než se zeptá — takže každé „zeptá se na X?" projde zdarma. A protože skill čte text z disku, testuje se to, co je v repu, ne co je právě nahrané v Hubu.

Tyhle skilly běží v claude.ai **samostatně** — žádný router, žádní sousedi, nic injektovaného před první zprávou. Runner jim to tak i podává; cokoli jiného by testovalo situaci, která nenastane.

Hodnocení je záměrně nepřátelské: scénář padá, když se stalo cokoli z `must_not`, nebo když jakékoli `must` nejde doložit citací. Žádné částečné body — každá položka na těch seznamech se už jednou pokazila.

**Dej tomu dost kol, ať se dojde k výstupu.** První skutečný běh měl strop čtyři a tři tvrzení padla konstrukcí: skill se ještě správně ptal a nebylo co hodnotit. Verdikt z ukráceného běhu není chybný, je nedokončený — přečti transkript, než mu uvěříš. Default je dvanáct.

Odpovídat ochotně netestuje nic. Spolupracující uživatel dostane dobrý výsledek skoro z každého promptu.

## Když scénář spadne

Oprav skill, ne eval. Když se ukáže, že `must` chtělo špatnou věc, změň ho ve stejném commitu jako skill a napiš do changelogu proč.

Pak přečti `qualitative` — tam žijí ty skutečné chyby. Jestli něco čte jako kolega, nebo jako formulář, se nedá tvrdit, jen posoudit. A `worst_finding` ve verdiktu je tam pro selhání, na které ještě nikdo nenapsal assertion: z jednoho běhu z toho vypadlo *„výslech s dobrým sluchem"*, což by mi žádná strukturální kontrola neřekla.

## Jazyk

Repliky česky, protože to člověk fakt napíše. Assertions anglicky, protože je čte model.

## Kde nejsou

Scénáře leží **vedle** skillů, ne v jejich složkách. Skill má v instrukcích, že si přečte soubory u sebe — kdyby tam ležely i assertions, čte si odpovědi. Proto má runner navíc zakázáno otevřít cokoli tady.

## Zdroj

Struktura vychází z konvence evalů v `anthropics/skills` (`skill-creator`): prompty s očekávaným chováním, tvrzení ověřitelná objektivně a pojmenovaná tak, aby čtenář poznal, co která kontroluje. Rozdělení na tvrzení a kvalitativní poznámku je odtamtud taky — *„subjective skills (writing style, design quality) are better evaluated qualitatively — don't force assertions onto things that need human judgment."*
