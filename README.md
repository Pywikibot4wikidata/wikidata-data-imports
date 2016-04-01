wikidata-data-imports
==============

Work in progress (currently being reworked from wikidata-stuff)

Library to aid data imports to Wikidata using pywikibot.

# Below stuff might all be wrong!
Random scripts used for Wikidata. These require [pywikibot](https://github.com/wikimedia/pywikibot-core)

* WikidataStuff.py: A set of generally useful functions for interacting
with Wikidata using pywikibot.

* WikidataStringSearch.py: A database hookup (to be run from labs) for
doing text string searches (SQL LIKE style) in labels, aliases and
descriptions of items.

* wdqsLookup.py: A module for doing [WDQS](http://query.wikidata.org/) look-ups
and for converting (some) [WDQ](http://wdq.wmflabs.org/) queries to WDQS
queries.

###KulturNav/ (possible source of example)
* kulturnavBot.py: A framework for building bots to adding and/or
sourcing statements made available through [KulturNav](http://kulturnav.org/).
Also includes some more general pywikibot methods for Wikidata.
  * kulturnavBotArkDes: A bot for adding and/or sourcing statements about
architects based on data curated by Swedish Centre for Architecture and
Design ([ArkDes](http://www.arkdes.se/)) made available through KulturNav.

###NatMus/ (possible source of example)
* nationalmuseumSE.py: A [sum of all paintings](http://www.wikidata.org/wiki/Wikidata:WikiProject_sum_of_all_paintings)
bot for importing paintings from Nationalmuseum Sweden to Wikidata
(via Europeana).

