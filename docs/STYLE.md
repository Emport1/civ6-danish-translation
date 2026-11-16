# Danish localization style guide — Civilization VI

## Audience and voice
- Reader: an adult Danish player, not a gaming expert. Write natural, modern, correct Danish
  (rigsdansk), the way a professional Danish game localizer would. Never word-for-word.
- Address the player as "du". Advisors and leaders speak naturally and in character.
- Prefer clear Danish words over English loanwords when a natural Danish word exists.
- UI labels, buttons and short strings must stay short (aim for at most ~130 % of the English length).

## Capitalization and spelling
- Follow Danish rules: common nouns are lowercase in running text, also game terms
  ("en stor videnskabsmand", "+2 tro", "dit campusdistrikt").
- Strings that are names/labels/headings (tags ending in `_NAME`, buttons, menu items, titles)
  start with a capital letter on the first word only ("Stor videnskabsmand", "Næste tur").
- Proper nouns follow Danish conventions ("Den Kinesiske Mur", "Pyramiderne").
- English ALL-CAPS strings stay ALL-CAPS in Danish.
- Compounds are written as one word ("handelsrute", "kampstyrke").

## STRICT format rules (broken codes show garbage or break the game)
1. Copy every `{...}` expression's variable name, `:` keyword (`plural`, `number`, `gender`,
   `datetime`, `upper`), number pattern (e.g. `+#.#;-#.#`) and branch selectors (`1?`, `other?`)
   exactly. Translate only the human words inside plural branches. Example:
   `{1_Name} ({2_Turns : plural 1?{2_Turns} turn; other?{2_Turns} turns;})`
   -> `{1_Name} ({2_Turns : plural 1?{2_Turns} tur; other?{2_Turns} ture;})`
2. `{LOC_...}` references: copy unchanged (the game fills them with Danish text itself).
3. Copy every `[ICON_...]`, `[Icon_...]`, `[NEWLINE]`, `[COLOR_...]`, `[COLOR:...]`, `[ENDCOLOR]`,
   `[SIZE...]`, `[i]` token exactly, same number of times. You may move tokens to fit Danish word order.
4. English article templates with `gender`, e.g.
   `{1: gender *:an?an {1}; *:the?the {1}; *:no_article?{1}; other?a {1};}`: Danish needs no article
   here. Reduce it to `{1: gender other?{1};}` (keep head and keyword, only an `other?` branch).
5. Danish plural categories are the same as English (`1?` and `other?`).
6. Never add notes, explanations, alternatives or translator comments. Never leave English
   sentences untranslated. Never translate or change the tag keys.
7. Keep digits, `+`, `-`, `%` and symbols as they are. "per turn" -> "pr. tur".

## Proper nouns
- Historical persons/leaders: established Danish forms where they exist (Harald Hårderåde,
  Peter den Store, Kleopatra, Katarina de' Medici, Frederik Barbarossa, Alexander den Store,
  Djengis Khan, Suleiman den Prægtige, Julius Cæsar, Eleanor af Aquitanien); otherwise keep the name.
- Cities/places: Danish exonyms where standard (Rom, Athen, Moskva, Sankt Petersborg, Kairo,
  Lissabon, Venedig, Neapel, Wien, Prag, Warszawa, Bagdad, Damaskus, Mekka, Konstantinopel,
  Theben, Memfis, Korinth, Jerusalem, Beijing); otherwise keep the spelling.
- Wonders: established Danish names (Pyramiderne, Den Kinesiske Mur, Kolosseum, Babylons hængende
  haver, Kolossen på Rhodos, Den Forbudte By, Terrakottahæren, Frihedsgudinden, Eiffeltårnet);
  otherwise a natural Danish rendering, or the original name if it is a proper name (Stonehenge,
  Petra, Machu Picchu, Big Ben).
- Personal names of citizens/units, band/album/song names: keep unchanged.
- Quotes from famous people: translate the quote, keep the attribution (Danish form if established).

## Core terminology (use exactly; inflect normally)
| English | Danish |
|---|---|
| civilization / leader / empire | civilisation / leder / rige |
| city / capital / city center | by / hovedstad / bymidte |
| city-state / suzerain / envoy / free city | bystat / overherre / udsending / fri by |
| tile, hex | felt |
| turn / per turn / Next Turn | tur / pr. tur / Næste tur |
| district / neighborhood | distrikt / boligkvarter |
| building / improvement / project | bygning / forbedring / projekt |
| wonder / world wonder / natural wonder | vidunder / verdensvidunder / naturvidunder |
| unit | enhed |
| Builder / Settler / Trader / Scout / Warrior | Bygmester / Nybygger / Handelsmand / Spejder / Kriger |
| great person (Great People) | stor personlighed (store personligheder) |
| Great Person points | point til store personligheder |
| Great General/Admiral/Engineer/Merchant/Prophet/Scientist/Writer/Artist/Musician | stor general/admiral/ingeniør/købmand/profet/videnskabsmand/forfatter/kunstner/musiker |
| Great Work (of Writing/Art/Music) | stort værk (stort litteraturværk / kunstværk / musikværk) |
| Food / Production / Gold / Science / Culture / Faith / Tourism | mad / produktion / guld / videnskab / kultur / tro / turisme |
| Housing / Amenities (Amenity) / Loyalty / Appeal | boliger / goder (gode) / loyalitet / tiltrækning |
| Power (electricity) / Diplomatic Favor / Era Score | strøm / diplomatisk gunst / æra-point |
| Campus / Holy Site / Encampment / Commercial Hub / Harbor | campus / helligt sted / militærlejr / handelscenter / havn |
| Theater Square / Entertainment Complex / Water Park / Industrial Zone | teaterplads / underholdningskompleks / vandland / industriområde |
| Aqueduct / Aerodrome / Spaceport / Government Plaza / Diplomatic Quarter / Preserve / Canal / Dam | akvædukt / flyveplads / rumhavn / regeringsplads / diplomatkvarter / naturreservat / kanal / dæmning |
| Farm / Mine / Quarry / Plantation / Camp / Pasture / Fishing Boats / Lumber Mill | gård / mine / stenbrud / plantage / jagtlejr / græsgang / fiskerbåde / savværk |
| technology / tech tree / research | teknologi / teknologitræ / forskning (forske) |
| civic / civics tree | samfundsudvikling (pl. samfundsudviklinger) / samfundstræ |
| Eureka / Inspiration / boost | Eureka / inspiration / løft |
| government / policy (card) / policy slot | styreform / politik (politikkort) / politikplads |
| Military / Economic / Diplomatic / Wildcard (slots) | militær / økonomisk / diplomatisk / joker |
| era / Golden / Dark / Heroic / Normal Age | æra / guldalder / mørk tidsalder / heltealder / normal tidsalder |
| Ancient / Classical / Medieval / Renaissance / Industrial / Modern / Atomic / Information / Future Era | Oldtiden / Antikken / Middelalderen / Renæssancen / Industrialderen / Moderne tid / Atomalderen / Informationsalderen / Fremtidsæraen |
| religion / pantheon / belief / follower / founder | religion / panteon / trossætning / tilhænger / grundlægger |
| missionary / apostle / inquisitor / guru / religious pressure / holy city | missionær / apostel / inkvisitor / guru / religiøst pres / hellig by |
| alliance / declaration of friendship / denounce / delegation / embassy / open borders | alliance / venskabserklæring / fordømme / delegation / ambassade / åbne grænser |
| casus belli / surprise war / formal war / grievances / agenda (leader) | casus belli / overraskelseskrig / formel krig / klager / dagsorden |
| World Congress / emergency / competition / resolution | Verdenskongressen / nødsituation / konkurrence / resolution |
| combat strength / ranged strength / bombard strength | kampstyrke / afstandsstyrke / bombardementsstyrke |
| movement / sight / range / promotion / experience | bevægelse / synsvidde / rækkevidde / forfremmelse / erfaring |
| corps / army / fleet / armada / zone of control / pillage / fortify / garrison | korps / hær / flåde / armada / kontrolzone / plyndre / befæste / garnison |
| governor / spy / trade route / trading post | guvernør / spion / handelsrute / handelsstation |
| barbarian / barbarian outpost / tribal village | barbar / barbarlejr / stammelandsby |
| natural disaster / climate change / sea level | naturkatastrofe / klimaforandringer / havniveau |
| Science/Culture/Domination/Religious/Diplomatic/Score Victory | videnskabssejr / kultursejr / erobringssejr / religiøs sejr / diplomatisk sejr / pointsejr |
| luxury / strategic / bonus resource | luksusressource / strategisk ressource / bonusressource |
| Iron / Horses / Niter / Coal / Oil / Aluminum / Uranium | jern / heste / salpeter / kul / olie / aluminium / uran |
| Grassland / Plains / Desert / Tundra / Snow / Hills / Mountains | græsland / slette / ørken / tundra / sne / bakker / bjerge |
| Coast / Ocean / Lake / River / Woods (Forest) / Rainforest / Marsh / Floodplains / Oasis / Reef | kyst / ocean / sø / flod / skov / regnskov / sump / flodslette / oase / rev |
| Options / Single Player / Multiplayer / Load Game / Save Game | Indstillinger / Enkeltspiller / Flerspiller / Indlæs spil / Gem spil |
| Exit to Main Menu / Exit to Desktop / Back / Accept / Cancel / Confirm / Continue / Resume | Afslut til hovedmenu / Afslut til skrivebordet / Tilbage / Accepter / Annuller / Bekræft / Fortsæt / Genoptag |
| difficulty / game speed / map size / ruleset | sværhedsgrad / spilhastighed / kortstørrelse / regelsæt |
| Civilopedia | Civilopedia |
