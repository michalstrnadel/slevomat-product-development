# Evaly

## Proč jsou tady

`validate.py` zkontroluje, jestli soubory drží formu. Nepozná ale, jestli se skill chová jako kolega — a to je na něm to podstatné.

Skill je prompt. Rozbije se potichu a v diffu to není vidět. Jediný způsob, jak to zjistit, je pustit ho a přečíst si, co z toho vyleze.

Každý scénář tady je něco, co už jednou selhalo. Rámování, které dostalo hotové řešení a jen ho přepsalo. Zadání, které vynechalo přesně to, kvůli čemu vzniklo. Když se to zapíše, přestane to být historka a stane se z toho test.

Pět scénářů, jeden na skill:

| Soubor | Co zkouší |
|---|---|
| `product-definice-problemu-a-hmw.json` | „chybí nám filtr" jako hotové řešení, chybějící číslo, nedoložené „obchod to říká" |
| `product-mapovani-stavu.json` | přímá žádost o návrh řešení, k tomu žádný přístup do kódu ani do adminu |
| `product-konkurence-inspirace.json` | tři e-shopy z jednoho oboru, žádné mezery z mapování, žádný prohlížeč |
| `product-zadani-pro-design.json` | zadání, které si předepisuje konkrétní obrazovku a nepočítá s žádným ověřením |
| `slevomat-design-principles.json` | blikající odpočet a „dívá se 12 lidí" — projde každou kontrolou a je to dark pattern |

## Jak je pustit

```
Workflow({ scriptPath: "skills/evals/run.js", args: { ids: ["hub-ramovani-schovane-reseni"] } })
```

Běh funguje jako scénka. Hrají v ní čtyři agenti:

1. **Loader** přečte scénáře a nahlásí jenom cesty k souborům.
2. **Kolega** drží scénář a odpovídá v roli — krátce a neochotně, jak to lidi opravdu dělají.
3. **Skill** vidí jen svůj vlastní text a konverzaci. Do složky `skills/evals/` nesmí.
4. **Grader** si přečte scénář i hotový rozhovor a u každého splněného bodu musí citovat řádek.

To oddělení je celý smysl. Kdyby skill viděl scénář, zná odpovědi dřív, než se stihne zeptat, a každé „zeptá se na X?" mu projde zadarmo.

Známkuje se přísně. Scénář padá, když se stane cokoli ze seznamu `must_not`, nebo když se něco z `must` nedá doložit citací. Žádné částečné body — každá položka na těch seznamech se už jednou pokazila.

**Nech běh doběhnout.** Když jsem strop nastavil na čtyři kola, tři body spadly jenom proto, že se skill ještě správně ptal a nebylo co hodnotit. Výchozí hodnota je dvanáct.

## Když scénář spadne

Oprav skill, ne eval. A když se ukáže, že špatný byl test, změň ho ve stejném commitu jako skill a napiš do changelogu proč.

Pak si přečti část `qualitative`. Tam bývají ty skutečné chyby — jestli něco čte jako kolega, nebo jako formulář, se nedá změřit, jenom posoudit. Z jednoho běhu takhle vypadlo *„výslech s dobrým sluchem"*, což by kontrola formy nikdy neřekla.

## Proč nejsou ve složkách skillů

Skill má v instrukcích, že si přečte soubory, které leží u něj. Kdyby vedle nich ležely i testy, četl by si rovnou odpovědi. Proto jsou vedle a runner je má navíc zakázáno otevřít.

## Jazyk

Repliky jsou česky, protože to člověk opravdu takhle napíše. Testovací tvrzení jsou anglicky, protože je čte model, ne člověk.

## Odkud je struktura

Z konvence evalů v `anthropics/skills` (`skill-creator`). Odtamtud je i rozdělení na měřitelná tvrzení a kvalitativní poznámku: *„subjective skills (writing style, design quality) are better evaluated qualitatively — don't force assertions onto things that need human judgment."*
