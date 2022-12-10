"""
This script creates the dimension of universalism versus populism

Versions:
Python - 3.10.4
Pandas - 1.5.2
"""
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Word Pairs
# 1. "Good incomes for our workers are the secret of our great and growing
#     consumer markets"
#     -
#    "We pledge vigorously and fearlessly to enforce the criminal and civil
#     provisions of the existing anti-trust laws, and to the extent that their
#     effectiveness has been weakened by new corporate devices or judicial
#     construction, we propose by law to restore their efficacy in stamping out
#     monopolistic practices and the concentration of economic power." - 1936

# 2. "We pledge ourselves to release the springs of abundance, to bring this
#     abundance to all, and thus to fulfill the full promise of America" -
#     -
#    "Monopolies are the most efficient means yet devised for appropriating the
#     fruits of industry to the benefit of the few at the expense of the many,
#     and unless their insatiate greed is checked, all wealth will be
#     aggregated in a few hands and the Republic destroyed" - 1900
#

# 3. "The new Democratic Administration will confidently proceed to unshackle
#     American enterprise and to free American labor industrial leadership
#     and capital to create an abundance that will outstrip any other system"
#     -
#   "We therefore favor the vigorous enforcement of the criminal law against
#    guilty trust magnates and officials, and demand the enactment of such
#    additional legislation as may be necessary to make it impossible for a
#    private monopoly to exist in the United States" - 1908

# 4. "Carry the War on Poverty forward as a total war against the causes of
#     human want." - 1964
#     -
#     "They have ruined our foreign trade; destroyed the values of our
#     commodities and products, crippled our banking system, robbed millions of
#     our people of their life savings, and thrown millions more out of work,
#     produced wide-spread poverty and brought the government to a state of
#     financial distress unprecedented in time of peace." - 1932

# 5. "For the past four years, this Administration has callously pursued
#     policies which have further impoverished those at the bottom of the
#     economic ladder and pushed millions of Americans, particularly women and
#     children, below the poverty line" -1984
#    -
#    "They have ruined our foreign trade; destroyed the values of our
#     commodities and products, crippled our banking system, robbed millions of
#     our people of their life savings, and thrown millions more out of work,
#     produced wide-spread poverty and brought the government to a state of
#     financial distress unprecedented in time of peace." - 1920

# 6. " But, we also pledge to attack the underlying injustices that contribute
#     to such violence so that no person need feel condemned to a life of
#     poverty and despair." - 1980
#    -
#    "In order to mitigate unemployment attending business depression, we urge
#     the enactment of legislation authorizing the construction and repair of
#     public works be initiated in periods of acute unemployment." - 1924

# 7.  "We have been and we shall remain the party of all Americans" - 1980
#     -
#     "In this world crisis, the purpose of the Democratic Party is to defend
#     against external attack and justify by internal progress the system of
#     government and way of life from which the Democratic Party takes its
#     name" - 1940

# 8. "We invite all to join us who believe that narrow partisanship takes too
#     small account of the size of our task, the penalties for failure and the
#     boundless rewards to all our people for success." - 1964
#    -
#    "The conscience of the nation is now aroused to free the Government from
#     the grip of those who have made it a business asset of the favor-seeking
#     corporations." - 1908

# 9. "In this platform of the Democratic Party, we present a clear alternative
#     to the failures of preceding administrations and a projection of the
#     common future to which we aspire: a world at peace; a just society of
#     equals; a society without violence; a society in consonance with its
#     natural environment, affording freedom to the individual and the
#     opportunity to develop to the fullest human Potential." - 1976
#    -
#    "Believing that our most cherished institutions are in great peril, that
#     the very existence of our constitutional republic is at stake, and that
#     the decision now to be rendered will determine whether or not our
#     children are to enjoy these blessed privileges of free government, which
#     have made the United States great, prosperous and honored, we earnestly
#     ask for the foregoing declaration of principles, the hearty support of
#     the liberty-loving American people, regardless of previous party
#     affiliations." -

# 10. "Our objective, however, is not the right to coexist in armed camps on
#     the same planet with totalitarian ideologies; it is the creation of an
#     enduring peace in which the universal values of human dignity, truth,
#     and justice under law are finally secured for all men everywhere on
#     earth." - 1960
#     -
#     "We reject the principle—which we have always rejected, but which the
#     Republican 80th Congress enthusiastically accepted—that government
#     exists for the benefit of the privileged few." - 1948
