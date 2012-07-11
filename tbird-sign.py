#!/usr/bin/env python
import tweepy


#Google Plus
useGooglePlus = 1
googleName = mariuscristianc
#Tweeter
useTweeter = 1
tweeterName = mariuscristianc
#Linkedin
useLinkedin = 1
linkedinName = mariuscristianc
#identica
useIdentica = 1
identicaName = mariuscristianc
#facebook
useFacebook = 1
facebookName = mariuscristianc
#stack overflow
useStackOverflow = 1
stackOverflowName = mariuscristianc
#pinterest
#wordpress
#blogger
#rss
#etsy
#ebay
#github
#digg
#quora
#


print tweepy.api.user_timeline('mariuscristianc')[0].text

