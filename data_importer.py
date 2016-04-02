#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Generic bot to import data to Wikidata.
"""
#import json
import pywikibot
#from pywikibot import pagegenerators
#import urllib2
#import re
#import pywikibot.data.wikidataquery as wdquery
#import datetime
#import HTMLParser
#import posixpath
#from urlparse import urlparse
#from urllib import urlopen
#import hashlib
#import io
#import base64
#import upload
#import tempfile
#import os
#import time
#import itertools

class DataImporter:
    """
    A bot to enrich and create items on Wikidata. This bot is not subclassed
    to any of the pywikibot bots, because the flow of data is different.
    """
    def __init__(self, dictGenerator, create=False):
        """
        Arguments:
            * generator    - A generator that yields Dict objects.
            The dict in this generator needs to contain 'idpid' and 'collectionqid'
            * create       - Boolean to say if you want to create new items or just update existing

        """
        
    def fillCache(self, collectionqid, idProperty, queryoverride=u'', cacheMaxAge=0):
        """
        Query Wikidata to fill the cache of items we already have an object for
        """
                        
    def run(self):
        """
        Starts the robot.
        """

    def findItem(self, metadata):
        """
        Based on the metadata, try to find an item to update.
        @param metadata: The metadata we want to add
        @type metadata: dict
        @return:  
        @rtype: pywikibot.Itempage
        """
        return

    def createItem(self, metadata):
        """
        Based on the metadata, create a new item.
        """
        return

    def treat(self, itempage, metadata):
        """
        Updata the itempage based on the metadata
        """
        
    def addLabelOrAlias(self, lang, name, item, prefix=None,
                        caseSensitive=False):
        """
        Add a name as either a label (if none) or an alias
        in the given language

        param lang: the language code
        param name: the value to be added
        param item: the item to which the label/alias should be added
        param prefix: a prefix for the edit summary
        param caseSensitive: if the comparison is case sensitive
        """

    def addDescription(self, lang, name, item, prefix=None,
                        caseSensitive=False):
        """
        """
        
    def addItemStatement(self, item, pid, qid, url):
        """
        Helper function to add a statement. Probably duplicate. Figure out
        """

    def hasClaim(self, prop, itis, item):
        """
        Checks if the claim already exists, if so returns that claim
        """

    def hasNoneCustomClaim(self, prop, snaktype, item):
        """
        hasClaim() in the special case of 'somevalue' and 'novalue'
        TODO: Is inverse of hasSpecialClaim. Figure out the best way to handle this
        """
        
    def addNewClaim(self, prop, statement, item, ref):
        """
        Given an item, a property and a claim (in the itis format) this
        either adds the sourced claim, or sources it if already existing

        Known issues:
        * Only allows one qualifier to be added
        * Will source a claim with other qualifiers

        prop: a PXX code, unicode
        statement: a Statement() object
        item: the item being checked
        ref: None|Reference
        quals: None|list of Qualifiers
        """


    def hasAllQualifiers(self, quals, claim):
        """
        Checks if all qualifier are already present
        param quals: list of Qualifier
        param claim: Claim
        """
        
    def hasQualifier(self, qual, claim):
        """
        Checks if qualifier is already present
        param qual: Qualifier
        param claim: Claim
        """

    def addQualifier(self, item, claim, qual):
        """
        Check if a qualifier is present at the given claim,
        otherwise add it

        Known issue: This will qualify an already referenced claim
            this must therefore be tested before

        param item: itemPage to check
        param claim: Claim to check
        param qual: Qualifier to check
        """


    def hasReference(self, prop, itis, claim):
        """
        Check if a given reference is already present at the given claim.

        param prop: the source property
        param itis: the source target value
        param claim: the pywikibot.Claim to be checked
        """
        
    def addReference(self, item, newclaim, url):
        """
        Add a reference with a retrieval url and todays date
        """
        
    def bypassRedirect(self, item):
        """
        Checks if an item is a Redirect, and if so returns the
        target item instead of the original.
        This is needed for itis comparisons

        Not that this should either be called before an
        item.exists()/item.get() call or a new one must be made afterwards

        FIXME: Move to pywikibot?
        
        return ItemPage
        """

    def compareWbTimeClaim(self, target, itis):
        """Compare if two WbTime claims are the same (regarding precision).

        FIXME: Move this to Pywikibot? See T131453

        thereby handling T107870

        param target: any Claim
        param itis: a WbTime
        raises: pywikibot.Error
        return bool
        """

    def QtoItemPage(self, Q):
        """Make a pywikibot.ItemPage given a Q-value.

        @param Q: the Q-id of the item (with or without "Q")
        @type Q: string or int
        @rtype pywikibot.ItemPage
        """
        return pywikibot.ItemPage(
            self.repo,
            u'Q%s' % str(Q).lstrip('Q'))

    def make_simple_claim(self, prop, target):
        """Make a pywikibot.Claim given a property and target.

        @param prop: the P-id of a property (with or without "P")
        @type prop: str or int
        @param target: the target of the Claim
        @type target: object
        @rtype: pywikibot.Claim
        """
        claim = pywikibot.Claim(self.repo, u'P%s' % str(prop).lstrip('P'))
        claim.setTarget(target)
        return claim

    def make_new_item(self, data, summary):
        """Make a new ItemPage given some data and an edit summary.

        @param data: data, correctly formatted, with which to create the item.
        @type data: dict
        @param summary: an edit summary for the action
        @type summary: str
        @rtype: pywikibot.ItemPage
        """
        identification = {}  # @todo: what does this do?
        result = self.repo.editEntity(identification, data, summary=summary)
        pywikibot.output(summary)  # afterwards in case an error is raised

        # return the new item
        return self.QtoItemPage(result.get(u'entity').get('id'))


class Reference(object):
    """A class for encoding the contents of a reference.

    Makes a distinction between the elements which should be included in a
    comparison with other references and those which shouldn't.

    e.g. for "reference URL: some URL", "retrieved: some_date" you would
    want to compare sources on the URL but not the date.

    A comparison will fail if ANY of the source_test sources are present.
    """

    def __init__(self, source_test=None, source_notest=None):
        """Make a Reference object from the provided sources.

        param source_test: claims which should be included in
            comparison tests
        type source_test: pywikibot.Claim|list of pywikibot.Claim
        param source_notest: claims which should be excluded from
            comparison tests
        type source_notest: pywikibot.Claim|list of pywikibot.Claim
        """
        # avoid mutable default arguments
        source_test = source_test or []
        source_notest = source_notest or []

        # standardise the two types of allowed input
        self.source_test = listify(source_test)
        self.source_notest = listify(source_notest)

        # validate input
        self.validate_sources()

    def validate_sources(self):
        """Validate the sources of a Reference."""
        sources = self.get_all_sources()
        if not sources:
            raise pywikibot.Error(
                'You tried to create a reference without any sources')
        if not all(isinstance(s, pywikibot.Claim) for s in sources):
            raise pywikibot.Error(
                'You tried to create a reference with a non-Claim source')

    def get_all_sources(self):
        """Return all the sources of a Reference."""
        return self.source_test + self.source_notest

    def __repr__(self):
        """Return a more complete string representation."""
        return u'WD.Reference(test: %s, no_test: %s)' % (
            self.source_test, self.source_notest)

class Qualifier(object):
    """A class for encoding the contents of a qualifier.

    Essentially pywikibot.Claim without having to provide an instantiated
    repo.

    @todo: redo as SimpleClaim (if so reuse in Reference) or
           retire in favour of pywikibot.Claim
    """

    def __init__(self, P, itis):
        """Make a correctly formatted qualifier object for claims.

        param P: string the property (with or without "P")
        param itis: a valid claim target e.g. pywikibot.ItemPage
        """
        self.prop = u'P%s' % P.lstrip('P')
        self.itis = itis

    def __repr__(self):
        """Return a more complete string representation."""
        return u'WD.Qualifier(%s, %s)' % (self.prop, self.itis)

class Statement(object):
    """A class for encoding the contents of a statement.

    Meaning a value and optional qualifiers
    @todo: itis test
    """

    def __init__(self, itis, special=False):
        """Make a correctly formatted statement object for claims.

        param itis: a valid claim target e.g. pywikibot.ItemPage
        param special: bool if itis is actaually a snackvalue
        """
        if special and itis not in ['somevalue', 'novalue']:
            raise pywikibot.Error(
                'You tried to create a special statement with a '
                'non-allowed snakvalue: %s' % itis)
        self.itis = itis
        self.quals = []
        self.special = special
        self.force = False

    def addQualifier(self, qual, force=False):
        """Add qualifer to the statement if not None.

        Returns self to allow chaining.

        param qual: Qualifier|None
        param force: bool whether qualifier should be added even to
                     already sourced items
        return Statement
        """
        # test input
        if qual is None:
            # simply skip any action
            return self
        elif not isinstance(qual, WikidataStuff.Qualifier):
            raise pywikibot.Error(
                'addQualifier was called with something other '
                'than a Qualifier|None object: %s' % qual)

        # register qualifier
        self.quals.append(qual)
        if force:
            self.force = True
        return self

    def isNone(self):
        """Test if Statment was created with itis=None."""
        return self.itis is None

    def __repr__(self):
        """Return a more complete string representation."""
        return u'WD.Statement(itis:%s, quals:%s, special:%s, force:%s)' % (
            self.itis, self.quals, self.special, self.force)

        
def main():
    print u'Dude, write your own bot'    
    

if __name__ == "__main__":
    main()
