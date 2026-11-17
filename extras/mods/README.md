# Danish text for Civilization VI mods

Danish text for 9 popular user-interface mods, one file per mod. It needs the main Danish
package (the `da_DK` language must exist).

**Install:** copy the files for the mods you use from `da_DK` here into the same
`Documents\My Games\Sid Meier's Civilization VI\Text\da_DK` folder as the main package.
Copy only files for mods you have installed: `SukritactSimpleUI_da_DK.xml` rewords 6 of the
game's own city tooltips in that mod's style, with a number only that mod supplies, so
without the mod those tooltips would show a blank.

| File | Mod | Lines |
|---|---|---|
| `BetterReportScreen_da_DK.xml` | [Better Report Screen](https://steamcommunity.com/sharedfiles/filedetails/?id=1312585482) | 58 |
| `BetterTechTree_da_DK.xml` | [Better Tech Tree](https://github.com/Infixo/Civ6-Mods) | 6 |
| `DetailedMapTacks_da_DK.xml` | [Detailed Map Tacks](https://steamcommunity.com/sharedfiles/filedetails/?id=2428969051) | 12 |
| `DetailedWonderReminder_da_DK.xml` | [Detailed Wonder Reminder](https://steamcommunity.com/sharedfiles/filedetails/?id=2798127335) | 19 |
| `MoreLenses_da_DK.xml` | [More Lenses](https://github.com/astog/MoreLenses) | 59 |
| `PolicyChangeReminder_da_DK.xml` | [Policy Change Reminder](https://steamcommunity.com/sharedfiles/filedetails/?id=1132600299) | 4 |
| `QuickDeals_da_DK.xml` | [Quick Deals](https://steamcommunity.com/sharedfiles/filedetails/?id=2460661464) | 14 |
| `RealEraTracker_da_DK.xml` | [Real Era Tracker](https://github.com/Infixo/Civ6-Mods) | 9 |
| `SukritactSimpleUI_da_DK.xml` | [Sukritact's Simple UI Adjustments](https://steamcommunity.com/sharedfiles/filedetails/?id=939149009) | 39 |

Better Loading Screen, Real Great People, Extended Policy Cards and Better Builder Charges
Tracking have no text files of their own, so there is nothing to add for them.

Translated from the mods' versions current in November 2026 and checked with
`tools/validate.py` against each mod's English text (0 errors). A few tooltips are written
directly into some mods' Lua code instead of their text files; those stay in English.
