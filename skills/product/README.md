# Pro Romču — co jsme s tvými skilly udělali a proč

Stav k 17. 8. 2026. Tři soubory vedle jsou tvoje kroky 1–3 pro Skill Hub; krok 4 se přesunul do `../design/design-prototypovani.md`, protože prototypování je designová práce a vzal si ho Michal.

**Texty jsou tvoje, slovo od slova.** Změnilo se jen to, co je vypsané níž — a formátování, které se poztrácelo přenosem (nadpisy, tabulky, odrážky).

## Jména pro Hub

| Tvůj osobní skill | V Hubu |
|---|---|
| slevomat-definice-problemu-a-hmw | `product-definice-problemu-a-hmw` |
| slevomat-mapovani-stavu | `product-mapovani-stavu` |
| slevomat-konkurence-inspirace | `product-konkurence-inspirace` |
| slevomat-zadani-pro-design | `design-prototypovani` |

Prefix není kosmetika: v claude.ai a v Coworku je seznam skillů plochý, bez uvedení pluginu, takže je to jediné, podle čeho člověk pozná, kam skill patří. A „slevomat" do názvu podle pravidel Hubu nepatří, protože celý hub je slevomatí. Kroky 5 a 6 už tam žijí jako `psani-zadani` a `kontrola-zadani`.

## Co je navíc — a proč

**Krok 1: otázka spouštěče.** *„Co se stalo, že to řešíme zrovna teď?"* Spouštěč a opakovaná potřeba jsou často dvě různé věci a rozsah se podle toho mění. Máme to z vlastního testu: někdo chtěl generátor OG obrázků „pravidelně", spouštěčem byla jednorázová dávka kvůli nové kreativě — a zadání tu dávku málem vyloučilo z rozsahu.

**Kroky 1, 2 a 4: příčky důkazů.** U každého tvrzení stojí, na čem stojí: behaviorální data / tickety zákaznické péče a partnerské podpory / rozhovory / desk research / domněnka. Domněnka je platná příčka, jen se nesmí vydávat za zjištění. Krok 3 dostal jen jednu větu navíc — celý stojí na desk research a má vlastní ostřejší disciplínu „vidím / odhaduju", takže duplikovat tam žebřík nemá smysl.

**Krok 3: kde skill běží.** Agenty s taby v prohlížeči máš v Claude Code a v Coworku, v obyčejném chatu claude.ai ne. Je to napsané i v description a je k tomu záložní cesta — rubrika vznikne stejně, obrázky a odkazy dodá pisatel.

**Kroky 2 a 3: hranice „kdy nepoužívat".** Mapování ne na hledání řešení, konkurence ne na výběr řešení a ne bez mezer z mapování. V plochém seznamu je kolize triggerů druhá nejčastější příčina, proč skill selže.

**Role.** „Produkťák" je nahrazený tvým vlastním slovem **„pisatel"** z kroku 2. Mapování stavu i konkurenční rešerši dělají designéři a výzkumníci úplně stejně, a jméno role v description rozhoduje, jestli si skill přiřadí k sobě.

**Opravené odkazy.** Mapování posílalo na `slevomat-ramovani-problemu`, který se ale jmenuje jinak — přejmenování ujelo odkazům. A „Co následuje" v kroku 1 tvrdilo, že návrh řešení dělá `slevomat-design-principles`; ten posuzuje, nenavrhuje.

### Krok 4 — tam je zásahů nejvíc

Dva bloky, které jsi nepsala, a stojí za to je projít:

**„Co má prototyp ověřit a co by koncept zabilo."** V šesti krocích procesu se prototyp nikdy neukáže zákazníkům — krok 4 ho nechá nakreslit, krok 5 řeší provoz, krok 6 píše zadání pro vývoj. Prototyp je ale experiment, a experiment bez předem napsané podmínky selhání selhat nemůže: vyrobí mandát místo odpovědi. Proto se ta podmínka píše **teď**, ne po ukázání, kdy už by to byla racionalizace. A ke komu se dostane: jména a termín, ne „plánujeme testování".

**„Co je v prototypu nafejkované."** Prototyp z Claude Design vypadá hotově a někdo ho ukáže na poradě, kde se přečte jako rozhodnutí. Seznam vymyšlených dat a mrtvých tlačítek je nejlevnější ochrana, jaká existuje.

K tomu: zavrhnuté vzory z kroku 3 patří do „Co nedělat" jmenovitě a s důvodem (jinak je designér za tři týdny navrhne znovu), Mini*S se jmenuje a nepopisuje, brief je jeden blok ke zkopírování, a nabídne se k projití místo odeslání — „tohle jsem neřekl" znamená přepsat, ne se hádat.

## Jak to dostat ven

1. **Projdi to** — hlavně krok 4, ty dva bloky výš.
2. Pak **„Sdílet ke schválení"** v claude.ai, schvaluje Andre. Drafty do té doby vidí jen Michal.
3. **Než to schválí:** když chceš mezitím aktualizovat svoje osobní skilly, vlož tenhle text a mechanicky nahraď prefix `product-` za `slevomat-` u těch čtyř jmen — a jen u nich, včetně frontmatteru. Osobní kopie jsou jediné místo, kde smí staré názvy existovat.
4. **Po schválení** osobní kopie smaž. Nic jiného se ten den nemění, kanonický text už finální jména má.

## Co ještě víme a neopravili jsme

- `slevomat-log-zmen-zprava` v pluginu `product` porušuje pravidla pojmenování Hubu a `psani-zadani` ani `kontrola-zadani` nenesou prefix — seznam bude míchat dva styly. Chce to samostatné přejmenovávací kolo, ne přílepek k tomuhle.
- Popis pluginu `product` po přidání těchhle skillů zastará. Navržené znění: „Produktová práce ve Slevomatu — od rámování problému přes mapování stavu a konkurenci až po zadání pro design, zadání pro vývoj, jeho kontrolu a oznámení nasazených změn."
- Jedna věc, kterou jsme **záměrně nezanesli**: sjednotit „co je fakt a co domněnka" na příčky důkazů i tam, kde to zní jinak. Je to zásah do tvé struktury, tak ať to nejdřív projde přes tebe.
